import pathlib

import astropy.units as u
import pandas as pd
import pytest
from astropy.coordinates import AltAz, EarthLocation
from astropy.time import Time

import nuts.observation_period.sun_moon_cuts as sun_moon_cuts
from nuts.compute import Compute
from nuts.config.config import ToOConfig
from nuts.detector_motion.constant_trajectory import ConstantDetectorLoc
from nuts.observation_period.sun_moon_cuts import moon_illumination


def test_sun(config):
    lat = 0 * u.deg
    long = 0 * u.deg
    time = Time("2023-01-01T00:00:00", format="isot", scale="utc")
    location = EarthLocation.from_geodetic(lat=lat, lon=long, height=33000 * u.m)
    det_frames = AltAz(obstime=time, location=location)

    cuts = sun_moon_cuts.SunMoonCuts(config)
    sun_down = cuts.sun_cut(time, det_frames)
    assert sun_down == 1


def test_sun_window(config: ToOConfig, compute: Compute):
    # Changing the detector setup to be on ground level
    config.settings.detector.const_height = 0 * u.km

    # Changing the observation settings by convention we use the center
    # of the sun as reference but other software may use the edge
    config.settings.observation.sun_altitude_cut = -0.5 * u.deg
    # In this test we want to disregard the moon
    config.settings.observation.moon_illumination_cut = 1

    # Apply changes to the compute object
    compute.build()
    compute.runtime_params()

    # run calculation
    option = "obs_window"
    observation_windows = compute(option)["obs-window_0"]

    # Truth value taken from https://www.timeanddate.com/sun/@2184707
    truth = [
        Time("2024-09-02T06:16:00", format="isot", scale="utc"),
        Time("2024-09-02T19:11:00", format="isot", scale="utc"),
    ]

    for i in range(len(truth)):
        assert observation_windows[i].gps == truth[i].gps


def test_moon_window(config: ToOConfig, compute: Compute):

    # Changing the detector setup to be on ground level
    config.settings.detector.const_height = 0 * u.km

    # Changing the observation settings.
    # For this test disregard the sun
    config.settings.observation.sun_altitude_cut = 91 * u.deg
    # In this test we never disregard the moon because of too little illumination
    config.settings.observation.moon_illumination_cut = 0
    # Moon's angular diameter
    config.settings.observation.moon_altitude_cut = -0.8 * u.deg
    compute.build()
    compute.runtime_params()

    # run calculation
    option = "obs_window"
    observation_windows = compute(option)["obs-window_0"]

    # Truth value taken from https://www.timeanddate.com/moon/@2184707
    truth = [
        Time("2024-09-02T05:14:00", format="isot", scale="utc"),
        Time("2024-09-02T19:21:00", format="isot", scale="utc"),
    ]

    for i in range(len(truth)):
        assert observation_windows[i].gps == truth[i].gps


def test_moon_illumination():

    # Test if moon illumination is correctly calculated
    times = pd.date_range("2024-10-01T00:00:00", "2024-10-30T00:00:00", freq="5min")
    times = Time(times)

    moon_illum = moon_illumination(times)
    min_illum = moon_illum.argmin()
    max_illum = moon_illum.argmax()

    # Truth values taken from https://www.timeanddate.com/moon/phases/timezone/utc?year=2024
    assert times[min_illum].gps == pytest.approx(
        Time("2024-10-02T18:50:00").gps, abs=30 * 60
    )
    assert times[max_illum].gps == pytest.approx(
        Time("2024-10-17T11:25:00").gps, abs=30 * 60
    )
