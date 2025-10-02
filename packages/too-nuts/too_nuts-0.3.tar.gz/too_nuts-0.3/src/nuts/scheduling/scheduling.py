"""
Compute the observation schedules.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: get_schedule

"""

import logging

from ..config.config import ToOConfig
from ..IO_funcs.TSPRPST_database import TSPRPST_IO
from ..scheduling import schedule_strategies as strat
from ..scheduling.schedule import ToOSchedule
from ..too_observation import ToOObservation


def get_schedule(config: ToOConfig, observables: list[ToOObservation]) -> None:
    """Compute observation schedule.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-09-04

    Args:
        config: configuration file
        observables: list of observations

    """
    logging.info("***************************************************")
    logging.info("Determine schedule...")
    observation_period = [
        config._runtime.observation_starts,
        config._runtime.observation_ends,
    ]
    schedule = ToOSchedule(
        config,
        observation_period,
    )

    # Load strategy parameters
    strategy_priority_sort = config.settings.scheduler.strategy_priority_sort
    strategy_obstime = config.settings.scheduler.strategy_obstime
    strategy_obsprev = config.settings.scheduler.strategy_obsprev
    strategy_priority_max = int(config.settings.scheduler.strategy_priority_max)

    strat.strategy_base(
        config,
        schedule,
        observables,
        strat_obstime=strategy_obstime,
        strat_obsprev=strategy_obsprev,
        sort=strategy_priority_sort,
        max_prior=strategy_priority_max,
    )

    schedule.save_schedule(config.output.observations.schedule_file)
    schedule.make_jsons(config.output.observations.scheduled_file)

    return schedule
