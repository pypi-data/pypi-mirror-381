"""Module to load the toml config file if it is provided. If not, the
default config file is loaded.
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-06-06
"""

import logging
import os

import toml
import tomli_w

from .config import ToOConfig


def load_config(config_path: str) -> dict:
    """Function to load the config file
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-06-05

    Args:
        config_path (str): Path to the config file

    Raises:
        FileNotFoundError: In case the config file is not found

    Returns:
        dict: Dictionary containing the config file data
    """
    if not os.path.exists(config_path):
        logging.error(f"Config file not found: {config_path}")
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path) as f:
        c = toml.load(f)
        return ToOConfig(**c)
