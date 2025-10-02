"""Module for creating a config file from the command line.

.. autosummary::

   make_config


"""

import warnings
from pathlib import Path

import click
import tomli_w

from ..config.config import ToOConfig


def create_toml(filename: str, c: ToOConfig):
    with open(filename, "wb") as f:
        tomli_w.dump(c.model_dump(), f)


@click.command()
@click.argument(
    "config_path",
    type=str,
    default="./config.toml",
    required=True,
)
@click.argument(
    "catalog_dir",
    default="./Catalogs",
)
def make_config(config_path: str, catalog_dir: str) -> None:
    """Create a new config file."""
    build_make_config(config_path, catalog_dir)


def build_make_config(config_path: str, catalog_dir: str) -> None:
    """Function to copy the config file from the default location to the user defines location.
    :Author: Claire Guepin
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-02-14

    Args:
        config_path (str): path for the new config file
        catalog_dir (str): path to the directory where the catalog files are stored.
    """

    build_config(config_path, catalog_dir)


def build_config(config_path: str, catalog_dir: str) -> None:
    """Function to copy the config file from the default location to the user defines location.
    :Author: Claire Guepin
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-02-14

    Args:
        config_path (str): path for the new config file
        catalog_dir (str): path to the directory where the catalog files are stored
    """

    # Create directory for outputs
    config_filename = Path(config_path).resolve()
    if config_filename.exists():
        print(f"Config file {config_filename} already exists. No changes made.")
        return

    # Ensure the directory exists
    catalog_dir = Path(catalog_dir).resolve()
    if not catalog_dir.exists():
        print(
            f"Error: Catalog directory {catalog_dir} does not exist. Please run `nuts init` first to create the necessary directory structure."
        )
        catalog_dir.mkdir(parents=True, exist_ok=True)

    config = ToOConfig()
    # Edit the path to the catalog directory
    config.files.global_path = str(catalog_dir)
    # Create the config file
    create_toml(config_filename, config)
