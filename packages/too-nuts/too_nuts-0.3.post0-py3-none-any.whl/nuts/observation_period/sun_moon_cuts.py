"""Field of view, sun and moon cuts.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: moon_phase_angle
.. autofunction:: moon_illumination

.. autoclass:: SunMoonAltitudeFoVCuts
    :noindex:
    :members:
    :undoc-members:

"""

import logging

import astropy.constants as const
import numpy as np
from astropy import units as u
from astropy.coordinates import AltAz, EarthLocation, get_body
from astropy.time import Time

from ..config.config import ToOConfig
from ..detector_motion.detector_uptime import UpTime
from ..detector_motion.log_pointing import LOGPointing


def moon_phase_angle(time: Time, ephemeris=None) -> u.Quantity:
    """Function to calculate the phase angle of the moon

    Args:
        time (Time): Time to calculate the phase angle for
        ephemeris (str, optional): Catalog of celestial objects and trajectories by default astropy's solarsystem one is used. Defaults to None.

    Returns:
        u.Quantity: Phase angle of the moon
    """
    sun = get_body("sun", time)
    moon = get_body("moon", time, ephemeris=ephemeris)
    elongation = sun.separation(moon)
    return np.arctan2(
        sun.distance * np.sin(elongation),
        moon.distance - sun.distance * np.cos(elongation),
    )


def moon_illumination(time: Time, ephemeris=None) -> float:
    """Function to calculate the illumination of the moon

    Args:
        time (Time): Time to calculate the illumination for
        ephemeris (str, optional): Catalog of celestial objects and trajectories by default astropy's solarsystem one is used. Defaults to None.

    Returns:
        float: Illumination of the moon
    """
    i = moon_phase_angle(time, ephemeris=ephemeris)
    k = (1 + np.cos(i)) / 2.0
    return k.value


def offset_angle(horiz_off_angle: u.Quantity, location: EarthLocation) -> u.Quantity:
    """Function to calculate the offset angle that angles are measured from

    Args:
        location (EarthLocation): Location of the observation

    Returns:
        u.Quantity: Offset angle
    """
    altitude = np.where(location.height < 0, 1 * u.m, location.height)
    if horiz_off_angle == "limb":
        return np.pi / 2.0 * u.rad - np.arcsin(
            const.R_earth / (altitude + const.R_earth)
        )
    return u.Quantity(horiz_off_angle)


class SunMoonCuts:
    """Class to calculate the cuts for the sun and moon"""

    def __init__(self, config=ToOConfig):
        logging.info("Initialising SunMoonCuts")
        self.horiz_off_angle = config.settings.observation.horizontal_offset_angle
        self.crit_sun_altitude = config.settings.observation.sun_altitude_cut
        self.crit_moon_altitude = config.settings.observation.moon_altitude_cut
        self.crit_moon_illumination = config.settings.observation.moon_illumination_cut

    def __call__(
        self,
        detector_frame: EarthLocation,
        time: Time,
    ) -> bool:
        """Function to calculate the cuts for the sun, moon

        Args:
            detector_frame (EarthLocation): Detector location
            time (Time): Time to calculate the cuts for

        Returns:
            bool: True if the source is observable
        """

        sun_cut = self.sun_cut(time, detector_frame)
        moon_cut = self.moon_cut(time, detector_frame)
        return np.logical_and(sun_cut, moon_cut)

    def sun_cut(self, time: Time, detector_frame: EarthLocation) -> bool:
        """Function to check if the sun is below the defined threshold angle

        Args:
            time (Time): time to calculate the cuts for
            detector_frame (EarthLocation): observation location

        Returns:
            bool: True if the sun is below the defined threshold angle
        """
        sun_alt = get_body("sun", time).transform_to(detector_frame).alt
        angle_off = offset_angle(self.horiz_off_angle, detector_frame.location)
        return np.where(sun_alt < self.crit_sun_altitude - angle_off, 1, 0)

    def moon_cut(self, time: Time, detector_frame: EarthLocation) -> bool:
        """Function to check if the moon is below the defined threshold angle or below the defined illumination threshold

        Args:
            time (Time): time to calculate the cuts for
            detector_frame (EarthLocation): observation location

        Returns:
            bool: True if the moon is below the defined threshold angle or below the defined illumination threshold
        """
        return np.where(
            moon_illumination(time) < self.crit_moon_illumination,
            True,
            self.moon_alt_cut(time, detector_frame),
        )

    def moon_alt_cut(self, time: Time, detector_frame: EarthLocation) -> bool:
        """Function to check if the moon is below the defined threshold angle

        Args:
            time (Time): time to calculate the cuts for
            detector_frame (EarthLocation): observation location

        Returns:
            bool: True if the moon is below the defined threshold angle
        """
        moon_alt = get_body("moon", time).transform_to(detector_frame).alt
        angle_off = offset_angle(self.horiz_off_angle, detector_frame.location)
        return np.where(moon_alt < self.crit_moon_altitude - angle_off, True, False)


class FoVCuts:
    """Class to calculate the cuts for the sun, moon and field of view"""

    def __init__(self, config=ToOConfig):
        logging.info("Initialising FoVCuts")
        self.lower_fov_cut = config.settings.observation.lower_fov_cut
        self.upper_fov_cut = config.settings.observation.upper_fov_cut
        self.horiz_off_angle = config.settings.observation.horizontal_offset_angle

    def __call__(
        self,
        source_loc: AltAz,
        time: Time,
    ) -> bool:
        """Function to check if the source is in the observable band

        Args:
            detector_frame (EarthLocation): Detector location
            source_loc (AltAz): Source location
            time (Time): Time to calculate the cuts for

        Returns:
            bool: True if the source is in the observable band
        """
        source_alt = source_loc.alt.deg
        angle_off = offset_angle(self.horiz_off_angle, source_loc.location)

        return np.logical_and(
            np.where(self.lower_fov_cut - angle_off < source_alt * u.deg, 1, 0),
            np.where(source_alt * u.deg < self.upper_fov_cut - angle_off, 1, 0),
        )


class PointingFoVCuts:
    """Class to calculate the cuts for the sun, moon and field of view"""

    def __init__(self, config=ToOConfig):
        logging.info("Initialising FoVCuts")
        self.horiz_off_angle = config.settings.observation.horizontal_offset_angle
        self.lower_fov_cut = config.settings.observation.lower_fov_cut
        self.upper_fov_cut = config.settings.observation.upper_fov_cut
        self.az_fov = config.settings.observation.fov_az
        self.alt_fov = config.settings.observation.fov_alt
        self.obs_fov = config._runtime.options == "obs-fov"
        self.pointing = LOGPointing(config)
        self.up_time = UpTime(config)

    def __call__(
        self,
        source_loc: AltAz,
        time: Time,
    ) -> bool:
        """Function to calculate the cuts for the sun, moon and field of view

        Args:
            detector_frame (EarthLocation): Detector location
            source_loc (AltAz): Source location
            time (Time): Time to calculate the cuts for

        Returns:
            bool: True if the source is observable
        """
        in_obs_band = self.in_obs_band(source_loc)
        in_fov = self.in_fov(source_loc, time)
        detector_active = self.up_time(time)
        return in_obs_band & in_fov & detector_active

    def in_obs_band(self, source_loc: AltAz) -> bool:
        """Function to check if the source is in the observable band

        Args:
            source_loc (AltAz): Source location
            time (Time): Time to calculate the cuts for
            obs_fov (bool): wheter to use pointing information

        Returns:
            bool: True if the source is in the observable band
        """
        source_alt = source_loc.alt.deg
        angle_off = offset_angle(self.horiz_off_angle, source_loc.location)

        observable = np.logical_and(
            np.where(self.lower_fov_cut - angle_off < source_alt * u.deg, 1, 0),
            np.where(source_alt * u.deg < self.upper_fov_cut - angle_off, 1, 0),
        )
        return observable

    def in_fov(self, source_loc: AltAz, time: Time) -> bool:
        """Function to check if the source is in the field of view

        Args:
            source_loc (AltAz): Source location
            time (Time): Time to calculate the cuts for

        Returns:
            bool: True if the source is in the field of view
        """
        yaw, tilt = self.pointing.get_pointing(time)
        in_az_fov = np.logical_and(
            yaw - self.az_fov / 2 <= source_loc.az,
            source_loc.az <= yaw + self.az_fov / 2,
        )
        in_alt_fov = np.logical_and(
            tilt - self.alt_fov / 2 <= source_loc.alt,
            source_loc.alt <= tilt + self.alt_fov / 2,
        )
        return np.logical_and(in_az_fov, in_alt_fov)
