"""Module for GUI.

.. autosummary::

   GUI

"""

import base64
import glob
from pathlib import Path

import streamlit as st

from nuts.UI.add_source_GUI import add_source
from nuts.UI.config_GUI import create_config, modify_config
from nuts.UI.getting_started_GUI import getting_started
from nuts.UI.listen_GUI import listen_gui
from nuts.UI.obs_single_source_GUI import obs_single
from nuts.UI.run_GUI import make_run
from nuts.UI.visuals_GUI import make_visuals


def GUI():
    UI_path = Path(__file__).resolve().parent
    NuTS_path = UI_path.parent.parent.parent

    # App title
    st.title("Neutrino Target Scheduler")
    image_path = UI_path / "too_method.png"
    st.image(str(image_path))

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        [
            "Getting Started",
            "Generate Config File",
            "Edit Config File",
            "Listener",
            "Add Source to Database",
            "Observability and Scheduling - Database",
            "Observability - Single Source",
            "Visuals",
        ]
    )

    with tab1:
        getting_started(UI_path, NuTS_path)

    with tab2:
        create_config()

    with tab3:
        modify_config()

    with tab4:
        listen_gui()

    with tab5:
        add_source(UI_path)

    with tab6:
        make_run()

    with tab7:
        obs_single()

    with tab8:
        make_visuals()


if __name__ == "__main__":
    GUI()
