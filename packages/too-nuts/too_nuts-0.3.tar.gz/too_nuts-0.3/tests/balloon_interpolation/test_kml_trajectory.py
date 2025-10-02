import pytest
from astropy import units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time
from pytest import approx


def test_location(kml_detector):
    """Test the location of the balloon is set correctly but changes over time"""
    time = Time("2023-05-14T03:00:00", format="isot", scale="utc")
    assert kml_detector.loc(time) != kml_detector.loc(time + 3 * u.hour)


def test_save_dict(kml_detector):
    """Test the save dictionary method. By asserting the values of
    the dictionary are the same as the expected values."""
    ret_dict = kml_detector.save_dict()
    test_dict = {
        "kml_file": "tests/test_data/Trajectories/test.kml",
        "log_start_time": "2023-05-14T00:00:00.000",
        "log_end_time": "2023-05-17T00:00:00.000",
        "velocity": "29.5290856 m / s",
    }
    for key in test_dict:
        if key == "kml_file":
            assert str(test_dict[key]) in str(ret_dict[key])
        else:
            assert ret_dict[key] == test_dict[key]


def test_limb_angle(kml_detector):
    """Test the limb angle method. By asserting the value of the limb
    angle is the same as the expected value for 33km altitude. As the detector
    drops in altitude the limb angle will increase."""
    start_time = Time("2023-05-14T04:00:00", format="isot", scale="utc")
    assert kml_detector.limb_angle(start_time).to(u.deg).value == approx(-5.8, 0.1)


def test_location_out_of_bounds(kml_detector):
    """Test the location of the balloon is set correctly but changes over time"""
    time = Time("2023-05-13T03:00:00", format="isot", scale="utc")
    with pytest.raises(ValueError):
        kml_detector.loc(time)
    time = Time("2023-05-17T03:00:00", format="isot", scale="utc")
    with pytest.raises(ValueError):
        kml_detector.loc(time)
