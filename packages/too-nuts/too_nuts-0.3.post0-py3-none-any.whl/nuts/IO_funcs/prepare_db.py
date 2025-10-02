"""
Module to prepare the database by adding the priorities for each event and
removing those that are outdated

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: init_db
.. autofunction:: clean_db

"""

import logging
import os
import pathlib as pl

from ..config.config import ToOConfig
from ..prioritization.prioritizer import ToOPrioritizer

# from .gen_from_csv import read_csv_table
from .too_database import DataBaseIO


def add_db(combined_db: DataBaseIO, additional_db: pl.Path) -> None:
    """Add events from an additional database to the combined database
    Note: there may be a more efficient way to do this by just adding the pandas dataframes

    Args:
        combined_db (DataBaseIO): PAth to the combined database
        additional_db (pl.Path): Path to the additional database
    """
    add_db = DataBaseIO(additional_db)
    add_db.read()
    db_events = add_db.get_events()
    for i in range(len(db_events)):
        combined_db.add_event(db_events[i])


def build_full_db(config: ToOConfig) -> None:
    """Initialize database from csv files, merge with previous database

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Tobias Heibegs (theibges@mines.edu)
    :Date: 2024-09-02

    Args:
        config (ToOConfig): Config file object
    """
    if config.settings.calculation.merge_listeners_database:
        # import databases from Catalogs/Listeners
        # and merge them with exiting TNS and GCN databases in Catalogs/Database
        listen_dir = config.files.listener.directory
        listen_databases = list(listen_dir.glob("*.csv"))
        for lis_db in listen_databases:
            lis_name = os.path.basename(lis_db)
            if lis_name == "TNS.csv":
                loc_db = DataBaseIO(config.files.database.tns)
                logging.info(f"Adding {lis_db} to TNS database")
            elif lis_name == "GCN.csv":
                loc_db = DataBaseIO(config.files.database.gcn)
                logging.info(f"Adding {lis_db} to GCN database")
            else:
                logging.error(
                    f"Error with {lis_db}, the corresponding database does not exist"
                )
            loc_db.read()
            try:
                add_db(loc_db, lis_db)
            except IndexError:
                logging.error(f"Error adding {lis_db} to TNS/GCN database")
                raise IndexError
            loc_db.write()

    # List of NuTS internal databses
    nuts_dbs = [config.files.database.combined, config.files.database.cleaned]

    # List of all databases in the directory
    db_dir = config.files.database.directory
    databases = list(db_dir.glob("*.csv"))

    # Create a new database to store the combined events
    combined_db = DataBaseIO(config.files.database.combined)
    for db in databases:
        if db not in nuts_dbs:
            logging.info(f"Adding {db} to Full database")
            db_file = pl.Path(db_dir) / db
            try:
                add_db(combined_db, db_file)
            except IndexError:
                logging.error(f"Error adding {db} to Full database")
                raise IndexError

    if combined_db.database is None or len(combined_db.database) == 0:
        logging.warning(
            f"No events found in the combined database: {config.files.database.combined} "
            "Please check the input databases."
        )
        exit(1)
    combined_db.write()


def clean_db(config: ToOConfig) -> None:
    """Delete outdated and uninteresting entries from the database and add a
    priority value to the alert

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-03-11

    Args:
        config (ToOConfig): Config file object
    """
    # Calculate time threshold that the transient has to be older than
    prioritizer = ToOPrioritizer(config)

    # Load events from combined database
    combined_db = DataBaseIO(config.files.database.combined)
    combined_db.read()
    all_events = combined_db.get_events()

    # Create a new database to store the cleaned events
    cleaned_db = DataBaseIO(config.files.database.cleaned)

    # Add the events with a priority value to the cleaned database
    for event in all_events:
        priority = prioritizer(event)
        if priority > 0:
            event.priority = priority
            cleaned_db.add_event(event)

    # Write the cleaned database to a csv file
    cleaned_db.write()
