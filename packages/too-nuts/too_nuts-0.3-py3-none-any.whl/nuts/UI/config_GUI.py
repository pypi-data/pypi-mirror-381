"""Module for creating and modifying a config file from GUI.

.. autosummary::

   edit_toml
   create_config
   modify_config

"""

from pathlib import Path

import streamlit as st
import toml

from nuts.apps.init import build_init
from nuts.apps.make_config import build_config


def edit_toml(config, parent_key=""):
    """
    Recursively render and edit a TOML config file in the Streamlit app.
    """
    updated_config = {}
    for key, value in config.items():
        full_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            st.subheader(f"Section: {full_key}")
            updated_config[key] = edit_toml(value, parent_key=full_key)
        elif isinstance(value, list):
            st.write(f"List Field: {full_key}")
            updated_list = []
            for i, item in enumerate(value):
                with st.container():
                    updated_list.append(
                        st.text_input(
                            f"{full_key}[{i}]", value=item, key=full_key + str(i)
                        )
                    )
            updated_config[key] = updated_list
        elif isinstance(value, bool):
            updated_config[key] = st.checkbox(full_key, value=value, key=full_key)
        elif isinstance(value, (int, float)):
            updated_config[key] = st.number_input(
                full_key,
                value=value,
                key=full_key,
                format="%.2f" if isinstance(value, float) else None,
            )
        else:
            updated_config[key] = st.text_input(
                full_key, value=str(value), key=full_key
            )
    return updated_config


def create_config():
    st.write(
        "In this tab, you can create a new configuration file, using the default configuration parameters. Enter the file name below and click the button 'Make config'. Use the next tab to modify these parameters."
    )
    config_name = st.text_input("Input configuration file name (include .toml)", "")
    init_path = Path(
        st.text_input("Input path to initialize database (default: './')", "./")
    )
    if st.button("Make config"):
        if not init_path.exists():
            build_init(path=init_path)
        build_config(config_name, init_path)


def modify_config():
    st.write(
        "In this tab, you can modify an existing configuration file. Enter the file name below and click enter. The configuration parameters will appear below. Change the desired parameters and click the button 'Save changes'."
    )

    st.warning(
        "Some parameters are not created by default in the configuration file. Specifically, figure names are not initialized (and thus figures are not created). To modify these parameters, open the .toml configuration file and add them in the file. The default figure names are the following:"
        + "\n\n[output.plots.detector]"
        + '\n\ndetector_location_mollweide = "Detector_location_mollweide"'
        + '\n\ndetector_location_hammer = "Detector_map_hammer"'
        + '\n\ndetector_location_aeqd = "Detector_map_aeqd"'
        + "\n\n[output.plots.source_skymaps]"
        + '\n\nskymap_none = "Sky_observable"'
        + '\n\nskymap_all = "Sources_all"'
        + '\n\nskymap_obs = "Sources_observable"'
        + '\n\nskymap_sched = "Sources_scheduled"'
        + '\n\nskymap_comp = "Sources_comp"'
        + "\n\n[output.plots.source_trajectories]"
        + '\n\nsource_trajectories_full_sky = "Traj_all"'
        + '\n\nsource_trajectories_zoom = "Traj_fov"'
        + '\n\nsource_trajectories_comp_full_sky = "Traj_Scheduled_all"'
        + '\n\nsource_trajectories_comp_zoom = "Traj_Scheduled_fov" ',
        icon="⚠️",
    )

    config_name = st.text_input(
        "Input current configuration file name (include .toml)", ""
    )
    if config_name != "":
        toml_data = toml.load(config_name)
        # Set the edit mode to true
        st.session_state.edit_mode = True
        # Display the editable fields
        toml_data = edit_toml(toml_data)

        if st.button("Save changes"):
            with open(config_name, "w") as file:
                toml.dump(toml_data, file)
            st.write("Changes saved successfully!")
