"""Module for testing csv database operations."""

from pathlib import Path

import pytest
from astropy import units as u
from flatdict import FlatDict

from nuts.IO_funcs.too_database import DataBaseIO
from nuts.too_event import ToOEvent


@pytest.fixture
def event():
    ra, dec = 12, -30
    time = "2022-10-19T10:58:55.123"
    params = {"redshift": 2, "energy": 1e20 * u.eV}

    event = ToOEvent(
        publisher="IceCube",
        publisher_id="1235456",
        event_type="IceCube Gold",
        event_id="IceCube Gold",
        priority=2,
        params=params,
    )
    event.set_coordinates(ra, dec, units="deg")
    event.set_time(time, format="isot")

    return event


@pytest.fixture
def database(tmp_path):
    return DataBaseIO(tmp_path / "test.csv")


@pytest.fixture
def write_database():
    return DataBaseIO(Path("test.csv"))


@pytest.fixture
def read_database():
    return DataBaseIO(Path("test.csv"))


def test_write_functionality(event, write_database):
    write_database.add_event(event)
    event.publisher_id = "1234567"
    write_database.add_event(event)
    event.publisher_id = "1234568f"
    event.params["prob"] = 0.4
    write_database.add_event(event)
    write_database.write()


def test_read_functionality(read_database):
    read_database.read()


def test_read_write_functionality(event, read_database):
    read_database.read()
    db_event = read_database.get_event(event.publisher_id)
    assert db_event == event


def test_read_db_functionality(event, write_database, read_database):
    write_database.add_event(event)
    event.publisher_id = "1234567"
    write_database.add_event(event)
    event.publisher_id = "1234568f"
    event.params["prob"] = 0.4
    write_database.add_event(event)
    write_database.write()

    read_database.read()
    db = read_database.get_events()
    assert len(db) == 3


def test_update_functionality(event, write_database, read_database):
    write_database.add_event(event)
    event.publisher_id = "1234567"
    write_database.add_event(event)
    event.publisher_id = "1234568f"
    event.params["prob"] = 0.4
    write_database.add_event(event)
    write_database.write()

    read_database.read()
    event.publisher_id = "1234567"
    event.params["prob"] = 0.5
    read_database.add_event(event)
    read_database.write()

    read_database.read()
    db = read_database.get_event(event.publisher_id)
    assert db.params["prob"] == 0.5
