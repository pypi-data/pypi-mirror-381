"""Compute and save list of observable sources using database as input

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: save_json_out
.. autofunction:: get_observations

"""

import logging
import os

import numpy as np

from ..config.config import ToOConfig
from ..IO_funcs.json_output import save_json_out
from ..IO_funcs.too_database import DataBaseIO
from ..IO_funcs.TSPRPST_database import TSPRPST_IO
from ..too_observation import ToOObservation


def get_observations(config: ToOConfig) -> TSPRPST_IO:
    """Compute a list of observable sources.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-09-02

    Args:
        config (dict): config file

    Returns:
        list[ToOObservation]: list of observable sources
    """
    logging.info("***************************************************")
    logging.info("Compute observability of sources from database...")

    # Load alerts from 'Full' schedule list
    database = DataBaseIO(config.files.database.cleaned)
    database.read()
    events = database.get_events()

    tpsrspt = TSPRPST_IO(
        config.output.observations.nss_output_file,
    )
    tpsrspt.add_detector(
        config._runtime.obs_times,
        config._runtime.detector,
    )
    # Calculate when sources are visible
    observations = []
    too_observations_dict = []
    too_observables_dict = []
    logging.info("Determine observability of sources...")
    for count in range(len(events)):
        logging.info(f"Processing event: {count + 1} / {len(events)}")
        observation = ToOObservation()
        observation.event = events[count]
        tracked_source_loc, visibility_cuts = observation.get_observation_periods(
            config
        )
        too_observations_dict.append(observation.save_dict())
        if np.any(visibility_cuts) > 0:
            logging.info(f"Observable Event: {str(observation)}")
            tpsrspt.add_event(
                observation.event,
                config._runtime.obs_times[visibility_cuts],
                tracked_source_loc[visibility_cuts],
            )
            observations.append(observation)
            too_observables_dict.append(observation.save_dict())
        else:
            logging.info(f"Event not observable: {str(observation)}")

    # Directory for outputs
    if not os.path.exists(config.output.observations.directory):
        os.makedirs(config.output.observations.directory)

    # Write observation results to files
    logging.info("All sources")
    save_json_out(too_observations_dict, config.output.observations.all_file)

    logging.info("Observable sources")
    save_json_out(too_observables_dict, config.output.observations.observable_file)

    # Write TSSPT database
    tpsrspt.write()
    return tpsrspt, observations
