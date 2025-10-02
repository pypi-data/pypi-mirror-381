""" Description.

"""

import astropy.coordinates as acoord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from ..config.config import ToOConfig
from ..too_event import ToOEvent


def plot_camera_pointing(
    config: ToOConfig,
    tracked_source_loc: acoord.AltAz,
    visibilities: np.ndarray,
    source: ToOEvent,
):
    times = config._runtime.obs_times[visibilities]
    tracked_source_loc = tracked_source_loc[visibilities]
    yaw, tilt = config._runtime.fov_cuts.pointing.get_pointing(times)
    camera_x = tracked_source_loc.az.to(u.deg).value - yaw.to(u.deg).value
    camera_y = (tracked_source_loc.alt - tilt).to(u.deg).value
    plot_camera(camera_x, camera_y, times, source, config)


def plot_camera(x, y, t, source: ToOEvent, config: ToOConfig):

    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(111)
    ax.set_xlim((-6.4, 6.4))
    ax.set_ylim((-3.2, 3.2))
    # ax.set_title("Source Track over Camera FoV", fontsize=14)
    ax.set_xlabel("Azimuth FoV in Degrees", fontsize=14)
    ax.set_ylabel("Altitude FoV in Degrees", fontsize=14)
    ax.set_xticks(np.arange(-6.4, 6.5, 0.4))
    ax.set_yticks(np.arange(-3.2, 3.3, 0.4))
    ax.tick_params(labelsize=14)
    colors = cm.jet(np.linspace(0, 1, len(x)))
    ax.scatter(x, y, marker="s", s=100, c=colors)
    ax.scatter(x[0], y[0], marker="s", color=colors[0], s=100, label=f"Start: {t[0]}")
    ax.scatter(x[-1], y[-1], marker="s", color=colors[-1], s=100, label=f"End: {t[-1]}")
    ax.grid()

    fig.legend(loc="upper right", fontsize=14)
    fig.suptitle(
        f"Event Type:{source.event_type.strip()}\nEvent ID:{source.event_id.strip()}\nPublisher:{source.publisher.strip()}\nTime in FoV:{len(x) * config.settings.calculation.time_increment.to(u.s)}\n",
        fontsize=16,
    )
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    ax.set_aspect("equal", adjustable="box")
    plt.savefig(f"Event{source.event_id}_obs_window_{config._runtime.iteration}.pdf")
    plt.close()


def plot_pointing(
    config, obs_time, yaw, evt_type, evt_id, publisher, obs_start_time, obs_end_time
):

    fig = plt.figure(figsize=(18, 6))
    colors = cm.jet(np.linspace(0, 1, len(yaw)))

    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax2.set_title("Azimuth Pointing over Observation Time", fontsize=14)
    ax2.set_xlabel("Observation Time in FoV", fontsize=14)
    ax2.set_ylabel("Azimuth in Degrees", fontsize=14)
    ax2.scatter(obs_time, yaw, c=colors)
    ax2.scatter(obs_time[0], yaw[0], marker="s", c=colors[0], s=100)
    ax2.scatter(obs_time[-1], yaw[-1], marker="s", c=colors[-1], s=100)

    fig.legend(loc="upper right")
    fig.suptitle(
        f"Event Type:{evt_type.strip()}\nEvent ID:{evt_id.strip()}\nPublisher:{publisher.strip()}\nObservation Start:{obs_start_time.strip()}\nObservation End:{obs_end_time.strip()}\n",
        fontsize=14,
    )
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    # plt.setp(ax2.get_xticklabels(), rotation=20, ha="right", rotation_mode="anchor")
    plt.tight_layout()
    plt.savefig(f"./events/Event_{evt_id}_obs_window_{config._runtime.iteration}.pdf")
    plt.show()
