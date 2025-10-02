"""Module for determining detector position using kml file.

.. autosummary::

   KMLInterpolation

.. autoclass:: KMLInterpolation
   :noindex:
   :members:

"""

import logging

import astropy.constants as const
import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import fiona
import geopandas as gpd
import numpy as np

from ..config.config import ToOConfig
from .detector import DetectorLocation


def parse_times(input_time: str) -> atime.Time:
    """Function to convert date and time provided in the kml fies
    to astropy time object.

    Args:
        input_time (str): date and time in format KML format

    Returns:
        atime.Time: astropy time object
    """
    date = input_time.split()[0]
    time = input_time.split()[1][:-1]
    if len(date.split("/")) > 1:
        tstring = (
            "20"
            + date.split("/")[2]
            + "-"
            + date.split("/")[0]
            + "-"
            + date.split("/")[1]
            + " "
            + time
            + ":00:00"
        )
        return tstring


def parse_speeds(vin: str) -> u.Quantity:
    """Parse the speed from the kml file and convert to m/s.

    Args:
        vin (str): speed in knots

    Returns:
        u.Quantity: speed in m/s
    """
    kts_to_mps = 0.514444
    return float(vin.split()[1]) * kts_to_mps * u.m / u.s


class KMLInterpolation(DetectorLocation):
    """Interpolate detector position using CSBF predictions from kml file."""

    def __init__(self, config: ToOConfig) -> None:
        self.height = config.settings.detector.kml_height
        self.kml_location = []

        self.filename = config.files.trajectories.kml_file
        logging.warning(f"Detector interpolation calculated using {self.filename}")
        self.load_kml(filename=self.filename)
        self.log_start_time = self.kml_times[0]
        self.log_end_time = self.kml_times[-1]

    def load_kml(self, filename: str) -> None:
        """Extract times, longitude, latitude and speed from kml file.

        Args:
            filename (str): filename of the kml file
        """

        # Load the kml file
        fiona.drvsupport.supported_drivers["KML"] = "rw"
        df = gpd.read_file(filename, driver="KML")

        # Extract the longitude and latitude
        self.longitudes = np.array(df["geometry"][2:-1].x) * u.deg
        self.latitudes = np.array(df["geometry"][2:-1].y) * u.deg

        # Extract the times and speeds
        self.kml_times = []
        times = np.array(df["Name"][2:-1])
        self.kml_speed = []
        speeds = np.array(df["Description"][2:-1])

        for i in range(len(times)):
            time_loc = parse_times(times[i])
            if time_loc is not None:
                self.kml_times.append(time_loc)
                self.kml_speed.append(parse_speeds(speeds[i]))

        # Convert to astropy time object
        self.kml_times = atime.Time(self.kml_times, format="iso", scale="utc")

    def loc(self, time: atime.Time) -> acoord.EarthLocation:
        """Return the expected location of the detector after a given time.

        Args:
            time (atime.Time): time to interpolate the location

        Raises:
            ValueError: if the time is outside of the kml file range

        Returns:
            acoord.EarthLocation: location of the detector at the given time
        """

        # check if time is within the flight log range
        if np.any(time < self.log_start_time) or np.any(time > self.log_end_time):
            raise ValueError(
                f"Time {time} is outside of flight log range from {self.log_start_time} to {self.log_end_time}"
            )

        # interpolate the location
        long = np.unwrap(self.longitudes.to(u.deg).value)
        lat = np.interp(time.gps, self.kml_times.gps, self.latitudes.to(u.deg).value)
        long = np.interp(time.gps, self.kml_times.gps, long)
        long = np.mod(long, 360)
        return acoord.EarthLocation(
            lat=lat * u.deg, lon=long * u.deg, height=self.height
        )

    def save_dict(self) -> dict:
        """Return a dictionary that can be saved easily."""
        ret_dict = {}
        ret_dict["kml_file"] = str(self.filename)
        ret_dict["log_start_time"] = self.log_start_time.utc.isot
        ret_dict["log_end_time"] = self.log_end_time.utc.isot
        ret_dict["velocity"] = str(self.kml_speed[0])
        return ret_dict

    def limb_angle(self, time: atime.Time) -> u.Quantity:
        """Function to calculate the angle with respect to detector horizon (in radians) to the limb of the Earth

        Returns:
            u.Quantity: angle in radians (negative)
        """

        return -np.arccos(const.R_earth / (const.R_earth + self.height))
