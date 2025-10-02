""" Functions for visualizations.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: fig_observability_windows
   :noindex:

"""

import os

import astropy.coordinates as acoord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy import interpolate

from ..config.config import ToOConfig
from ..observation_period.sun_moon_cuts import moon_illumination

plt.rc("text", usetex=False)
plt.rc("font", family="serif")


def fig_observability_windows(
    config: ToOConfig,
    arr_time,
    moon_ill,
    sta_time_sun,
    end_time_sun,
    sta_time_moon,
    end_time_moon,
    sta_time,
    end_time,
):
    """Visualize successive observability windows.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-10-09

    Args:
        config (dict): config file

    """
    jdtoh = 24.0  # units: set to 1 for days, and 24 for hours

    fig, ax = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": [1, 3]})
    fig.subplots_adjust(hspace=0.2)

    ax[0].plot((arr_time - arr_time[0]) / jdtoh, moon_ill, ls="-")

    fsta = interpolate.interp1d(
        sta_time_sun - arr_time[0],
        sta_time_sun - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    fend = interpolate.interp1d(
        end_time_sun - arr_time[0],
        end_time_sun - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    ax[1].fill_between(
        (sta_time_sun - arr_time[0]) / jdtoh,
        fsta(sta_time_sun - arr_time[0]),
        fend(sta_time_sun - arr_time[0]),
        alpha=0.2,
        label="Sun constraint",
    )

    fsta = interpolate.interp1d(
        sta_time_moon - arr_time[0],
        sta_time_moon - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    fend = interpolate.interp1d(
        end_time_moon - arr_time[0],
        end_time_moon - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    ax[1].fill_between(
        (sta_time_moon - arr_time[0]) / jdtoh,
        fsta(sta_time_moon - arr_time[0]),
        fend(sta_time_moon - arr_time[0]),
        alpha=0.2,
        label="Moon constraint",
    )

    fsta = interpolate.interp1d(
        sta_time - arr_time[0],
        sta_time - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    fend = interpolate.interp1d(
        end_time - arr_time[0],
        end_time - sta_time_sun,
        bounds_error=False,
        fill_value="extrapolate",
    )
    ax[1].fill_between(
        (sta_time - arr_time[0]) / jdtoh,
        fsta(sta_time - arr_time[0]),
        fend(sta_time - arr_time[0]),
        alpha=0.2,
        label="Sun and Moon constraints",
    )

    for i in range(len(arr_time)):
        ax[1].plot(
            [(sta_time[i] - arr_time[0]) / jdtoh, (end_time[i] - arr_time[0]) / jdtoh],
            [sta_time[i] - sta_time_sun[i], end_time[i] - sta_time_sun[i]],
            ls="-",
        )

    ax[0].set_yticks([0.0, 0.5, 1.0])
    ax[0].xaxis.set_ticks_position("both")
    ax[0].yaxis.set_ticks_position("both")
    ax[1].xaxis.set_ticks_position("both")
    ax[1].yaxis.set_ticks_position("both")
    ax[0].tick_params(labelsize=12)
    ax[1].tick_params(labelsize=12)
    ax[1].set_xlim(
        np.nanmin(sta_time - arr_time[0]) / jdtoh - 1,
        np.nanmax(end_time - arr_time[0]) / jdtoh + 1,
    )
    ax[1].set_ylim(-0.4 * jdtoh, jdtoh)
    ax[1].set_xlabel("Days after beginning of observations", fontsize=10)
    ax[0].set_ylabel("Moon illumination", fontsize=10)
    ax[1].set_ylabel(
        "Time observability \n- Time astronomical night (hours)", fontsize=10
    )
    plt.subplots_adjust(left=0.14)
    plt.legend(fontsize=8, loc="upper right")

    # Save figure
    dirf = str(config.output.plots.directory)
    if not os.path.exists(dirf):
        os.makedirs(dirf)
    plt.savefig(
        dirf + "/" + f"Observability_windows_obs_window_{config._runtime.iteration}.pdf"
    )
    plt.close(fig)
