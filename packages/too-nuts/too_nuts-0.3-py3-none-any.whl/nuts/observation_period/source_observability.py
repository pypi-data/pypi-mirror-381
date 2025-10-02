""" Functions to determine source observability and characteristics.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: get_observation_times
.. autofunction:: get_detector_pointing
.. autofunction:: get_source_trajectories

"""

import astropy.constants as const
import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.coordinates import AltAz
from astropy.time import Time

from ..config.config import ToOConfig
from ..detector_motion.detector import DetectorLocation
from ..too_event import ToOEvent
from .observation import ObservationPeriod
from .sun_moon_cuts import FoVCuts
from .too_obs_time import get_observation_windows


def get_observation_times(
    config: ToOConfig,
    source: ToOEvent,
) -> list[ObservationPeriod]:
    """Calculate time and location when a source would be in the detectable range

    Args:
        config (dict): config file
        source (ToOEvent): Source to be tracked

    Returns:
        list[ObservationPeriod]: list of possible observations
    """
    # Make list of times to check location of the source for
    times = config._runtime.obs_times
    det_frames = config._runtime.obs_detector_frames
    fov_cuts = config._runtime.fov_cuts

    # Track the source through the sky during observation period
    tracked_source_loc = source.coordinates.transform_to(det_frames)

    # Calculate times when source would be visible
    visibility_cuts = fov_cuts(tracked_source_loc, times)

    # If source is never visible, return empty list
    if np.sum(visibility_cuts) == 0:
        return [], tracked_source_loc, visibility_cuts

    start, end, start_time, end_time = get_observation_windows(visibility_cuts, times)

    # Write result into observation period object
    observation_periods = [
        ObservationPeriod(
            start_time=start_time[i],
            start_loc=tracked_source_loc[start[i]],
            end_time=end_time[i],
            end_loc=tracked_source_loc[end[i]],
            move_time=start_time[i],
            pointing_dir=get_detector_pointing(
                config, tracked_source_loc, start[i], end[i]
            ),
        )
        for i in range(len(start))
    ]
    if config._runtime.options == "obs-fov" and len(observation_periods) > 0:
        from ..visualization.plot_source_in_fov import plot_camera_pointing

        plot_camera_pointing(config, tracked_source_loc, visibility_cuts, source)
    return observation_periods, tracked_source_loc, visibility_cuts


def get_detector_pointing(config: ToOConfig, tracked_source_loc, start, end):
    """Determine where to point the observation.

    Center source trajectory in fov and maximize observation time
    """
    fov_az = config.settings.observation.fov_az.to("rad").value

    altitude = tracked_source_loc[start].location.height
    if config.settings.observation.horizontal_offset_angle == "limb":
        angle_off = (
            np.pi / 2.0 - np.arcsin(const.R_earth / (altitude + const.R_earth)).value
        )
    else:
        angle_off = (
            u.Quantity(config.settings.observation.horizontal_offset_angle)
            .to("rad")
            .value
        )
    point_alt = -angle_off - config.settings.observation.fov_alt.to("rad").value / 2.0

    az_st = tracked_source_loc[start].az.rad
    if end > 0:
        az_en = tracked_source_loc[end - 1].az.rad
    else:
        az_en = tracked_source_loc[end].az.rad
    az_diff = az_en - az_st
    if (fov_az - np.abs(az_diff)) > 0:
        point_az = tracked_source_loc[start].az.rad + az_diff / 2.0
    else:
        point_az = tracked_source_loc[start].az.rad - fov_az / 2.0
    return AltAz(az=point_az * u.rad, alt=point_alt * u.rad)


def get_source_trajectories(
    config: ToOConfig,
    source_location: ToOEvent,
) -> tuple[Time, AltAz, list[bool]]:
    """Compute source trajectories for visualization.

    Args:
        config (ToOConfig): config parameters
        source_location (ToOEvent): Source to be tracked

    Returns:
        tuple[Time, AltAz, list[bool]]: list of source locations

    """
    time_steps = config._runtime.obs_times
    det_frames = config._runtime.obs_detector_frames

    tracked_source_loc = source_location.coordinates.transform_to(det_frames)
    sun_moon_fov_cuts = config._runtime.fov_cuts
    visibility_cuts = sun_moon_fov_cuts(tracked_source_loc, time_steps)

    return time_steps, tracked_source_loc, visibility_cuts
