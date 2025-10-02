""" Visualize source trajectories in detector frame.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: fig_add_fov
   :noindex:

.. autofunction:: fig_add_time
   :noindex:

.. autofunction:: save_traj_data
   :noindex:

.. autofunction:: fig_trajectories
   :noindex:

.. autofunction:: fig_trajectories_scheduled
   :noindex:

"""

import glob
import logging
import os

import astropy.coordinates as acoord
import astropy.time as atime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as u
from astropy.time import Time, TimeDelta

from ..config.config import ToOConfig
from ..observation_period.source_observability import get_source_trajectories

plt.rc("text", usetex=False)
plt.rc("font", family="serif")


def fig_add_fov(ax, det_az, det_al, halffov_az, halffov_alt, booldeg):
    """Add detector field of view to figure.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-07-29

    Args:
        ax
        det_az
        det_al
        halffov_az
        halffov_alt
    """
    maxang = booldeg * 360.0 + (1.0 - booldeg) * 2.0 * np.pi

    if det_az - halffov_az < 0:
        miniaz1 = 0
        maxiaz1 = det_az + halffov_az
        miniaz2 = maxang + (det_az - halffov_az)
        maxiaz2 = maxang
    elif det_az + halffov_az > maxang:
        miniaz1 = det_az - halffov_az
        maxiaz1 = maxang
        miniaz2 = 0
        maxiaz2 = det_az + halffov_az - maxang
    else:
        miniaz1 = det_az - halffov_az
        maxiaz1 = det_az + halffov_az
        miniaz2 = det_az - halffov_az
        maxiaz2 = det_az + halffov_az

    ax.fill_between(
        [miniaz1, maxiaz1],
        det_al - halffov_alt,
        det_al + halffov_alt,
        facecolor="lightsteelblue",
    )
    ax.fill_between(
        [miniaz2, maxiaz2],
        det_al - halffov_alt,
        det_al + halffov_alt,
        facecolor="lightsteelblue",
    )


def fig_add_time(ax, traj_ti, traj_az, traj_al, ind):
    """Write time stamp on figure.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-09-10

    Args:
        ax
        traj_ti
        traj_az
        traj_al
        ind
    """
    ax.annotate(
        str(traj_ti[ind])[11:16] + " UTC",
        xy=(traj_az[ind], traj_al[ind]),
        xycoords="data",
        xytext=(traj_az[ind], traj_al[ind] + 1),
        textcoords="data",
        va="top",
        ha="center",
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )


def save_traj_data(config: ToOConfig, observation, name_event, traj, fname):
    """Save trajectory data in txt file for later use.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-02-26

    Args:
        config (dict): config file
        observation (ToOObservation): Observation object with source information
        name_event (str): Name of source used to save file
        traj: Trajectory of source in detector frame
        fname: file name

    """
    f = open(fname, "w")
    if len(observation.observations) > 0:
        f.write(
            str(observation.event.event_type)
            + ","
            + str(observation.event.event_id)
            + ","
            + str(observation.event.coordinates.ra.deg)
            + ","
            + str(observation.event.coordinates.dec.deg)
            + ","
            + str(observation.observations[0].pointing_dir.az.rad)
            + ","
            + str(observation.observations[0].pointing_dir.alt.rad)
            + "\n"
        )
    else:
        f.write(
            str(observation.event.event_type)
            + ","
            + str(observation.event.event_id)
            + ","
            + "none,"
            + "none\n"
        )
    for i in range(len(traj[2])):
        f.write(
            str(traj[0][i])
            + ","
            + str(traj[1][i].az.deg)
            + ","
            + str(traj[1][i].alt.deg)
            + ","
            + str(traj[2][i])
            + "\n"
        )
    f.close()


def fig_trajectories(config: ToOConfig, observation, count, time_loc):
    """Visualize source trajectories from detector's frame.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-15

    Args:
        config (dict): config file
        observation (ToOObservation): Observation object with source information
        count: source number
        time_loc (Time): beginning observation window

    """
    name_event = str(
        str(observation.event.event_type) + "_" + str(observation.event.event_id)
    )
    name_event = name_event.replace(" ", "")
    name_event = name_event.replace("/", "")
    traj = get_source_trajectories(config, observation.event)

    # Save trajectory info
    dir_save = config.output.plots.source_trajectories.directory
    dir_save.mkdir(parents=True, exist_ok=True)
    fname = dir_save / f"Traj_{name_event}.txt"
    save_traj_data(config, observation, name_event, traj, fname)
    if len(observation.observations) > 0:
        fname = dir_save / f"Traj_observable_{name_event}.txt"
        save_traj_data(config, observation, name_event, traj, fname)

    # =========================================================================
    # Figure with full sky
    plot_directory = config.output.plots.source_trajectories.directory
    plot_directory.mkdir(parents=True, exist_ok=True)
    plot_name = config.output.plots.source_trajectories.source_trajectories_full_sky

    if plot_name is not None:
        extension = config.output.plots.detector.plot_format
        plot_name = f"{plot_name}_{name_event}_{config._runtime.iteration}.{extension}"

        # Detector fov
        halffov_az = config.settings.observation.fov_az.to("rad").value / 2.0
        halffov_alt = config.settings.observation.fov_alt.to("rad").value / 2.0

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_subplot(111, projection="aitoff")
        plt.subplots_adjust(left=0.05, right=0.98, bottom=0.0, top=1.0)

        if len(observation.observations) > 0:
            # Visualize detector fov (optimized)
            det_point = observation.observations[0].pointing_dir
            ax.fill_between(
                [
                    det_point.az.rad - np.pi - halffov_az,
                    det_point.az.rad - np.pi + halffov_az,
                ],
                det_point.alt.rad - halffov_alt,
                det_point.alt.rad + halffov_alt,
                facecolor="lightsteelblue",
            )

        # Source trajectory
        plt.plot(
            traj[1].az.rad - np.pi,
            traj[1].alt.rad,
            linestyle="",
            marker="*",
            markersize=5,
            color="k",
        )

        # Observable source trajectory
        plt.plot(
            (traj[1].az.rad - np.pi)[traj[2]],
            (traj[1].alt.rad)[traj[2]],
            linestyle="",
            marker="*",
            markersize=10,
            color="b",
        )

        plt.xticks([-180, -90, 0, 90])
        tick_labels = np.array(["N", "E", "S", "W"])
        ax.set_xticklabels(tick_labels)
        plt.grid(True, color="w", lw=0.25)
        ax.tick_params(labelsize=12)
        ax.tick_params(axis="x", colors="k")
        ax.set_rasterized(True)
        plt.title(
            observation.event.event_id + " (" + observation.event.event_type + ")",
            size=18,
        )
        plt.savefig(plot_name)
        plt.close(fig)

    # =========================================================================
    # Zoomed figure
    plot_directory = config.output.plots.source_trajectories.directory
    plot_directory.mkdir(parents=True, exist_ok=True)
    plot_name = config.output.plots.source_trajectories.source_trajectories_zoom

    if plot_name is not None:
        extension = config.output.plots.detector.plot_format
        plot_name = f"{plot_name}_{name_event}_{config._runtime.iteration}.{extension}"

        # Detector fov
        halffov_az = config.settings.observation.fov_az.to("rad").value / 2.0
        halffov_alt = config.settings.observation.fov_alt.to("rad").value / 2.0

        if len(observation.observations) > 0:
            # Values in degrees
            halffov_az = config.settings.observation.fov_az.to("deg").value / 2.0
            halffov_alt = config.settings.observation.fov_alt.to("deg").value / 2.0

            fig = plt.figure()
            ax = fig.add_subplot(111)
            plt.subplots_adjust(left=0.15, bottom=0.13)

            # Source trajectory
            plt.plot(
                traj[1].az.deg,
                traj[1].alt.deg,
                linestyle="",
                marker="*",
                markersize=5,
                color="k",
            )

            # Observable source trajectory
            plt.plot(
                (traj[1].az.deg)[traj[2]],
                (traj[1].alt.deg)[traj[2]],
                linestyle="",
                marker="*",
                markersize=10,
                color="b",
            )

            # Beginning of the observability window
            det_point = observation.observations[0].pointing_dir
            index_min = np.argmin(
                abs((traj[1].az.deg)[traj[2]] - (det_point.az.deg + halffov_az) % 360)
            )
            fig_add_time(
                ax,
                traj[0][traj[2]],
                (traj[1].az.deg)[traj[2]],
                (traj[1].alt.deg)[traj[2]],
                index_min,
            )

            # Visualize detector fov
            fig_add_fov(
                ax, det_point.az.deg, det_point.alt.deg, halffov_az, halffov_alt, True
            )

            ax.tick_params(labelsize=14)
            ax.set_xlim([det_point.az.deg - 8.0, det_point.az.deg + 8.0])
            ax.set_ylim([det_point.alt.deg - 5.0, det_point.alt.deg + 5.0])
            ax.set_xlabel("Azimuth", fontsize=16)
            ax.set_ylabel("Altitude", fontsize=16)
            plt.title(
                observation.event.event_id + " (" + observation.event.event_type + ")",
                size=18,
            )
            plt.savefig(plot_name)
            plt.close(fig)


def load_sched_data(config: ToOConfig):
    """Load source trajectory data.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-02-26

    Args:
        config (dict): config file
    """
    arr = pd.read_json(config.output.observations.scheduled_file)
    name_event = []
    stype = []
    sname = []
    scoor = []
    stimemin = []
    stimemax = []
    stimemov = []
    spoint = []
    for i in range(len(arr)):
        stype.append(arr["event"][i]["event_type"])
        sname.append(arr["event"][i]["event_id"])
        scoor.append(arr["event"][i]["coordinates"])
        stimemin.append(arr["observations"][i]["1"]["start_time"])
        stimemax.append(arr["observations"][i]["1"]["end_time"])
        stimemov.append(arr["observations"][i]["1"]["move_time"])
        spoint.append(arr["observations"][i]["1"]["pointing_dir"])

    ra = np.zeros(len(scoor))
    dec = np.zeros(len(scoor))
    for i in range(len(scoor)):
        coor = acoord.SkyCoord(ra=scoor[i]["ra"], dec=scoor[i]["dec"])
        ra[i] = coor.ra.deg
        dec[i] = coor.dec.deg

    # List of observable sources trajectory files
    files_traj = glob.glob(
        str(config.output.plots.directory) + "/Source_Trajectories/Traj_observable*.txt"
    )
    num_obs = len(files_traj)
    # Load trajectories
    info = []
    traj_ti = []
    traj_az = []
    traj_al = []
    traj_bo = []
    for i in range(num_obs):
        info.append(
            np.array(
                pd.read_csv(
                    files_traj[i], delimiter=",", nrows=1, header=None, dtype=str
                )
            )
        )
        f = np.array(pd.read_csv(files_traj[i], delimiter=","))
        traj_ti.append(f[:, 0])
        traj_az.append(f[:, 1])
        traj_al.append(f[:, 2])
        traj_bo.append(f[:, 3])

    # Find scheduled sources trajectory files
    ind_arr = np.empty(len(stype))
    for index in range(num_obs):
        for k in range(len(stype)):
            if (
                (str(info[index][0][0]) == str(stype[k]))
                and (info[index][0][1] == sname[k])
                and (abs(float(info[index][0][2]) - ra[k]) < 1e-3)
                and (abs(float(info[index][0][3]) - dec[k]) < 1e-3)
            ):
                ind_arr[k] = index

    # Loop over scheduled sources
    for it in range(len(ind_arr)):
        index = int(ind_arr[it])
        # bool_nl = 0
        logging.info(
            "Source observed: "
            + str(info[index][0][1])
            + " ("
            + str(info[index][0][0])
            + ")"
        )

        name_ev = str(str(info[index][0][0]) + "_" + str(info[index][0][1]))
        name_ev = name_ev.replace(" ", "")
        name_ev = name_ev.replace("/", "")
        name_event.append(name_ev)

        # Scheduled source properties
        time_move = Time(stimemov[it])
        time_min = Time(stimemin[it])
        time_max = Time(stimemax[it])

        # Save this info to the log file
        logging.info("Repointing time: " + str(time_move))
        logging.info("Time min: " + str(time_min))
        logging.info("Time max: " + str(time_max))
        logging.info("Pointing direction: " + str(spoint[it]))

    return (
        name_event,
        stimemin,
        stimemax,
        spoint,
        ind_arr,
        info,
        traj_ti,
        traj_az,
        traj_al,
        traj_bo,
    )


def fig_trajectories_scheduled(config: ToOConfig):
    """Visualize scheduled source trajectories in detector's frame.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-07-29

    Args:
        config (dict): config file
    """
    plot_directory = config.output.plots.source_trajectories.directory
    plot_directory.mkdir(parents=True, exist_ok=True)

    # =====================================================================
    # First general figure

    plot_name_ini = (
        config.output.plots.source_trajectories.source_trajectories_comp_full_sky
    )
    if plot_name_ini is not None:
        extension = config.output.plots.source_trajectories.plot_format

        # Detector fov
        halffov_az = config.settings.observation.fov_az.to("deg").value / 2.0
        halffov_alt = config.settings.observation.fov_alt.to("deg").value / 2.0

        (
            name_event,
            stimemin,
            stimemax,
            spoint,
            ind_arr,
            info,
            traj_ti,
            traj_az,
            traj_al,
            traj_bo,
        ) = load_sched_data(config)
        num_obs = len(traj_ti)

        # Loop over scheduled sources
        for it in range(len(ind_arr)):
            index = int(ind_arr[it])

            # Detector's properties
            det_az = float(spoint[it]["AZ"])
            det_al = float(spoint[it]["ALT"])

            # Scheduled source properties
            time_min = Time(stimemin[it])
            time_max = Time(stimemax[it])
            arr_bo = np.array(traj_bo[index], dtype=bool)

            plot_name = f"{plot_name_ini}_{name_event[it]}_{stimemin[it]}__{config._runtime.iteration}.{extension}"

            fig = plt.figure()
            ax = fig.add_subplot(111)
            plt.subplots_adjust(left=0.15, bottom=0.13)

            # Visualize detector fov
            fig_add_fov(ax, det_az, det_al, halffov_az, halffov_alt, True)
            # Visualize full trajectory of scheduled source
            plt.plot(
                traj_az[index],
                traj_al[index],
                ls="",
                marker="*",
                markersize=5,
                color="k",
            )
            # Visualize observable portion of trajectory of scheduled source
            ax.plot(
                traj_az[index][arr_bo],
                traj_al[index][arr_bo],
                ls="",
                marker="*",
                markersize=10,
                color="b",
            )

            # Loop over other sources
            for i in range(num_obs):
                # Observability times
                arr_bo_loc = np.array(traj_bo[i], dtype=bool)
                timetest = Time(
                    np.array(traj_ti[i][arr_bo_loc], dtype="S"),
                    format="isot",
                    scale="utc",
                )
                # Define times of interest
                bool_time = (timetest >= time_min) * (timetest <= time_max)
                if sum(bool_time) > 0:
                    traj_ti_loc = traj_ti[i][arr_bo_loc][bool_time]
                    traj_az_loc = traj_az[i][arr_bo_loc][bool_time]
                    traj_al_loc = traj_al[i][arr_bo_loc][bool_time]
                    # Determine obervability time intervals
                    timetest = Time(
                        np.array(traj_ti_loc, dtype="S"), format="isot", scale="utc"
                    )
                    timelim = TimeDelta(
                        config.settings.calculation.time_increment + 0.5 * u.min
                    )
                    ittime = np.argwhere(np.diff(timetest.jd) > timelim.jd)
                    itall = np.append([0], ittime)
                    itall = np.append(itall, [len(timetest) - 1])
                    # Loop over observability time intervals
                    for itit in range(len(itall) - 1):
                        if np.isin(itall[itit], ittime):
                            idmin = itall[itit] + 1
                        else:
                            idmin = itall[itit]
                        idmax = itall[itit + 1] - 1
                        time_min_loc = Time(traj_ti[i][arr_bo_loc][idmin])
                        time_max_loc = Time(traj_ti[i][arr_bo_loc][idmax])

                    if (time_max_loc >= time_min) and (time_min_loc <= time_max):
                        plt.plot(
                            traj_az[i][arr_bo_loc],
                            traj_al[i][arr_bo_loc],
                            ls="",
                            marker="*",
                            markersize=5,
                            color="r",
                        )

            ax.tick_params(labelsize=14)
            ax.set_ylim([0, 360.0])
            ax.set_ylim([det_al - 25.0, det_al + 25.0])
            ax.set_xlabel("Azimuth", fontsize=16)
            ax.set_ylabel("Altitude", fontsize=16)
            plt.savefig(plot_name)
            plt.close(fig)

    # =====================================================================
    # Second zoomed figure

    plot_name_ini = (
        config.output.plots.source_trajectories.source_trajectories_comp_zoom
    )
    if plot_name_ini is not None:
        extension = config.output.plots.source_trajectories.plot_format

        # Detector fov
        halffov_az = config.settings.observation.fov_az.to("deg").value / 2.0
        halffov_alt = config.settings.observation.fov_alt.to("deg").value / 2.0

        (
            name_event,
            stimemin,
            stimemax,
            spoint,
            ind_arr,
            info,
            traj_ti,
            traj_az,
            traj_al,
            traj_bo,
        ) = load_sched_data(config)
        num_obs = len(traj_ti)

        # Loop over scheduled sources
        for it in range(len(ind_arr)):
            index = int(ind_arr[it])

            # Detector's properties
            det_az = float(spoint[it]["AZ"])
            det_al = float(spoint[it]["ALT"])

            # Scheduled source properties
            time_min = Time(stimemin[it])
            time_max = Time(stimemax[it])
            arr_bo = np.array(traj_bo[index], dtype=bool)

            plot_name = f"{plot_name_ini}_{name_event[it]}_{stimemin[it]}_{config._runtime.iteration}"

            fig = plt.figure(figsize=(8, 5))
            ax = fig.add_subplot(111)
            plt.subplots_adjust(left=0.12, right=0.95, bottom=0.12, top=0.95)

            # Visualize detector fov
            fig_add_fov(ax, det_az, det_al, halffov_az, halffov_alt, True)
            # Visualize full trajectory of scheduled source
            ax.plot(
                traj_az[index],
                traj_al[index],
                ls="",
                marker="*",
                markersize=10,
                color="k",
            )
            # Visualize observable portion of trajectory of scheduled source
            ax.plot(
                traj_az[index][arr_bo],
                traj_al[index][arr_bo],
                ls="",
                marker="*",
                markersize=10,
                color="b",
            )

            # Visualize time min and max of the source observation period
            timesrc = Time(
                np.array(traj_ti[index][arr_bo], dtype="S"), format="isot", scale="utc"
            )
            index_min = np.argmin(abs(timesrc - time_min))
            index_max = np.argmin(abs(timesrc - time_max))
            fig_add_time(
                ax,
                traj_ti[index][arr_bo],
                traj_az[index][arr_bo],
                traj_al[index][arr_bo],
                index_min,
            )
            fig_add_time(
                ax,
                traj_ti[index][arr_bo],
                traj_az[index][arr_bo],
                traj_al[index][arr_bo],
                index_max,
            )

            # Loop over other sources
            for i in range(num_obs):
                # Observability times
                arr_bo_loc = np.array(traj_bo[i], dtype=bool)
                timetest = Time(
                    np.array(traj_ti[i][arr_bo_loc], dtype="S"),
                    format="isot",
                    scale="utc",
                )
                # Define times of interest
                bool_time = (timetest >= time_min) * (timetest <= time_max)
                if sum(bool_time) > 0:
                    traj_ti_loc = traj_ti[i][arr_bo_loc][bool_time]
                    traj_az_loc = traj_az[i][arr_bo_loc][bool_time]
                    traj_al_loc = traj_al[i][arr_bo_loc][bool_time]
                    # Determine obervability time intervals
                    timetest = Time(
                        np.array(traj_ti_loc, dtype="S"), format="isot", scale="utc"
                    )
                    timelim = TimeDelta(
                        config.settings.calculation.time_increment + 0.5 * u.min
                    )
                    ittime = np.argwhere(np.diff(timetest.jd) > timelim.jd)
                    itall = np.append([0], ittime)
                    itall = np.append(itall, [len(timetest) - 1])
                    # Loop over observability time intervals
                    for itit in range(len(itall) - 1):
                        if np.isin(itall[itit], ittime):
                            idmin = itall[itit] + 1
                        else:
                            idmin = itall[itit]
                        idmax = itall[itit + 1]
                        # Redefine useful trajectory portions
                        traj_ti_loc = traj_ti_loc[idmin : idmax + 1]
                        traj_az_loc = traj_az_loc[idmin : idmax + 1]
                        traj_al_loc = traj_al_loc[idmin : idmax + 1]
                        # Determine if source crosses field of view
                        sumlow = 0
                        if det_az - halffov_az < 0.0:
                            sumlow = sum(
                                (traj_az_loc >= 360.0 + det_az - halffov_az)
                                * (traj_az_loc <= 360.0)
                            )
                        sumhig = 0
                        if det_az + halffov_az > 360.0:
                            sumhig = sum(
                                (traj_az_loc >= 0.0)
                                * (traj_az_loc <= det_az + halffov_az - 360.0)
                            )
                        summed = sum(
                            (traj_az_loc >= np.max([0, det_az - halffov_az]))
                            * (traj_az_loc <= np.min([det_az + halffov_az, 360.0]))
                        )
                        if (
                            summed + sumlow + sumhig > 0
                            and info[index][0][1] != info[i][0][1]
                        ):
                            # Save information about these coincident observations
                            logging.info("Coincident observation:")
                            logging.info(
                                str(info[i][0][1]) + " (" + str(info[i][0][0]) + ")"
                            )
                            # Visualize markers and times for coincident observations
                            ax.plot(
                                traj_az[i][arr_bo_loc],
                                traj_al[i][arr_bo_loc],
                                ls="",
                                marker="*",
                                markersize=5,
                                color="k",
                            )
                            ax.plot(
                                traj_az_loc,
                                traj_al_loc,
                                ls="",
                                marker="*",
                                markersize=10,
                                label=str(info[i][0][1])
                                + " ("
                                + str(info[i][0][0])
                                + ")",
                            )
                            ind = np.argmin(abs(timetest - time_min))
                            fig_add_time(ax, traj_ti_loc, traj_az_loc, traj_al_loc, ind)

            ax.tick_params(labelsize=14)
            ax.set_ylim([det_al - 5.0, det_al + 5.0])
            ax.set_xlabel("Azimuth", fontsize=16)
            ax.set_ylabel("Altitude", fontsize=16)
            ax.set_aspect("equal", adjustable="box")
            plt.legend(fontsize=12, frameon=False)

            # Make sure to save two figures if fov cut in azimuth
            if (det_az - halffov_az < 0.0) or (det_az + halffov_az > 360.0):
                ax.set_xlim([0.0, 16.0])
                plt.savefig(f"{plot_name}_1.{extension}")
                ax.set_xlim([360.0 - 16.0, 360.0])
                plt.savefig(f"{plot_name}_2.{extension}")
            else:
                ax.set_xlim([det_az - 8.0, det_az + 8.0])
                plt.savefig(f"{plot_name}.{extension}")
            plt.close(fig)
