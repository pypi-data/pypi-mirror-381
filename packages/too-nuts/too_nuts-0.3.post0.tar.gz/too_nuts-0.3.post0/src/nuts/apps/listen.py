"""
Module to run the GCN and TNS listeners via the command line interface.
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-03-11
"""

import logging
import time as t

import click

from ..alert_listeners import GCN_listener, TNS_download, TNS_parser
from ..config.config import ToOConfig
from ..config.load_config import load_config
from ..config.logging_setup import setup_logging
from ..IO_funcs.too_database import DataBaseIO


def GCN(config: ToOConfig):
    """Function to run the GCN listener in an endless loop.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-03-11

    Args:
        config (ToOConfig): Configuration object
    """
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG
    )

    # Initialize listener script
    listener = GCN_listener.GCN_listener(config)

    # Run the listener in an endless loop
    # COMMENT: unsure if this works perfectly, more real time testing required.
    while True:
        alert_file = listener()
        if alert_file is not None:
            too_event = listener.parse_alert(alert_file)
            if too_event is not None:
                GCN_database = DataBaseIO(config.files.listener.gcn_file)
                try:
                    GCN_database.read()
                except FileNotFoundError:
                    logging.error("FILE GCN.csv DOES NOT EXIST. CREATE FILE.")
                GCN_database.add_event(too_event)
                GCN_database.write()
        t.sleep(2)


def TNS(config: ToOConfig):
    """Function to run the TNS listener in an endless loop.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-03-11

    Args:
        config (ToOConfig): Configuration object
    """
    update_period = config.settings.tns.update_period
    while True:
        tns_filename = TNS_download.search_tns(config)
        tns_events = TNS_parser.read_TNS_table(
            tns_filename, config.files.listener.tns_file
        )
        TNS_parser.save_list(config, tns_events)
        t.sleep(update_period.to("s").value)


@click.command()
@click.argument("config_path", type=click.Path(exists=True))
@click.option(
    "--listener",
    "-l",
    type=click.Choice(["GCN", "TNS"], case_sensitive=False),
)
@click.option("--log-dir", "-log", default="./logs", help="Directory to save log files")
@click.option("--log-level", "-ll", default="INFO", help="Log level")
def listen(config_path: str, listener: str, log_level: str, log_dir: str) -> None:
    """Run the specified alert listener."""
    build_listen(config_path, listener, log_level, log_dir)


def build_listen(
    config_path: str, listener: str, log_level: str = "INFO", log_dir: str = "./logs"
) -> None:
    """Run listeners to collect alerts from GCN and TNS.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-03-11

    Args:
        config_path (str): Path to the configuration file
        listener (str): Listener name GCN or TNS
        log_level (str): logging level
        log_dir (str): Directory to save log files
    """
    # Set up logging
    setup_logging(f"listener_{listener}.log", log_dir, log_level)

    # Check listener name was specified
    if listener is None:
        logging.error("Please specify a listener from 'GCN' or 'TNS'")
        return

    # Parse config in out dir
    config = load_config(config_path)

    # Run listener
    logging.info("Start listener...")
    if listener == "GCN":
        GCN(config)
    elif listener == "TNS":
        TNS(config)
    else:
        logging.error("Listener not recognized")
        return
