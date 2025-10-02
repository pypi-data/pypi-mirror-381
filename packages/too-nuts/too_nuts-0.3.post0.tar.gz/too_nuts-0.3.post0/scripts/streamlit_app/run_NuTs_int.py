import base64
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
import toml

from nuts.apps.listen import build_listen
from nuts.apps.make_config import build_config
from nuts.apps.run import build_run


# Function to load markdown files
def load_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


# Function to load a TOML file
def load_toml_file(file_path):
    return toml.load(file_path)


# Function to save changes to a TOML file
def save_toml_file(file_path, data):
    with open(file_path, "w") as file:
        toml.dump(data, file)


def display_toml_editor(toml_data, parent_key=""):
    """Display input widgets based on the TOML file's structure for editing."""
    for key, value in toml_data.items():
        full_key = (
            f"{parent_key}.{key}" if parent_key else key
        )  # Create a full key for nested structure
        if isinstance(value, str):
            toml_data[key] = st.text_input(full_key, value)
        elif isinstance(value, int):
            toml_data[key] = st.number_input(full_key, value)
        elif isinstance(value, float):
            toml_data[key] = st.number_input(full_key, value)
        elif isinstance(value, bool):
            toml_data[key] = st.checkbox(full_key, value)
        elif isinstance(value, list):
            toml_data[key] = st.multiselect(key, options=value, default=value)
        elif isinstance(value, dict):
            st.subheader(full_key)  # Create a subsection for nested dictionaries
            display_toml_editor(value, full_key)  # Recursively display the dictionary
        else:
            st.warning(f"Unsupported type for key {full_key}: {type(value)}")


def run_nuts():

    # App title
    st.title("Neutrino Target Scheduler")
    image_path = "./too_method.png"
    st.image(image_path, use_column_width=True)

    st.write("Welcome to the Neutrino Target Scheduler.")
    st.write("For more information on NuTS, see [Cite Paper].")
    st.write(
        "Link to Gitlab: https://gitlab.com/jem-euso/euso-spb2/too/too-scource-parser.git"
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Getting Started",
            "Generate Config File",
            "Edit Config File",
            "Listener",
            "Observables and Scheduler",
        ]
    )

    with tab1:
        md_file_path = "../../README.md"
        md_content = load_markdown_file(md_file_path)
        st.markdown(md_content)

    with tab2:
        config_name = st.text_input("Input configuration file name (include .toml)", "")
        if st.button("Make config"):
            build_config(config_name)

    with tab3:
        config_name = st.text_input(
            "Input current configuration file name (include .toml)", ""
        )

        if st.button("Edit config file"):
            toml_data = load_toml_file(config_name)
            st.session_state.edit_mode = True  # Set the edit mode to true

            if "edit_mode" in st.session_state and st.session_state.edit_mode:
                display_toml_editor(toml_data)  # Display the editable fields

                # # Button to save changes
                # if st.button("Save Changes"):
                #     save_toml_file(config_name, toml_data)
                #     st.success("TOML file updated successfully!")
                #     st.session_state.edit_mode = False

            # if st.button("Advanced Options"):
            #     st.write(
            #         "To develop a custom run sequence mark the modules included in the sequence:"
            #     )

            #     module_1 = st.checkbox("Module 1", "")
            #     module_2 = st.checkbox("Module 2", "")

    with tab4:
        # Buttons

        listen_config_name = st.text_input("Input config file name (include .toml)", "")

        listen_option = st.selectbox("Select an alert provider", ["TNS", "GCN"])

        if st.button("Listen"):

            build_listen(listen_config_name, listen_option)

    with tab5:

        run_config_name = st.text_input(
            "Input run config file name (include .toml)", ""
        )

        run_option = st.selectbox(
            "Select a run option",
            [
                "Run all",
                "Prepare database",
                "Display observation window",
                "Calculate observables",
                "Schedule observables",
                "Calculate observables which cross FoV",
            ],
        )

        if st.button("Run NuTS"):

            if run_option == "Display observation window":
                option = "obs_window"
                output = build_run(run_config_name, option)

                start_times = output[0][0]
                end_times = output[0][1]

                time_frame = pd.DataFrame(
                    {"Observation Start": start_times, "Observation End": end_times}
                )
                st.write(time_frame)


if __name__ == "__main__":
    run_nuts()
