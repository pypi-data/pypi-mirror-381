""" Visualize source locations on a sky map.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: read_json_key
   :noindex:

.. autofunction:: visualize_sources
   :noindex:

"""

import logging
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy.time import Time

from ..config.config import ToOConfig
from ..detector_motion.detector import DetectorLocation
from ..visualization.exposure import compute_geo_exp_day, exp_gal
from ..visualization.functions import EquatorialToGalactic, fig_Equatorial, fig_Galactic
from ..visualization.parameters import Alpha_tab, Delta_tab


def read_json_key(sources: dict, source_choice: str) -> str:
    """Select source types considering format used in json files.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-07-25

    Args:
        sources: list of sources
        source_choice: all or observable or scheduled

    Returns:
        stype, sname, scoor, stime, sobse (str): properties of events

    """
    stype = []
    sname = []
    scoor = []
    stime = []
    sobse = []
    for i in range(len(sources)):
        if source_choice != "all":
            stype.append(sources["event"][i]["event_type"])
            sname.append(sources["event"][i]["event_id"])
            scoor.append(sources["event"][i]["coordinates"])
            stime.append(sources["event"][i]["detection_time"])
            sobse.append(sources["observations"][i])
        else:
            stype.append(sources["event"][i]["event_type"])
            sname.append(sources["event"][i]["event_id"])
            scoor.append(sources["event"][i]["coordinates"])
            stime.append(sources["event"][i]["detection_time"])
    return stype, sname, scoor, stime, sobse


def visualize_sources(config: ToOConfig, **kwargs):
    """Plot sky maps with sources.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-07-25

    Args:
        config (dict): config file
    """
    time = config._runtime.observation_starts

    source_choice = kwargs["source_choice"]
    if str(source_choice) == "none":
        plot_name = config.output.plots.source_skymaps.skymap_none
        if plot_name is None:
            return
        else:
            sources = []
    elif str(source_choice) == "all":
        plot_name = config.output.plots.source_skymaps.skymap_all
        if plot_name is None:
            return
        else:
            sources_file = config.output.observations.all_file
            sources = pd.read_json(sources_file)
            print_bool = False
    elif str(source_choice) == "observable":
        plot_name = config.output.plots.source_skymaps.skymap_obs
        if plot_name is None:
            return
        else:
            sources_file = config.output.observations.observable_file
            sources = pd.read_json(sources_file)
            print_bool = True
    elif str(source_choice) == "scheduled":
        plot_name = config.output.plots.source_skymaps.skymap_sched
        if plot_name is None:
            return
        else:
            sources_file = config.output.observations.scheduled_file
            sources = pd.read_json(sources_file)
            print_bool = True
    else:
        print("YOU CHOSE A KEYWORD THAT DOES NOT EXIST")

    logging.info("***************************************************")
    logging.info("Visualize sources... " + str(source_choice))
    # Compute exposure as a background
    bg, bg_fov, bg_sun = np.nan_to_num(
        compute_geo_exp_day(config, Alpha_tab, Delta_tab, time)
    )
    np.seterr(divide="ignore")
    bg_equ_ful = np.log10(bg[:, ::-1] / np.max(bg))
    bg_equ_fov = np.log10(bg_fov[:, ::-1] / np.max(bg_fov))
    bg_equ_sun = np.log10(bg_sun[:, ::-1] / np.max(bg_sun))
    bg_gal_ful = np.log10(exp_gal(Alpha_tab, Delta_tab, bg) / np.max(bg))
    bg_gal_fov = np.log10(exp_gal(Alpha_tab, Delta_tab, bg_fov) / np.max(bg_fov))
    bg_gal_sun = np.log10(exp_gal(Alpha_tab, Delta_tab, bg_sun) / np.max(bg_sun))
    np.seterr(divide="warn")

    # Directory for figures
    dirf = str(config.output.plots.directory)
    if not os.path.exists(dirf):
        os.makedirs(dirf)

    if str(source_choice) != "none":
        stype, sname, scoor, stime, sobse = read_json_key(sources, str(source_choice))

        ra = np.zeros(len(scoor))
        dec = np.zeros(len(scoor))
        for i in range(len(scoor)):
            coor = SkyCoord(ra=scoor[i]["ra"], dec=scoor[i]["dec"])
            ra[i] = coor.ra.rad
            dec[i] = coor.dec.rad

        for i in range(len(stype)):
            logging.info(str(i + 1) + "/ " + stype[i] + ", " + sname[i])
            logging.info(
                "Coordinates (RA, DEC): (" + str(ra[i]) + "," + str(dec[i]) + ")"
            )
            logging.info(
                "Coordinates (RA, DEC): ("
                + str(ra[i] * 180.0 / np.pi)
                + ","
                + str(dec[i] * 180.0 / np.pi)
                + ")"
            )
            logging.info("Detection time: " + str(stime[i]))
            if len(sobse) > 0:
                logging.info("Observation:")
                logging.info("Move time: " + str(sobse[i]["1"]["move_time"]))
                logging.info("Start time: " + str(sobse[i]["1"]["start_time"]))
                logging.info("End time: " + str(sobse[i]["1"]["end_time"]))
                logging.info("Pointing: " + str(sobse[i]["1"]["pointing_dir"]))

        fig_Equatorial(
            config,
            Alpha_tab,
            Delta_tab,
            bg_equ_ful,
            plot_name,
            s_ra=ra,
            s_dec=dec,
            s_type=stype,
            s_name=sname,
            print_names=print_bool,
        )
        fig_Galactic(
            config,
            Alpha_tab,
            Delta_tab,
            bg_gal_ful,
            plot_name,
            s_ra=ra,
            s_dec=dec,
            s_type=stype,
            s_name=sname,
            print_names=print_bool,
        )
    else:
        # Plot geometrical exposure
        bg_equ = [bg_equ_fov, bg_equ_sun, bg_equ_ful]
        bg_gal = [bg_gal_fov, bg_gal_sun, bg_gal_ful]
        name = [f"{plot_name}_fov", f"{plot_name}_sun", f"{plot_name}_sun_moon"]
        for iname in range(len(name)):
            fig_Equatorial(config, Alpha_tab, Delta_tab, bg_equ[iname], name[iname])
            fig_Galactic(config, Alpha_tab, Delta_tab, bg_gal[iname], name[iname])


def visualize_sources_obs_sched(config: ToOConfig, **kwargs):
    """Plot sky maps with sources, superimpose obs and sched.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-07-25

    Args:
        config (dict): config file
    """
    plot_name = config.output.plots.source_skymaps.skymap_comp
    extension = config.output.plots.source_skymaps.plot_format

    if plot_name is None:
        return

    else:
        logging.info("Visualize sources... ")
        time = config._runtime.observation_starts
        sources_file = config.output.observations.observable_file
        sources_obs = pd.read_json(sources_file)
        sources_file = config.output.observations.scheduled_file
        sources = pd.read_json(sources_file)

        # Compute exposure as a background
        bg, bg_fov, bg_sun = np.nan_to_num(
            compute_geo_exp_day(config, Alpha_tab, Delta_tab, time)
        )
        np.seterr(divide="ignore")
        bg_equ_ful = np.log10(bg[:, ::-1] / np.max(bg))
        bg_gal_ful = np.log10(exp_gal(Alpha_tab, Delta_tab, bg) / np.max(bg))
        np.seterr(divide="warn")

        # Directory for figures
        dirf = str(config.output.plots.directory)
        if not os.path.exists(dirf):
            os.makedirs(dirf)

        stype, sname, scoor, stime, sobse = read_json_key(sources_obs, "observable")

        ra_obs = np.zeros(len(scoor))
        dec_obs = np.zeros(len(scoor))
        for i in range(len(scoor)):
            coor = SkyCoord(ra=scoor[i]["ra"], dec=scoor[i]["dec"])
            ra_obs[i] = coor.ra.rad
            dec_obs[i] = coor.dec.rad

        stype, sname, scoor, stime, sobse = read_json_key(sources, "scheduled")

        ra = np.zeros(len(scoor))
        dec = np.zeros(len(scoor))
        for i in range(len(scoor)):
            coor = SkyCoord(ra=scoor[i]["ra"], dec=scoor[i]["dec"])
            ra[i] = coor.ra.rad
            dec[i] = coor.dec.rad

        # =====================================================================
        # Figure in equatorial coordinates

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_subplot(111, projection="aitoff")
        plt.subplots_adjust(left=0.05, right=0.98, bottom=0.0, top=1.0)

        plt.pcolormesh(Alpha_tab - np.pi, Delta_tab, bg_equ_ful, vmin=-1.0, vmax=0.0)

        for i in range(len(ra_obs)):
            plt.plot(
                np.pi - ra_obs[i],
                dec_obs[i],
                linestyle="",
                marker="*",
                markersize=20,
                mec="k",
                mfc="w",
                markeredgewidth=2,
            )

        for i in range(len(ra)):
            plt.plot(
                np.pi - ra[i],
                dec[i],
                linestyle="",
                marker="*",
                markersize=10,
                label=sname[i] + " (" + stype[i] + ")",
            )

        tick_labels = np.array(
            ["22h", "20h", "18h", "16h", "14h", "12h", "10h", "8h", "6h", "4h", "2h"]
        )
        ax.set_xticklabels(tick_labels)
        plt.grid(True, color="grey", lw=0.25)
        ax.tick_params(labelsize=16)
        ax.tick_params(axis="x", colors="grey")
        plt.legend(fontsize=14)

        ax.set_rasterized(True)
        plt.savefig(f"{plot_name}_Equatorial_{config._runtime.iteration}.{extension}")

        # =====================================================================
        # Figure in galactic coordinates

        long_tab = np.concatenate(
            (
                Alpha_tab[:, int(len(Alpha_tab[0, :]) / 2) :] - 2 * np.pi,
                Alpha_tab[:, : int(len(Alpha_tab[0, :]) / 2)],
            ),
            axis=1,
        )
        lat_tab = Delta_tab

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_subplot(111, projection="aitoff")
        plt.subplots_adjust(left=0.05, right=0.98, bottom=0.05, top=0.98)

        plt.pcolormesh(long_tab, lat_tab, bg_gal_ful, lw=2, vmin=-1.0, vmax=0)

        for i in range(len(ra_obs)):
            lon_loc, lat_loc = EquatorialToGalactic(dec_obs[i], ra_obs[i])
            if lon_loc < np.pi:
                lon_loc = -lon_loc
            else:
                lon_loc = 2.0 * np.pi - lon_loc
            plt.plot(
                lon_loc,
                lat_loc,
                linestyle="",
                marker="*",
                markersize=20,
                mec="k",
                mfc="w",
                markeredgewidth=2,
            )

        for i in range(len(ra)):
            lon_loc, lat_loc = EquatorialToGalactic(dec[i], ra[i])
            if lon_loc < np.pi:
                lon_loc = -lon_loc
            else:
                lon_loc = 2.0 * np.pi - lon_loc
            plt.plot(
                lon_loc,
                lat_loc,
                linestyle="",
                marker="*",
                markersize=10,
                label=sname[i] + " (" + stype[i] + ")",
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
        plt.legend(fontsize=14, loc=1)

        ax.set_rasterized(True)
        plt.savefig(f"{plot_name}_Galactic_{config._runtime.iteration}.{extension}")
