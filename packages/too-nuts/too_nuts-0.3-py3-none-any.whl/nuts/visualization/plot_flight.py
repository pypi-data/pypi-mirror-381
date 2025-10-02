"""Visualize sources types scheduled for a flight.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: append_sources
   :noindex:

.. autofunction:: append_sources_priority
   :noindex:

.. autofunction:: fig_obs_sources
   :noindex:

.. autofunction:: fig_obs_sources_priorities
   :noindex:

.. autofunction:: fig_stat_flight
   :noindex:

"""

import glob
import json
import logging
import os

import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time

from ..config.config import ToOConfig

plt.rc("text", usetex=False)
plt.rc("font", family="serif")


def append_sources(observable, path: str):
    """Append sources properties from json file.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-05-26

    Args:
        observable: list of sources
        path: path to json file

    Returns:
        observable: list of sources
    """
    f = open(path)
    sources = json.load(f)

    for i in range(len(sources)):
        event = []
        event_id = sources[i]["event"]["event_id"]
        publisher_id = sources[i]["event"]["publisher_id"]
        priority = sources[i]["event"]["priority"]
        existbool = False

        for j in range(len(sources[i]["observations"])):
            sourcesobs = sources[i]["observations"][str(j + 1)]
            obstime = Time(sourcesobs["end_time"]) - Time(sourcesobs["start_time"])

            for k in range(len(observable)):
                if event_id == observable[k][0] and publisher_id == observable[k][1]:
                    observable[k][2] += obstime
                    observable[k][3].append(obstime)
                    existbool = True

        if existbool is False:
            event.append(event_id)
            event.append(publisher_id)
            event.append(obstime)
            event.append([obstime])
            event.append(priority)
            observable.append(event)

    return observable


def append_sources_priority(observable, path: str):
    """Append sources properties from json file using priority ranking.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-05-26

    Args:
        observable: list of sources
        path: path to json file

    Returns:
        observable: list of sources
    """
    f = open(path)
    sources = json.load(f)

    for i in range(len(sources)):
        event = []
        priority = sources[i]["event"]["priority"]
        existbool = False

        for j in range(len(sources[i]["observations"])):
            sourcesobs = sources[i]["observations"][str(j + 1)]
            obstime = Time(sourcesobs["end_time"]) - Time(sourcesobs["start_time"])

            for k in range(len(observable)):
                if priority == observable[k][2]:
                    observable[k][0] += obstime
                    observable[k][1].append(obstime)
                    existbool = True

        if existbool is False:
            event.append(obstime)
            event.append([obstime])
            event.append(priority)
            observable.append(event)

    return observable


def fig_obs_sources(config, scheduled, times_str, fd):
    """Create and save figure with cumulative observation time.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-05-26

    Args:
        config: configuration parameters
        scheduled: list of scheduled sources
        times_str: list of str for file name
        fd: int, iteration index
    """
    extension = config.output.plots.flight.plot_format
    fname = config.output.plots.flight.tobs_sources
    nsources = 30
    tobsmin = 6e2
    tobsmax = 1e5
    fig = plt.figure(figsize=(14, 6))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(left=0.1, bottom=0.12)
    for k in range(len(scheduled)):
        for i in range(len(scheduled[k][3])):
            plt.plot(
                k + 1,
                # scheduled[k][1],
                scheduled[k][3][i].sec,
                linestyle="",
                marker="o",
                markersize=4,
                color="grey",
            )
        plt.plot(
            k + 1,
            # scheduled[k][1],
            scheduled[k][2].sec,
            linestyle="",
            marker="o",
            markersize=6,
            label=(
                str(k + 1)
                + ": "
                + str(scheduled[k][0])
                + ", priority: "
                + str(scheduled[k][4])
            ),
        )
    ax.tick_params(labelsize=14)
    ax.set_xticks(range(1, nsources + 1))
    ax.set_xlim([0.5, nsources + 0.5])
    ax.set_yscale("log")
    ax.set_ylim([tobsmin, tobsmax])
    ax.set_xlabel("Source #", fontsize=16)
    ax.set_ylabel("Total observation time (s)", fontsize=16)
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 0.8, pos.height])
    ax.legend(loc="center right", bbox_to_anchor=(1.4, 0.5), fontsize=10, frameon=False)
    plt.title(
        "Observations from " + times_str[0] + " to " + times_str[fd],
        size=14,
    )
    plt.savefig(f"{fname}_{times_str[fd]}.{extension}")
    plt.close(fig)


def fig_obs_sources_priorities(config, scheduled, observable, times_str, fd):
    """Create and save figure with cumulative observation time using priority ranking.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-05-26

    Args:
        config: configuration parameters
        scheduled: list of scheduled sources
        observable: list of obervable sources
        times_str: list of str for file name
        fd: int, iteration index
    """
    extension = config.output.plots.flight.plot_format
    fname = config.output.plots.flight.tobs_priorities
    tobsmin = 6e2
    tobsmax = 2e7
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for k in range(len(scheduled)):
        for i in range(len(scheduled[k][1])):
            plt.plot(
                scheduled[k][2],
                scheduled[k][1][i].sec,
                linestyle="",
                marker="o",
                markersize=4,
                color="grey",
            )
        plt.plot(
            scheduled[k][2],
            scheduled[k][0].sec,
            linestyle="",
            marker="o",
            markersize=6,
            color=colors[scheduled[k][2] - 2],
        )
    for k in range(len(observable)):
        plt.plot(
            observable[k][2],
            observable[k][0].sec,
            linestyle="",
            marker="o",
            markersize=6,
            markerfacecolor="None",
            markeredgecolor=colors[observable[k][2] - 2],
        )
    ax.tick_params(labelsize=14)
    ax.set_xticks(range(1, 9))
    ax.set_xlim([0.5, 8.5])
    ax.set_yscale("log")
    ax.set_ylim([tobsmin, tobsmax])
    ax.set_xlabel("Priority #", fontsize=16)
    ax.set_ylabel("Total observation time (s)", fontsize=16)
    plt.title(
        "Observations from " + times_str[0] + " to " + times_str[fd],
        size=14,
    )
    plt.subplots_adjust(bottom=0.13)
    plt.savefig(f"{fname}_{times_str[fd]}.{extension}")
    plt.close(fig)


def fig_stat_flight(config: ToOConfig):
    """Visualize source types scheduled for a flight.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-05-26

    Args:
        config
    """
    # Load output files
    filedir = np.array(glob.glob("*[!.toml][!.pdf][!.csv][!.npz]"))
    # Determine observation times and sort files
    times = np.array([])
    times_str = np.array([])
    i = 0
    while i < len(filedir):
        try:
            sources = json.load(
                open(filedir[i] + "/Observations/scheduled_output.json")
            )
            times = np.append(
                times, Time(sources[0]["observations"]["1"]["start_time"]).jd
            )
            times_str = np.append(
                times_str, sources[0]["observations"]["1"]["start_time"][0:10]
            )
            i += 1
        except Exception:
            logging.info(f"This file does not contain scheduled sources: {filedir[i]}")
            filedir = np.delete(filedir, i)
    idt = np.argsort(times)
    filedir = filedir[idt]
    times = times[idt]
    times_str = times_str[idt]
    logging.info(f"Input files: {filedir}")
    logging.info(f"Start of observations: {times_str[0]}")
    logging.info(f"End of observations: {times_str[len(times_str) - 1]}")
    # Name figures
    plot_directory = config.output.plots.flight.directory
    plot_directory.mkdir(parents=True, exist_ok=True)
    fname_tobs_sources = config.output.plots.flight.tobs_sources
    fname_tobs_priorities = config.output.plots.flight.tobs_priorities
    # Load sources info
    sources_sch_detail = []
    sources_obs = []
    sources_sch = []
    for fd in range(len(filedir)):
        namein_obs = filedir[fd] + "/Observations/observable_output.json"
        namein_sch = filedir[fd] + "/Observations/scheduled_output.json"
        sources_sch_detail = append_sources(sources_sch_detail, namein_sch)
        sources_obs = append_sources_priority(sources_obs, namein_obs)
        sources_sch = append_sources_priority(sources_sch, namein_sch)
        # Visualize results
        if fname_tobs_sources is not None:
            fig_obs_sources(config, sources_sch_detail, times_str, fd)
        if fname_tobs_priorities is not None:
            fig_obs_sources_priorities(config, sources_sch, sources_obs, times_str, fd)
    # Print observation times
    times_sch_sources = np.zeros(len(sources_sch_detail))
    times_obs = np.zeros(len(sources_obs))
    times_sch = np.zeros(len(sources_obs))
    for k in range(len(sources_sch_detail)):
        times_sch_sources[k] = sources_sch_detail[k][2].sec
    for k in range(len(sources_obs)):
        times_obs[k] = sources_obs[k][0].sec
    for k in range(len(sources_sch)):
        times_sch[k] = sources_sch[k][0].sec
    logging.info("Scheduled (sources):")
    logging.info(f"minimum observation time: {min(times_sch_sources)}")
    logging.info(f"maximum observation time: {max(times_sch_sources)}")
    logging.info(f"cumulated observation time: {sum(times_sch_sources)}")
    logging.info("Observability (priority):")
    logging.info(f"minimum observation time: {min(times_obs)}")
    logging.info(f"maximum observation time: {max(times_obs)}")
    logging.info(f"cumulated observation time: {sum(times_obs)}")
    logging.info("Scheduled (priority):")
    logging.info(f"minimum observation time: {min(times_sch)}")
    logging.info(f"maximum observation time: {max(times_sch)}")
    logging.info(f"cumulated observation time: {sum(times_sch)}")
