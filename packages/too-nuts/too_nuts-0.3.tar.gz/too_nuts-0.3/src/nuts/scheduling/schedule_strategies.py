"""
Build the schedules.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: schedule_windows
.. autofunction:: schedule_earliest_window
.. autofunction:: strategy_flat
.. autofunction:: strategy_distribute
.. autofunction:: strategy_base

"""

import logging

import numpy as np

from nuts.too_observation import ToOObservation

from ..config.config import ToOConfig
from ..IO_funcs.json_input import load_observable_sources
from ..IO_funcs.TSPRPST_database import TSPRPST_IO
from .schedule import ToOSchedule


def schedule_windows(schedule: ToOSchedule, observation: ToOObservation) -> bool:
    """Schedule all observation windows for a source (possible double observation in one night)

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-01-01

    Args:
        schedule (ToOSchedule): scheduling object
        observation (ToOObservation): Observation to schedule
    """
    for obs_window in observation.observations:
        while schedule.num_scheduled_sources + 1 <= schedule.max_num_sources:
            try:
                bool_scheduled = schedule(observation, obs_window)
                return bool_scheduled
            except RuntimeError:
                logging.warning(f"Collision in scheduling of source {observation}")


def schedule_earliest_window(
    schedule: ToOSchedule, observation: ToOObservation
) -> None:
    """Schedule the earliest observation windows for a source. If that doesn't work move to next source

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-01-01

    Args:
        schedule (ToOSchedule): scheduling object
        observation (ToOObservation): Observation to schedule
    """
    try:
        schedule(observation, observation.observations[0])
    except RuntimeError:
        logging.warning(f"Collision in scheduling of source {observation}")


def sort_observations(
    observations: TSPRPST_IO,
) -> list[ToOObservation]:
    """Sort all of the observations using priotities and observation times.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-03-12

    Args:
        observations (list[ToOObservation]): list of observable sources

    Returns:
        list[ToOObservation]: ordered list of observable sources
    """
    obs_prior = [np.array([]) for i in range(9)]
    obs_times = [np.array([]) for i in range(9)]
    for observation in observations:
        prior = observation.event.priority
        obs_prior[prior] = np.append(obs_prior[prior], observation)
        obs_times[prior] = np.append(
            obs_times[prior],
            (
                observation.observations[0].end_time.gps
                - observation.observations[0].start_time.gps
            ),
        )
    observations.clear()
    # For each tier sort according to the observation time
    for tier in range(len(obs_times)):
        arg_sort = np.argsort(np.array(obs_times[tier]))[::-1]
        obs_times[tier] = np.take_along_axis(obs_times[tier], arg_sort, axis=0)
        obs_prior[tier] = np.take_along_axis(obs_prior[tier], arg_sort, axis=0)
        observations.append(obs_prior[tier])
    observations = np.concatenate(observations)
    return observations


def strategy_flat(
    schedule: ToOSchedule,
    observations: TSPRPST_IO,
    max_priority: int = 10,
) -> list[ToOObservation]:
    """Create the schedule following the source list order.

    Without/with accounting for priorities if sort=False/sort=True.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-01-01

    Args:
        schedule (ToOSchedule): Scheduling object
        observations (list[ToOObservation]): List of observable sources
        max_priority (int, optional): Maximum priority before stopping the scheduling. Defaults to 10.

    Returns:
        list[ToOObservation]: list of remaining observable sources
    """
    # Loop over all sources and try to schedule both observation windows
    for observation in observations:
        if observation.event.priority < max_priority:
            try:
                schedule_windows(schedule, observation)
                observations.remove(observation)
            except IndexError:
                logging.warning("Schedule is filled, abort scheduling")
                return []

    return observations


def strategy_distribute(
    schedule: ToOSchedule,
    observations: TSPRPST_IO,
    max_iter: int = 500,
) -> list[ToOObservation]:
    """Create the schedule following the source list order.

    Select one source of each tier until the schedule is filled.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-01-01

    Args:
        schedule (ToOSchedule): Scheduling object
        observations (ToOObservation): List of observable sources
        max_iter (int, optional): Maximum number of iterations on distributing the sources. Defaults to 50.

    Returns:
        list[ToOObservation]: list of remaining observable sources
    """
    # Loop over observations and select one in each tier.
    # Once successfully scheduled move to next tier and disregard
    # other sources in this tier.
    # Repeat until either schedule is full or all observations
    # are distributed or max num of iterations is reached.
    i = 0
    current_priority = 0
    while len(observations) > 0 and i < max_iter:
        i += 1
        current_priority = int(current_priority % 8) + 1
        iter = 0
        while iter < len(observations):
            observation = observations[iter]
            if int(observation.event.priority) == current_priority:
                try:
                    bool_scheduled = schedule_windows(schedule, observation)
                    observations.remove(observation)
                    if bool_scheduled:
                        break
                    else:
                        iter -= 1
                except IndexError:
                    logging.warning("Schedule is filled, abort scheduling")
                    return []
            iter += 1

    return observations


def strategy_base(
    config: ToOConfig,
    schedule: ToOSchedule,
    observations: ToOObservation,
    sort: bool = False,
    strat_obstime: bool = False,
    strat_obsprev: bool = False,
    max_prior: int = 3,
    max_iter: int = 500,
) -> list[ToOObservation]:
    """Create the schedule following the source list order.

    Select all sources in first tiers < max_prior,
    and one source of each tier >= max_prior until the schedule is filled.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-01-01

    Args:
        config: configuration file
        schedule (ToOSchedule): Scheduling object
        observations (ToOObservation): List of observable sources
        sort (bool, optional): Sort observations according to priority.
        strat_obstime (bool, optional): Sort observations according to observable time.
        strat_obstime (bool, optional): Try to schedule previously observed sources.
        max_priority (int, optional): Maximum priority before stopping the scheduling. Defaults to 3.
        max_iter (int, optional): Maximum number of iterations on distributing the sources. Defaults to 50.

    Returns:
        list[ToOObservation]: list of remaining observable sources
    """
    # Sort observations according to their priority
    if sort:
        observations = sorted(observations)

    # Loop over all sources in the first n < max_prior tiers and try to schedule them
    observations = strategy_flat(schedule, list(observations), max_priority=max_prior)

    if strat_obsprev:
        # Path of previously observed sources
        previous_obs_path = config.output.previous_observation_path
        try:
            # Load list of previously observed sources
            prev_obs = load_observable_sources(previous_obs_path)
            # Determine if they are in the list of observable sources
            for i in range(len(prev_obs)):
                for observation in observations:
                    if observation.event.publisher_id == prev_obs[i].event.publisher_id:
                        try:
                            schedule_windows(schedule, observation)
                            observations.remove(observation)
                        except IndexError:
                            logging.warning("Schedule is filled, abort scheduling")
                            return []
        except FileNotFoundError:
            logging.error(
                "List of previously observed sources not found there: {previous_obs_path}."
            )

    if strat_obstime:
        observations = sort_observations(observations)

    # Loop over remaining sources and try to select one from each tier
    observations = strategy_distribute(schedule, list(observations), max_iter=max_iter)
