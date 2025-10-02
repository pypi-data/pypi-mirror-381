import pathlib

import astropy.time as atime
import astropy.units as u
import numpy as np
import pytest
from astropy.coordinates import AltAz

from nuts.config.config import ToOConfig
from nuts.detector_motion.constant_trajectory import ConstantDetectorLoc
from nuts.observation_period.sun_moon_cuts import FoVCuts, SunMoonCuts
from nuts.observation_period.too_obs_time import get_observation_windows
from nuts.too_event import ToOEvent
from nuts.too_observation import ToOObservation


@pytest.fixture
def init(config: ToOConfig) -> None:
    """Initialize computations for the ToO parser.

    Args:
        config (ToOConfig): Configuration object for the ToO parser
    """

    obs_start_time = atime.Time("2023-03-20T21:24:00", format="isot", scale="utc")
    schedule_period = [obs_start_time, obs_start_time + 24 * u.hour]

    # Initialize sun, moon and field of view cuts
    config._runtime.fov_cuts = FoVCuts(config)
    sun_moon_cuts = SunMoonCuts(config)

    # Initialize time and location for the detector

    balloon = ConstantDetectorLoc()
    start_time = schedule_period[0]
    obs_duration = schedule_period[1] - start_time
    times = start_time + np.arange(0, obs_duration.to("hour").value, (0.1 / 6)) * u.hour
    detector_frames = AltAz(obstime=times, location=balloon.loc(times))

    # Determine observation condidtions
    observable_conditions = sun_moon_cuts(detector_frames, times)
    config._runtime.all_times = times
    config._runtime.obs_times = times[observable_conditions]
    config._runtime.obs_detector_frames = detector_frames[observable_conditions]

    # Determine start and end times of observation windows
    _, _, start_times, end_times = get_observation_windows(observable_conditions, times)
    return config


@pytest.fixture
def event() -> ToOEvent:
    """Event at ra,dec (0,0) detected at March equinox 2023 (should be right behind the sun)

    Returns:
        ToOEvent: Event object
    """
    ra = 0 * u.deg
    dec = 0 * u.deg
    event = ToOEvent()
    event.set_coordinates(ra=ra.to("deg").value, dec=dec.to("deg").value)
    event.detection_time = atime.Time("2023-03-20T21:24:00", format="isot", scale="utc")
    return event


@pytest.fixture
def observation(event) -> ToOObservation:
    """Observation of event behind the sun on March equinox 2023 for 24h at lat,long,height (0,0,0)

    Args:
        event (ToOEvent fixture): event sitting behind the sun

    Returns:
        ToOObservation: Observation object
    """

    observation = ToOObservation()
    observation.event = event
    return observation


@pytest.fixture
def sun_moon_cuts(config) -> SunMoonCuts:
    return SunMoonCuts(config)


def test_observation_schedule(observation, init):
    """Test if observation period code runs

    Assumption: Source located behind the sun at March equinox 2023 is never visible
    and we therefore don't get any observation times

    Args:
        observation (ToOObservation Fixture): Observation object containing the source information
    """
    observation.get_observation_periods(init)
    assert observation.observations == []
