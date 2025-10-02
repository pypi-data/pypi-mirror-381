"""Module for handling input and output to the ToO database.

.. autosummary::

   DataBaseIO

.. autoclass:: DataBaseIO
   :noindex:
   :members:

"""

import pathlib as pl
from pathlib import Path

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from flatdict import FlatDict

from ..too_event import ToOEvent


class DataBaseIO:
    def __init__(self, filename: str | Path) -> None:
        self.path = pl.Path(filename)
        self.database = None

    def add_event(self, event: ToOEvent) -> None:
        """Function to add an event to the database.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20

        If the event is already in the
        database, it will be updated. If not, it will be added. Every event needs to
        have a unique publisher_id.

        Args:
            event (ToOEvent): event to be added to the database
        """
        # Convert the event to a flat dictionary and make everything lowercase
        flat_event = FlatDict(event.save_dict(), delimiter=".")
        flat_event = {k.lower(): v for k, v in flat_event.items()}

        # Convert the flat dictionary to a dataframe
        event_df = pd.DataFrame.from_dict(
            flat_event, orient="index", columns=[event.publisher_id]
        )

        # Add the event to the database
        if self.database is None:
            self.database = event_df
        elif self.check_event(event):
            self.database[event.publisher_id] = event_df
        else:
            self.database = self.database.join(event_df, how="outer")

    def check_event(self, event: ToOEvent) -> bool:
        """Function to check if an event is already in the database.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20

        Args:
            event (ToOEvent): Event to be checked

        Returns:
            bool: True if the event is already in the database, False otherwise
        """
        if event.publisher_id in self.database.columns:
            return True
        else:
            return False

    def write(self) -> None:
        """Function to write the database to a csv file.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20
        """
        self.database.T.to_csv(self.path, sep=";")

    def read(self) -> None:
        """Read the database from a csv file.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20
        """
        self.database = pd.read_csv(self.path, index_col=0, dtype={0: str}, sep=";").T
        self.database.columns = self.database.columns.astype(str)

    def get_event(self, publisher_id: str) -> ToOEvent:
        """Function to get an event from the database by its publisher_id.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2024-10-04

        Args:
            publisher_id (str): publisher_id of the event to be retrieved

        Raises:
            KeyError: If the event is not in the database

        Returns:
            ToOEvent: The event with the given publisher_id
        """
        try:
            event_dict = self.database[publisher_id]
        except KeyError:
            raise KeyError(f"Event with publisher_id {publisher_id} not in database.")
        event = ToOEvent()
        event.coordinates = SkyCoord(
            ra=event_dict["coordinates.ra"],
            dec=event_dict["coordinates.dec"],
            frame="icrs",
        )
        event.set_time(event_dict["detection_time"])
        event.event_type = str(event_dict["event_type"])
        event.event_id = str(event_dict["event_id"])
        event.publisher = str(event_dict["publisher"])
        event.publisher_id = str(event_dict["publisher_id"])
        event.priority = int(event_dict["priority"])
        event.params = {}
        parameters = [i for i in list(event_dict.keys()) if "params" in i]
        if parameters == ["params"]:
            return event
        if "params" in parameters:
            parameters.remove("params")
        for p in parameters:
            if p != "params":
                if isinstance(event_dict[p], str):
                    event.params[p.split(".")[1]] = event_dict[p]
                elif not np.isnan(event_dict[p]):
                    event.params[p.split(".")[1]] = event_dict[p]
        return event

    def get_events(self) -> list[ToOEvent]:
        """Function to get all events from the database.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2023-12-20

        Returns:
            list[ToOEvent]: List of all events in the database
        """
        events = []
        for publisher_id in self.database.columns:
            events.append(self.get_event(publisher_id))
        return events
