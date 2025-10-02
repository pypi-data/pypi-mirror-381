"""Test module for the too_event.py module.
original author: Tobias Heibges
email: theibges@mines.edu
last edit by: Tobias Heibges
email: theibges@mines.edu
date: 2024-01-08
"""

import attrs
import numpy as np
import pytest
from deepdiff import DeepDiff

from nuts.too_event import ToOEvent, check_coordinates

####################################################################################################
# Test the check_coordinates function
####################################################################################################


def test_check_coordinates_true():
    """Test the check_coordinates function with valid coordinates."""
    ra, dec = 12, -30
    ra, dec = check_coordinates(ra, dec, units="deg")
    assert ra == 12 and dec == -30
    ra, dec = np.radians(ra), np.radians(dec)
    ra, dec = check_coordinates(ra, dec, units="rad")
    assert ra == pytest.approx(12) and dec == pytest.approx(-30)


def test_check_coordinates_false():
    """Test the check_coordinates function with invalid coordinates."""
    with pytest.raises(RuntimeError):
        ra, dec = 12, -30
        ra, dec = check_coordinates(ra, dec, units="bla")
    with pytest.raises(ValueError):
        ra, dec = -12, -30
        ra, dec = check_coordinates(ra, dec, units="deg")
    with pytest.raises(ValueError):
        ra, dec = 12, 150
        ra, dec = check_coordinates(ra, dec, units="deg")
    with pytest.raises(ValueError):
        ra, dec = -12, -30
        ra, dec = check_coordinates(np.radians(ra), np.radians(dec), units="rad")
    with pytest.raises(ValueError):
        ra, dec = 12, 150
        ra, dec = check_coordinates(np.radians(ra), np.radians(dec), units="rad")


####################################################################################################
# Test the ToOEvent class
####################################################################################################


def test_event_creation(too_event: ToOEvent):
    """Test the creation of a ToOEvent object.

    Args:
        expl_event (ToOEvent fixture): ToOEvent object created by the fixture
    """
    attrs.asdict(too_event)
    assert True


def test_set_coordinates_true(too_event: ToOEvent):
    """Test the set_coordinates function with valid coordinates.

    Args:
        expl_event (ToOEvent): Fixture of a ToOEvent object
    """
    ra, dec = 12, -30
    too_event.set_coordinates(ra, dec, units="deg")
    assert too_event.coordinates.ra.deg == ra and too_event.coordinates.dec.deg == dec
    too_event.set_coordinates(np.radians(ra), np.radians(dec), units="rad")
    assert too_event.coordinates.ra.deg == pytest.approx(
        ra
    ) and too_event.coordinates.dec.deg == pytest.approx(dec)


def test_set_coordinates_false(too_event: ToOEvent):
    """Test the set_coordinates function with invalid coordinates.

    Args:
        expl_event (ToOEvent): Fixture of a ToOEvent object
    """
    with pytest.raises(RuntimeError):
        ra, dec = 12, -30
        too_event.set_coordinates(ra, dec, units="bla")
    with pytest.raises(ValueError):
        ra, dec = -12, -30
        too_event.set_coordinates(ra, dec, units="deg")
    with pytest.raises(ValueError):
        ra, dec = 12, 150
        too_event.set_coordinates(ra, dec, units="deg")
    with pytest.raises(ValueError):
        ra, dec = -12, -30
        too_event.set_coordinates(np.radians(ra), np.radians(dec), units="rad")
    with pytest.raises(ValueError):
        ra, dec = 12, 150
        too_event.set_coordinates(np.radians(ra), np.radians(dec), units="rad")


def test_set_time_true(too_event: ToOEvent):
    """Test the set_time function with valid times.

    Args:
        expl_event (ToOEvent): Fixture of a ToOEvent object
    """
    time = "2022-10-19T10:58:55.123"
    too_event.set_time(time, format="isot")
    assert too_event.detection_time.isot == time
    time = "2022-10-19 10:58:55.123"
    too_event.set_time(time, format="iso")
    assert too_event.detection_time.iso == time
    time = "2022-10-1 10:58:55.123"
    ctime = "2022-10-01 10:58:55.123"
    too_event.set_time(time, format="iso")
    assert too_event.detection_time.iso == ctime


def test_set_time_false(too_event: ToOEvent):
    """Test the set_time function with invalid times.

    Args:
        expl_event (ToOEvent): Fixture of a ToOEvent object
    """
    with pytest.raises(AssertionError):
        time = "2022-10-19T10:58:55.123"
        too_event.set_time(time, format="isot")
        assert too_event.detection_time.iso == time
    with pytest.raises(ValueError):
        time = "2022-10-1 10:58:55.123"
        too_event.set_time(time, format="isot")


def test_set_params(too_event: ToOEvent):
    """Test setting and adding parameters.

    Args:
        expl_event (ToOEvent): Fixture of a ToOEvent object
    """
    params = {"Redshift": 2, "Energy": 1e20}
    too_event.params = params
    too_event.params["follow_time"] = 3000
    params["follow_time"] = 3000
    assert not DeepDiff(too_event.params, params)
