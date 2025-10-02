"""Listening to GCN alerts."""

import datetime as dt
import logging
import os
from pathlib import Path

import pandas as pd
from gcn_kafka import Consumer

from ..config.config import ToOConfig
from ..too_event import ToOEvent
from .GCN_alerts_template import GCNTemplates


def read_alert_list(config: ToOConfig) -> pd.DataFrame:
    """Function to load a list of the alerts that we want to
    subscribe to

    Args:
        config (ToOConfig): config file

    Returns:
        pd.DataFrame: Resulting list of files
    """
    alert_list_file = config.files.general.gcn_file
    return pd.read_csv(alert_list_file)


def filter_interesting_alerts(alert_list: pd.DataFrame) -> pd.DataFrame:
    """Select the alerts that are labeled as interesting (True)

    Args:
        alert_list (pd.DataFrame): List of available alerts

    Returns:
        pd.DataFrame: Subset of interesting alerts
    """
    alerts = alert_list["Alert name"]
    logging.debug(f"List of all available alerts: {alert_list}")
    # Warning: "alert_list["Monitor"] is True" only returns one bool
    mask = alert_list["Monitor"] == True
    return alerts[mask].to_list()


def get_subscribed_alerts(config: ToOConfig) -> list[str]:
    """Select the interesting alerts and format them in a way that can be used
    by GCN

    Args:
        config (dict): config file

    Returns:
        list[str]: list of formated alerts
    """
    alert_list = read_alert_list(config)
    prefix = "gcn.classic.text."
    # Filter the alerts we want to listen to
    alert_list = filter_interesting_alerts(alert_list)
    alert_list = [prefix + alert for alert in alert_list]
    logging.info(f"Subscribe to the following alerts: {alert_list}")
    return alert_list


def save_alert(alert_message: str, alert_store_directory: Path) -> str:
    """Function to directly save the text of an alert to a file

    Args:
        alert_message (str): input alert
        alert_store_directory (str): path to where the alert is stored

    Returns:
        str: full path + filename to the alert
    """
    now = dt.datetime.now().isoformat("T", "seconds")
    filename = f"gcn_alert_text_{now}.txt"
    alert_path = alert_store_directory / Path(filename)
    with open(alert_path, "w+") as f:
        for i in range(len(alert_message)):
            f.write(str(alert_message[i]))
    return alert_path


def load_alert(filename: Path) -> list[str]:
    """Function to load an alert given a path to the alert

    Args:
        filename (str): path + filename to the alert

    Returns:
        list[str]: alert message
    """
    with open(filename) as f:
        lines = f.readlines()
    return lines


def alert_available(alert_message: str) -> bool:
    """Catch if message is an alert

    Args:
        alert_message (str): input alert message

    Returns:
        bool: if the message is an alert
    """
    if alert_message.startswith("Subscribed topic not available:"):
        return False
    return True


class GCN_listener:
    """Class to represent the GCN listener"""

    def __init__(self, config: ToOConfig) -> None:
        """Initialization of the listening script

        Args:
            config (ToOConfig): config file
        """

        # Get directories to save the raw alerts
        self.alert_directory = config.files.listener.gcn_alerts_dir
        self.unknown_alert_directory = config.files.listener.gcn_unknown_alerts_dir
        # Create GCN folders if they do not exist
        if not os.path.exists(config.files.listener.gcn_alerts_dir):
            os.makedirs(config.files.listener.gcn_alerts_dir)
        if not os.path.exists(config.files.listener.gcn_unknown_alerts_dir):
            os.makedirs(config.files.listener.gcn_unknown_alerts_dir)

        # Set up connection to subscribed alerts
        self.alert_list = get_subscribed_alerts(config)
        self.consumer = Consumer(
            client_id=config.settings.gcn.client_id,
            client_secret=config.settings.gcn.client_secret_name,
        )
        self.consumer.subscribe(self.alert_list)
        self.alert_counter = 0

    def __call__(self) -> str:
        """Save and incoming alerts to file

        Returns:
            str: Path to raw alert file if not state message otherwise None
        """

        for message in self.consumer.consume():
            self.alert_counter += 1
            logging.warning(f"New GCN alert number: {self.alert_counter}")

            alert_message = message.value().decode("ascii")
            logging.info(f"New alert message: {alert_message}")
            if alert_available(alert_message):
                return save_alert(alert_message, self.alert_directory)

    def parse_alert(self, alert_path: str) -> ToOEvent:
        """Parse alert and return a ToOEvent object if alert has a matching template

        Args:
            alert_path (str): Path to raw aler file

        Returns:
            ToOEvent: Parsed alert if template is available otherwise None
        """
        alert_content = load_alert(alert_path)

        try:
            gcn_template = GCNTemplates()
            too_event = gcn_template(alert_content)
            logging.info(f"New alert loaded: {too_event.save_dict()}")
            return too_event

        except KeyError:
            logging.warning(
                f"Unknown alert type! Alert has been saved to {self.unknown_alert_directory}"
            )
            save_alert(alert_content, self.unknown_alert_directory)
            return
