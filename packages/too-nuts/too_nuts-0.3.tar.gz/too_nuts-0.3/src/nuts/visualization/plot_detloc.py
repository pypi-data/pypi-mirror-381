""" Functions for visualizations.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: fig_detector_position
   :noindex:

.. autofunction:: fig_observation_conditions
   :noindex:

"""

import logging

import astropy.coordinates as acoord
import astropy.units as u
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from ..config.config import ToOConfig
from ..observation_period.sun_moon_cuts import moon_illumination

plt.rc("text", usetex=False)
plt.rc("font", family="serif")


def fig_detector_position(config: ToOConfig, detector_frames: acoord.AltAz):
    """Visualize ballon trajectory.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2024-03-31

    Args:
        config (dict): config file
        detector_frames (AltAz): detector location properties

    """
    plot_directory = config.output.plots.detector.directory
    plot_directory.mkdir(parents=True, exist_ok=True)

    plot_name = config.output.plots.detector.detector_location_mollweide
    if plot_name is not None:
        logging.info("***************************************************")
        logging.info("Visualize detector... ")
        extension = config.output.plots.detector.plot_format
        plot_name = f"{plot_name}_{config._runtime.iteration}.{extension}"
        if "times" not in locals():
            times = config._runtime.all_times
            detector = config._runtime.detector
            locations = detector.loc(times)
            start_index = np.argwhere(
                times == config._runtime.observation_starts
            ).item()
            end_index = np.argwhere(times == config._runtime.observation_ends).item()
            lon_map = locations.lon.to(u.deg)[start_index:end_index]
            lat_map = locations.lat.to(u.deg)[start_index:end_index]
            cm_map = cm.rainbow(np.linspace(0, 1, end_index - start_index))

        fig = plt.figure()
        ax = fig.add_subplot(projection="mollweide")

        ax.scatter(
            locations.lon.to(u.rad),
            locations.lat.to(u.rad),
            ls="-",
            color="k",
        )
        ax.scatter(
            lon_map.to(u.rad),
            lat_map.to(u.rad),
            ls="-",
            color=cm_map,
        )
        ax.scatter(
            lon_map.to(u.rad)[0],
            lat_map.to(u.rad)[0],
            marker="*",
            color=cm_map[0],
            label="Start",
            s=100,
        )
        ax.scatter(
            lon_map.to(u.rad)[-1],
            lat_map.to(u.rad)[-1],
            marker="x",
            color=cm_map[-1],
            label="End",
            s=100,
        )
        ax.legend()
        ax.set_xlabel("Detector longitude (deg)", fontsize=16)
        ax.set_ylabel("Detector latitude (deg)", fontsize=16)
        ax.grid(True)
        fig.savefig(plot_name)
        plt.close(fig)

    plot_name = config.output.plots.detector.detector_location_hammer
    if plot_name is not None:
        logging.info("***************************************************")
        logging.info("Visualize detector... ")
        extension = config.output.plots.detector.plot_format
        plot_name = f"{plot_name}_{config._runtime.iteration}.{extension}"
        if "times" not in locals():
            times = config._runtime.all_times
            detector = config._runtime.detector
            locations = detector.loc(times)
            start_index = np.argwhere(
                times == config._runtime.observation_starts
            ).item()
            end_index = np.argwhere(times == config._runtime.observation_ends).item()
            lon_map = locations.lon.to(u.deg)[start_index:end_index]
            lat_map = locations.lat.to(u.deg)[start_index:end_index]
            cm_map = cm.rainbow(np.linspace(0, 1, end_index - start_index))

        # Create figure
        fig = plt.figure(figsize=(14, 8))
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

        # Use Hammer projection
        ax = plt.axes(projection=ccrs.Hammer())
        ax.set_global()

        # Add map features
        ax.coastlines(linewidth=0.25)
        ax.add_feature(cfeature.BORDERS.with_scale("110m"), linewidth=0.25)
        ax.add_feature(cfeature.LAND, facecolor="grey")
        ax.add_feature(cfeature.OCEAN, facecolor="white")  # for lake_color equivalent

        # Add meridians and parallels
        gl = ax.gridlines(
            draw_labels=False, linewidth=0.5, color="gray", linestyle="--"
        )
        gl.xlocator = plt.MultipleLocator(30)
        gl.ylocator = plt.MultipleLocator(30)

        # Plot location points
        ax.scatter(
            locations.lon.to(u.deg),
            locations.lat.to(u.deg),
            transform=ccrs.PlateCarree(),
            s=10,
            color="k",
            marker="o",
        )

        # Plot path points
        sc = ax.scatter(
            lon_map,
            lat_map,
            transform=ccrs.PlateCarree(),
            s=10,
            c=cm_map,
        )

        # Annotate start
        start_lon, start_lat = lon_map[0], lat_map[0]
        ax.annotate(
            str(times[start_index])[:16] + " UTC",
            xy=(start_lon.to(u.deg).value, start_lat.to(u.deg).value),
            xytext=(
                start_lon.to(u.deg).value,
                (lat_map[0].to(u.deg) - 10 * u.deg).value,
            ),
            textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
            arrowprops=dict(facecolor="black", arrowstyle="->"),
            fontsize=16,
            ha="center",
            va="top",
            transform=ccrs.PlateCarree(),
        )

        # Annotate end
        end_lon, end_lat = lon_map[-1], lat_map[-1]
        ax.annotate(
            str(times[end_index])[:16] + " UTC",
            xy=(end_lon.to(u.deg).value, end_lat.to(u.deg).value),
            xytext=(
                end_lon.to(u.deg).value,
                (lat_map[-1].to(u.deg) + 20 * u.deg).value,
            ),
            textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
            arrowprops=dict(facecolor="black", arrowstyle="->"),
            fontsize=16,
            ha="center",
            va="top",
            transform=ccrs.PlateCarree(),
        )

        # Save plot
        plt.savefig(plot_name, bbox_inches="tight")
        plt.close(fig)

    plot_name = config.output.plots.detector.detector_location_aeqd
    if plot_name is not None:
        logging.info("***************************************************")
        logging.info("Visualize detector... ")
        extension = config.output.plots.detector.plot_format
        plot_name = f"{plot_name}_{config._runtime.iteration}.{extension}"
        if "times" not in locals():
            times = config._runtime.all_times
            detector = config._runtime.detector
            locations = detector.loc(times)
            start_index = np.argwhere(
                times == config._runtime.observation_starts
            ).item()
            end_index = np.argwhere(times == config._runtime.observation_ends).item()
            lon_map = locations.lon.to(u.deg)[start_index:end_index]
            lat_map = locations.lat.to(u.deg)[start_index:end_index]
            cm_map = cm.rainbow(np.linspace(0, 1, end_index - start_index))

        # Create Cartopy figure
        fig = plt.figure(figsize=(8, 8))
        ax = plt.axes(
            projection=ccrs.AzimuthalEquidistant(
                central_longitude=0, central_latitude=-90
            )
        )
        ax.set_global()

        # Add map features
        ax.coastlines(linewidth=0.25)
        ax.add_feature(cfeature.BORDERS, linewidth=0.25)
        ax.add_feature(cfeature.LAND, facecolor="grey")
        ax.add_feature(cfeature.LAKES, facecolor="white")
        ax.gridlines(draw_labels=False, linewidth=0.5)

        # Plot locations
        ax.scatter(
            locations.lon.to_value(u.deg),
            locations.lat.to_value(u.deg),
            s=10,
            color="k",
            transform=ccrs.PlateCarree(),
            zorder=5,
        )

        # Plot track
        ax.scatter(
            lon_map.to_value(u.deg),
            lat_map.to_value(u.deg),
            s=10,
            c=cm_map,
            transform=ccrs.PlateCarree(),
            zorder=5,
        )

        # Annotate start
        start_lon, start_lat = lon_map[0], lat_map[0]
        ax.annotate(
            str(times[start_index])[:16] + " UTC",
            xy=(start_lon.to_value(u.deg), start_lat.to_value(u.deg)),
            xytext=(
                start_lon.to_value(u.deg),
                (start_lat - 20 * u.deg).to_value(u.deg),
            ),
            textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
            arrowprops=dict(facecolor="black", arrowstyle="->"),
            fontsize=16,
            ha="center",
            va="top",
            transform=ccrs.PlateCarree(),
        )

        # Annotate end
        end_lon, end_lat = lon_map[-1], lat_map[-1]
        ax.annotate(
            str(times[end_index])[:16] + " UTC",
            xy=(end_lon.to_value(u.deg), end_lat.to_value(u.deg)),
            xytext=(end_lon.to_value(u.deg), (end_lat + 10 * u.deg).to_value(u.deg)),
            textcoords=ccrs.PlateCarree()._as_mpl_transform(ax),
            arrowprops=dict(facecolor="black", arrowstyle="->"),
            fontsize=16,
            ha="center",
            va="top",
            transform=ccrs.PlateCarree(),
        )

        ax.set_extent([-180, 180, -90, -0], crs=ccrs.PlateCarree())
        # Save and close
        plt.savefig(plot_name, bbox_inches="tight")
        plt.close(fig)


def fig_observation_conditions(config: ToOConfig, detector_frames: acoord.AltAz):
    name_save = config.output.plots.directory / "trajectories" / "observation"
    name_save.mkdir(parents=True, exist_ok=True)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    fig.subplots_adjust(right=0.75)
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax3.spines.right.set_position(("axes", 1.2))

    alpha = 0.4
    alts = detector_frames.location.height.to(u.km).value

    ax.set_xlabel("Time", fontsize=16)
    ax.set_ylabel("Detector altitude (km)", fontsize=16)
    ax.plot(
        config._runtime.all_times.to_datetime(),
        alts,
        color="black",
        label="Detector altitude",
        linewidth=3,
    )

    ax.fill_between(
        x=config._runtime.all_times.to_datetime(),
        y1=np.max(alts)
        * config._runtime.sun_moon_fov_cuts.moon_cut(
            config._runtime.all_times, detector_frames
        ),
        color="C0",
        step="mid",
        label="Moon cut",
        alpha=alpha,
    )
    ax.fill_between(
        x=config._runtime.all_times.to_datetime(),
        y1=np.max(alts)
        * config._runtime.sun_moon_fov_cuts.sun_cut(
            config._runtime.all_times, detector_frames
        ),
        color="C1",
        step="mid",
        label="Sun cut",
        alpha=alpha,
    )
    ax.fill_between(
        x=config._runtime.all_times.to_datetime(),
        y1=np.max(alts)
        * config._runtime.sun_moon_fov_cuts.observable_conditions(
            detector_frames,
            config._runtime.all_times,
        ),
        color="C2",
        step="mid",
        label="Observation conditions",
        alpha=alpha,
    )
    ax3.plot(
        config._runtime.all_times.to_datetime(),
        moon_illumination(config._runtime.all_times),
        color="red",
        label="Moon illumination + cut",
    )
    ax3.axhline(
        config.settings.observation.moon_illumination_cut, color="red", linestyle="--"
    )
    ax3.set_ylim(0, 1)
    ax3.set_ylabel("Moon illumination", fontsize=16)

    sun_alt = (
        acoord.get_body("sun", config._runtime.all_times)
        .transform_to(detector_frames)
        .alt
    )
    moon_alt = (
        acoord.get_body("moon", config._runtime.all_times)
        .transform_to(detector_frames)
        .alt
    )
    angle_off = config._runtime.sun_moon_fov_cuts.offset_angle(detector_frames.location)
    ax2.plot(
        config._runtime.all_times.to_datetime(),
        sun_alt.to("deg").value,
        color="C1",
        marker="x",
        label="Sun elevation + cut",
    )
    ax2.plot(
        config._runtime.all_times.to_datetime(),
        (config.settings.observation.sun_altitude_cut - angle_off).to(u.deg).value,
        color="C1",
        linestyle="--",
    )
    ax2.set_ylabel("Elevation angle (deg)", fontsize=16)

    ax2.plot(
        config._runtime.all_times.to_datetime(),
        moon_alt.to("deg").value,
        color="C0",
        label="Moon elevation + cut",
        marker="x",
    )
    ax2.plot(
        config._runtime.all_times.to_datetime(),
        (config.settings.observation.moon_altitude_cut - angle_off).to(u.deg).value,
        color="C0",
        linestyle="--",
    )

    fig.legend(ncols=2)
    plt.savefig(
        name_save / f"Detector_lat_long_obs_window_{config._runtime.iteration}.pdf"
    )
    plt.close(fig)
