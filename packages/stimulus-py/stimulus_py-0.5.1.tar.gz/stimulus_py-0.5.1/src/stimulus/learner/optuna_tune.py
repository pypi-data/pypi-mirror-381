"""Optuna tuning module."""

import inspect
import json
import logging
import os
import uuid
from typing import Any

import datasets
import optuna
import torch
from safetensors.torch import save_file
from safetensors.torch import save_model as safe_save_model

from stimulus.learner.interface import model_config_parser, model_schema
from stimulus.typing.protocols import StimulusModel

logger = logging.getLogger(__name__)

# Constants for model interface
STANDARD_MODEL_RETURN_COUNT = 2  # (loss, metrics)
EXTENDED_MODEL_RETURN_COUNT = 3  # (loss, metrics, per_sample_dict)


class Objective:
    """Objective class for Optuna tuning."""

    def __init__(
        self,
        model_class: type[StimulusModel],
        network_params: dict[str, model_schema.TunableParameter | model_schema.VariableList],
        optimizer_params: dict[str, model_schema.TunableParameter],
        data_params: dict[str, model_schema.TunableParameter],
        loss_params: dict[str, model_schema.TunableParameter],
        train_torch_dataset: datasets.Dataset,
        val_torch_dataset: datasets.Dataset,
        artifact_store: Any,
        max_samples: int = 1000,
        compute_objective_every_n_samples: int = 50,
        target_metric: str = "val_loss",
        device: torch.device | None = None,
    ):
        """Initialize the Objective class.

        Args:
            model_class: The model class to be tuned.
            network_params: The network parameters to be tuned.
            optimizer_params: The optimizer parameters to be tuned.
            data_params: The data parameters to be tuned.
            loss_params: The loss parameters to be tuned.
            train_torch_dataset: The training dataset.
            val_torch_dataset: The validation dataset.
            artifact_store: The artifact store to save the model and optimizer.
            max_samples: The maximum number of samples to train.
            compute_objective_every_n_samples: The number of samples to compute the objective.
            target_metric: The target metric to optimize.
            device: The device to run the training on.
        """
        self.model_class = model_class
        self.network_params = network_params
        self.optimizer_params = optimizer_params
        self.data_params = data_params
        self.loss_params = loss_params

        # Add sample_id column to datasets for per-sample loss tracking (as integers)
        self.train_torch_dataset = train_torch_dataset.add_column(
            "sample_id",
            list(range(len(train_torch_dataset))),
        )
        self.val_torch_dataset = val_torch_dataset.add_column(
            "sample_id",
            list(range(len(val_torch_dataset))),
        )

        self.artifact_store = artifact_store
        self.target_metric = target_metric
        self.max_samples = max_samples
        self.compute_objective_every_n_samples = compute_objective_every_n_samples
        if device is None:
            self.device = torch.device("cpu")
        else:
            self.device = device

    def _get_optimizer(self, optimizer_name: str) -> type[torch.optim.Optimizer]:
        """Get the optimizer from the name."""
        try:
            return getattr(torch.optim, optimizer_name)
        except AttributeError as e:
            raise ValueError(f"Optimizer {optimizer_name} not found in torch.optim") from e

    def __call__(self, trial: optuna.Trial):
        """Execute a full training trial and return the objective metric value."""
        # Setup phase - capture all parameter suggestions before conversion
        model_instance, model_suggestions = self._setup_model(trial)

        # Capture parameter suggestions before they're converted to instances
        optimizer_suggestions = model_config_parser.suggest_parameters(trial, self.optimizer_params)
        loss_suggestions = model_config_parser.suggest_parameters(trial, self.loss_params)
        data_suggestions = model_config_parser.suggest_parameters(trial, self.data_params)

        # Create complete suggestions dictionary
        complete_suggestions = {
            "network_params": model_suggestions,
            "optimizer_params": optimizer_suggestions,
            "loss_params": loss_suggestions,
            "data_params": data_suggestions,
        }

        optimizer = self._setup_optimizer(trial, model_instance)
        train_loader, val_loader, batch_size = self._setup_data_loaders(trial)
        loss_dict = self._setup_loss_functions(trial)

        # Training loop
        batch_idx: int = 0
        metric_dict: dict = {}

        # Per-sample loss tracking
        completed_sample_trajectories: dict[str, list[torch.Tensor]] = {}

        while batch_idx * batch_size < self.max_samples:
            nb_computed_samples = 0
            epoch_sample_lists: dict[str, list[torch.Tensor]] = {}  # Reset each epoch
            epoch_completed = True

            for batch in train_loader:
                # set model in train mode
                model_instance.train()
                try:
                    # Move all tensors to device (sample_id is now an integer tensor)
                    device_batch = {}
                    for key, value in batch.items():
                        try:
                            device_batch[key] = value.to(self.device, non_blocking=True)
                        except AttributeError as e:
                            raise AttributeError(
                                f"Error moving '{key}' to device. Expected tensor but got {type(value)}. "
                                f"This usually happens when dataset columns contain non-tensor data. "
                                f"Original error: {e}",
                            ) from e

                    # Perform a batch update
                    result = model_instance.train_batch(batch=device_batch, optimizer=optimizer, **loss_dict)

                    # Handle optional per-sample data (3rd return value)
                    if len(result) == EXTENDED_MODEL_RETURN_COUNT:
                        _loss, _metrics, per_sample_dict = result
                        # Collect per-sample data for this epoch
                        for sample_id, sample_loss in per_sample_dict.items():
                            if sample_id not in epoch_sample_lists:
                                epoch_sample_lists[sample_id] = []
                            epoch_sample_lists[sample_id].append(sample_loss)
                    else:
                        _loss, _metrics = result

                except RuntimeError as e:
                    if ("CUDA out of memory" in str(e) and self.device.type == "cuda") or (
                        "MPS backend out of memory" in str(e) and self.device.type == "mps"
                    ):
                        logger.warning(f"{self.device.type.upper()} out of memory during training: {e}")
                        logger.warning("Falling back to CPU for this trial")
                        temp_device = torch.device("cpu")
                        model_instance = model_instance.to(temp_device)
                        # Consider adjusting batch size or other parameters
                        # Move all tensors to device (sample_id is now an integer tensor)
                        device_batch = {}
                        for key, value in batch.items():
                            try:
                                device_batch[key] = value.to(temp_device)
                            except AttributeError as e:
                                raise AttributeError(
                                    f"Error moving '{key}' to device during fallback. Expected tensor but got {type(value)}. "
                                    f"This usually happens when dataset columns contain non-tensor data. "
                                    f"Original error: {e}",
                                ) from e
                        # Retry the batch
                        result = model_instance.train_batch(
                            batch=device_batch,
                            optimizer=optimizer,
                            **loss_dict,
                        )

                        # Handle optional per-sample data in error recovery
                        if len(result) == EXTENDED_MODEL_RETURN_COUNT:
                            _loss, _metrics, per_sample_dict = result
                            # Collect per-sample data for this epoch
                            for sample_id, sample_loss in per_sample_dict.items():
                                if sample_id not in epoch_sample_lists:
                                    epoch_sample_lists[sample_id] = []
                                epoch_sample_lists[sample_id].append(sample_loss)
                        else:
                            _loss, _metrics = result
                    else:
                        raise

                batch_idx += 1
                nb_computed_samples += batch_size
                # Compute objective periodically
                if nb_computed_samples >= self.compute_objective_every_n_samples:
                    nb_computed_samples = 0
                    # Evaluate current model performance
                    metric_dict = self.objective(
                        model_instance=model_instance,
                        train_loader=train_loader,
                        val_loader=val_loader,
                        loss_dict=loss_dict,
                        device=self.device,
                    )
                    logger.info(f"Objective: {metric_dict} at batch {batch_idx}")

                    trial.report(metric_dict[self.target_metric], batch_idx)
                    for metric_name, metric_value in metric_dict.items():
                        trial.set_user_attr(metric_name, metric_value)

                    # Check if trial should be pruned
                    if trial.should_prune():
                        self.save_checkpoint(trial, model_instance, optimizer, complete_suggestions)
                        raise optuna.TrialPruned()  # noqa: RSE102

                if batch_idx * batch_size >= self.max_samples:
                    epoch_completed = False  # Mark epoch as incomplete
                    break

            # After epoch loop - check if epoch completed and save per-sample data
            if epoch_completed and epoch_sample_lists:
                # Epoch completed naturally - aggregate per-sample data
                for sample_id, loss_list in epoch_sample_lists.items():
                    if sample_id not in completed_sample_trajectories:
                        completed_sample_trajectories[sample_id] = []
                    completed_sample_trajectories[sample_id].extend(loss_list)

        # Ensure we have computed metrics at least once before returning
        if not metric_dict:
            logger.info("Computing final objective metrics before returning")
            metric_dict = self.objective(
                model_instance=model_instance,
                train_loader=train_loader,
                val_loader=val_loader,
                loss_dict=loss_dict,
                device=self.device,
            )
            for metric_name, metric_value in metric_dict.items():
                trial.set_user_attr(metric_name, metric_value)

        # Save per-sample artifacts if data was collected
        if completed_sample_trajectories:
            # Convert lists to tensors
            sample_trajectories = {
                sample_id: torch.stack(loss_list) for sample_id, loss_list in completed_sample_trajectories.items()
            }

            # Save to safetensors
            unique_id = str(uuid.uuid4())[:8]
            per_sample_path = f"{trial.number}_{unique_id}_per_sample.safetensors"
            save_file(sample_trajectories, per_sample_path)

            # Upload to artifact store
            artifact_id = optuna.artifacts.upload_artifact(
                artifact_store=self.artifact_store,
                file_path=per_sample_path,
                study_or_trial=trial.study,
            )

            # Clean up local file
            try:
                os.remove(per_sample_path)
            except FileNotFoundError:
                logger.info(f"File was already deleted: {per_sample_path}")

            # Store artifact reference
            trial.set_user_attr("per_sample_artifact_id", artifact_id)
            trial.set_user_attr("per_sample_artifact_path", per_sample_path)

        # Final checkpoint and return objective value
        self.save_checkpoint(trial, model_instance, optimizer, complete_suggestions)
        return metric_dict[self.target_metric]

    def _setup_model(self, trial: optuna.Trial) -> tuple[StimulusModel, dict]:
        """Setup the model for the trial."""
        model_suggestions = model_config_parser.suggest_parameters(trial, self.network_params)
        logger.info(f"Model suggestions: {model_suggestions}")
        model_instance = self.model_class(**model_suggestions)

        try:
            model_instance = model_instance.to(self.device)
            logger.info(f"Model moved to device: {self.device}")
        except RuntimeError as e:
            if self.device.type in ["cuda", "mps"]:
                logger.warning(f"Failed to move model to {self.device.type.upper()}: {e}")
                logger.warning("Falling back to CPU")
                self.device = torch.device("cpu")
                model_instance = model_instance.to(self.device)
            else:
                raise
        return model_instance, model_suggestions

    def _setup_optimizer(self, trial: optuna.Trial, model_instance: StimulusModel) -> torch.optim.Optimizer:
        """Setup the optimizer for the trial."""
        optimizer_suggestions = model_config_parser.suggest_parameters(trial, self.optimizer_params)
        logger.info(f"Optimizer suggestions: {optimizer_suggestions}")

        optimizer_class = self._get_optimizer(optimizer_suggestions["method"])
        optimizer_kwargs = {}
        optimizer_signature = inspect.signature(optimizer_class).parameters
        for k, v in optimizer_suggestions.items():
            if k in optimizer_signature and k != "method":
                optimizer_kwargs[k] = v
            elif k != "method":
                logger.warning(f"Parameter '{k}' not found in optimizer signature, skipping")

        return optimizer_class(model_instance.parameters(), **optimizer_kwargs)

    def _setup_data_loaders(
        self,
        trial: optuna.Trial,
    ) -> tuple[torch.utils.data.DataLoader, torch.utils.data.DataLoader, int]:
        """Setup the data loaders for the trial."""
        batch_size = model_config_parser.suggest_parameters(trial, self.data_params)["batch_size"]
        logger.info(f"Batch size: {batch_size}")

        train_loader = torch.utils.data.DataLoader(
            self.train_torch_dataset,
            batch_size=batch_size,
            shuffle=True,
        )
        val_loader = torch.utils.data.DataLoader(
            self.val_torch_dataset,
            batch_size=batch_size,
            shuffle=False,
        )
        return train_loader, val_loader, batch_size

    def _setup_loss_functions(self, trial: optuna.Trial) -> dict[str, torch.nn.Module]:
        """Setup the loss functions for the trial."""
        loss_dict = model_config_parser.suggest_parameters(trial, self.loss_params)
        for key, loss_fn in loss_dict.items():
            loss_dict[key] = getattr(torch.nn, loss_fn)()
        logger.info(f"Loss parameters: {loss_dict}")
        return loss_dict

    def save_checkpoint(
        self,
        trial: optuna.Trial,
        model_instance: StimulusModel,
        optimizer: torch.optim.Optimizer,
        complete_suggestions: dict,
    ) -> None:
        """Save the model and optimizer to the trial."""
        # Convert model to CPU before saving to avoid device-specific tensors
        model_instance = model_instance.cpu()
        optimizer_state = optimizer.state_dict()

        # Convert optimizer state to CPU tensors
        for param in optimizer_state["state"].values():
            for k, v in param.items():
                if isinstance(v, torch.Tensor):
                    param[k] = v.cpu()
        unique_id = str(uuid.uuid4())[:8]
        model_path = f"{trial.number}_{unique_id}_model.safetensors"
        optimizer_path = f"{trial.number}_{unique_id}_optimizer.pt"
        model_suggestions_path = f"{trial.number}_{unique_id}_model_suggestions.json"
        safe_save_model(model_instance, model_path)
        torch.save(optimizer_state, optimizer_path)
        with open(model_suggestions_path, "w") as f:
            json.dump(complete_suggestions, f)
        artifact_id_model = optuna.artifacts.upload_artifact(
            artifact_store=self.artifact_store,
            file_path=model_path,
            study_or_trial=trial.study,
        )
        artifact_id_optimizer = optuna.artifacts.upload_artifact(
            artifact_store=self.artifact_store,
            file_path=optimizer_path,
            study_or_trial=trial.study,
        )
        artifact_id_model_suggestions = optuna.artifacts.upload_artifact(
            artifact_store=self.artifact_store,
            file_path=model_suggestions_path,
            study_or_trial=trial.study,
        )
        # delete the files from the local filesystem
        try:
            os.remove(model_path)
            os.remove(optimizer_path)
            os.remove(model_suggestions_path)
        except FileNotFoundError:
            logger.info(
                f"File was already deleted: {model_path} or {optimizer_path} or {model_suggestions_path}, most likely due to pruning",
            )
        trial.set_user_attr("model_id", artifact_id_model)
        trial.set_user_attr("model_path", model_path)
        trial.set_user_attr("optimizer_id", artifact_id_optimizer)
        trial.set_user_attr("optimizer_path", optimizer_path)
        trial.set_user_attr("model_suggestions_id", artifact_id_model_suggestions)
        trial.set_user_attr("model_suggestions_path", model_suggestions_path)

    def objective(
        self,
        model_instance: StimulusModel,
        train_loader: torch.utils.data.DataLoader,
        val_loader: torch.utils.data.DataLoader,
        loss_dict: dict[str, torch.nn.Module],
        device: torch.device,
    ) -> dict[str, float]:
        """Compute the objective metric(s) for the tuning process.

        The objectives are outputed by the model's batch function in the form of loss, metric_dictionary.
        """
        train_metrics = self.get_metrics(model_instance, train_loader, loss_dict, device)
        val_metrics = self.get_metrics(model_instance, val_loader, loss_dict, device)

        # add train_ and val_ prefix to related keys.
        return {
            **{f"train_{k}": v for k, v in train_metrics.items()},
            **{f"val_{k}": v for k, v in val_metrics.items()},
        }

    def get_metrics(
        self,
        model_instance: StimulusModel,
        data_loader: torch.utils.data.DataLoader,
        loss_dict: dict[str, torch.nn.Module],
        device: torch.device,
    ) -> dict[str, float]:
        """Compute the objective metric(s) for the tuning process."""

        def update_metric_dict(
            metric_dict: dict[str, torch.Tensor],
            metrics: dict[str, torch.Tensor],
            loss: torch.Tensor,
        ) -> dict[str, torch.Tensor]:
            """Update the metric dictionary with the new metrics and loss."""
            for key, value in metrics.items():
                if key not in metric_dict:
                    if value.ndim == 0:
                        metric_dict[key] = value.unsqueeze(0)
                    else:
                        metric_dict[key] = value
                elif value.ndim == 0:
                    metric_dict[key] = torch.cat([metric_dict[key], value.unsqueeze(0)], dim=0)
                else:
                    metric_dict[key] = torch.cat([metric_dict[key], value], dim=0)
            if "loss" not in metric_dict:
                if loss.ndim == 0:
                    metric_dict["loss"] = loss.unsqueeze(0)
                else:
                    metric_dict["loss"] = loss
            elif loss.ndim == 0:
                metric_dict["loss"] = torch.cat([metric_dict["loss"], loss.unsqueeze(0)], dim=0)
            else:
                metric_dict["loss"] = torch.cat([metric_dict["loss"], loss], dim=0)
            return metric_dict

        # set model in eval mode
        model_instance.eval()

        metric_dict: dict = {}

        for batch in data_loader:
            try:
                # Move all tensors to device (sample_id is now an integer tensor)
                device_batch = {}
                for key, value in batch.items():
                    try:
                        device_batch[key] = value.to(device, non_blocking=True)
                    except AttributeError as e:
                        raise AttributeError(
                            f"Error moving '{key}' to device during inference. Expected tensor but got {type(value)}. "
                            f"This usually happens when dataset columns contain non-tensor data. "
                            f"Original error: {e}",
                        ) from e

                # Perform a batch update
                loss, metrics = model_instance.inference(batch=device_batch, **loss_dict)

            except RuntimeError as e:
                if ("CUDA out of memory" in str(e) and self.device.type == "cuda") or (
                    "MPS backend out of memory" in str(e) and self.device.type == "mps"
                ):
                    logger.warning(f"{self.device.type.upper()} out of memory during training: {e}")
                    logger.warning("Falling back to CPU for this trial")
                    temp_device = torch.device("cpu")
                    model_instance = model_instance.to(temp_device)
                    # Consider adjusting batch size or other parameters
                    device_batch = {key: value.to(temp_device) for key, value in batch.items()}
                    # Retry the batch
                    loss, metrics = model_instance.inference(batch=device_batch, **loss_dict)
                else:
                    raise

            metric_dict = update_metric_dict(metric_dict, metrics, loss)

        # devide all metrics by number of batches
        for key in metric_dict:
            metric_dict[key] = metric_dict[key].mean()

        # Convert tensors to floats before returning
        return {k: v.item() if isinstance(v, torch.Tensor) else v for k, v in metric_dict.items()}


def tune_loop(
    objective: Objective,
    pruner: optuna.pruners.BasePruner,
    sampler: optuna.samplers.BaseSampler,
    n_trials: int,
    direction: str,
    storage: optuna.storages.BaseStorage | None = None,
) -> optuna.Study:
    """Run the tuning loop.

    Args:
        objective: The objective function to optimize.
        pruner: The pruner to use.
        sampler: The sampler to use.
        n_trials: The number of trials to run.
        direction: The direction to optimize.
        storage: The storage to use.

    Returns:
        The study object.
    """
    if storage is None:
        study = optuna.create_study(direction=direction, sampler=sampler, pruner=pruner)
    else:
        study = optuna.create_study(direction=direction, sampler=sampler, pruner=pruner, storage=storage)
    study.optimize(objective, n_trials=n_trials)
    return study
