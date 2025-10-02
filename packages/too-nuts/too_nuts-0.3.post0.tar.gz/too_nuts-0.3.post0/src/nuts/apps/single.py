"""
This module contains the main function to run the scheduler.
"""

import logging

import astropy.units as u
import click
from astropy.time import Time

from ..compute import Compute
from ..config.config import ToOConfig
from ..config.load_config import load_config
from ..config.logging_setup import setup_logging
from ..IO_funcs.too_database import DataBaseIO
from ..too_event import ToOEvent


@click.command()
@click.argument("config_path", type=click.Path(exists=True))
@click.option("--log-dir", "-log", default="./logs", help="Directory to save log files")
@click.option("--log-level", "-ll", default="INFO", help="Log level")
@click.option("--RA", "-ra", default="0", help="Right Ascension")
@click.option("--DEC", "-dec", default="0", help="Declination")
@click.option(
    "--detection_time",
    "-dt",
    default="2023-05-13T00:00:00.000",
    help="Source Detection Time",
)
@click.option("--event_id", "-eid", default="None", help="Event id")
@click.option("--event_type", "-etype", default="None", help="Event Type")
@click.option("--publisher", "-pub", default="None", help="Publisher")
@click.option("--publisher_id", "-pubid", default="SingleSource", help="Publisher id")
@click.option("--priority", "-prio", default="1", help="Event Priority")
@click.option("--redshift", "-z", help="Source Redshift")
@click.option("--distance", "-dL", help="Source Distance in pc")
def single(
    config_path: str,
    log_level: str,
    log_dir: str,
    ra: str,
    dec: str,
    detection_time: str,
    event_id: str,
    event_type: str,
    publisher: str,
    publisher_id: str,
    priority: str,
    redshift: float,
    distance: float,
) -> None:
    """
    Build a single source event.
    """
    build_single(
        config_path,
        ra,
        dec,
        detection_time,
        event_id,
        event_type,
        publisher,
        publisher_id,
        priority,
        redshift,
        distance,
        log_level,
        log_dir,
    )


def build_single(
    config_path: str,
    ra: str,
    dec: str,
    detection_time: str,
    event_id: str,
    event_type: str,
    publisher: str,
    publisher_id: str,
    priority: str,
    redshift: float,
    distance: float,
    log_level: str = "INFO",
    log_dir: str = "./logs",
) -> None:
    """Update database, compute observing schedule and visualize results."""

    options = ["obs-window", "observability", "visuals"]

    # Set up logging
    setup_logging(f"run_{options}.log", log_dir, log_level)

    # Parse config in out dir
    config: ToOConfig = load_config(config_path)
    logging.info(f"Config file: {config_path}")

    config.files.database.cleaned = "single_source.csv"

    # build single source db
    event = ToOEvent()
    event.set_coordinates(float(ra), float(dec), units="deg")
    event.set_time(detection_time)
    event.event_id = event_id
    event.event_type = event_type
    event.publisher = publisher
    event.publisher_id = publisher_id
    event.priority = int(priority)
    event.params["redshift"] = redshift
    event.params["distance"] = distance

    database = DataBaseIO(config.files.database.cleaned)
    database.add_event(event)
    database.write()

    # Run NUTS
    compute = Compute(config)
    results = compute(options)
    return results
