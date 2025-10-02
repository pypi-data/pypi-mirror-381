"""Library for all visualization routines for GW module.

original author: Luke Kupari (luke-kupari@uiowa.edu)

.. autofunction:: plot_traces_unoptimized
.. autofunction:: plot_traces_optimized
.. autofunction:: plot_azimuth

"""

import os

import matplotlib.pyplot as plt
import numpy as np


def plot_traces_unoptimized(event_name, coordinates, config):
    """Plots trajectories before optimization

    Args:
        event_name (str): name of event
        coordinates (array): trajectories for each point
        config (ToOConfig): config file
    """

    output_dir = config.output.plots.directory / "GW_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    single_az = coordinates[0][0].az.deg
    single_alt = coordinates[0][0].alt.deg
    ptime = config.settings.calculation.start_time.to_string().split("T")[0]

    plt.scatter(coordinates[0][0].az.deg, coordinates[0][0].alt.deg, s=1.5, c="black")
    plt.scatter(single_az[0], single_alt[0], s=1.5, color="cyan", label="Start")
    plt.scatter(single_az[-1], single_alt[-1], s=1.5, color="red", label="End")
    plt.xlabel("Azimuth (deg)")
    plt.ylabel("Altitude (deg)")
    plt.title(event_name + " Over Wānaka")
    plt.legend()
    plt.savefig(
        os.path.join(output_dir, f"{event_name}_traces_unoptimized_single.pdf"),
        format="pdf",
    )
    plt.clf()

    for i in range(len(coordinates)):
        plt.scatter(
            coordinates[i][0].az.deg, coordinates[i][0].alt.deg, s=0.5, c="black"
        )

    plt.xlabel("Azimuth (deg)")
    plt.ylabel("Altitude (deg)")
    plt.title(event_name + " " + ptime + " Over Wānaka")
    plt.savefig(
        os.path.join(output_dir, f"{event_name}_traces_unoptimized.pdf"), format="pdf"
    )


def plot_traces_optimized(event_name, coordinates, pointing_fov, azimuth_fov, config):
    """Plots trajectories after optimization

    Args:
        event_name (str): name of event
        coordinates (array): trajectories for each point
        pointing_fov (float): optimal fov pointing
        azimuth_fov (float): total azimuth fov defined in config
        config (ToOConfig): config file
    """
    output_dir = config.output.plots.directory / "GW_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    point_alt = -9.2
    halffov_alt = 3.2
    ptime = config.settings.calculation.start_time.to_string().split("T")[0]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(len(coordinates)):
        temp = coordinates[i]
        plt.scatter(temp[0].az.deg, temp[0].alt.deg, s=0.5, color="black")

    ax.fill_between(
        [pointing_fov - azimuth_fov / 2, pointing_fov + azimuth_fov / 2],
        point_alt - halffov_alt,
        point_alt + halffov_alt,
        alpha=0.25,
        color="r",
    )

    plt.title(event_name + " " + ptime + " Over Wānaka")
    plt.xlabel("Azimuth (Deg)")
    plt.ylabel("Altitude (Deg)")
    plt.savefig(
        os.path.join(output_dir, f"{event_name}_traces_optimized.pdf"), format="pdf"
    )


def plot_azimuth(event_name, pointing_fov, pointing_time, config):
    """Plots the weighted time over azimuth values with EUSO-SPB2 FOV
    centered around the optimal azimuth value

    Args:
        event_name (str): event name
        pointing_fov (float): optimal pointing fov
        pointing_time (Time): optimal pointing time
        config (ToOConfig): config file
    """
    output_dir = config.output.plots.directory / "GW_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ptime = config.settings.calculation.start_time.to_string().split("T")[0]
    mark = np.argmax(pointing_time)
    mark_min = np.argmin(pointing_time)

    box_width = 6.4  # Changeable parameter: Width of the box
    box_center = pointing_fov[mark]
    box_left = box_center - box_width / 2
    box_right = box_center + box_width / 2
    box_color = "grey"
    box_alpha = 0.5
    plt.clf()
    plt.plot(pointing_fov, pointing_time)
    plt.plot(
        [pointing_fov[mark], pointing_fov[mark]],
        [pointing_time[mark_min], pointing_time[mark]],
        linestyle="--",
        color="black",
        label="Optimal Pointing",
    )

    plt.axvspan(
        box_left, box_right, color=box_color, alpha=box_alpha, label="EUSO-SPB2 FOV"
    )

    plt.title(event_name + " " + ptime + " Over Wānaka")
    plt.xlabel("Pointing FOV in Azimuth")
    plt.ylabel("Weighted Time (P*dt)")
    plt.ylim(0, pointing_time[mark])
    plt.savefig(
        os.path.join(output_dir, f"{event_name}_paper_figure.pdf"), format="pdf"
    )

    plt.clf()
    plt.plot(pointing_fov, pointing_time)
    # plt.plot([pointing_fov[mark],pointing_fov[mark]], [pointing_time[mark_min],pointing_time[mark]], linestyle = '--', color = 'black')
    plt.plot(
        [pointing_fov[mark], pointing_fov[mark]],
        [pointing_time[mark_min], pointing_time[mark]],
        linestyle="--",
        color="black",
        label="Optimal Pointing",
    )

    plt.axvspan(
        box_left, box_right, color=box_color, alpha=box_alpha, label="EUSO-SPB2 FOV"
    )

    plt.title(event_name + " " + ptime + " Over Wānaka")
    plt.xlabel("Pointing FOV in Azimuth")
    plt.ylabel("Weighted Time (P*dt)")
    plt.xlim(box_left - 25, box_right + 25)
    plt.ylim(0, pointing_time[mark])
    plt.savefig(
        os.path.join(output_dir, f"{event_name}_paper_figure_zoomed.pdf"), format="pdf"
    )
