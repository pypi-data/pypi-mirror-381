"""The Target Source Position Relative Point Source Tensor (TPSRSPT) database module. This database is designed
to hold the positions of point sources (so far it is limited to point sources) relative to a detector. It has a
nested structure where each event can have multiple observation periods (entries), each with its own set of times and
locations.

:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2025-07-18

.. autosummary::

   TPSRPST_IO
   Detector
   TPSRSPT_entry
   TPSRSPT_event

.. autoclass:: TPSRPST_IO
   :noindex:
   :members:

.. autoclass:: Detector
   :noindex:
   :members:

.. autoclass:: TPSRSPT_entry
   :noindex:
   :members:

.. autoclass:: TPSRSPT_event
   :noindex:
   :members:

"""

import json
import logging
import pathlib as pl
from dataclasses import dataclass
from pathlib import Path

import astropy.units as u
import h5py
import numpy as np
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.io import fits
from astropy.table import Column, QTable, Table
from astropy.time import Time

from ..detector_motion.detector import DetectorLocation
from ..too_event import ToOEvent


@dataclass
class TPSRSPT_entry:
    """A class to hold the times and locations of a source for a single observation period.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18"""

    times: Time = None
    locations: AltAz = None


@dataclass
class TPSRSPT_event:
    """A class to hold the relative source positions for an event across multiple observation periods.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18"""

    event: ToOEvent
    tpsrspt: list[TPSRSPT_entry]


@dataclass
class Detector:
    """A class to hold the detector's location and times of observation.
    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18
    """

    times: Time = None
    locations: EarthLocation = None


class TSPRPST_IO:
    """Database for Target Source Position Relative Point Source Tensor (TPSRSPT) data. This class manages the storage and retrieval of
    point source positions relative to a detector, organized by events and observation periods. It allows for adding new events, retrieving existing ones, and saving/loading the database to/from various formats (FITS, HDF5, NumPy).
    It is designed to handle multiple events, each with multiple observation periods, and supports serialization to different file formats.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18
    """

    def __init__(self, path: pl.Path) -> None:
        self.path: pl.Path = pl.Path(path)
        self.event_ids: list[str] = []
        self.events: dict[str, TPSRSPT_event] = {}
        self.detector: Detector = Detector()

    def __len__(self) -> int:
        return len(self.event_ids)

    def add_detector(self, times: Time, detector: DetectorLocation) -> None:
        """Add a detector to the TPSRPST_IO instance.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18

        Args:
            times (Time): The times at which the detector is active.
            detector (DetectorLocation): The location of the detector.
        """
        locs = detector.loc(times)
        self.detector.times = times
        self.detector.locations = locs

    def add_event(
        self,
        event: ToOEvent,
        visible_times: Time,
        visible_locations: SkyCoord,
    ) -> None:
        """Add a new event to the TPSRPST_IO instance.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18

        Args:
            event (ToOEvent): The event to add.
            visible_times (Time): The times at which the event is visible.
            visible_locations (SkyCoord): The locations of the event.
        """

        eid = event.publisher_id
        entry = TPSRSPT_entry(visible_times, visible_locations)

        if eid not in self.event_ids:
            logging.info(f"Adding event {eid}")
            self.events[eid] = TPSRSPT_event(
                event=event,
                tpsrspt=[entry],
            )
            self.event_ids.append(eid)
        else:
            logging.warning(f"Appending to existing event {eid}")
            self.events[eid].tpsrspt.append(entry)

    def write(self, **opts) -> None:
        """
        Save the TPSRPST_IO instance to a file at self.path.
        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18
        """
        to_file(self, str(self.path), **opts)
        logging.info(f"Saved TPSRSPT data to {self.path}")

    def read(self, **opts) -> None:
        """Load events (and detector) from the file at self.path.
        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18
        """
        self.detector, self.events = from_file(str(self.path), **opts)

    def get_event_ids(self) -> list[str]:
        """Retrieve the list of event IDs stored in this TPSRPST_IO instance.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18

        Returns:
            list[str]: The list of event IDs.
        """
        return self.event_ids

    def get_event(self, event_id: str) -> ToOEvent:
        """Retrieve the ToOEvent object for a given event ID.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18

        Args:
            event_id (str): The ID of the event.

        Raises:
            KeyError: If the event ID is not found.
            ValueError: If no event is found for the event ID.

        Returns:
            ToOEvent: The ToOEvent object for the event ID.
        """
        if event_id not in self.events:
            raise KeyError(f"Event ID {event_id} not found in TPSRPST_IO.")
        if not self.events[event_id].event:
            raise ValueError(f"No event found for event ID {event_id}.")
        return self.events[event_id].event

    def get_tpsrspt(self, event_id: str) -> list[np.ndarray]:
        """Retrieve the TPSRSPT entries for a given event ID.

        :Author: Tobias Heibges (theibges@mines.edu)
        :Last edit by: Tobias Heibges (theibges@mines.edu)
        :Date: 2025-07-18

        Args:
            event_id (str): The ID of the event.

        Raises:
            KeyError: If the event ID is not found.
            ValueError: If no TPSRSPT entries are found for the event ID.

        Returns:
            list[np.ndarray]: The TPSRSPT entries for the event ID.
        """
        if event_id not in self.events:
            raise KeyError(f"Event ID {event_id} not found in TPSRPST_IO.")
        if not self.events[event_id].tpsrspt:
            raise ValueError(f"No TPSRSPT entries found for event ID {event_id}.")
        return self.events[event_id].tpsrspt


def to_fits(data: TSPRPST_IO, filename: Path) -> None:
    """Write a FITS file with 3 HDUs: Primary, DETECTOR, EVENTS, TPSRSPT.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        data (TSPRPST_IO): The TPSRPST_IO instance containing the data to write.
        filename (Path): The name of the output FITS file.
    """

    hdus = [fits.PrimaryHDU()]

    # 1) DETECTOR extension (if any)
    if data.detector:
        det = data.detector
        det_tab = Table(
            {
                "TIME": det.times.isot,  # ISO‐T strings
                "HEIGHT": det.locations.height,  # Quantity column
                "LATITUDE": det.locations.lat,
                "LONGITUDE": det.locations.lon,
            }
        )
        hdus.append(fits.BinTableHDU(det_tab, name="DETECTOR"))

    # 2) EVENTS extension: one row per event key
    ev_tab = Table(
        {
            "KEY": list(data.events.keys()),
            "EVENT": [json.dumps(ev.event.save_dict()) for ev in data.events.values()],
        }
    )
    hdus.append(fits.BinTableHDU(ev_tab, name="EVENTS"))

    # 3) TPSRSPT extension: one row per (key, period_idx),
    #    with variable-length arrays for times/alt/az

    for key, ev in data.events.items():

        keys, idxs, mjds, alts, azs = (
            np.array([]),
            np.array([]),
            np.array([]),
            np.array([]),
            np.array([]),
        )
        for period_idx, entry in enumerate(ev.tpsrspt):
            keys = np.append(keys, key)
            idxs = np.append(idxs, period_idx * np.ones_like(entry.times, dtype=int))
            mjds = np.append(mjds, entry.times.utc.mjd)
            alts = np.append(alts, entry.locations.alt.to_value(u.deg))
            azs = np.append(azs, entry.locations.az.to_value(u.deg))

        tps_tab = QTable()
        tps_tab.add_column(Column(idxs, name="PERIOD_IDX"))
        tps_tab.add_column(Column(mjds, name="MJD", unit=u.day))
        tps_tab.add_column(Column(alts, name="ALTITUDE", unit=u.deg))
        tps_tab.add_column(Column(azs, name="AZIMUTH", unit=u.deg))

        hdus.append(fits.BinTableHDU(tps_tab, name=key))

    # write to disk
    if Path(filename).exists():
        logging.warning(f"Overwriting existing file: {filename}")
    fits.HDUList(hdus).writeto(filename, overwrite=True)


def from_fits(filename: Path) -> tuple[Detector, dict[str, TPSRSPT_event]]:
    """Read back the three HDUs and rebuild detector + events dict.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        filename (Path): The path to the input FITS file.

    Returns:
        tuple[Detector, dict[str, TPSRSPT_event]]: The reconstructed detector and events.
    """

    hdul = fits.open(filename)
    # --- 1) DETECTOR ---
    if "DETECTOR" in hdul:
        det_tab = Table(hdul["DETECTOR"].data)
        det_times = Time(det_tab["TIME"].astype(str), format="isot")
        detector = type("D", (), {})()
        detector.times = det_times
        detector.locations = EarthLocation(
            lat=det_tab["LATITUDE"],
            lon=det_tab["LONGITUDE"],
            height=det_tab["HEIGHT"],
        )
        hdul.pop("DETECTOR")  # remove from HDUList after reading
    else:
        detector = Detector()

    # --- 2) EVENTS metadata ---
    ev_tab = Table(hdul["EVENTS"].data)
    events: dict[str, TPSRSPT_event] = {}
    for row in ev_tab:
        key = row["KEY"]
        # if stored as bytes, decode
        if isinstance(key, (bytes, np.bytes_)):
            key = key.decode("utf-8")
        evdict = row["EVENT"]
        if isinstance(evdict, (bytes, np.bytes_)):
            evdict = evdict.decode("utf-8")
        evdict = json.loads(evdict)

        too = ToOEvent().from_dict(evdict)
        events[key] = TPSRSPT_event(event=too, tpsrspt=[])
    hdul.pop("EVENTS")  # remove from HDUList after reading

    # --- 3) One HDU per event key, named exactly by that key ---
    #    each has columns: PERIOD_IDX, MJD, ALTITUDE, AZIMUTH
    names = [hdu.name for hdu in hdul if isinstance(hdu, fits.BinTableHDU)]

    for name in names:
        tab = QTable(hdul[name].data)
        # group by PERIOD_IDX
        for period_idx in np.unique(tab["PERIOD_IDX"]):
            sel = tab["PERIOD_IDX"] == period_idx
            block = tab[sel]

            # MJD → Time; ALTITUDE/AZIMUTH → Quantity
            mjd_vals = block["MJD"].tolist()
            times = Time(mjd_vals, format="mjd")
            alt = block["ALTITUDE"].data * u.deg
            az = block["AZIMUTH"].data * u.deg

            entry = TPSRSPT_entry(
                times=times, locations=AltAz(alt=alt, az=az, obstime=times)
            )
            events[name.lower()].tpsrspt.append(entry)

    hdul.close()
    return detector, events


def to_hdf5(data: TSPRPST_IO, filename: Path) -> None:
    """Write the TSPRPST_IO data to an HDF5 file.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        data (TSPRPST_IO): The TSPRPST_IO instance containing the data to write.
        filename (Path): The name of the output HDF5 file.
    """

    def write_times(group: h5py.Group, times: Time) -> None:
        """Write astropy Time to HDF5 group as ISO strings.

        Args:
            group (h5py.Group): The HDF5 group to write to.
            times (Time): The astropy Time object to write.
        """
        dset = group.create_dataset("times", data=times.isot.astype("S26"))
        dset.attrs["format"] = "isot"

    def write_quantity(group: h5py.Group, quantity: u.Quantity, name: str) -> None:
        """Write astropy Quantity to HDF5 group.

        Args:
            group (h5py.Group): The HDF5 group to write to.
            quantity (u.Quantity): The astropy Quantity object to write.
            name (str): The name of the dataset within the group.
        """
        dset = group.create_dataset(name, data=quantity.value.astype(float))
        dset.attrs["unit"] = str(quantity.unit)

    # Create the HDF5 file
    with h5py.File(filename, "w") as f:
        if data.detector is not {}:
            det_grp = f.create_group("detector")
            write_times(det_grp, data.detector.times)
            write_quantity(det_grp, data.detector.locations.height, name="height")
            write_quantity(det_grp, data.detector.locations.lat, name="latitude")
            write_quantity(det_grp, data.detector.locations.lon, name="longitude")

        for key, event in data.events.items():
            grp = f.create_group(key)
            grp.attrs["event"] = json.dumps(event.event.save_dict())

            for i, arr in enumerate(event.tpsrspt):
                entry = grp.create_group(f"observation_period_{i}")
                write_times(entry, arr.times)
                write_quantity(entry, arr.locations.alt, name="altitude")
                write_quantity(entry, arr.locations.az, name="azimuth")


def from_hdf5(filename: Path) -> tuple[Detector, dict[str, TPSRSPT_event]]:
    """Load TSPRPST data from an HDF5 file.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        filename (Path): The name of the HDF5 file to read.

    Returns:
        tuple[Detector, dict[str, TPSRSPT_event]]: The loaded detector and events.
    """

    def _read_times(group: h5py.Group) -> Time:
        """Reverse of write_times: load ISO-T strings and wrap in astropy Time.

        Args:
            group (h5py.Group): The HDF5 group to read from.

        Returns:
            Time: The astropy Time object read from the group.
        """
        dset = group["times"]
        # HDF5 stores them as S26 (bytes), so decode to unicode
        iso = dset[()].astype("U26")
        fmt = dset.attrs.get("format", "isot")
        return Time(iso, format=fmt)

    def _read_quantity(group: h5py.Group, name: str) -> u.Quantity:
        """Reverse of write_quantity: load .value + unit attr.

        Args:
            group (h5py.Group): The HDF5 group to read from.
            name (str): The name of the dataset within the group.

        Returns:
            u.Quantity: The astropy Quantity object read from the group.
        """
        dset = group[name]
        vals = dset[()]
        unit = dset.attrs["unit"]
        return vals * u.Unit(unit)

    detector = Detector()
    events: dict[str, TPSRSPT_event] = {}

    with h5py.File(filename, "r") as f:
        # --- detector (optional) ---
        if "detector" in f:
            det = f["detector"]
            detector.times = _read_times(det)
            height = _read_quantity(det, "height")
            latitude = _read_quantity(det, "latitude")
            longitude = _read_quantity(det, "longitude")
            detector.locations = EarthLocation(
                lat=latitude, lon=longitude, height=height
            )

        # --- each event group ---
        for key, grp in f.items():
            if key == "detector":
                continue

            # ToOEvent dict
            evdict = json.loads(grp.attrs["event"])

            tpsrspt_list = []
            # we named these "observation_period_0", "observation_period_1", …
            # so sort by the trailing index:
            for name in sorted(grp.keys(), key=lambda s: int(s.split("_")[-1])):
                entry = grp[name]
                times = _read_times(entry)
                alt = _read_quantity(entry, "altitude")
                az = _read_quantity(entry, "azimuth")

                entry = TPSRSPT_entry(
                    times=times,
                    locations=AltAz(
                        alt=alt,
                        az=az,
                        obstime=times,
                    ),
                )

                tpsrspt_list.append(entry)

            events[key] = TPSRSPT_event(
                event=ToOEvent().from_dict(evdict),
                tpsrspt=tpsrspt_list,
            )

    return detector, events


def to_numpy(data: dict, filename: Path, compressed: bool = True) -> None:
    """Serialize nested dict to a NumPy file.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        data (dict): The data to serialize.
        filename (Path): The name of the file to write to.
        compressed (bool, optional): Whether to compress the file. Defaults to False.
    """

    ext = Path(filename).suffix.lower()
    if ext == ".npz" or compressed:
        np.savez_compressed(filename, data=data)
    elif ext == ".npy" and not compressed:
        np.save(filename, data)
    else:
        # fallback: choose based on compressed flag
        if compressed:
            np.savez_compressed(filename, data=data)
        else:
            np.save(filename, data)


def from_numpy(filename: Path) -> tuple[Detector, dict[str, TPSRSPT_event]]:
    """Deserialize nested dict from a NumPy file (.npz or .npy).

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        filename (Path): The name of the file to read from.

    Returns:
        tuple[Detector, dict[str, TPSRSPT_event]]: The deserialized detector and events.
    """

    ext = Path(filename).suffix.lower()
    if ext == ".npz":
        with np.load(filename, allow_pickle=True) as arr:
            data = arr["data"].item()
    else:
        data = np.load(filename, allow_pickle=True).item()
    return data.detector, data.events


def to_file(data: dict, filename: Path, overwrite: bool = True, **opts) -> None:
    """Serialize data to a file. based on the file extension, it will choose the appropriate format.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        data (dict): The data to serialize.
        filename (Path): The name of the file to write to.

    Raises:
        ValueError: If the file extension is not supported.
    """
    if not isinstance(filename, Path):
        filename = Path(filename)

    if filename.exists() and not overwrite:
        logging.warning(
            f"File: {filename} already exists. Use overwrite=True to overwrite."
        )
        return

    if filename.exists() and overwrite:
        filename.unlink()  # remove existing file
        logging.warning(f"Overwriting existing file: {filename}")

    ext = filename.suffix.lower()
    if ext in (".h5", ".hdf5"):
        to_hdf5(data, filename, **opts)
    elif ext in (".npz", ".npy"):
        to_numpy(data, filename, compressed=opts.get("compressed", False))
    elif ext in (".fits"):
        to_fits(data, filename)
    else:
        raise ValueError(f"Unsupported extension for output: {ext}")


def from_file(filename: Path, **opts) -> tuple[Detector, dict[str, TPSRSPT_event]]:
    """Load data from a file. Based on the file extension, it will choose the appropriate format.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2025-07-18

    Args:
        filename (Path): The name of the file to read from.

    Raises:
        ValueError: If the file extension is not supported.

    Returns:
        tuple[Detector, dict[str, TPSRSPT_event]]: The deserialized detector and events.
    """

    if not isinstance(filename, Path):
        filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")

    ext = filename.suffix.lower()
    if ext in (".h5", ".hdf5"):
        return from_hdf5(filename, **opts)
    elif ext in (".npz", ".npy"):
        return from_numpy(filename)
    elif ext in (".fits"):
        return from_fits(filename)
    else:
        raise ValueError(f"Unsupported extension for input: {ext}")
