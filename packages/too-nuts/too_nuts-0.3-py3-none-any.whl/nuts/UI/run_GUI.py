"""Module to use NuTS run options from GUI.

.. autosummary::

   display_observation_window
   display_observables
   display_scheduled
   make_run

"""

from pathlib import Path

import pandas as pd
import streamlit as st
import toml

from nuts.apps.run import build_run


def display_observation_window(run_config_name: Path) -> None:
    """Display the observation window.

    Args:
        run_config_name (Path): Path to the run config file.
    """

    option = "obs_window"
    output = build_run(run_config_name, option)
    output = output["obs-window_0"]
    start_times = output[0]
    end_times = output[1]

    time_frame = pd.DataFrame(
        {"Observation Start": start_times, "Observation End": end_times}
    )
    st.write("Observation windows:")
    st.write(time_frame)


def display_observables(output: dict) -> None:
    """Display the observables.

    Args:
        run_config_name (Path): Path to the run config file.
    """
    if len(output["observability_0"][1]) == 0:
        st.write("No observables found.")
        return

    for ob in output["observability_0"][1]:
        st.write(ob.event.event_type, ob.event.publisher, ob.event.publisher_id)
        st.write("Start Observation Time, End Observation Time")
        for time_index, time in enumerate(ob.observations):
            if time.start_time is None:
                continue
            else:

                st.write(time_index + 1, time.start_time, time.end_time)
        st.write("Start Azimuth, End Azimuth, Start Altitude, End Altitude")
        for loc_index, loc in enumerate(ob.observations):
            if loc.start_loc is None:
                continue
            else:
                st.write(
                    loc_index + 1,
                    loc.start_loc.az.deg,
                    loc.end_loc.az.deg,
                    loc.start_loc.alt.deg,
                    loc.end_loc.alt.deg,
                )

        st.write("_______________________________________________________________")

    st.write("Observables calculated.")


def display_scheduled(output: dict) -> None:
    """Display scheduled sources.

    Args:
        output (dict): scheduled sources and properties.
    """
    for i in range(len(output["event"])):
        ev = output["event"][i]
        st.subheader(
            "Event type: " + ev["event_type"] + ", Event id: " + ev["event_id"],
            divider=True,
        )
        st.write("Publisher: " + ev["publisher"])
        st.write("Publisher id: " + ev["publisher_id"])
        st.write("Priority: " + str(ev["priority"]))
        ob = output["observations"][i]["1"]
        st.write("Move time: " + ob["move_time"])
        st.write("Start time: " + ob["start_time"])
        st.write("End time: " + ob["end_time"])
        st.write(
            "Pointing detector: altitude "
            + ob["pointing_dir"]["ALT"][0:6]
            + " deg, azimuth "
            + ob["pointing_dir"]["AZ"][0:6]
            + " deg"
        )


def make_run():
    st.write(
        "In this tab, you can run NuTS with different options. Enter the name of the configuration file, select a run option, and click the button 'Run NuTS.'"
    )
    run_config_name = st.text_input("Input run config file name (include .toml)", "")

    run_option = st.selectbox(
        "Select a run option",
        [
            "Display observation window",
            "Prepare database",
            "Calculate observable sources",
            "Schedule observable sources",
            "Calculate observables which cross FoV",
        ],
    )

    if st.button("Run NuTS"):

        if run_option == "Display observation window":
            display_observation_window(run_config_name)

        if run_option == "Prepare database":
            option = "prep_db"
            st.write("Preparing database ...")
            build_run(run_config_name, option)
            st.write("Database prepared.")

        if run_option == "Calculate observable sources":
            option = "observability"
            st.write("Calculating observables ...")
            output = build_run(run_config_name, option)
            display_observables(output)

        if run_option == "Schedule observable sources":
            option = "obs_sched"
            st.write("Calculating schedule ...")
            build_run(run_config_name, option)
            st.write("Schedule calculated.")
            toml_data = toml.load(run_config_name)
            scheduled_file = (
                toml_data["output"]["global_path"]
                + "/"
                + toml_data["output"]["directory"]
                + "/"
                + toml_data["output"]["observations"]["directory"]
                + "/"
                + toml_data["output"]["observations"]["scheduled_file"]
            )
            sched = pd.read_json(scheduled_file)
            display_scheduled(sched)
        #            st.dataframe(output.schedule, use_container_width=True)

        if run_option == "Calculate observables which cross FoV":
            option = "pointing_obs"
            st.write("Calculating observables which cross FoV ...")
            output = build_run(run_config_name, option)
            display_observables(output)
