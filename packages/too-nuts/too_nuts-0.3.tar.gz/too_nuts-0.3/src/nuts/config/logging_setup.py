"""Module to set up logging
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-03-11
"""

import logging
import pathlib as pl


def setup_logging(log_file: str, log_dir: str, log_level: str = "INFO"):
    """Set up logging

    Args:
        listener (str): _description_
        log_dir (str): _description_
        log_level (str, optional): _description_. Defaults to "INFO".
    """
    logging_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    # Define log file
    log_dir = pl.Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / f"{log_file}"
    logging.basicConfig(
        level=logging_levels[log_level.upper()],
        format="%(levelname)s - %(asctime)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        force=True,
    )
