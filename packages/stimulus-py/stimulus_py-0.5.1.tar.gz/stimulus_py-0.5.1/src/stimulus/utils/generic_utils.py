"""Utility functions for general purpose operations like seed setting and tensor manipulation."""

import random
from typing import Union

import numpy as np
import torch


def ensure_at_least_1d(tensor: torch.Tensor) -> torch.Tensor:
    """Function to make sure tensors given are not zero dimensional. if they are add one dimension."""
    if tensor.dim() == 0:
        tensor = tensor.unsqueeze(0)
    return tensor


def set_general_seeds(seed_value: Union[int, None]) -> None:
    """Set all relevant random seeds to a given value.

    Especially useful for hyperparameter tuning with Optuna.
    """
    # Set python seed
    random.seed(seed_value)

    # set numpy seed
    np.random.seed(seed_value)

    # set torch seed, diffrently from the two above torch can nopt take Noneas input value so it will not be called in that case.
    if seed_value is not None:
        torch.manual_seed(seed_value)
