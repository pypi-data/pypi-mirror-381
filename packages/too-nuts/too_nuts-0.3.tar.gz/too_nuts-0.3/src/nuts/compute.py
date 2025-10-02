"""
Prepare the list of observable sources.

Run during the day
Run when important alerts occur during the night to update observing schedule
"""

import logging
import os
from enum import Enum

import astropy.units as u
import numpy as np
import toml
from astropy.coordinates import AltAz
from astropy.time import Time

from .config.config import ToOConfig
from .config.logging_setup import setup_logging
from .detector_motion.detector_init import detector_init
from .IO_funcs.json_input import load_observable_sources
from .IO_funcs.prepare_db import build_full_db, clean_db
from .observation_period.observability import get_observations
from .observation_period.sun_moon_cuts import (
    FoVCuts,
    PointingFoVCuts,
    SunMoonCuts,
    moon_illumination,
)
from .observation_period.too_obs_time import get_observation_windows
from .poorly_localized.poorly_localized import gw_localization_pointing
from .scheduling.scheduling import get_schedule
from .visualization.plot_detloc import fig_detector_position
from .visualization.plot_flight import fig_stat_flight
from .visualization.plot_obs_window import fig_observability_windows
from .visualization.plot_skymap import visualize_sources, visualize_sources_obs_sched
from .visualization.plot_trajectories import (
    fig_trajectories,
    fig_trajectories_scheduled,
)


class Sequences(Enum):
    obs_window: list = ["obs-window"]
    combine_db: list = ["obs-window", "combine-db"]
    clean_db: list = ["obs-window", "clean-db"]
    prep_db: list = ["obs-window", "combine-db", "clean-db"]
    observability: list = ["obs-window", "observability"]
    observations: list = ["obs-window", "combine-db", "clean-db", "observability"]
    schedule: list = ["obs-window", "schedule", "visuals"]
    obs_sched: list = ["obs-window", "obs-sched", "visuals"]
    gw: list = ["obs-window", "gw_obs"]
    pointing_obs: list = [
        "obs-window",
        "combine-db",
        "clean-db",
        "pointing-fov",
        "observability",
    ]
    visuals: list = ["obs-window", "visuals"]
    all: list = ["obs-window", "combine-db", "clean-db", "obs-sched", "visuals"]
    obs_windows_all: list = ["calc-obs-period"]
    flight: list = ["flight-calc"]


class Compute:
    def __init__(self, config: ToOConfig):

        # Load the configuration file
        self.config: ToOConfig = config
        self.n_observation_windows: int = (
            config.settings.calculation.num_observation_windows
        )
        self.calc_start_time: Time = config.settings.calculation.start_time
        self.calc_period: u.Quantity = config.settings.calculation.calculation_period
        self.calc_increment: u.Quantity = config.settings.calculation.time_increment
        self.calc_end_time: Time = self.calc_start_time + self.calc_period
        # True if observations windows exist
        self.flag_obs = False

        # Functions that can be run independently in order to
        # calculate the observability of sources. These are the
        # basic building blocks for the scheduling software and
        # can be toggled on or off depending on the use case. Note
        # that the order of the functions is important.
        self.options = {
            "obs-window": self.get_observation_windows,
            "combine-db": build_full_db,
            "clean-db": clean_db,
            "observability": get_observations,
            "schedule": self.compute_schedule,
            "obs-sched": self.compute_observability_schedule,
            "pointing-fov": self.pointing_fov_cuts,
            "calc-obs-period": self.calc_observation_period,
            "visuals": self.create_visuals,
            "gw_obs": self.run_GW,
            "flight-calc": self.flight_calculation,
        }

        # A sequence is a list of options that
        # are run consecutively. There are several predefined sequences
        # or can be user provided from the config file
        self.sequences = Sequences

    def build(self) -> None:
        """Build derived quantities for the computation."""
        logging.info("Building derived quantities (this may take a while) ...")

        # Build array of times for the calculations
        self.times = self.build_times()

        # Build detector configuration
        # Maybe rename to detector_init? Could be moved to config
        self.detector = detector_init(self.config)
        self.detector_frames = AltAz(
            obstime=self.times, location=self.detector.loc(self.times)
        )

        # Calculate timeperiods when an observation may be possible
        self.sun_moon_cuts = SunMoonCuts(self.config)
        self.night_conditions = self.sun_moon_cuts(
            detector_frame=self.detector_frames, time=self.times
        )

        if self.n_observation_windows == "all":
            self.n_observation_windows = len(
                get_observation_windows(
                    self.night_conditions, self.times, one_window=False
                )[0]
            )

    def runtime_params(self) -> None:
        self.config._runtime.fov_cuts = FoVCuts(self.config)
        self.config._runtime.all_times = self.times
        self.config._runtime.detector = self.detector
        self.config._runtime.detector_frames = self.detector_frames

    def __call__(self, sequence: str | list[str]) -> None:

        if isinstance(sequence, str):
            sequence = self.sequences[sequence].value
            logging.info(f"Start scheduling software in {sequence} mode ...")

        #  Build derived quantities
        self.build()
        self.runtime_params()
        self.sequence = sequence
        self.returns = {}

        for i in range(self.n_observation_windows):
            self.config._runtime.iteration = i
            for option in sequence:
                if (
                    option == "obs-window"
                    or option == "flight-calc"
                    or option == "calc-obs-period"
                ):
                    logging.info(f"Running {option} for observation window {i}...")
                    self.returns[f"{option}_{i}"] = self.options[option](self.config)
                else:
                    if self.flag_obs:
                        logging.info(f"Running {option} for observation window {i}...")
                        self.returns[f"{option}_{i}"] = self.options[option](
                            self.config
                        )

        return self.returns

    def build_times(self) -> np.ndarray[u.Quantity]:
        """Get the times for the calculations."""
        return (
            self.calc_start_time
            + np.arange(
                0,
                self.calc_period.to("min").value,
                self.calc_increment.to("min").value,
            )
            * u.min
        )

    def pointing_fov_cuts(self, config: ToOConfig) -> None:
        """Build the field of view cuts."""
        self.config._runtime.fov_cuts = PointingFoVCuts(config)

    def get_observation_windows(self, config: ToOConfig) -> np.ndarray:

        # Information about the next observation window
        start_id, end_id, start_time, end_time = get_observation_windows(
            self.night_conditions, self.times, one_window=False
        )

        logging.info("***************************************************")
        logging.info(
            f"The time period from {self.calc_start_time} to {self.calc_end_time} contains {len(start_time)} observation windows."
        )
        if len(start_time) >= 1:
            self.flag_obs = True
            for i in range(len(start_time)):
                logging.info(
                    f"Observation window {i + 1}: {start_time[i]} to {end_time[i]}"
                )
            logging.info("***************************************************")

            index = config._runtime.iteration
            config._runtime.observation_starts = start_time[index]
            config._runtime.observation_ends = end_time[index]
            config._runtime.obs_times = self.times[start_id[index] : end_id[index]]
            config._runtime.obs_detector_frames = self.detector_frames[
                start_id[index] : end_id[index]
            ]

            logging.info("***************************************************")
            logging.info(
                f"Next observation window: from {start_time[index]} to {end_time[index]}."
            )

            return start_time, end_time, self.flag_obs

        else:
            self.flag_obs = False
            logging.info("No observation window can be scheduled.")
            return start_time, end_time, self.flag_obs

    def compute_schedule(self, config: ToOConfig):
        """Compute the schedule of observations, using input file for observable sources."""
        # Determine schedule
        logging.info("***************************************************")
        logging.info("Compute schedule using list of observable sources...")
        observable = load_observable_sources(config.output.observations.observable_file)
        schedule = get_schedule(config, observable)
        return schedule

    def calc_observation_period(self, config: ToOConfig):
        """Compute the observation periods for 31 days.

        Args:
            config (ToOConfig): Configuration object for the ToO parser
        """
        logging.info("Compute observability windows for next xx days")

        # Initialize detector object
        detector = self.detector

        # Initialize sun, moon and field of view cuts
        sun_moon_cuts = self.sun_moon_cuts

        # Initialize time and location for the detector
        start_time = config.settings.calculation.start_time
        calc_period = config.settings.calculation.calculation_period
        time_increment = config.settings.calculation.time_increment

        # Time array
        arr_time = np.array([])
        # Moon illumination array
        moon_ill = np.array([])
        # Observability window with Sun
        sta_time_sun = np.array([])
        end_time_sun = np.array([])
        # Observability window with Moon
        sta_time_moon = np.array([])
        end_time_moon = np.array([])
        # Observability window with Sun and Moon
        sta_time = np.array([])
        end_time = np.array([])
        # Total observation time
        tot_obs_time = np.array([])

        # Set the time of the end of the flight
        # Determines the maximum number of iterations
        trajectory_type = config.settings.detector.trajectory_type
        if trajectory_type == "cst":
            end_time_flight = start_time + config.settings.calculation.num_days_flight
        elif trajectory_type == "log":
            end_time_flight = detector.log_end_time
        elif trajectory_type == "sim":
            end_time_flight = detector.sim_end_time

        # Loop over days to compute observability windows
        ktime = 0
        while end_time_flight - start_time - calc_period > 0:
            arr_time = np.append(arr_time, start_time.jd)

            times = (
                start_time
                + np.arange(
                    0,
                    calc_period.to("min").value,
                    time_increment.to("min").value,
                )
                * u.min
            )
            logging.info("New day - times in UTC")
            logging.info(f"Start time: {start_time}")
            logging.info(f"End time: {start_time + calc_period}")

            detector_frames = AltAz(obstime=times, location=detector.loc(times))

            # Determine observation conditions with only Sun
            observable_conditions_sun = sun_moon_cuts.sun_cut(times, detector_frames)
            # Determine observation conditions with only Moon
            observable_conditions_moon = sun_moon_cuts.moon_alt_cut(
                times, detector_frames
            )
            # Determine observation conditions with Sun and Moon
            observable_conditions = sun_moon_cuts(detector_frames, times)
            # Maximum Moon illumunation
            moon_ill = np.append(moon_ill, np.max(moon_illumination(times)))
            try:
                # Determine start and end times with only Sun
                logging.info("Sun only")
                (
                    start_id,
                    end_id,
                    start_times_sun,
                    end_times_sun,
                ) = get_observation_windows(
                    observable_conditions_sun, times, one_window=True
                )
                sta_time_sun = np.append(sta_time_sun, start_times_sun.jd)
                end_time_sun = np.append(end_time_sun, end_times_sun.jd)
            except IndexError:
                logging.info("We can't schedule - Sun")
                sta_time_sun = np.append(sta_time_sun, np.nan)
                end_time_sun = np.append(end_time_sun, np.nan)

            try:
                # Determine start and end times with only Moon
                logging.info("Moon only")
                (
                    start_id,
                    end_id,
                    start_times_moon,
                    end_times_moon,
                ) = get_observation_windows(
                    observable_conditions_moon, times, one_window=True
                )
                sta_time_moon = np.append(sta_time_moon, start_times_moon.jd)
                end_time_moon = np.append(end_time_moon, end_times_moon.jd)
            except IndexError:
                logging.info("We can't schedule - Moon")
                sta_time_moon = np.append(sta_time_moon, np.nan)
                end_time_moon = np.append(end_time_moon, np.nan)

            try:
                # Determine start and end times of the next observation window
                logging.info("Sun and Moon")
                start_id, end_id, start_times, end_times = get_observation_windows(
                    observable_conditions, times, one_window=True
                )
                sta_time = np.append(sta_time, start_times.jd)
                end_time = np.append(end_time, end_times.jd)
                logging.info(f"start time: {start_times}")
                logging.info(f"end time: {end_times}")
            except IndexError:
                logging.info("We can't schedule - Sun and Moon")
                sta_time = np.append(sta_time, np.nan)
                end_time = np.append(end_time, np.nan)

            # Remove data that corresponds to next day
            if sta_time[ktime] - arr_time[ktime] > 1:
                sta_time[ktime] = np.nan
                end_time[ktime] = np.nan

            tot_obs_time = np.append(
                tot_obs_time, np.nan_to_num(end_time[ktime] - sta_time[ktime])
            )
            logging.info(f"obs window time: {tot_obs_time[ktime] * 24 * 3600}s")
            sum_obs_time = np.sum(tot_obs_time) * 24 * 3600
            logging.info(f"cumulated obs window time: {sum_obs_time}s")

            # Increment start time (next day, or less)
            if np.isnan(end_time[ktime]):
                start_time += 24.0 * 60.0 * u.min
            else:
                start_time = end_times + 1.0 * 60.0 * u.min

            ktime += 1

        # Multiply by 24 to convert days in hours (adapted to visualization routine)
        jdtoh = 24.0
        fig_observability_windows(
            config,
            arr_time * jdtoh,
            moon_ill,
            sta_time_sun * jdtoh,
            end_time_sun * jdtoh,
            sta_time_moon * jdtoh,
            end_time_moon * jdtoh,
            sta_time * jdtoh,
            end_time * jdtoh,
        )

    def compute_observability_schedule(self, config: ToOConfig):
        """Compute the observability of sources and the observation schedule."""

        # Compute list of observable sources
        logging.info("***************************************************")
        logging.info("Compute observability of sources from database...")
        logging.info(config.files.database.directory)
        logging.info(config.files.database.cleaned)
        observable = get_observations(config)[1]
        for count in range(len(observable)):
            fig_trajectories(
                config, observable[count], count, config.settings.calculation.start_time
            )
        # Determine schedule
        logging.info("***************************************************")
        logging.info("Compute schedule using list of observable sources...")
        get_schedule(config, observable)

    def run_GW(self, config: ToOConfig):
        """Compute the observability of GW sources and the observation schedule"""
        logging.info("***************************************************")
        logging.info("Run the GW localization module...")
        gw_obs = gw_localization_pointing(config)

        logging.info("***************************************************")
        logging.info("Compute schedule using list of observable sources...")
        get_schedule(config, gw_obs)

    def create_visuals(self, config: ToOConfig):
        # Visualizations
        logging.info("***************************************************")
        logging.info("Visualize...")
        # Visualize detector trajectory
        fig_detector_position(config, config._runtime.detector_frames)
        # Visualize observable fraction of the sky
        visualize_sources(config, source_choice="none")
        visualize_sources(config, source_choice="all")
        # Visualize outputs
        visualize_sources(config, source_choice="observable")
        visualize_sources(config, source_choice="scheduled")
        visualize_sources_obs_sched(config, source_choice="scheduled")
        fig_trajectories_scheduled(config)

    def flight_calculation(self, config: ToOConfig):
        num_obs_periods = int(config.settings.calculation.num_days_flight.value)
        for i in range(num_obs_periods):
            st_time, en_time, flag_obs = self.get_observation_windows(config)
            # Run NuTS only if observation window exists
            if flag_obs:
                flag_time = (
                    st_time[0] - config.settings.calculation.start_time
                ) < 24.0 * 60.0 * u.min
                # Run NuTS only if observation window same day
                if flag_time:
                    build_full_db(config)
                    clean_db(config)
                    self.compute_observability_schedule(config)
                    self.create_visuals(config)

            # Update start time (next day, or less)
            try:
                self.calc_start_time = st_time[1]
            except Exception:
                self.calc_start_time += 24.0 * 60.0 * u.min
            self.calc_end_time = self.calc_start_time + self.calc_period

            # Update directory name and config
            # WARNING - current version uses a specific directory name
            c = toml.load("./config.toml")
            c["settings"]["calculation"]["start_time"] = str(self.calc_start_time)
            c["output"]["previous_observation_path"] = (
                c["output"]["directory"] + "/Observations/scheduled_output.json"
            )
            c["output"]["directory"] = (
                c["output"]["directory"][:15] + str(self.calc_start_time)[5:10]
            )
            if os.path.isdir(
                str(os.path.dirname(config.output.directory))
                + "/"
                + c["output"]["directory"]
            ):
                c["output"]["directory"] = c["output"]["directory"] + "_2"
            config = ToOConfig(**c)
            self.config = config
            setup_logging("run_flight.log", config.output.directory, "INFO")
            self.build()
            self.runtime_params()

            # Update start time (next day, or less)
            try:
                self.calc_start_time = st_time[1]
            except Exception:
                self.calc_start_time += 24.0 * 60.0 * u.min
            self.calc_end_time = self.calc_start_time + self.calc_period

            # Update directory name and config
            # WARNING - current version uses a specific directory name
            c = toml.load("./config.toml")
            print("")
            c["settings"]["calculation"]["start_time"] = str(self.calc_start_time)
            c["output"]["previous_observation_path"] = (
                c["output"]["directory"] + "/Observations/scheduled_output.json"
            )
            c["output"]["directory"] = (
                c["output"]["directory"][:15] + str(self.calc_start_time)[5:10]
            )
            if os.path.isdir(
                str(os.path.dirname(config.output.directory))
                + "/"
                + c["output"]["directory"]
            ):
                c["output"]["directory"] = c["output"]["directory"] + "_2"
            config = ToOConfig(**c)
            self.config = config
            setup_logging("run_flight.log", config.output.directory, "INFO")
            self.build()
            self.runtime_params()

            # Update start time (next day, or less)
            try:
                self.calc_start_time = st_time[1]
            except Exception:
                self.calc_start_time += 24.0 * 60.0 * u.min
            self.calc_end_time = self.calc_start_time + self.calc_period

            # Update directory name and config
            # WARNING - current version uses a specific directory name
            c = toml.load("./config.toml")
            c["settings"]["calculation"]["start_time"] = str(self.calc_start_time)
            c["output"]["previous_observation_path"] = (
                c["output"]["directory"] + "/Observations/scheduled_output.json"
            )
            c["output"]["directory"] = (
                c["output"]["directory"][:15] + str(self.calc_start_time)[5:10]
            )
            if os.path.isdir(
                str(os.path.dirname(config.output.directory))
                + "/"
                + c["output"]["directory"]
            ):
                c["output"]["directory"] = c["output"]["directory"] + "_2"
            config = ToOConfig(**c)
            self.config = config
            setup_logging("run_flight.log", config.output.directory, "INFO")
            self.build()
            self.runtime_params()

        fig_stat_flight(config)
