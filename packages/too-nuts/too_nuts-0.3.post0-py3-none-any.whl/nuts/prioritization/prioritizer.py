"""
Module contains the prioritizer class for the ToO parser.
This is loosely based on a previous version of the Prioritizer
implemented by Hannah Wistrand and adds functionality by combining the
priority value with the time a source would be interesting.

.. autosummary::

   ToOPrioritizer

.. autoclass:: ToOPrioritizer
   :noindex:
   :members:

"""

import logging

import pandas as pd
from astropy import units as u

from ..config.config import ToOConfig
from ..too_event import ToOEvent


class ToOPrioritizer:
    def __init__(self, config: ToOConfig) -> None:
        """Class to prioritize events based on their type and publisher

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20

        Args:
            config (ToOConfig): Configuration file object
            time (Time): Time to check priorities for
        """

        self.config = config
        self.priority_file = config.files.general.priority_file
        self.start_time = config._runtime.observation_starts
        self.end_time = config._runtime.observation_ends

        self.priorities = pd.read_csv(
            self.priority_file,
            names=["publisher", "priority", "earliest"],
            header=0,
        )
        self.publishers = self.priorities["publisher"].str.upper().unique()
        self.priorities["publisher"] = self.priorities["publisher"].str.upper()
        self.priorities.set_index("publisher", inplace=True)

        self.priorities["earliest"] = (
            self.start_time - self.priorities["earliest"].to_numpy() * u.day
        )

    def __call__(self, event: ToOEvent) -> int:
        """Method to check if event type or publisher is in the list of wanted sources

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2024-10-06

        Args:
            observation (ToOEvent): Event to check

        Returns:
            int: Priority value
        """

        publisher = event.publisher.upper()
        event_type = event.event_type.upper()

        if publisher in self.publishers:
            priority = self.priorities.at[publisher, "priority"]
            earliest = self.priorities.at[publisher, "earliest"]

        elif event_type in self.publishers:
            priority = self.priorities.at[event_type, "priority"]
            earliest = self.priorities.at[event_type, "earliest"]

        elif "STEADY" in event_type:
            priority = self.priorities.at["STEADY", "priority"]
            earliest = self.priorities.at["STEADY", "earliest"]

        else:
            logging.error(
                f"Unknown Publisher {publisher} and Event type please add to priority file {self.priority_file}"
            )
            raise RuntimeError(
                f"Unknown Publisher {publisher} and Event type please add to priority file {self.priority_file}"
            )

        # Alert not interesting
        if priority == 0:
            return priority

        # catch too old
        if event.detection_time < earliest:
            return 0

        # catch in the future
        if event.detection_time > self.end_time:
            return 0

        return priority
