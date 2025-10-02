"""
Initialize detector object.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: detector_init

"""

import logging

import astropy.coordinates as acoord

from ..config.config import ToOConfig
from .constant_trajectory import ConstantDetectorLoc
from .detector import DetectorLocation
from .kml_trajectory import KMLInterpolation
from .log_trajectory import FlightLog
from .sim_trajectory import SimTrajectory


def detector_init(config: ToOConfig) -> DetectorLocation:
    """Initialize general detector objects using config file.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2023-12-20

    Args:
        config (dict): config file

    Returns:
        detector: DetectorLocation
    """
    traj_type = config.settings.detector.trajectory_type
    if traj_type == "cst":
        logging.info("Constant detector location.")
        return ConstantDetectorLoc(
            acoord.EarthLocation(
                lon=config.settings.detector.const_long,
                lat=config.settings.detector.const_lat,
                height=config.settings.detector.const_height,
            )
        )

    elif traj_type == "kml":
        logging.info("Load detector trajectory predictions from kml file.")
        return KMLInterpolation(config)

    elif traj_type == "log":
        logging.info("Load detector trajectory from log file.")
        flight_log_file = config.files.trajectories.log_file
        return FlightLog(flight_log_file)

    elif traj_type == "sim":
        logging.info("Load detector trajectory from simulation file.")
        flight_sim_file = config.files.trajectories.sim_file
        return SimTrajectory(flight_sim_file)

    else:
        print(
            "ERROR: select trajectory type that was implemented (cst, kml, log or sim)"
        )
