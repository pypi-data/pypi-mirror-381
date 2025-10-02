"""Module to define listener in GUI.

.. autosummary::

   listen_gui

"""

import streamlit as st

from nuts.apps.listen import build_listen


def listen_gui():
    st.write(
        "In this tab, you can run the GCN and TNS listeners to receive ToO alerts. Enter the configuration file name below, select an alert provider and click the button 'Listen'."
    )
    listen_config_name = st.text_input("Input config file name (include .toml)", "")
    listen_option = st.selectbox("Select an alert provider", ["TNS", "GCN"])
    if st.button("Listen"):
        build_listen(listen_config_name, listen_option)
