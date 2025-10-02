""" This module contains some of the main fixtures that can be used in subsequent tests."""

import pathlib

import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import pytest

from nuts.compute import Compute
from nuts.config.config import ToOConfig
from nuts.config.load_config import load_config
from nuts.detector_motion.constant_trajectory import ConstantDetectorLoc
from nuts.detector_motion.kml_trajectory import KMLInterpolation
from nuts.detector_motion.linear_trajectory import LinearMotionDetector
from nuts.detector_motion.log_trajectory import FlightLog
from nuts.detector_motion.sim_trajectory import SimTrajectory
from nuts.observation_period.observation import ObservationPeriod
from nuts.too_event import ToOEvent
from nuts.too_observation import ToOObservation


@pytest.fixture
def config() -> ToOConfig:
    """Load the test config file

    Returns:
        ToOConfig: Contents of config file
    """

    path = pathlib.Path(__file__).parent.resolve()
    config_file = f"{path}/test_config.toml"
    return load_config(config_file)


@pytest.fixture
def compute(config: ToOConfig) -> Compute:
    """Return a Compute object.

    Args:
        config (ToOConfig): Configuration object for the ToO parser

    Returns:
        Compute: Compute object
    """
    return Compute(config=config)


@pytest.fixture
def too_event() -> ToOEvent:
    """Return an example ToOEvent object."""
    return ToOEvent(
        publisher="IceCube",
        publisher_id=1235456,
        event_type="IceCube Gold",
        event_id=1235456,
        priority=2,
    )


@pytest.fixture
def observation_period() -> ObservationPeriod:
    """Observation period around march equinox for 1 hour

    Returns:
        ObservationPeriod: Observation period object
    """
    t1 = atime.Time("2023-3-20T21:00:00", format="isot", scale="utc")
    t2 = atime.Time("2023-3-20T22:00:00", format="isot", scale="utc")
    c1 = acoord.AltAz(az=30 * u.deg, alt=0 * u.deg)
    c2 = acoord.AltAz(az=33 * u.deg, alt=-2 * u.deg)
    return ObservationPeriod(t1, t2, c1, c2)


@pytest.fixture
def observation(
    too_event: ToOEvent, observation_period: ObservationPeriod
) -> ToOObservation:
    observation = ToOObservation()
    observation.event = too_event
    observation.observations = [observation_period]
    return observation


@pytest.fixture
def constant_detector() -> ConstantDetectorLoc:
    """Return a constant detector location at Wanaka, New Zealand on 2023-05-13

    Returns:
        ConstantDetectorLoc: Constant detector location object
    """
    wanaka = acoord.EarthLocation(
        lon=169.1 * u.deg, lat=-44.7 * u.deg, height=33 * u.km
    )
    return ConstantDetectorLoc(coordinates=wanaka)


@pytest.fixture
def linear_detector() -> LinearMotionDetector:
    """Return a linear motion detector location at Wanaka, New Zealand on 2023-05-13

    Returns:
        LinearMotionDetector: Linear motion detector location object
    """
    wanaka = acoord.EarthLocation(
        lon=169.1 * u.deg, lat=-44.7 * u.deg, height=33 * u.km
    )
    start_time = atime.Time("2023-05-13T00:00:00", format="isot", scale="utc")
    velocity = [0 * u.km / u.hour, 0 * u.km / u.hour, -1 * u.km / u.hour]
    return LinearMotionDetector(
        coordinates=wanaka, start_time=start_time, velocity=velocity
    )


@pytest.fixture
def log_detector(config: ToOConfig) -> FlightLog:
    """Return a Flight Log detector location at Wanaka, New Zealand on 2023-05-13

    Returns:
        LinearMotionDetector: Flight log detector location object
    """

    return FlightLog(config.files.trajectories.log_file)


@pytest.fixture
def sim_detector(config: ToOConfig) -> SimTrajectory:
    """Return a Flight Log detector location at Wanaka, New Zealand on 2023-05-13

    Returns:
        LinearMotionDetector: Flight log detector location object
    """

    return SimTrajectory(config.files.trajectories.sim_file)


@pytest.fixture
def kml_detector(config: ToOConfig) -> KMLInterpolation:
    """Return a Flight Log detector location at Wanaka, New Zealand on 2023-05-13

    Returns:
        LinearMotionDetector: Flight log detector location object
    """

    return KMLInterpolation(config)
