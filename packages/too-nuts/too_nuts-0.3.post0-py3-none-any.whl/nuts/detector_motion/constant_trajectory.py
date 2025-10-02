"""Module for detector position fixed in lon, lat and height.

.. autosummary::

   ConstantDetectorLoc

.. autoclass:: ConstantDetectorLoc
   :noindex:
   :members:

"""

import astropy.constants as const
import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import attr
import numpy as np

from .detector import DetectorLocation


@attr.s
class ConstantDetectorLoc(DetectorLocation):
    """Constant detector position at fixed lon, lat and height. Default (0,0,0)."""

    coordinates = attr.ib(default=acoord.EarthLocation(lon=0, lat=0, height=0))

    def loc(self, time: atime.Time) -> acoord.EarthLocation:
        """
        Method to return the expected location of the detector after a given time
        """
        try:
            return acoord.EarthLocation(
                lon=self.coordinates.lon * np.ones(len(time)),
                lat=self.coordinates.lat * np.ones(len(time)),
                height=self.coordinates.height * np.ones(len(time)),
            )
        except TypeError:
            return acoord.EarthLocation(
                lon=self.coordinates.lon,
                lat=self.coordinates.lat,
                height=self.coordinates.height,
            )

    def save_dict(self) -> dict:
        """
        Method to return a dictionary that can be saved easily
        """
        ret_dict = {}
        ret_dict["location"] = {
            "LAT": str(self.coordinates.lat.deg),
            "LONG": str(self.coordinates.lon.deg),
            "HEIGHT": str(self.coordinates.height.to(u.m)),
        }
        return ret_dict

    def limb_angle(self) -> u.Quantity:
        """Function to return the angle of the detector with respect to detector horizon (in radians) to the limb of the Earth

        Returns:
            u.Quantity: angle in radians (negative)
        """
        return -np.arccos(const.R_earth / (const.R_earth + self.coordinates.height))
