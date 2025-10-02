"""Generate detector trajectory using flight log data.

.. autosummary::

   FlightLog

.. autoclass:: FlightLog
   :noindex:
   :members:



"""

import logging

import astropy.constants as const
import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import numpy as np
import pandas as pd

from .detector import DetectorLocation

u.imperial.enable()


def get_times(date: list[str], time: list[str]) -> atime.Time:
    """Function to convert date and time to astropy time object

    Args:
        date (list[str]): date in format "YY/MM/DD"
        time (list[str]): time in format "HH:MM:SS"

    Returns:
        atime.Time: astropy time object
    """
    real_date = []
    for i in range(len(date)):
        ldate = str(date[i]).replace("/", "-")
        ldate = f"20{ldate[-2:]}-{ldate[:-3]}"
        ldate += "T"
        ldate += str(time[i])
        real_date.append(ldate)
    real_date = atime.Time(real_date, format="isot", scale="utc")
    return real_date


class FlightLog(DetectorLocation):
    """Interpolate detector position using CSBF predictions.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-05-29
    """

    def __init__(self, filename: str) -> None:
        """Initialize the FlightLog class.

        Args:
            filename (str): filename of the flight log
        """

        self.filename = filename
        logging.info(f"Detector interpolation calculated using {filename}")
        self.load_flight_log(filename=filename)
        self.log_start_time = self.log_times[0]
        self.log_end_time = self.log_times[-1]
        logging.info(f"Flight log start time: {self.log_start_time}")
        logging.info(f"Flight log end time: {self.log_end_time}")

    def load_flight_log(self, filename: str) -> None:
        """Compute times, longitude, latitude and speed from kml file.

        Args:
            filename (str): filename of the flight log
        """
        columns = ["date", "time", "long", "lat", "alt", "?", "??"]
        logging.info(f"Loading file: {filename}")
        self.log_data = pd.read_csv(filename, sep="\t", names=columns)
        self.log_times = get_times(self.log_data["date"], self.log_data["time"])

    def loc(self, time: atime.Time) -> acoord.EarthLocation:
        """Function to interpolate the location of the detector at a given time.
        Based on the flight log data.

        Args:
            time (atime.Time): time to interpolate the location for

        Raises:
            ValueError: if the time is outside of the flight log range

        Returns:
            acoord.EarthLocation: location of the detector at the given time
        """

        # check if time is within the flight log range
        if np.any(time < self.log_start_time) or np.any(time > self.log_end_time):
            raise ValueError(
                f"Time {time} is outside of flight log range from {self.log_start_time} to {self.log_end_time}"
            )

        # interpolate the location
        long = np.unwrap(self.log_data["long"])
        lat = np.interp(time.gps, self.log_times.gps, self.log_data["lat"])
        long = np.interp(time.gps, self.log_times.gps, long)
        alt = np.interp(time.gps, self.log_times.gps, self.log_data["alt"])
        long = np.mod(long, 360)

        # insert back into EarthLocation
        return acoord.EarthLocation.from_geodetic(
            lat=lat * u.deg, lon=long * u.deg, height=alt * u.imperial.ft
        )

    def save_dict(self) -> dict:
        """Function to save the flight log information in a dictionary

        Returns:
            dict: dictionary with flight log information of type str
        """

        ret_dict = {}
        ret_dict["flight_log"] = str(self.filename)
        ret_dict["log_start_time"] = str(self.log_start_time)
        ret_dict["log_end_time"] = str(self.log_end_time)
        return ret_dict

    def limb_angle(self, time: atime.Time) -> u.Quantity:
        """Function to calculate the angle with respect to detector horizon (in radians) to the limb of the Earth

        Args:
            time (atime.Time): time to calculate the limb for

        Returns:
            u.Quantity: angle in radians (negative)
        """

        return -np.arccos(const.R_earth / (const.R_earth + self.loc(time).height))
