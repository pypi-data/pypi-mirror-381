""" Output into a json file

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: load_observable_sources

"""

import json
import logging

import astropy.units as u
from astropy.coordinates import AltAz, SkyCoord
from astropy.time import Time

from ..observation_period.observation import ObservationPeriod
from ..too_event import ToOEvent
from ..too_observation import ToOObservation


def load_observable_sources(path: str) -> list[ToOObservation]:
    """Load list of observable sources from json file.

    :Author: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2025-03-12

    Args:
        path: path to json file

    Returns:
        observable: list of observations
    """
    f = open(path)
    sources = json.load(f)

    observable = []
    for i in range(len(sources)):
        observation = ToOObservation()
        tooev = ToOEvent()
        tooev.coordinates = SkyCoord(
            ra=sources[i]["event"]["coordinates"]["ra"],
            dec=sources[i]["event"]["coordinates"]["dec"],
            frame="icrs",
        )
        tooev.set_time(sources[i]["event"]["detection_time"])
        tooev.event_type = sources[i]["event"]["event_type"]
        tooev.event_id = sources[i]["event"]["event_id"]
        tooev.publisher = sources[i]["event"]["publisher"]
        tooev.publisher_id = sources[i]["event"]["publisher_id"]
        tooev.priority = sources[i]["event"]["priority"]

        observation.event = tooev

        tooob = []
        for j in range(len(sources[i]["observations"])):
            sourcesobs = sources[i]["observations"][str(j + 1)]
            obs = ObservationPeriod(
                start_time=Time(sourcesobs["start_time"]),
                start_loc=AltAz(
                    az=float(sourcesobs["start_loc"]["AZ"]) * u.deg,
                    alt=float(sourcesobs["start_loc"]["ALT"]) * u.deg,
                ),
                end_time=Time(sourcesobs["end_time"]),
                end_loc=AltAz(
                    az=float(sourcesobs["end_loc"]["AZ"]) * u.deg,
                    alt=float(sourcesobs["end_loc"]["ALT"]) * u.deg,
                ),
                move_time=Time(sourcesobs["move_time"]),
                pointing_dir=AltAz(
                    az=float(sourcesobs["pointing_dir"]["AZ"]) * u.deg,
                    alt=float(sourcesobs["pointing_dir"]["ALT"]) * u.deg,
                ),
            )
            tooob.append(obs)

        observation.observations = tooob

        observable.append(observation)

    return observable
