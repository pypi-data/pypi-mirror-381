"""Define ToO event class.

Module deines the ToOEvent class that stores the information of a ToO event.

original author: Tobias Heibges (theibges@mines.edu)

.. autoclass:: ToOEvent
    :noindex:
    :members:
    :undoc-members:

.. autofunction:: check_coordinates

"""

import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u
import attr
import numpy as np


def check_coordinates(ra: float, dec: float, units: str) -> tuple[float, float]:
    """Function to check the coordinates of an event are valid.

    Args:
        ra (float): Right ascension of the event
        dec (float): Declination of the event
        units (str): Units of the coordinates, either "rad" or "deg"

    Raises:
        RuntimeError: Unknown units
        ValueError: Coordinates are not valid

    Returns:
        tuple[float, float]: Right ascension and declination of the event
    """
    if units == "rad":
        ra = np.rad2deg(ra)
        dec = np.rad2deg(dec)
    elif units != "deg":
        raise RuntimeError('UnitError: Use "rad" or "deg"!')

    if not ((0 <= ra <= 360) and (-90 <= dec <= 90)):
        raise ValueError(
            """ra has to be 0 <= ra <= 360 or 2*pi and
            dec has to be -90 or -pi/2 <= dec <= -90 or -pi/2"""
        )
    return ra, dec


@attr.s
class ToOEvent:
    """Class to store the information of a ToO event."""

    # Name of the instrument that detected the event
    publisher = attr.ib(converter=str, default=None)
    # ID of the event given by the publisher
    # IMPORTANT: this is the id that is used to identify events in the rest of the code
    publisher_id = attr.ib(converter=str, default=None)

    # Type of event
    event_type = attr.ib(converter=str, default=None)
    # Name of the event given by distribution service such as GCN
    event_id = attr.ib(converter=str, default=None)

    # Priority of the event as defined in src/nuts/catalogs/Priority.csv
    priority = attr.ib(converter=int, default=0)
    # Additional parameters of the event
    params = attr.field(default={})

    # Coordinates of the event in the ICRS frame given as an astropy SkyCoord object
    coordinates = attr.ib(
        validator=attr.validators.instance_of(acoord.SkyCoord),
        default=acoord.SkyCoord(ra=0 * u.deg, dec=0 * u.deg, frame="icrs"),
    )
    # Detection time of the event given as an astropy Time object
    detection_time = attr.ib(
        validator=attr.validators.instance_of(atime.Time),
        default=atime.Time("2022-11-11T11:11:11", format="isot", scale="utc"),
    )

    def set_coordinates(
        self, ra: float, dec: float, units: str = "deg", frame: str = "icrs"
    ) -> None:
        """Function to set the coordinates of an event.

        Args:
            ra (float): Right ascension of the event
            dec (float): Declination of the event
            units (str, optional): Units of ra and dec. Defaults to "deg".
            frame (str, optional): Frame RA and DEC are proided in. Defaults to "icrs".
        """
        ra, dec = check_coordinates(ra, dec, units)
        self.coordinates = acoord.SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame=frame)

    def set_time(self, time: str, format="isot", scale="utc") -> None:
        """Function to set the detection time of an event.

        Args:
            time (str): Time of the event
            format (str, optional): Formatting of the time of the event. Defaults to "isot".
            scale (str, optional): Time scale or time zone the time is provided in. Defaults to "utc".
        """
        self.detection_time = atime.Time(time, format=format, scale=scale)

    def save_dict(self) -> dict:
        """Function returns a dict that can be used to save the data of the event.

        Returns:
            dict: Dict containing the data of the event
        """
        save_data = attr.asdict(self)
        save_data["coordinates"] = {
            "ra": str(save_data["coordinates"].icrs.ra.to(u.deg).value * u.deg),
            "dec": str(save_data["coordinates"].icrs.dec.to(u.deg).value * u.deg),
        }
        save_data["detection_time"] = self.detection_time.isot
        return save_data

    def __str__(self) -> str:
        str = f"Event: {self.event_id}\n"
        str += f"Detection time: {self.detection_time}\n"
        str += f"Type: {self.event_type}\n"
        str += f"Priority: {self.priority}"
        return str

    def from_dict(self, data: dict):
        """Function to load the data of the event from a dict.

        Args:
            data (dict): Dict containing the data of the event
        """
        self.publisher = data.get("publisher", None)
        self.publisher_id = data.get("publisher_id", None)
        self.event_type = data.get("event_type", None)
        self.event_id = data.get("event_id", None)
        self.priority = data.get("priority", 0)
        self.params = data.get("params", {})

        ra = data["coordinates"]["ra"]
        dec = data["coordinates"]["dec"]
        self.coordinates = acoord.SkyCoord(ra=u.Quantity(ra), dec=u.Quantity(dec))

        self.set_time(data["detection_time"])
        return self
