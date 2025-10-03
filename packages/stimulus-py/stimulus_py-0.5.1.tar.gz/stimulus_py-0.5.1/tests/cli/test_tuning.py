# mypy: disable-error-code="unused-ignore"
"""Test the tuning CLI."""

import json
import logging
import os
import shutil
import tempfile
from pathlib import Path

import pytest
import safetensors

from stimulus.cli import tuning
from stimulus.utils import model_file_interface

logger = logging.getLogger(__name__)


@pytest.fixture
def data_path() -> str:
    """Get path to test data CSV file."""
    return str(
        Path(__file__).parent.parent / "test_data" / "titanic_performant" / "titanic_encoded_hf",
    )


@pytest.fixture
def model_path() -> str:
    """Get path to test model file."""
    return str(Path(__file__).parent.parent / "test_model" / "titanic_perf_model.py")


@pytest.fixture
def model_config() -> str:
    """Get path to test model config YAML."""
    return str(Path(__file__).parent.parent / "test_model" / "titanic_perf_model.yaml")


def test_tuning_main(
    data_path: str,
    model_path: str,
    model_config: str,
) -> None:
    """Test that tuning.tune runs without errors."""
    # Verify all required files exist
    with tempfile.TemporaryDirectory() as temp_dir:
        assert os.path.exists(data_path), f"Data file not found at {data_path}"
        assert os.path.exists(model_path), f"Model file not found at {model_path}"
        assert os.path.exists(model_config), f"Model config not found at {model_config}"

        results_dir = Path(temp_dir) / "test_results" / "test_tuning"
        results_dir.mkdir(parents=True, exist_ok=True)

        best_model_path = os.path.join(temp_dir, "best_model.safetensors")
        best_optimizer_path = os.path.join(temp_dir, "best_optimizer.pt")
        best_config_path = os.path.join(temp_dir, "best_config.json")
        try:
            tuning.tune(
                data_path=data_path,
                model_path=model_path,
                model_config_path=model_config,
                optuna_results_dirpath=temp_dir,
                best_model_path=str(best_model_path),
                best_optimizer_path=str(best_optimizer_path),
                best_config_path=str(best_config_path),
            )

            # Check that output files were created
            assert os.path.exists(best_model_path), "Best model file was not created"
            assert os.path.exists(best_optimizer_path), "Best optimizer file was not created"
            assert os.path.exists(best_config_path), "Best config file was not created"

            with open(best_config_path) as f:
                full_config = json.load(f)

            # Check that the model can be loaded
            model = model_file_interface.import_class_from_file(model_path)
            model_instance = model(**full_config["network_params"])
            assert model_instance is not None, "Model could not be loaded"

            log = safetensors.torch.load_model(model_instance, best_model_path)  # type: ignore[attr-defined]
            logger.info(f"Log: {log}")

        finally:
            # Clean up
            shutil.rmtree(temp_dir, ignore_errors=True)
