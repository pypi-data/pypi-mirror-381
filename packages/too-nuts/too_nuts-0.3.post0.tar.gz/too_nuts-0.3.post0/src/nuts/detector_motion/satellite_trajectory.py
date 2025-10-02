import logging

import astropy.coordinates as acoord
import astropy.time as atime
import numpy as np
from astropy import units as u
from astropy.constants import R_earth

from .detector import DetectorLocation


class SatelliteLocation(DetectorLocation):
    """Propagate a Keplerian satellite orbit and interpolate geodetic positions.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-05-11
    """

    def __init__(self, config: dict) -> None:
        """
        Initialize the SatelliteLocation class with orbital parameters.

        Args:
            config (dict): configuration containing Keplerian elements
                           keys: a, e, inc, raan, argp, M0, epoch (ISO str)
        """
        self.config = config
        logging.info("Initializing SatelliteLocation with provided config.")
        self._load_orbit_params()

    def _load_orbit_params(self) -> None:
        """
        Load Keplerian elements from the config dictionary.
        """
        orb = self.config
        self.a = orb["a"] * u.m
        self.e = orb["e"]
        self.inc = orb["inc"] * u.rad
        self.raan = orb["raan"] * u.rad
        self.argp = orb["argp"] * u.rad
        self.M0 = orb["M0"]
        self.epoch = atime.Time(orb["epoch"], scale="utc")
        self.mu = orb.get("mu", 398600.4418e9) * u.m**3 / u.s**2
        logging.info(
            f"Orbit params: a={self.a}, e={self.e}, inc={self.inc}, \
             raan={self.raan}, argp={self.argp}, M0={self.M0}, epoch={self.epoch}"
        )

    @staticmethod
    def _kepler_E(M, e, tol=1e-10, max_iter=100):
        """
        Solve Kepler's equation: E - e*sin(E) = M
        """
        E = M.copy() if isinstance(M, np.ndarray) else M
        for _ in range(max_iter):
            f = E - e * np.sin(E) - M
            f_prime = 1 - e * np.cos(E)
            delta = -f / f_prime
            E = E + delta
            if np.all(np.abs(delta) < tol):
                break
        return E

    def _eci_position(self, time: atime.Time):
        """
        Compute ECI (GCRS) position vectors at given time(s).
        """
        # Mean motion [rad/s]
        n = np.sqrt(self.mu / self.a**3).to(1 / u.s).value
        # Mean anomaly at times
        M = (self.M0 + n * (time - self.epoch).to(u.s).value) % (2 * np.pi)
        # Eccentric anomaly
        E = self._kepler_E(M, self.e)
        # True anomaly
        nu = 2 * np.arctan2(
            np.sqrt(1 + self.e) * np.sin(E / 2), np.sqrt(1 - self.e) * np.cos(E / 2)
        )
        # Radius
        r = self.a.value * (1 - self.e * np.cos(E))
        # Orbital-plane coords
        x_orb = r * np.cos(nu)
        y_orb = r * np.sin(nu)
        # Rotation coefficients
        cos_O, sin_O = np.cos(self.raan.value), np.sin(self.raan.value)
        cos_i, sin_i = np.cos(self.inc.value), np.sin(self.inc.value)
        cos_w, sin_w = np.cos(self.argp.value), np.sin(self.argp.value)
        # Rotate to ECI
        x = (cos_O * cos_w - sin_O * sin_w * cos_i) * x_orb + (
            -cos_O * sin_w - sin_O * cos_w * cos_i
        ) * y_orb
        y = (sin_O * cos_w + cos_O * sin_w * cos_i) * x_orb + (
            -sin_O * sin_w + cos_O * cos_w * cos_i
        ) * y_orb
        z = (sin_w * sin_i) * x_orb + (cos_w * sin_i) * y_orb
        return x, y, z

    def loc(self, time: atime.Time, *args, **kwargs) -> acoord.EarthLocation:
        """
        Compute the satellite geodetic location at given time(s).

        Args:
            time (astropy.time.Time): time(s) to compute location

        Returns:
            astropy.coordinates.EarthLocation: geodetic positions
        """
        x, y, z = self._eci_position(time)
        gcrs_cart = acoord.CartesianRepresentation(x * u.m, y * u.m, z * u.m)
        gcrs = acoord.GCRS(gcrs_cart, obstime=time)
        itrs = gcrs.transform_to(acoord.ITRS(obstime=time))
        return acoord.EarthLocation.from_geocentric(itrs.x, itrs.y, itrs.z)

    def save_dict(self) -> dict:
        """
        Save orbit configuration to a dictionary for serialization.
        """
        return {
            "a": str(self.a),
            "e": self.e,
            "inc": str(self.inc),
            "raan": str(self.raan),
            "argp": str(self.argp),
            "M0": self.M0,
            "epoch": str(self.epoch),
        }

    def limb_angle(self, time: atime.Time, *args, **kwargs) -> u.Quantity:
        """
        Calculate the limb angle (radians) relative to the Earth's horizon.

        Args:
            time (astropy.time.Time): time(s) to compute limb angle

        Returns:
            astropy.units.Quantity: negative limb angle in radians
        """
        loc = self.loc(time)
        # Ratio of Earth's radius to satellite distance from center
        ratio = R_earth / (R_earth + loc.height)
        # dimensionless ratio
        val = ratio.to(u.dimensionless_unscaled).value
        return -np.arccos(val) * u.rad
