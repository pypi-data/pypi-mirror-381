"""
Prepare the list of observable sources.

Run during the day
Run when important alerts occur during the night to update observing schedule
"""

import logging
import os
import sys
from importlib import reload

import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
from too_parser.balloon_motion.balloon_init import balloon_init
from too_parser.config import config_parser
from too_parser.IO_funcs.prepare_db import clean_db
from too_parser.operation.too_obs_time import time_window
from too_parser.scheduling.scheduling import get_observations, get_schedule
from too_parser.visualization.too_skymap import visualize_observations

# from too_parser.IO_funcs.prepare_db import add_transients_to_db
# from too_parser.IO_funcs.prepare_db import delete_db_table
# from too_parser.IO_funcs.prepare_db import combine_db_tables


def main(config: dict, time_in: atime.Time, plot_trajectories: bool) -> None:
    """Update database, compute observing schedule and visualize results."""
    fout_name = (
        config["Outputs"]["out_dir"]
        + "logfiles/log_"
        + time_in.isot[:-10]
        + time_in.isot[-9:-7]
        + time_in.isot[-6:-4]
        + ".txt"
    )
    reload(logging)
    logging.basicConfig(
        filename=fout_name,
        level=logging.INFO,
        filemode="w",
        format="%(message)s",
    )
    logging.info("Starting scheduling software...")
    logging.info("Date chosen: " + str(time_in.isot))

    logging.info("\n***************************************************")
    logging.info("Computing observing schedule...")
    make_observable_list(config, time_in, plot_trajectories)


def make_observable_list(config: dict, start_time, bool_traj):
    """Make list of observable sources."""
    event_dir = config["Database"]["database_dir"] + "/"
    event_db = config["Database"]["database_name"]
    # event_db_table = config["Database"]["Combined_table"]
    # events = read_db.read_database(event_dir, event_db, event_db_table)

    # Make a balloon object to represent the detector
    balloon = balloon_init(config)

    # Information about observation window
    s_time, e_time = time_window(config, start_time, balloon)

    # Delete outdated and non interesting entries from the database
    # and add a priority value to the alert

    # logging.info("\n***************************************************")
    # logging.info("Archiving database from previous day...")
    # archive_db(input_dir, input_db, input_db_table, time_in)

    # logging.info("\n***************************************************")
    # logging.info("Adding sources added by hand (ATels and others)...")
    # add_transients_to_db(config, event_dir, event_db)

    # logging.info("\n***************************************************")
    # logging.info("Removing old sources from database tables...")
    # clean_db(config, input_dir, input_db, time_in)

    # logging.info("\n***************************************************")
    # logging.info("Deleting combined table...")
    # delete_db_table(event_dir, event_db, event_db_table)

    # logging.info("\n***************************************************")
    # logging.info("Creating new combined table...")
    # combine_db_tables(config, event_dir, event_db)

    logging.info("\n***************************************************")
    logging.info("Removing old sources from database tables...")
    clean_db(config, event_dir, event_db, start_time)

    # Create directory for outputs
    str_time = start_time.isot[:-13]
    dir_save = config["Outputs"]["out_dir"] + "outfiles_" + str_time + "/sources/"
    if not os.path.exists(dir_save):
        os.makedirs(dir_save)

    # Compute list of observable sources
    get_observations(
        config, event_dir, event_db, dir_save, s_time, e_time, balloon, bool_traj
    )


if __name__ == "__main__":
    config_path = sys.argv[1]
    time_schedule = atime.Time(sys.argv[2], format="isot", scale="utc")
    plot_traj = bool(sys.argv[3] == "True")
    config = config_parser.load_config(config_path)
    main(config, time_schedule, plot_traj)
