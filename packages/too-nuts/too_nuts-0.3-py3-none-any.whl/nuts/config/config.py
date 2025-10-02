"""
Module holds dataclasses for the configuration of the ToO parser.
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-06-06
"""

import logging
from typing import Any, Literal, Union

import astropy.units as u
from astropy.coordinates import AltAz
from astropy.time import Time
from pydantic import BaseModel, ConfigDict, field_serializer, field_validator

from .file_config import Files, Output


def valid_quantity(data: str) -> u.Quantity:
    return u.Quantity(data)


def valid_time(data: str) -> Time:
    return Time(data, scale="utc")


def serialize_quantities(v):
    return str(v)


class TNS(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # User ID and user name used for TNS
    user_id: int = 2981
    user_name: str = "tobias_heibges"
    # Time period TNS data is downloaded for allowed units are [days, months, years]
    discovered_period_value: str = "1"
    discovered_period_units: str = "days"
    # Download fast radio bursts?
    include_frb: int = 1
    # File format of downloaded TNS data
    format: str = "csv"
    # Limits maximum number of events to download (the total number is bigger than this number)
    num_page: int = 100
    # Combine all files into one file?
    merge_files: int = 1
    # Preiod of time between updates of the TNS data
    update_period: u.Quantity = 1 * u.hour

    _vaidate_quantity = field_validator("update_period", mode="before")(valid_quantity)
    _serialize_quantities = field_serializer("update_period")(serialize_quantities)


class GCN(BaseModel):
    # User ID and user name used for GCN
    client_id: str = "insert client id here"
    client_secret_name: str = "insert client secret here"


class Detector(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Detector trajectory type (cst, kml, log, sim)
    trajectory_type: Literal["cst", "kml", "log", "sim"] = "cst"
    # Constant detector trajectory parameters
    const_lat: u.Quantity = -44.7 * u.deg
    const_long: u.Quantity = 169.1 * u.deg
    const_height: u.Quantity = 33000 * u.m
    # KML detector trajectory parameters
    kml_height: u.Quantity = 33000 * u.m
    kml_url: str = "https://pinwheel.balloonfacility.org/Trajectory/SPBKML729NT.kml"

    _vaidate_quantity = field_validator(
        "const_lat", "const_long", "const_height", "kml_height", mode="before"
    )(valid_quantity)
    _serialize_quantities = field_serializer(
        "const_lat", "const_long", "const_height", "kml_height"
    )(serialize_quantities)


class Observation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    horizontal_offset_angle: str = "limb"
    sun_altitude_cut: u.Quantity = -18.0 * u.deg
    moon_altitude_cut: u.Quantity = -1.0 * u.deg
    moon_illumination_cut: float = 0.05
    fov_az: u.Quantity = 12.8 * u.deg
    fov_alt: u.Quantity = 6.4 * u.deg
    lower_fov_cut: u.Quantity = -6.4 * u.deg
    upper_fov_cut: u.Quantity = 0.0 * u.deg

    _vaidate_quantity = field_validator(
        "sun_altitude_cut",
        "moon_altitude_cut",
        "fov_az",
        "fov_alt",
        "lower_fov_cut",
        "upper_fov_cut",
        mode="before",
    )(valid_quantity)
    _serialize_quantities = field_serializer(
        "sun_altitude_cut",
        "moon_altitude_cut",
        "fov_az",
        "fov_alt",
        "lower_fov_cut",
        "upper_fov_cut",
    )(serialize_quantities)


class Scheduler(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # Scheduling strategy
    strategy_priority_sort: bool = False
    strategy_obstime: bool = False
    strategy_obsprev: bool = False
    strategy_priority_max: int = 3
    # Time period for the rotation of the detector
    rotation_time: u.Quantity = 10 * u.min
    # Minimum observation time for a source
    min_obs_time: u.Quantity = 10 * u.min
    # Maximum number of sources to be scheduled
    max_num_sources: int = 5
    # Sources can not overlap in time
    exclusive: bool = True

    _validate_quantity = field_validator(
        "rotation_time",
        "min_obs_time",
        mode="before",
    )(valid_quantity)
    _serialize_quantities = field_serializer("rotation_time", "min_obs_time")(
        serialize_quantities
    )


class Calculation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Time of the start of the observation given in utc and following isot standard
    start_time: Time = Time("2023-05-15T00:00:00", format="isot", scale="utc")
    # Time period for the calculation
    calculation_period: u.Quantity = 24 * u.hour
    # Time increment for the calculation
    time_increment: u.Quantity = 10 * u.min
    # relationship between utc and local time
    utc_relation: u.Quantity = 0 * u.h
    # number of days for flight
    num_days_flight: u.Quantity = 10.0 * u.day
    # number of observation windows to calculate
    num_observation_windows: Union[int, Literal["all"]] = "all"
    # option to merge databases saved in Listeners to Database
    merge_listeners_database: bool = False
    # Sequence of modules to run
    sequence: list[
        Literal[
            "observation-window",
            "combine-db",
            "clean-db",
            "observability",
            "schedule",
            "in-fov",
        ]
    ] = [
        "observation-window",
        "combine-db",
        "clean-db",
        "observability",
        "schedule",
    ]

    _validate_quantity = field_validator(
        "calculation_period",
        "time_increment",
        "utc_relation",
        "num_days_flight",
        mode="before",
    )(valid_quantity)

    _validate_time = field_validator("start_time", mode="before")(valid_time)
    _serialize_quantities = field_serializer(
        "start_time",
        "calculation_period",
        "time_increment",
        "utc_relation",
        "num_days_flight",
    )(serialize_quantities)


class GWaves(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    obs_timewindow: u.Quantity = 15 * u.min
    downsample: int = 32
    confidence: int = 90
    visualize: bool = False
    time_increment: u.Quantity = 1 * u.min
    _validate_quantity = field_validator(
        "obs_timewindow", "time_increment", mode="before"
    )(valid_quantity)
    _serialize_quantities = field_serializer("obs_timewindow", "time_increment")(
        serialize_quantities
    )


class Settings(BaseModel):
    # Settings for the calculation
    calculation: Calculation = Calculation()
    # Setup for GW poorly localized
    gwaves: GWaves = GWaves()
    # Setup for detector trajectory
    detector: Detector = Detector()
    # Setup for detector
    observation: Observation = Observation()
    # Setup for scheduling
    scheduler: Scheduler = Scheduler()
    # Setup for TNS listener
    tns: TNS = TNS()
    # Setup for GCN
    gcn: GCN = GCN()


class Runtime(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Config file used
    config_file: str = None
    iteration: int = 0
    # Options used
    options: str = None
    observation_starts: Time = None
    observation_ends: Time = None

    all_times: Time = None
    times: Time = None
    detector_frames: AltAz = None
    fov_cuts: Any = None
    detector: Any = None
    obs_times: Time = None
    obs_detector_frames: AltAz = None
    observation_times: Time = None
    observation_detector_frames: AltAz = None


class ToOConfig(BaseModel):
    # Settings for the ToO parser
    settings: Settings = Settings()
    # Output files for the ToO parser
    output: Output = Output()
    # Files used for the ToO parser
    files: Files = Files()
    # Runtime parameters for the ToO parser
    _runtime: Runtime = Runtime()
