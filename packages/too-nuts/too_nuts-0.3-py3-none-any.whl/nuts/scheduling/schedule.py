"""
Define scheduling class ToOSchedule.

Purpose: scheduling and keeping track of the schedule.
- Use to add sources to the source list. Raises an error when the scheduled times overlap.
- Use to outputs schedule into json files.

.. autosummary::
   :toctree:
   :recursive:

.. autoclass:: ToOSchedule
    :noindex:
    :members:
    :undoc-members:

"""

import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd
from astropy import units as u
from astropy.time import Time, TimeDelta

from ..config.config import ToOConfig
from ..IO_funcs.TSPRPST_database import TSPRPST_IO
from ..observation_period.observation import ObservationPeriod
from ..observation_period.source_observability import get_detector_pointing
from ..too_observation import ToOObservation


class ToOSchedule:
    """Scheduling class."""

    def __init__(
        self,
        config: ToOConfig,
        obs_period: list[Time],
    ):
        self.config = config
        self.num_scheduled_sources = 0
        self.max_num_sources = config.settings.scheduler.max_num_sources
        self.min_obs_t = config.settings.scheduler.min_obs_time
        self.rotation_time = config.settings.scheduler.rotation_time
        self.time_increment = config.settings.calculation.time_increment
        self.exclusive = config.settings.scheduler.exclusive

        self.schedule = pd.DataFrame(
            np.array(
                [
                    self.config._runtime.obs_times,
                    np.zeros_like(self.config._runtime.obs_times, dtype=bool),
                ]
            ).T,
            columns=["times", "allocated"],
        )
        self.schedule_times = self.config._runtime.obs_times.gps

        self.schedule["source"] = [[] for _ in range(len(self.schedule))]
        self.schedule_list = []

    def __call__(
        self,
        observation: ToOObservation,
        obs_window: ObservationPeriod,
    ) -> bool:
        """Add an event to the schedule and check that the time slot is still available

        Args:
            observation (ToOObservation): observation to be scheduled
            obs_window (ObservationPeriod): Observation window of this observation to be scheduled

        Raises:
            RuntimeError: Time slot is already allocated
            IndexError: Schedule is contains maximum number of sources
        """
        # Initialize quantities
        bool_scheduled = False

        # Make a source specific schedule
        available_times = self.config._runtime.obs_times
        allocated_times = np.zeros_like(available_times, dtype=bool)
        source_schedule = pd.DataFrame(
            np.array([available_times, allocated_times]).T,
            columns=["times", "allocated"],
        )

        # Calculate the times when the source is visible
        obs = np.logical_and(
            obs_window.start_time <= source_schedule["times"].to_numpy(),
            source_schedule["times"].to_numpy() <= obs_window.end_time,
        )
        obs = np.logical_and(self.schedule["allocated"] == False, obs)

        # Extract source coordinates for all observable times
        det_frames = self.config._runtime.obs_detector_frames
        tracked_source_full = observation.event.coordinates.transform_to(det_frames)
        tracked_source_loc = tracked_source_full[obs]

        # Determine if times are not contiguous
        timetest = Time(tracked_source_loc.obstime, format="isot", scale="utc")
        # Increment of 0.5*u.min arbitrary, chosen avoid precision issues
        timelim = TimeDelta(self.time_increment + 0.5 * u.min)
        ittime = np.argwhere(np.diff(timetest.jd) > timelim.jd)

        # Define array for successive observation windows
        itall = np.append([0], ittime)
        itall = np.append(itall, [len(timetest) - 1])
        itall = np.unique(np.sort(itall))

        # Avoid trying to schedule if not enough time available
        if len(itall) == 2 and itall[1] - itall[0] < 2:
            return bool_scheduled

        # Determine number of potential observation periods
        ilen = (len(itall) > 0) * len(itall)
        it = 0
        # Loop over potential observation periods
        while it < ilen - 1:
            # Define time period min and max times
            if np.isin(itall[it], ittime):
                idmin = itall[it] + 1
            else:
                idmin = itall[it]
            idmax = itall[it + 1] - 1
            timemin = timetest[idmin]
            timemax = timetest[idmax]

            # Determine if azimuth extent of observation larger than fov
            daz = tracked_source_loc.az.deg[idmin] - tracked_source_loc.az.deg
            daz[daz < 0] += 360
            diffaz = daz % 360 / self.config.settings.observation.fov_az.to("deg").value
            # If it is the case cut the observation and update array for observation windows
            if diffaz[idmax] > 1:
                idmax = np.argmin(np.abs(diffaz - 1)) - 1
                timemax = timetest[idmax]
                itall = np.append(itall, idmax + 1)
                itall = np.unique(np.sort(itall))

            # Adjust minimum observation time to provide time for repointing
            tfull = Time(tracked_source_full.obstime, format="isot", scale="utc")
            itfull = np.argmin(np.abs(tfull.jd - (timemin - self.rotation_time).jd))
            if itfull != 0:
                itfull_corr = len(
                    np.argwhere(
                        (self.schedule["allocated"][itfull:] == True)
                        * (tfull[itfull:] <= timemin)
                    )
                )
                timemin = tfull[itfull + itfull_corr] + self.rotation_time

            # Update observability condition
            obs_loc = (
                obs
                * (source_schedule["times"] >= timemin - 0.5 * u.min)
                * (source_schedule["times"] < timemax)
            )

            # Condition minimum obs time
            timebool = timemax - timemin >= self.min_obs_t
            # Condition number of repointings
            nsourcebool = self.num_scheduled_sources + 1 <= self.max_num_sources
            # If conditions are fulfilled, add source to schedule
            if timebool and nsourcebool:
                source_schedule["allocated"] = obs_loc
                obs_window.move_time = timemin - self.rotation_time
                self.num_scheduled_sources += 1
                logging.info(f"New source scheduled {observation}")
                self.schedule["allocated"] += source_schedule["allocated"]
                # Define local ToOObservation
                tooobsloc = ToOObservation()
                tooobsloc.event = observation.event
                tooobsloc.detector = observation.detector
                # Redefine observation properties, and pointing direction
                tooobsloc.observations = [
                    ObservationPeriod(
                        start_time=timemin,
                        start_loc=tracked_source_loc[idmin],
                        end_time=timemax,
                        end_loc=tracked_source_loc[idmax],
                        move_time=timemin - self.rotation_time,
                        pointing_dir=get_detector_pointing(
                            self.config, tracked_source_loc, idmin, idmax
                        ),
                    )
                ]
                self.schedule.loc[obs_loc, "source"] = tooobsloc
                self.schedule_list.append(tooobsloc)
                bool_scheduled = True

            # Update loop index
            it += 1
            ilen = (len(itall) > 0) * len(itall)

        return bool_scheduled

    def make_jsons(self, path_save):
        """Produce file to be read by UI."""
        obs_list = sorted(
            self.schedule_list, key=lambda obs: obs.observations[0].start_time.value
        )
        self.schedule_list = obs_list
        save_dict = [event.save_dict() for event in self.schedule_list]
        schedule = json.dumps(save_dict)

        with open(path_save, "w") as fp:
            fp.write(schedule)

    def add_event(
        self,
        event_id: str,
        locations: np.ndarray,
    ) -> bool:
        """Add an event to the schedule and check that the time slot is still available

        Args:
            observation (ToOObservation): observation to be scheduled
            obs_window (ObservationPeriod): Observation window of this observation to be scheduled

        Raises:
            RuntimeError: Time slot is already allocated
            IndexError: Schedule is contains maximum number of sources
        """

        times = Time(locations[:, 0]).gps
        mask = np.flatnonzero(np.isin(self.schedule_times, times))

        if self.exclusive and self.schedule["allocated"][mask].any():
            logging.error(
                f"Time slot is already allocated to another source. Event {event_id} cannot be scheduled."
            )
            return False

        self.schedule.loc[mask, "allocated"] = True
        for i in mask:
            self.schedule.loc[i, "source"].append(event_id)
        self.num_scheduled_sources += 1

        return True

    def save_schedule(self, path: Path) -> None:
        """Save schedule to json file.

        Args:
            path (str): path to save the schedule
        """
        logging.info(f"Saving schedule to {path}")
        self.schedule.to_csv(path, index=False)
