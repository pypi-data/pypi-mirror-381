import pytest
from astropy import units as u
from astropy.time import Time
from pytest import approx


def test_location(sim_detector):
    """Test the location of the balloon is set correctly but changes over time"""
    time = Time("2023-05-14T03:00:00", format="isot", scale="utc")
    assert sim_detector.loc(time) != sim_detector.loc(time + 3 * u.hour)


def test_save_dict(sim_detector):
    """Test the save dictionary method. By asserting the values of
    the dictionary are the same as the expected values."""
    ret_dict = sim_detector.save_dict()
    assert str("tests/test_data/Trajectories/test_sim_traj.csv") in str(
        ret_dict["trajectory_file"]
    )


def test_limb_angle(sim_detector):
    """Test the limb angle method. By asserting the value of the limb
    angle is the same as the expected value for 33km altitude. As the detector
    drops in altitude the limb angle will increase."""
    start_time = Time("2023-05-14T04:00:00", format="isot", scale="utc")
    assert sim_detector.limb_angle(start_time).to(u.deg).value == approx(-5.8, 0.1)


def test_location_out_of_bounds(sim_detector):
    """Test the location of the balloon is set correctly but changes over time"""
    time = Time("2023-05-13T03:00:00", format="isot", scale="utc")
    with pytest.raises(ValueError):
        sim_detector.loc(time)
    time = Time("2023-05-17T03:00:00", format="isot", scale="utc")
    with pytest.raises(ValueError):
        sim_detector.loc(time)
