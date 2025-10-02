import astropy.coordinates as acoord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from ..config.config import ToOConfig


def plot_pointing(config: ToOConfig):
    pointing = config._runtime.fov_cuts.pointing

    times = (
        config._runtime.observation_starts
        + np.arange(
            0,
            config.settings.calculation.schedule_period.to("min").value,
            config.settings.calculation.time_increment.to("min").value / 50,
        )
        * u.min
    )

    interpolated_yaw, interpolated_tilt = pointing.get_pointing(times)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="polar")
    colors = cm.jet(np.linspace(0, 1, len(pointing.yaw)))
    ax.scatter(
        pointing.yaw.to(u.rad),
        pointing.yaw_times.to_datetime(),
        c=colors,
        label="Yaw",
    )
    ax.plot(
        interpolated_yaw.to(u.rad),
        times.to_datetime(),
        color="black",
        label="Interpolated Yaw",
    )

    ax.set_title("Pointing of the Detector", fontsize=14)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    colors = cm.jet(np.linspace(0, 1, len(pointing.tilt)))
    ax.scatter(
        pointing.tilt_times.to_datetime(),
        pointing.tilt,
        c=colors,
        label="Yaw",
    )
    ax.plot(
        times.to_datetime(),
        interpolated_tilt.to(u.deg),
        color="black",
        label="Interpolated Yaw",
    )
    ax.set_title("Tilt of the Detector", fontsize=14)
