"""Module to handle simulated trajectories of the detector.

.. autosummary::

   SimTrajectory

.. autoclass:: SimTrajectory
   :noindex:
   :members:

"""

import astropy.constants as const
import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import numpy as np
import pandas as pd

from .detector import DetectorLocation


class SimTrajectory(DetectorLocation):
    """Class to load an old detector trajectory

    Args:
        DetectorLocation (abstract class): Detector trajectory interpolation template
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

        columns = [
            "Time",
            "Latitude in Deg",
            "Longitude in Deg",
            "Elevation in m",
            "East Windspeed in m/s",
            "North Windspeed in m/s",
        ]
        self.flight_data = pd.read_csv(filename, header=10, names=columns, sep=",")
        self.times = self.load_times()
        self.coordinates = self.load_coordinates()
        self.sim_start_time = self.times[0]
        self.sim_end_time = self.times[-1]

    def loc(self, time: atime.Time) -> acoord.EarthLocation:
        """Function to calculate a location prediction from an input time

        Args:
            end_times (atime.Time): time input (time to calculate the position for)

        Returns:
            acoord.EarthLocation: Detector frame at the given location
        """

        # check if time is within the flight log range
        if np.any(time < self.sim_start_time) or np.any(time > self.sim_end_time):
            raise ValueError(
                f"Time {time} is outside of flight log range from {self.sim_start_time} to {self.sim_end_time}"
            )

        # interpolate the location
        x, y, z = self.coordinates.to_geocentric()
        ix = np.interp(time.gps, self.times.gps, x)
        iy = np.interp(time.gps, self.times.gps, y)
        iz = np.interp(time.gps, self.times.gps, z)
        return acoord.EarthLocation(x=ix, y=iy, z=iz)

    def limb_angle(self, time: atime.Time) -> u.Quantity:
        """Function to calculate the angle with respect to detector horizon (in radians) to the limb of the Earth

        Args:
            time (atime.Time): time to calculate altitude of detector for limb calculation

        Returns:
            u.Quantity: angle in radians (negative)
        """
        # Extract the index in the datafile that is closest to the input time
        return -np.arccos(const.R_earth / (const.R_earth + self.loc(time).height))

    def load_times(self) -> list[atime.Time]:
        """Function to load the times from a csv file

        Returns:
            list[atime.Time]: time entries
        """
        times = pd.to_datetime(self.flight_data["Time"]).to_numpy()
        times = atime.Time(times)
        return times

    def load_coordinates(self) -> list[acoord.EarthLocation]:
        """Function to load coordinates from csv file

        Returns:
            list[acoord.EarthLocation]: output coordinates of lat [deg], long [dg], height [m]
        """
        return acoord.EarthLocation(
            lat=self.flight_data["Latitude in Deg"] * u.deg,
            lon=self.flight_data["Longitude in Deg"] * u.deg,
            height=self.flight_data["Elevation in m"] * u.m,
        )

    def save_dict(self) -> dict:
        """Function that returns a dictionary with the data file used

        Returns:
            dict: trajectory data file name
        """
        return {
            "trajectory_file": str(self.filename),
            "start_time": self.sim_start_time,
            "end_time": self.sim_end_time,
        }
