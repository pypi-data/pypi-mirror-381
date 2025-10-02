import logging

import astropy.coordinates
import astropy.time
import astropy.units as u
import pandas as pd

from .. import too_event as too
from ..config.config import ToOConfig
from ..IO_funcs.too_database import DataBaseIO


def key_formatter(input_key: str) -> str:
    """Function to reformat input strings to only allow characters available to save in
    an sql database

    Args:
        input_key (str): string to be formatted

    Returns:
        str: formatted string
    """
    if "/" in input_key:
        input_key = input_key.replace("/", "_")
    if " " in input_key:
        input_key = input_key.replace(" ", "_")
    if "-" in input_key:
        input_key = input_key.replace("-", "_")
    if "." in input_key:
        input_key = input_key.replace(".", "")
    return input_key.lower()


def read_TNS_table(tns_file_path: str, publisher: str = "TNS") -> list[too.ToOEvent]:
    """Function to read a csv in the form provided by TNS

    Args:
        tns_file_path (str): path to the TNS csv file
        publisher (str, optional): Publisher in case you have a different csv in the same format. Defaults to "TNS".

    Returns:
        list[too.ToOEvent]: Parsed ToO events
    """
    data = pd.read_csv(tns_file_path)
    tns_events = []

    constant_params = ["ID", "Obj. Type", "Name", "Discovery Date (UT)", "RA", "DEC"]
    for index in range(len(data["ID"])):
        event = too.ToOEvent()
        event.publisher = publisher
        event.publisher_id = data["ID"][index]
        if not pd.isnull(data["Obj. Type"][index]):
            event.event_type = data["Obj. Type"][index]
        event.event_id = data["Name"][index]
        event.set_time(data["Discovery Date (UT)"][index], format="iso")
        event.set_coordinates(
            astropy.coordinates.Angle(data["RA"][index], unit=u.hourangle).deg,
            astropy.coordinates.Angle(data["DEC"][index], unit=u.deg).deg,
        )

        param_dict = {}
        for param in data.columns:
            if param not in constant_params:
                save_key = key_formatter(param)
                if not pd.isnull(data[param][index]):
                    param_dict[save_key] = data[param][index]

        event.params = param_dict
        logging.debug(f"New alert parsed: {event}")
        tns_events.append(event)
    return tns_events


def save_list(config: ToOConfig, tns_alerts: list[too.ToOEvent]) -> None:
    """Function to save the list of TNS events to a database

    Args:
        config (ToOConfig): config file that contains information about the config file
        tns_alerts (list[too.ToOEvent]): list of parsed TNS alerts
    """

    if len(tns_alerts) == 0:
        logging.info("No new events found!")
        return

    spb2_database = DataBaseIO(config.files.listener.tns_file)
    logging.info("Start writing TNS to database")
    for event in tns_alerts:
        spb2_database.add_event(event)

        logging.debug(f"Alert added to TNS database: {event.publisher_id}")

    spb2_database.write()
    logging.info("Writing TNS to database complete")
