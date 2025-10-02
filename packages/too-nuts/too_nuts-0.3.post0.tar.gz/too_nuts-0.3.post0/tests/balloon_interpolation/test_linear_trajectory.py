from astropy import units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time
from pytest import approx


def test_location(linear_detector):
    """Test the location of the balloon is set correctly but changes over time
    The change will be linear therefore the z location will be
        startz + velocity * (time_now - start_time)

    """
    wanaka = EarthLocation(lon=169.1 * u.deg, lat=-44.7 * u.deg, height=33 * u.km)
    start_time = Time("2023-05-13T00:00:00", format="isot", scale="utc")
    assert linear_detector.loc(start_time) == wanaka
    assert linear_detector.loc(Time.now()) != linear_detector.loc(
        Time.now() + 24 * u.hour
    )


def test_save_dict(linear_detector):
    """Test the save dictionary method. By asserting the values of
    the dictionary are the same as the expected values."""
    ret_dict = linear_detector.save_dict()
    assert ret_dict["time"] == "2023-05-13T00:00:00.000"
    assert ret_dict["location"] is not None
    assert ret_dict["velocity"] is not None


def test_limb_angle(linear_detector):
    """Test the limb angle method. By asserting the value of the limb
    angle is the same as the expected value for 33km altitude. As the detector
    drops in altitude the limb angle will increase."""
    start_time = Time("2023-05-13T00:00:00", format="isot", scale="utc")
    assert linear_detector.limb_angle(start_time).to(u.deg).value == approx(-5.8, 0.1)
