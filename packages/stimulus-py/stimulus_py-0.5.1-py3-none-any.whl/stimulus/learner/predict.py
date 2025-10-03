"""A module for making predictions with PyTorch models using DataLoaders."""

import logging
from typing import Any, Optional, Union

import torch
from torch import Tensor
from torch.utils.data import DataLoader

from stimulus.typing.protocols import StimulusModel
from stimulus.utils.generic_utils import ensure_at_least_1d
from stimulus.utils.performance import Performance

logger = logging.getLogger(__name__)


class PredictWrapper:
    """A wrapper to predict the output of a model on a datset loaded into a torch DataLoader.

    It also provides the functionalities to measure the performance of the model.
    """

    def __init__(
        self,
        model: StimulusModel,
        dataloader: DataLoader,
        loss_dict: Optional[dict[str, Any]] = None,
        device: torch.device | None = None,
    ) -> None:
        """Initialize the PredictWrapper.

        Args:
            model: The PyTorch model to make predictions with
            dataloader: DataLoader containing the evaluation data
            loss_dict: Optional dictionary of loss functions
            device: The device to run the model on
        """
        if device is None:
            self.device = torch.device("cpu")
        else:
            self.device = device

        try:
            self.model = model.to(self.device)
        except RuntimeError as e:
            if self.device.type in ["cuda", "mps"]:
                logger.warning(f"Failed to move model to {self.device.type.upper()}: {e}")
                logger.warning("Falling back to CPU")
                self.device = torch.device("cpu")
                self.model = model.to(self.device)
            else:
                raise

        self.dataloader = dataloader
        self.loss_dict = loss_dict

        try:
            self.model.eval()
        except RuntimeError as e:
            logger.warning("Not able to run model.eval: %s", str(e))

    def predict(
        self,
        *,
        return_labels: bool = False,
    ) -> Union[dict[str, Tensor], tuple[dict[str, Tensor], dict[str, Tensor]]]:
        """Get the model predictions.

        Basically, it runs a foward pass on the model for each batch,
        gets the predictions and concatenate them for all batches.
        Since the returned `current_predictions` are formed by tensors computed for one batch,
        the final `predictions` are obtained by concatenating them.

        At the end it returns `predictions` as a dictionary of tensors with the same keys as `y`.

        If return_labels if True, then the `labels` will be returned as well, also as a dictionary of tensors.

        Args:
            return_labels: Whether to also return the labels

        Returns:
            Dictionary of predictions, and optionally labels
        """
        # create empty dictionaries with the column names
        first_batch = next(iter(self.dataloader))
        keys = first_batch[1].keys()
        predictions: dict[str, list[Tensor]] = {k: [] for k in keys}
        labels: dict[str, list[Tensor]] = {k: [] for k in keys}

        # get the predictions (and labels) for each batch
        with torch.no_grad():
            for x, y, _ in self.dataloader:
                try:
                    x_device = {key: value.to(self.device) for key, value in x.items()}
                    current_predictions = self.model(**x_device).detach().cpu()
                    current_predictions = self.handle_predictions(current_predictions, y)
                except RuntimeError as e:
                    if ("CUDA out of memory" in str(e) and self.device.type == "cuda") or (
                        "MPS backend out of memory" in str(e) and self.device.type == "mps"
                    ):
                        logger.warning(f"{self.device.type.upper()} out of memory during prediction: {e}")
                        logger.warning("Falling back to CPU for this batch")
                        temp_device = torch.device("cpu")
                        # Use CPU for this batch
                        x_cpu = {key: value.to(temp_device) for key, value in x.items()}
                        # Move model to CPU temporarily
                        model_on_cpu = self.model.to(temp_device)
                        current_predictions = model_on_cpu(**x_cpu).detach().cpu()
                        current_predictions = self.handle_predictions(current_predictions, y)
                        # Move model back to original device for next batches
                        try:
                            self.model = self.model.to(self.device)
                        except RuntimeError:
                            logger.warning(f"Failed to move model back to {self.device.type}. Staying on CPU.")
                            self.device = temp_device
                    else:
                        raise

                for k in keys:
                    # it might happen that the batch consists of one element only so the torch.cat will fail. To prevent this the function to ensure at least one dimensionality is called.
                    predictions[k].append(ensure_at_least_1d(current_predictions[k]))
                    if return_labels:
                        labels[k].append(ensure_at_least_1d(y[k]))

        # return the predictions (and labels) as a dictionary of tensors for the entire dataset.
        if not return_labels:
            return {k: torch.cat(v) for k, v in predictions.items()}
        return {k: torch.cat(v) for k, v in predictions.items()}, {k: torch.cat(v) for k, v in labels.items()}

    def handle_predictions(self, predictions: Any, y: dict[str, Tensor]) -> dict[str, Tensor]:
        """Handle the model outputs from forward pass, into a dictionary of tensors, just like y."""
        if len(y) == 1:
            return {next(iter(y.keys())): predictions}
        return dict(zip(y.keys(), predictions))

    def compute_metrics(self, metrics: list[str]) -> dict[str, float]:
        """Wrapper to compute the performance metrics."""
        return {m: self.compute_metric(m) for m in metrics}

    def compute_metric(self, metric: str = "loss") -> float:
        """Wrapper to compute the performance metric."""
        if metric == "loss":
            return self.compute_loss()
        return self.compute_other_metric(metric)

    def compute_loss(self) -> float:
        """Compute the loss.

        The current implmentation basically computes the loss for each batch and then averages them.
        TODO we could potentially summarize the los across batches in a different way.
        Or sometimes we may potentially even have 1+ losses.
        """
        if self.loss_dict is None:
            raise ValueError("Loss function is not provided.")
        loss = 0.0
        with torch.no_grad():
            for x, y, _ in self.dataloader:
                try:
                    # Move input tensors to the same device as the model
                    device_x = {key: value.to(self.device) for key, value in x.items()}
                    device_y = {key: value.to(self.device) for key, value in y.items()}
                    # the loss_dict could be unpacked with ** and the function declaration handle it differently like **kwargs. to be decided, personally find this more clean and understable.
                    batch_combined = {**device_x, **device_y}
                    current_loss = self.model.inference(batch=batch_combined, **self.loss_dict)[0]
                except RuntimeError as e:
                    if ("CUDA out of memory" in str(e) and self.device.type == "cuda") or (
                        "MPS backend out of memory" in str(e) and self.device.type == "mps"
                    ):
                        logger.warning(f"{self.device.type.upper()} out of memory during loss computation: {e}")
                        logger.warning("Falling back to CPU for this batch")
                        temp_device = torch.device("cpu")
                        # Use CPU for this batch
                        x_cpu = {key: value.to(temp_device) for key, value in x.items()}
                        y_cpu = {key: value.to(temp_device) for key, value in y.items()}
                        # Move model to CPU temporarily
                        model_on_cpu = self.model.to(temp_device)
                        batch_combined = {**x_cpu, **y_cpu}
                        current_loss = model_on_cpu.inference(batch=batch_combined, **self.loss_dict)[0]
                        # Move model back to original device for next batches
                        try:
                            self.model = self.model.to(self.device)
                        except RuntimeError:
                            logger.warning(f"Failed to move model back to {self.device.type}. Staying on CPU.")
                            self.device = temp_device
                    else:
                        raise

                loss += current_loss.item()
        return loss / len(self.dataloader)

    def compute_other_metric(self, metric: str) -> float:
        """Compute the performance metric.

        # TODO currently we computes the average performance metric across target y, but maybe in the future we want something different
        """
        if not hasattr(self, "predictions") or not hasattr(self, "labels"):
            predictions, labels = self.predict(return_labels=True)
            self.predictions = predictions
            self.labels = labels

        # Explicitly type the labels and predictions as dictionaries with str keys
        labels_dict: dict[str, Tensor] = self.labels if isinstance(self.labels, dict) else {}
        predictions_dict: dict[str, Tensor] = self.predictions if isinstance(self.predictions, dict) else {}

        return sum(
            Performance(labels=labels_dict[k], predictions=predictions_dict[k], metric=metric).val for k in labels_dict
        ) / len(labels_dict)
