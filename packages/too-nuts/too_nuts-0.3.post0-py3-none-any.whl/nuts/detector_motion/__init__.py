r""" Detector motion

.. autosummary::
   :toctree:
   :recursive:


    detector
    detector_init
    constant_trajectory
    linear_trajectory
    kml_trajectory
    sim_trajectory
    log_pointing
    log_trajectory
"""

__all__ = [
    "detector",
    "detector_init",
    "constant_trajectory",
    "linear_trajectory",
    "kml_trajectory",
    "sim_trajectory",
    "log_pointing",
    "log_trajectory",
]

from . import (
    constant_trajectory,
    detector,
    detector_init,
    kml_trajectory,
    linear_trajectory,
    log_pointing,
    log_trajectory,
    sim_trajectory,
)
