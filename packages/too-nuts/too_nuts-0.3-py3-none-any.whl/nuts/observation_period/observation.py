""" Characteristics of observation period.

.. autosummary::
   :toctree:
   :recursive:

.. autoclass:: ObservationPeriod
    :noindex:
    :members:
    :undoc-members:

"""

from dataclasses import dataclass

import astropy.coordinates as acoord
import astropy.time as atime


@dataclass
class ObservationPeriod:
    start_time: atime.Time = None
    end_time: atime.Time = None
    move_time: atime.Time = None
    start_loc: acoord.AltAz = None
    end_loc: acoord.AltAz = None
    pointing_dir: acoord.AltAz = None

    def __lt__(self, other):
        return self.start_time < other.start_time

    def __gt__(self, other):
        return self.start_time > other.start_time

    def save_dict(self) -> dict:
        ret_dict = {}
        ret_dict["start_time"] = self.start_time.utc.isot
        ret_dict["end_time"] = self.end_time.utc.isot
        ret_dict["start_loc"] = {
            "ALT": str(self.start_loc.alt.deg),
            "AZ": str(self.start_loc.az.deg),
        }
        ret_dict["end_loc"] = {
            "ALT": str(self.end_loc.alt.deg),
            "AZ": str(self.end_loc.az.deg),
        }
        ret_dict["pointing_dir"] = {
            "ALT": str(self.pointing_dir.alt.deg),
            "AZ": str(self.pointing_dir.az.deg),
        }
        ret_dict["move_time"] = self.move_time.utc.isot
        return ret_dict
