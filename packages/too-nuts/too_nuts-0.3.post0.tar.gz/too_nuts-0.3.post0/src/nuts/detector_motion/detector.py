from abc import ABC, abstractmethod

import astropy.coordinates as acoord
import astropy.time as atime
import astropy.units as u


class DetectorLocation(ABC):
    @abstractmethod
    def loc(self, time: atime.Time, *args, **kwargs) -> acoord.EarthLocation:
        pass

    @abstractmethod
    def save_dict(self) -> dict:
        pass

    @abstractmethod
    def limb_angle(self, *args, **kwargs) -> u.Quantity:
        pass
