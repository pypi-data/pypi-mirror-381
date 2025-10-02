"""Module for interpolating detector position using constant velocity.

.. autosummary::

   LinearMotionDetector

.. autoclass:: LinearMotionDetector
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
class LinearMotionDetector(DetectorLocation):
    """Interpolate detector position using constant velocity. Default (0,0,0)."""

    coordinates = attr.ib(default=acoord.EarthLocation(lon=0, lat=0, height=0))
    start_time = attr.ib(default=atime.Time.now())
    velocity = attr.ib(default=[0 * u.m / u.s, 0 * u.m / u.s, 0 * u.m / u.s])

    def loc(self, time: atime.Time) -> acoord.EarthLocation:
        """
        Method to return the expected location of the detector after a given time
        for constant wind velocity.

        Args:
            time (atime.Time): time input (time to calculate the position for)

        Returns:
            acoord.EarthLocation: Detector frame at the given location
        """

        # convert lat, long, alt -> x,y,z
        x, y, z = self.coordinates.geocentric

        # calculate the interpolation time period
        time_period = (time - self.start_time).to("s")

        # calculate the new position
        x += self.velocity[0].to(u.m / u.s) * np.ones_like(x.value) * time_period
        y += self.velocity[1].to(u.m / u.s) * np.ones_like(y.value) * time_period
        z += self.velocity[2].to(u.m / u.s) * np.ones_like(z.value) * time_period

        # insert back into EarthLocation
        return acoord.EarthLocation(x=x, y=y, z=z)

    def save_dict(self) -> dict:
        """
        Method to return a dictionary that can be saved easily
        """
        ret_dict = {}
        ret_dict["time"] = str(self.start_time.utc.isot)
        ret_dict["velocity"] = {
            "Vx": str(self.velocity[0]),
            "Vy": str(self.velocity[1]),
            "Vz": str(self.velocity[2]),
        }
        ret_dict["location"] = {
            "LAT": str(self.coordinates.lat.deg),
            "LONG": str(self.coordinates.lon.deg),
            "HEIGHT": str(self.coordinates.height),
        }
        return ret_dict

    def limb_angle(self, time: atime.Time) -> u.Quantity:
        """Function to calculate the angle with respect to detector horizon (in radians) to the limb of the Earth

        Returns:
            u.Quantity: angle in radians (negative)
        """
        return -np.arccos(const.R_earth / (const.R_earth + self.loc(time).height))
