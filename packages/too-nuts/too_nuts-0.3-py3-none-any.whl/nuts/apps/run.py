"""
This module contains the main function to run the scheduler.
"""

import logging

import click

from ..compute import Compute, Sequences
from ..config.load_config import load_config
from ..config.logging_setup import setup_logging


@click.command()
@click.argument("config_path", type=click.Path(exists=True))
@click.option(
    "--options",
    "-o",
    type=click.Choice(
        Sequences.__members__,
        case_sensitive=False,
    ),
)
@click.option("--log-level", "-ll", default="INFO", help="Log level")
def run(config_path: str, options: str, log_level: str) -> None:
    """Run the NUTS pipeline."""
    build_run(config_path, options, log_level)


def build_run(config_path: str, options: str, log_level: str = "INFO") -> None:
    """Update database, compute observing schedule and visualize results."""
    # Parse config in out dir
    config = load_config(config_path)
    # Set up logging
    setup_logging(f"run_{options}.log", config.output.directory, log_level)
    logging.info(f"Config file: {config_path}")

    # Run NUTS
    compute = Compute(config)
    return compute(options)
