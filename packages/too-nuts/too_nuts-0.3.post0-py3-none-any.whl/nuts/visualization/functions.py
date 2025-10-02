""" Functions for visualizations.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: GalacticToEquatorial
   :noindex:

.. autofunction:: EquatorialToGalactic
   :noindex:

.. autofunction:: fig_Galactic
   :noindex:

.. autofunction:: fig_Equatorial
   :noindex:

"""

import os

import astropy.coordinates as acoord
import matplotlib.pyplot as plt
import numpy as np

from nuts.visualization.parameters import alphaG, deltaG, lNCP

from ..config.config import ToOConfig

plt.rc("text", usetex=False)
plt.rc("font", family="serif")


def GalacticToEquatorial(long, lat):
    """From Galactic to Equatorial coordinates.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-15

    Args:
        long: longitude (rad)
        lat: latitude (rad)

    Returns:
        delta: declination (rad)
        alpha: right ascension (rad)

    """
    sin_delta = np.sin(lat) * np.sin(deltaG) + np.cos(lat) * np.cos(deltaG) * np.cos(
        lNCP - long
    )
    cos_delta = np.sqrt(1.0 - sin_delta**2)

    delta = np.arcsin(sin_delta)

    sin_alpha_alphaG = np.cos(lat) * np.sin(lNCP - long) / cos_delta
    cos_alpha_alphaG = (
        np.sin(lat) * np.cos(deltaG)
        - np.cos(lat) * np.sin(deltaG) * np.cos(lNCP - long)
    ) / cos_delta

    boolsin = sin_alpha_alphaG > 0
    boolcos = cos_alpha_alphaG > 0

    alpha_alphaG = (
        boolcos * boolsin * np.arcsin(sin_alpha_alphaG)
        + (1.0 - boolcos) * boolsin * np.arccos(cos_alpha_alphaG)
        + (1.0 - boolcos) * (1.0 - boolsin) * (np.pi - np.arcsin(sin_alpha_alphaG))
        + boolcos * (1.0 - boolsin) * (2.0 * np.pi - np.arccos(cos_alpha_alphaG))
    )

    alpha = np.mod(alpha_alphaG + alphaG, 2.0 * np.pi)

    return delta, alpha


def EquatorialToGalactic(delta, alpha):
    """From Galactic to Equatorial coordinates.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-15

    Args:
        delta: declination (rad)
        alpha: right ascension (rad)

    Returns:
        long: longitude (rad)
        lat: latitude (rad)

    """
    sin_lat = np.sin(delta) * np.sin(deltaG) + np.cos(delta) * np.cos(deltaG) * np.cos(
        alpha - alphaG
    )
    cos_lat = np.sqrt(1.0 - sin_lat**2)

    lat = np.arcsin(sin_lat)

    sin_lNCP_long = np.cos(delta) * np.sin(alpha - alphaG) / cos_lat
    cos_lNCP_long = (
        np.sin(delta) * np.cos(deltaG)
        - np.cos(delta) * np.sin(deltaG) * np.cos(alpha - alphaG)
    ) / cos_lat

    boolsin = sin_lNCP_long > 0
    boolcos = cos_lNCP_long > 0

    lNCP_long = (
        boolcos * boolsin * np.arcsin(sin_lNCP_long)
        + (1.0 - boolcos) * boolsin * np.arccos(cos_lNCP_long)
        + (1.0 - boolcos) * (1.0 - boolsin) * (np.pi - np.arcsin(sin_lNCP_long))
        + boolcos * (1.0 - boolsin) * (2.0 * np.pi - np.arccos(cos_lNCP_long))
    )

    long = np.mod(lNCP - lNCP_long, 2.0 * np.pi)

    return long, lat


def fig_Galactic(config, long_tab, lat_tab, quant, plot_name, **kwargs):
    """Effective area map in Galactic coordinates.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-15

    Args:
        long_tab: array of longitudes
        lat_tab: array of latitudes
        quant: quantity to plot as a function of longitude and latitude
        s_ra (list): right ascensions of sources
        s_dec (list): declinations of sources
        s_type (list): types of sources
        s_name (list): names of sources
        plot_name (path): figure path

    """
    long_tab = np.concatenate(
        (
            long_tab[:, int(len(long_tab[0, :]) / 2) :] - 2 * np.pi,
            long_tab[:, : int(len(long_tab[0, :]) / 2)],
        ),
        axis=1,
    )

    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111, projection="aitoff")
    plt.subplots_adjust(left=0.05, right=0.98, bottom=0.05, top=0.98)

    plt.pcolormesh(long_tab, lat_tab, quant, lw=2, vmin=-1.0, vmax=0)

    if "s_ra" in kwargs:
        s_ra = kwargs["s_ra"]
        s_dec = kwargs["s_dec"]
        s_type = kwargs["s_type"]
        s_name = kwargs["s_name"]
        for i in range(len(s_ra)):
            lon_loc, lat_loc = EquatorialToGalactic(s_dec[i], s_ra[i])
            if lon_loc < np.pi:
                lon_loc = -lon_loc
            else:
                lon_loc = 2.0 * np.pi - lon_loc
            plt.plot(
                lon_loc, lat_loc, linestyle="", marker="*", markersize=10, color="r"
            )
            if kwargs["print_names"]:
                ax.annotate(
                    s_name[i] + " (" + s_type[i] + ")",
                    (lon_loc, lat_loc),
                    color="k",
                    size=14,
                )

    tick_labels = np.array(
        [
            r"150$\degree$",
            r"120$\degree$",
            r"90$\degree$",
            r"60$\degree$",
            r"30$\degree$",
            r"0$\degree$",
            r"330$\degree$",
            r"300$\degree$",
            r"270$\degree$",
            r"240$\degree$",
            r"210$\degree$",
        ]
    )
    ax.set_xticklabels(tick_labels)
    tick_labels = np.array(
        [
            r"-75$\degree$",
            r"-60$\degree$",
            r"-45$\degree$",
            r"-30$\degree$",
            r"-15$\degree$",
            r"0$\degree$",
            r"15$\degree$",
            r"30$\degree$",
            r"45$\degree$",
            r"60$\degree$",
            r"75$\degree$",
        ]
    )
    ax.set_yticklabels(tick_labels)
    plt.grid(True, color="grey", lw=0.25)
    ax.tick_params(labelsize=16)
    ax.tick_params(axis="x", colors="grey")

    ax.set_rasterized(True)
    extension = config.output.plots.source_skymaps.plot_format
    plt.savefig(f"{plot_name}_Galactic_{config._runtime.iteration}.{extension}")
    plt.close()


def fig_Equatorial(config, RA_tab, DEC_tab, quant, plot_name, **kwargs):
    """Effective area map in Equatorial coordinates.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-15

    Args:
        RA_tab: array of right ascensions
        DEC_tab: array of declinations
        quant: quantity to plot as a function of RA and DEC
        s_ra (list): right ascensions of sources
        s_dec (list): declinations of sources
        s_type (list): types of sources
        s_name (list): names of sources
        plot_name (path): figure path

    """
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111, projection="aitoff")
    plt.subplots_adjust(left=0.05, right=0.98, bottom=0.0, top=1.0)

    plt.pcolormesh(RA_tab - np.pi, DEC_tab, quant, vmin=-1.0, vmax=0.0)

    if "s_ra" in kwargs:
        s_ra = kwargs["s_ra"]
        s_dec = kwargs["s_dec"]
        s_type = kwargs["s_type"]
        s_name = kwargs["s_name"]
        for i in range(len(s_ra)):
            plt.plot(
                np.pi - s_ra[i],
                s_dec[i],
                linestyle="",
                marker="*",
                markersize=10,
                color="r",
            )
            if kwargs["print_names"]:
                ax.annotate(
                    s_name[i] + " (" + s_type[i] + ")",
                    (np.pi - s_ra[i], s_dec[i]),
                    color="k",
                    size=14,
                )

    tick_labels = np.array(
        ["22h", "20h", "18h", "16h", "14h", "12h", "10h", "8h", "6h", "4h", "2h"]
    )
    ax.set_xticklabels(tick_labels)
    plt.grid(True, color="grey", lw=0.25)
    ax.tick_params(labelsize=16)
    ax.tick_params(axis="x", colors="grey")

    ax.set_rasterized(True)
    extension = config.output.plots.source_skymaps.plot_format
    plt.savefig(f"{plot_name}_Equatorial_{config._runtime.iteration}.{extension}")
