"""Module to add source to database.

.. autosummary::

   add_source

"""

import streamlit as st

from nuts.IO_funcs.too_database import DataBaseIO
from nuts.too_event import ToOEvent


def add_source(UI_path):
    st.write(
        "In this tab, you can add a source to an existing database. Enter below the source parameters, the name of the database, and click the button 'Save source parameters'."
    )
    st.write("Source and Database Parameters (* required fields):")
    event_ra = st.text_input("Right Ascension (deg)*", "0.0")
    event_dec = st.text_input("Declination (deg)*", "0.0")
    detection_time = st.text_input("Detection Time*", "2025-01-01T00:00:00")
    event_id = st.text_input("Event id*", "None")
    event_type = st.text_input("Event type*", "None")
    publisher = st.text_input("Publisher*", "ATels")
    publisher_id = st.text_input("Publisher id*", "ATels1")
    obsbool = st.checkbox("Observed", value=False)
    if obsbool is True:
        obstime = st.text_input("Observation Time", "2025-01-01T00:00:00")
    redshift = st.text_input("Redshift", "0.0")
    distance = st.text_input("Distance", "0.0")
    db_name = st.text_input("Database name (include .csv)*", "OtherTransients.csv")

    if st.button("Save source parameters"):
        event = ToOEvent()
        event.set_coordinates(float(event_ra), float(event_dec), units="deg")
        event.set_time(str(detection_time))
        event.event_id = event_id
        event.event_type = event_type
        event.publisher = publisher
        event.publisher_id = publisher_id
        event.params["observed"] = obsbool
        if obsbool is True:
            event.params["obstime"] = str(obstime)
        event.params["redshift"] = redshift
        event.params["distance"] = distance
        db_path = UI_path / "../Catalogs/Database" / db_name
        loc_db = DataBaseIO(db_path)
        loc_db.read()
        loc_db.add_event(event)
        loc_db.write()
        st.write("Source parameters saved in database.")
