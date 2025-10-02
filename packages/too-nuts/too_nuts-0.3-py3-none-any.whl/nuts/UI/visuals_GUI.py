"""Module to display visuals created by NuTS.

.. autosummary::

   try_visuals
   make_visuals

"""

import glob

import numpy as np
import streamlit as st
import toml
from streamlit_pdf_viewer import pdf_viewer

from nuts.apps.run import build_run


def try_visuals(name_tab, desc_tab, path, toml_in, name_in, name_add, desc_in):
    """Determine if visual is defined in config file, thus created bu NuTS."""
    path_loc = path + "/" + toml_in["directory"] + "/"
    try:
        name_tab.append(path_loc + toml_in[name_in] + name_add)
        desc_tab.append(desc_in)
    except KeyError:
        st.warning(
            "In configuration file, keyword '" + name_in + "' does not exist.",
            icon="⚠️",
        )
    return name_tab, desc_tab


def make_visuals():
    """Create and print visuals produced by NuTS."""
    st.write(
        "In this tab, you can produce and visualize all the figures produced while running NuTS. Enter below the name of the configuration file and click the buttons 'Run visuals' and/or 'Show visuals'."
    )
    config_name_vis = st.text_input(
        "Input single source configuration file name (include .toml)", ""
    )

    if st.button("Run visuals"):
        build_run(config_name_vis, "visuals")

    if st.button("Show visuals"):
        toml_data = toml.load(config_name_vis)
        tomlout = toml_data["output"]
        path = (
            tomlout["global_path"]
            + "/"
            + tomlout["directory"]
            + "/"
            + tomlout["plots"]["directory"]
        )

        # Detector related figures
        st.header("Detector", divider=True)
        st.write(
            "Different views of the detector trajectory during observation window."
        )
        toml_detector = toml_data["output"]["plots"]["detector"]
        list_figures = glob.glob(
            path + "/" + toml_detector["directory"] + "/" + "*.pdf"
        )
        name_list = np.array(
            [
                ["detector_location_mollweide", "_0.pdf"],
                ["detector_location_hammer", "_0.pdf"],
                ["detector_location_aeqd", "_0.pdf"],
            ]
        )
        desc_list = [
            "Detector location during observation window. Mollweide projection.",
            "Detector location during observation window. Hammer projection.",
            "Detector location during observation window. aeqd projection.",
        ]
        name_tab = []
        desc_tab = []
        for i in range(len(name_list)):
            name_tab, desc_tab = try_visuals(
                name_tab,
                desc_tab,
                path,
                toml_detector,
                name_list[i, 0],
                name_list[i, 1],
                desc_list[i],
            )
        for i in range(len(name_tab)):
            if name_tab[i] in list_figures:
                st.write(name_tab[i])
                st.write(desc_tab[i])
                pdf_viewer(name_tab[i])

        # Skymap figures
        st.header("Sky maps", divider=True)
        st.write(
            "For all skymaps below, the colormap shows the geometrical exposure, normalized by its maximum value, in logarithmic scale between 0.1 and 1."
        )
        toml_skymap = toml_data["output"]["plots"]["source_skymaps"]
        list_figures = glob.glob(path + "/" + toml_skymap["directory"] + "/" + "*.pdf")
        name_list = np.array(
            [
                ["skymap_none", "_fov_Equatorial_0.pdf"],
                ["skymap_none", "_fov_Galactic_0.pdf"],
                ["skymap_none", "_sun_Equatorial_0.pdf"],
                ["skymap_none", "_sun_Galactic_0.pdf"],
                ["skymap_none", "_sun_moon_Equatorial_0.pdf"],
                ["skymap_none", "_sun_moon_Galactic_0.pdf"],
                ["skymap_all", "_Equatorial_0.pdf"],
                ["skymap_all", "_Galactic_0.pdf"],
                ["skymap_obs", "_Equatorial_0.pdf"],
                ["skymap_obs", "_Galactic_0.pdf"],
                ["skymap_sched", "_Equatorial_0.pdf"],
                ["skymap_sched", "_Galactic_0.pdf"],
                ["skymap_comp", "_Equatorial_0.pdf"],
                ["skymap_comp", "_Galactic_0.pdf"],
            ]
        )
        desc_list = [
            "Observable portion of the sky during one day, with field of view constraints. Equatorial coordinates.",
            "Observable portion of the sky during one day, with field of view constraints. Galactic coordinates.",
            "Observable portion of the sky during one day, with field of view and Sun constraints. Equatorial coordinates.",
            "Observable portion of the sky during one day, with field of view and Sun constraints. Galactic coordinates.",
            "Observable portion of the sky during one day, with field of view, Sun and Moon constraints. Equatorial coordinates.",
            "Observable portion of the sky during one day, with field of view, Sun and Moon constraints. Galactic coordinates.",
            "Observable portion of the sky, with all sources from database (red stars). Equatorial coordinates.",
            "Observable portion of the sky, with all sources from database (red stars). Galactic coordinates.",
            "Observable portion of the sky, with observable sources(red stars). Equatorial coordinates.",
            "Observable portion of the sky, with observable sources(red stars). Galactic coordinates.",
            "Observable portion of the sky, with scheduled sources(red stars). Equatorial coordinates.",
            "Observable portion of the sky, with scheduled sources (red stars). Galactic coordinates.",
            "Observable portion of the sky, with observable sources (white stars) and scheduled sources (colored stars). Equatorial coordinates.",
            "Observable portion of the sky, with observable sources (white stars) and scheduled sources (colored stars). Galactic coordinates.",
        ]
        name_tab = []
        desc_tab = []
        for i in range(len(name_list)):
            name_tab, desc_tab = try_visuals(
                name_tab,
                desc_tab,
                path,
                toml_skymap,
                name_list[i, 0],
                name_list[i, 1],
                desc_list[i],
            )
        for i in range(len(name_tab)):
            if name_tab[i] in list_figures:
                st.write(name_tab[i])
                st.write(desc_tab[i])
                pdf_viewer(name_tab[i])

        # Source trajectories
        st.header("Source trajectories", divider=True)
        st.write("Source trajectories in the detector frame are showed.")

        toml_traj = toml_data["output"]["plots"]["source_trajectories"]
        list_figures = glob.glob(path + "/" + toml_traj["directory"] + "/" + "*.pdf")
        name_list = [
            "source_trajectories_full_sky",
            "source_trajectories_zoom",
            "source_trajectories_comp_full_sky",
            "source_trajectories_comp_zoom",
        ]
        desc_list = [
            "Source trajectory in the detector's frame.",
            "Source trajectory in the detector's frame. Zoomed view.",
            "Scheduled source trajectory in the detector's frame.",
            "Scheduled source trajectory in the detector's frame. Zoomed view.",
        ]
        name_tab = []
        desc_tab = []
        for i in range(len(name_list)):
            name_tab, desc_tab = try_visuals(
                name_tab, desc_tab, path, toml_traj, name_list[i], "", desc_list[i]
            )
        for i in range(len(name_tab)):
            st.subheader(desc_tab[i], divider=True)
            list_figures = glob.glob(name_tab[i] + "*.pdf")
            for nfig in list_figures:
                st.write(nfig)
                pdf_viewer(nfig)
