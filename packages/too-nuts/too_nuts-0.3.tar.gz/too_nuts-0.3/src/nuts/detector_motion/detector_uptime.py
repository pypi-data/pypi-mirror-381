from pathlib import Path

import numpy as np
from astropy.time import Time
from scipy.interpolate import interp1d

from ..config.config import ToOConfig


class UpTime:
    def __init__(self, config: ToOConfig):

        self.file_name = config.files.pointing.uptime_file
        self.times, self.up = self.load_uptime_data()
        self.uptime_interpolation = self.build_interpolation()

    def load_uptime_data(self) -> tuple[Time, np.ndarray]:
        uptime_data = np.load(self.file_name, allow_pickle=True)
        times = uptime_data["times"]
        times = np.append(times[0] - np.diff(times)[0], times)
        times = np.append(times, times[-1] + np.diff(times)[-1])
        times = Time(times)
        up = uptime_data["counts"]
        up = np.append(0, up)
        up = np.append(up, 0)
        up = np.append(up, 0)
        return times, up

    def build_interpolation(self) -> interp1d:
        return interp1d(
            self.times.gps, self.up, kind="nearest", fill_value="extrapolate"
        )

    def __call__(self, time: Time) -> bool:
        return self.uptime_interpolation(time.gps) > 0
