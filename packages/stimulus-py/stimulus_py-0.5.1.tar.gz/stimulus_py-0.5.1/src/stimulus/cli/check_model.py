#!/usr/bin/env python3
"""CLI module for checking model configuration and running initial tests."""

import logging
import os
from typing import Optional

import datasets
import optuna
import yaml

from stimulus.learner import optuna_tune
from stimulus.learner.device_utils import resolve_device
from stimulus.learner.interface import model_schema
from stimulus.utils import model_file_interface

logger = logging.getLogger(__name__)

MAX_SAMPLES = 1000
COMPUTE_OBJECTIVE_EVERY_N_SAMPLES = 100
N_TRIALS = 5


def check_model(
    data_path: str,
    model_path: str,
    model_config_path: str,
    optuna_results_dirpath: str = "./optuna_results",
    force_device: Optional[str] = None,
) -> tuple[str, str]:
    """Run the main model checking pipeline.

    Args:
        data_path: Path to input data file.
        model_path: Path to model file.
        model_config_path: Path to model config file.
        optuna_results_dirpath: Directory for optuna results.
        force_device: Force the device to use.
    """
    dataset_dict = datasets.load_from_disk(data_path)
    dataset_dict.set_format("torch")
    train_dataset = dataset_dict["train"]
    validation_dataset = dataset_dict["test"]
    logger.info("Dataset loaded successfully.")

    model_class = model_file_interface.import_class_from_file(model_path)

    logger.info("Model class loaded successfully.")

    with open(model_config_path) as file:
        model_config_content = yaml.safe_load(file)
        model_config = model_schema.Model(**model_config_content)

    logger.info("Model config loaded successfully.")

    base_path = optuna_results_dirpath
    artifact_path = optuna_results_dirpath + "/artifacts"
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(artifact_path, exist_ok=True)
    artifact_store = optuna.artifacts.FileSystemArtifactStore(base_path=artifact_path)
    storage = optuna.storages.JournalStorage(
        optuna.storages.journal.JournalFileBackend(f"{base_path}/optuna_journal_storage.log"),
    )

    device = resolve_device(force_device=force_device, config_device=model_config.device)
    objective = optuna_tune.Objective(
        model_class=model_class,
        network_params=model_config.network_params,
        optimizer_params=model_config.optimizer_params,
        data_params=model_config.data_params,
        loss_params=model_config.loss_params,
        train_torch_dataset=train_dataset,
        val_torch_dataset=validation_dataset,
        artifact_store=artifact_store,
        max_samples=model_config.max_samples,
        compute_objective_every_n_samples=model_config.compute_objective_every_n_samples,
        target_metric=model_config.objective.metric,
        device=device,
    )

    logger.info(f"Objective: {objective}")
    study = optuna_tune.tune_loop(
        objective=objective,
        pruner=optuna.pruners.MedianPruner(n_warmup_steps=2, n_startup_trials=2),
        sampler=optuna.samplers.TPESampler(),
        n_trials=N_TRIALS,
        direction=model_config.objective.direction,
        storage=storage,
    )
    if study is None:
        raise ValueError("Study is None")
    logger.info(f"Study: {study}")
    logger.info(f"Study best trial: {study.best_trial}")
    logger.info(f"Study direction: {study.direction}")
    logger.info(f"Study best value: {study.best_value}")
    logger.info(f"Study best params: {study.best_params}")
    logger.info(f"Study trials count: {len(study.trials)}")

    for artifact_meta in optuna.artifacts.get_all_artifact_meta(study_or_trial=study):
        logger.info(artifact_meta)
    # Download the best model
    trial = study.best_trial
    best_artifact_id = trial.user_attrs["model_id"]
    file_path = trial.user_attrs["model_path"]
    optuna.artifacts.download_artifact(
        artifact_store=artifact_store,
        file_path=file_path,
        artifact_id=best_artifact_id,
    )

    logger.info(f"Best model downloaded successfully to {file_path}")

    return base_path, file_path
