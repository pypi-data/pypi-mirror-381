import logging

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.time import Time

from ..config.config import ToOConfig


class LOGPointing:
    def __init__(self, config: ToOConfig):
        logging.info(
            f"Loading pointing data... from yaw: {config.files.pointing.yaw_file} and tilt: {config.files.pointing.tilt_file}"
        )
        yaw_data = pd.read_csv(config.files.pointing.yaw_file)
        self.yaw_times = Time(pd.to_datetime(yaw_data["Date Time"]))
        self.yaw = np.unwrap(yaw_data["26 GPS Yaw"].to_numpy() * u.deg)

        tilt_data = pd.read_csv(
            config.files.pointing.tilt_file,
            names=[
                "date",
                "Tilt",
            ],
            index_col=False,
            header=0,
            sep=",",
        )
        format = "%m/%d/%Y %I:%M:%S %p"
        self.tilt_times = Time(pd.to_datetime(tilt_data["date"], format=format))
        self.tilt = tilt_data["Tilt"]

    def get_yaw(self, times: np.ndarray[Time]) -> np.ndarray:
        yaw = np.interp(times.gps, self.yaw_times.gps, self.yaw)
        return np.mod(yaw.to(u.deg).value, 360) * u.deg

    def get_tilt(self, times: np.ndarray[Time]) -> np.ndarray:
        tilt = np.interp(times.gps, self.tilt_times.gps, self.tilt)
        return tilt * u.deg

    def get_pointing(self, times: np.ndarray[Time]) -> tuple[np.ndarray, np.ndarray]:
        return self.get_yaw(times), self.get_tilt(times)
