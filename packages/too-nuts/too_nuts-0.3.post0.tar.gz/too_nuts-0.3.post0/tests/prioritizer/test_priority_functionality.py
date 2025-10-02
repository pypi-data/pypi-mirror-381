import pathlib

import astropy.time as atime
import astropy.units as u
import pytest

from nuts.config.config import ToOConfig
from nuts.prioritization.prioritizer import ToOPrioritizer
from nuts.too_event import ToOEvent

####################################################################################################
# Fixtures
####################################################################################################


@pytest.fixture
def event() -> ToOEvent:
    """IceCube Gold Event at ra,dec (0,0) detected at March equinox 2023 (should be right behind the sun)

    Returns:
        ToOEvent: Event object
    """
    publisher = "IceCube"
    publisher_id = 1235456
    event_type = "ICECUBE Astrotrack Gold"
    event_id = publisher_id

    event = ToOEvent(
        publisher=publisher,
        publisher_id=publisher_id,
        event_type=event_type,
        event_id=event_id,
    )

    ra = 0 * u.deg
    dec = 0 * u.deg
    event.set_coordinates(ra=ra.to("deg").value, dec=dec.to("deg").value)
    event.detection_time = atime.Time("2023-03-20T21:24:00", format="isot", scale="utc")
    return event


####################################################################################################
# Test the prioritizer functionality
####################################################################################################


def test_priority_assignment(config: ToOConfig, event: ToOEvent) -> None:
    scheduler_time = config.settings.calculation.start_time
    config._runtime.observation_starts = scheduler_time
    config._runtime.observation_ends = scheduler_time + 1.0 * u.day
    prioritizer = ToOPrioritizer(config=config)

    # test case 1: event is too early (1year before start time)
    event.detection_time = scheduler_time - 365 * u.day
    priority = prioritizer(event)
    assert priority == 0

    # test case 2: event is too late (1 year after start time)
    event.detection_time = scheduler_time + 365 * u.day
    priority = prioritizer(event)
    assert priority == 0

    # test case 3: event is just before start time (1 day)
    event.detection_time = scheduler_time - 1 * u.day
    priority = prioritizer(event)
    assert priority == 2
