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
    config_file = f"{path}/obs_period_test_config.toml"
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
