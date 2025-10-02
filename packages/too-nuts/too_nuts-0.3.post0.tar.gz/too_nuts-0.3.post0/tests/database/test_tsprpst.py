import shutil
from pathlib import Path

import astropy.units as u
import numpy as np
import pandas as pd
import pytest
from astropy.coordinates import AltAz, EarthLocation
from astropy.time import Time

from nuts.detector_motion.constant_trajectory import ConstantDetectorLoc
from nuts.IO_funcs.too_database import DataBaseIO
from nuts.IO_funcs.TSPRPST_database import TSPRPST_IO
from nuts.too_event import ToOEvent


# Fixture: Build a TSPRPST_IO from the first 10 sources in Full.csv
@pytest.fixture
def sample_io(tmp_path):
    # Load the first 10 sources from the CSV
    csv_path = Path(__file__).parent.parent / "test_data/Database/Full.csv"
    db = DataBaseIO(csv_path)
    db.read()
    events = db.get_events()[:10]

    # Create timestamps over 48 hours in 1 min steps
    start_time = Time("2023-01-01T00:00:00", format="isot", scale="utc")
    times = np.arange(0, 48 * 60, 60) * u.min + start_time

    # build detector frames assuming a constant location
    detloc = ConstantDetectorLoc()
    detloc.coordinates = EarthLocation(lat=0 * u.deg, lon=0 * u.deg, height=33 * u.m)
    detector_frames = AltAz(obstime=times, location=detloc.loc(times))

    # Create a TSPRPST_IO instance
    outpath = tmp_path / "tsprpst_test.npz"
    io = TSPRPST_IO(outpath)
    io.add_detector(times, detloc)

    # For the events calculate their location in the detector frame
    for ev in events:
        io.add_event(
            ev,
            visible_times=times,
            visible_locations=ev.coordinates.transform_to(detector_frames),
        )

    return io


@pytest.mark.parametrize("ext", [".h5", ".fits", ".npz", ".npy"])
def test_roundtrip_hdf5_fits(sample_io: TSPRPST_IO, tmp_path: Path, ext: str):
    """
    Round-trip through HDF5 and FITS and assert that
    detector times/locations and all events match exactly.
    """
    io1 = sample_io
    outpath = tmp_path / f"roundtrip{ext}"
    io1.path = outpath
    io1.write()

    io2 = TSPRPST_IO(outpath)
    io2.read()

    # --- detector round-trip ---
    assert np.all(io1.detector.times.isot == io2.detector.times.isot)
    assert u.allclose(io1.detector.locations.height, io2.detector.locations.height)
    assert u.allclose(io1.detector.locations.lat, io2.detector.locations.lat)
    assert u.allclose(io1.detector.locations.lon, io2.detector.locations.lon)

    # --- events round-trip ---
    assert set(io1.events) == set(io2.events)
    for key in io1.events:
        ev1 = io1.events[key]
        ev2 = io2.events[key]
        assert ev1.event.save_dict() == ev2.event.save_dict()
        assert len(ev1.tpsrspt) == len(ev2.tpsrspt)
        for entry1, entry2 in zip(ev1.tpsrspt, ev2.tpsrspt):
            assert np.all(entry1.times.isot == entry2.times.isot)
            assert u.allclose(entry1.locations.alt, entry2.locations.alt)
            assert u.allclose(entry1.locations.az, entry2.locations.az)
