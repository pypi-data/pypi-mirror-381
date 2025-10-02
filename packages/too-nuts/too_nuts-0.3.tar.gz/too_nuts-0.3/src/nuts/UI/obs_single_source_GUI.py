"""Module to define observability conditions for a single source from GUI.

.. autosummary::

   obs_single

"""

import pandas as pd
import streamlit as st

from nuts.apps.single import build_single


def obs_single():
    """Compute the observability conditions for a single source from GUI."""
    st.write(
        "In this tab, you can compute the observability conditions for a single source. Enter below the name of the configuration file and the properties of the source, and click the button 'Run Single Target Scheduler'."
    )
    st.warning(
        "If you want to schedule a single source on top of an existing database, use the other tabs 1/ to add the source to the database and 2/ to compute the observability and scheduling for the full database.",
        icon="⚠️",
    )

    config_name = st.text_input(
        "Input single source configuration file name (include .toml)", "config.toml"
    )

    st.write("Source Parameters (* required fields):")
    event_ra = st.text_input("Right Ascension (deg)*", "0.0", key="event_ra_source")
    event_dec = st.text_input("Declination (deg)*", "0.0", key="event_deg_source")
    detection_time = st.text_input(
        "Detection Time*", "2025-01-01T00:00:00", key="det_time_source"
    )
    event_id = st.text_input("Event id*", "None", key="event_id_source")
    event_type = st.text_input("Event type*", "None", key="event_type_source")
    publisher = st.text_input("Publisher*", "SourcePublisher", key="pub_source")
    publisher_id = st.text_input(
        "Publisher id*", "SourcePublisher1", key="pub_id_source"
    )
    priority = st.text_input("Priority*", "1", key="priority_source")
    redshift = st.text_input("Redshift", "0.0", key="z_source")
    distance = st.text_input("Distance", "0.0", key="dL_source")

    if st.button("Run Single Target Scheduler"):
        results = build_single(
            config_name,
            event_ra,
            event_dec,
            detection_time,
            event_id,
            event_type,
            publisher,
            publisher_id,
            priority,
            redshift,
            distance,
        )

        st.write("Single source properties:")
        st.write(results["observability_0"][0].event)
        st.write("Single source observability:")
        key = list(results["observability_0"][0].tsprpst.keys())
        df = pd.DataFrame(results["observability_0"][0].tsprpst[key[0]])
        df.columns = ["Time (UTC)", "Altitude (deg)", "Azimuth (deg)"]
        st.dataframe(df)
