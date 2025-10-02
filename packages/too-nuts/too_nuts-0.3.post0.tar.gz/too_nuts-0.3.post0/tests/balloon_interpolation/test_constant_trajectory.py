from astropy import units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time
from pytest import approx


def test_location(constant_detector):
    """Test the location of the balloon is fixed. and does not change"""
    wanaka = EarthLocation(lon=169.1 * u.deg, lat=-44.7 * u.deg, height=33 * u.km)

    assert constant_detector.loc(Time.now()).lat.to(u.deg).value == approx(
        wanaka.lat.to(u.deg).value
    )
    assert constant_detector.loc(Time.now()).lon.to(u.deg).value == approx(
        wanaka.lon.to(u.deg).value
    )
    assert constant_detector.loc(Time.now()).height.to(u.m).value == approx(
        wanaka.height.to(u.m).value
    )

    assert constant_detector.loc(Time.now()) == constant_detector.loc(
        Time.now() + 24 * u.hour
    )


def test_save_dict(constant_detector):
    """Test the save dictionary method. By asserting the values of
    the dictionary are the same as the expected values."""
    ret_dict = constant_detector.save_dict()
    assert u.Quantity(ret_dict["location"]["LAT"]).value == approx(
        u.Quantity("-44.7 deg").value
    )
    assert u.Quantity(ret_dict["location"]["LONG"]).value == approx(
        u.Quantity("169.1 deg").value
    )
    assert u.Quantity(ret_dict["location"]["HEIGHT"]).to(u.m).value == approx(
        u.Quantity("33000.0 m").value
    )


def test_limb_angle(constant_detector):
    """Test the limb angle method. By asserting the value of the limb
    angle is the same as the expected value for 33km altitude."""
    assert constant_detector.limb_angle().to(u.deg).value == approx(-5.8, 0.1)
