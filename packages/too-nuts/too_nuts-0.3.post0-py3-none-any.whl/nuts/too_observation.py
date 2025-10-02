"""Define class for ToO observation properties.

.. autoclass:: ToOObservation
    :noindex:
    :members:
    :undoc-members:

"""

from dataclasses import dataclass, field

import numpy as np
from astropy.coordinates import AltAz
from astropy.time import Time

from .config.config import ToOConfig
from .detector_motion.constant_trajectory import ConstantDetectorLoc
from .detector_motion.detector import DetectorLocation
from .observation_period.source_observability import (
    get_observation_times,
    get_source_trajectories,
)
from .too_event import ToOEvent


@dataclass
class ToOObservation:
    event: ToOEvent = field(default_factory=ToOEvent)
    detector: DetectorLocation = field(default_factory=ConstantDetectorLoc)
    observations: list = field(default_factory=list)
    observed: bool = False

    def get_observation_periods(
        self,
        config: ToOConfig,
    ):

        self.observations, tracked_source_loc, visibility_cuts = get_observation_times(
            config,
            self.event,
        )
        return tracked_source_loc, visibility_cuts

    def __str__(self) -> str:
        return f"""Type: {self.event.event_type}, Publisher: {self.event.publisher}, ID: {self.event.event_id}, Priority: {self.event.priority}, Coords: ({self.event.coordinates.ra.deg:.1f}, {self.event.coordinates.dec.deg:.1f})"""

    def __repr__(self) -> str:
        return f"{self.event.event_type}, {self.event.publisher}, {self.event.event_id}, {self.event.priority}, ({self.event.coordinates.ra.deg}, {self.event.coordinates.dec.deg})"

    def __le__(self, other):
        return int(self.event.priority) <= int(other.event.priority)

    def __ge__(self, other):
        return int(self.event.priority) >= int(other.event.priority)

    def __lt__(self, other):
        return int(self.event.priority) < int(other.event.priority)

    def __gt__(self, other):
        return int(self.event.priority) > int(other.event.priority)

    def save_dict(self) -> dict:
        ret_dict = {}
        ret_dict["event"] = self.event.save_dict()
        ret_dict["detector"] = self.detector.save_dict()
        ret_dict["observed"] = self.observed
        ret_dict["observations"] = {}
        for count, observ in enumerate(self.observations):
            ret_dict["observations"][count + 1] = observ.save_dict()
        return ret_dict
