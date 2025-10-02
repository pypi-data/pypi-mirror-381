"""
Module holds dataclasses for the configuration of the ToO parser.
:Author: Tobias Heibges (theibges@mines.edu)
:Last edit by: Tobias Heibges (theibges@mines.edu)
:Date: 2024-06-06
"""

import logging
import pathlib as pl

from pydantic import BaseModel, Field, field_serializer, field_validator
from pydantic_core.core_schema import ValidationInfo


def global_paths(v, info: ValidationInfo):
    v["global_path"] = info.data["global_path"]
    return v


def local_paths(v, info: ValidationInfo):
    v["global_path"] = info.data["directory"]
    return v


def build_dir(path: pl.Path, info: ValidationInfo) -> pl.Path:
    path = info.data["global_path"] / path
    path = path.resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def build_path(path: pl.Path):
    path = path.resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def build_file(path, info: ValidationInfo):
    path = info.data["directory"] / path
    return path


def serialize_paths(v):
    return str(v)


class DetectorTrajectories(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Trajectories directory
    directory: pl.Path = pl.Path("Trajectories")
    # Path to KML file containing the detector trajectory
    kml_file: pl.Path = pl.Path("flight.kml")
    # Path to Flight-log file containing the log of the detector trajectory
    log_file: pl.Path = pl.Path("flight.log")
    # Path to Flight-sim file containing the simulated detector trajectory
    sim_file: pl.Path = pl.Path("simulated_traj.csv")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator("kml_file", "log_file", "sim_file", mode="after")(
        build_file
    )
    _output_paths = field_serializer("directory", "kml_file", "log_file", "sim_file")(
        serialize_paths
    )


class DataBase(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Trajectories directory
    directory: pl.Path = pl.Path("Database")
    # GCN database file
    gcn: pl.Path = pl.Path("GCN.csv")
    # TNS database file
    tns: pl.Path = pl.Path("TNS.csv")
    # Other transients database file
    other: pl.Path = pl.Path("OtherTransients.csv")
    # Steady sources database file
    steady: pl.Path = pl.Path("SteadySources.csv")
    # TDE database file
    tde: pl.Path = pl.Path("TDE.csv")
    # test database file
    test: pl.Path = pl.Path("test.csv")

    # combined database file
    combined: pl.Path = pl.Path("Full.csv")
    # database file after cleaning
    cleaned: pl.Path = pl.Path("Full_clean.csv")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "gcn",
        "tns",
        "other",
        "steady",
        "tde",
        "combined",
        "cleaned",
        "test",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "gcn",
        "tns",
        "other",
        "steady",
        "tde",
        "combined",
        "cleaned",
        "test",
    )(serialize_paths)


class Listener(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Listener directory
    directory: pl.Path = pl.Path("Listeners")
    # Path to the directory containing the raw alerts
    gcn_alerts_dir: pl.Path = pl.Path("GCN")
    # Path to the directory containing the unknown raw alerts
    gcn_unknown_alerts_dir: pl.Path = pl.Path("GCN/unknown")
    # Path to the directory containing the test alerts
    gcn_test_alerts_dir: pl.Path = pl.Path("GCN_Test")
    # Path to the file containing the GCN data
    gcn_file: pl.Path = pl.Path("GCN.csv")
    # Path to the directory containing the TNS data
    tns_dir: pl.Path = pl.Path("TNS")
    # Path to the file containing the TNS data
    tns_file: pl.Path = pl.Path("TNS.csv")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "gcn_alerts_dir",
        "gcn_unknown_alerts_dir",
        "gcn_test_alerts_dir",
        "gcn_file",
        "tns_dir",
        "tns_file",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "gcn_alerts_dir",
        "gcn_unknown_alerts_dir",
        "gcn_test_alerts_dir",
        "gcn_file",
        "tns_dir",
        "tns_file",
    )(serialize_paths)


class Pointing(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Pointing directory
    directory: pl.Path = pl.Path("Pointing")
    # Path to tilt data file
    tilt_file: pl.Path = pl.Path("tilt.csv")
    # Path to yaw data file
    yaw_file: pl.Path = pl.Path("yaw_pointing.csv")
    # Path to file containing detector uptime data
    uptime_file: pl.Path = pl.Path("uptime.npz")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "tilt_file",
        "yaw_file",
        "uptime_file",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "tilt_file",
        "yaw_file",
        "uptime_file",
    )(serialize_paths)


class GeneralFiles(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to General settings directory
    directory: pl.Path = pl.Path("General")
    # Path to the file containing the GCN alerts
    gcn_file: pl.Path = pl.Path("GCN_alerts.csv")
    # Path to the file containing the alert priorities
    priority_file: pl.Path = pl.Path("Priorities.csv")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator("gcn_file", "priority_file", mode="after")(build_file)
    _output_paths = field_serializer("directory", "gcn_file", "priority_file")(
        serialize_paths
    )


class Files(BaseModel):
    # Path to directory containing all data files
    global_path: pl.Path = pl.Path("../../Catalogs/")

    general: GeneralFiles = GeneralFiles()
    trajectories: DetectorTrajectories = DetectorTrajectories()
    database: DataBase = DataBase()
    listener: Listener = Listener()
    pointing: Pointing = Pointing()

    _forward_global_paths = field_validator(
        "trajectories", "database", "listener", "pointing", "general", mode="before"
    )(global_paths)
    _output_paths = field_serializer(
        "global_path",
    )(serialize_paths)


class DetectorPlots(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Plots directory
    directory: pl.Path = pl.Path("Detector")
    # Format to save the plots in
    plot_format: str = "pdf"

    # Detector location mollweide plot
    detector_location_mollweide: pl.Path = Field(default=None)
    detector_location_hammer: pl.Path = Field(default=None)
    detector_location_aeqd: pl.Path = Field(default=None)

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "detector_location_mollweide",
        "detector_location_hammer",
        "detector_location_aeqd",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "detector_location_mollweide",
        "detector_location_hammer",
        "detector_location_aeqd",
    )(serialize_paths)


class SourceSkyPlots(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Plots directory
    directory: pl.Path = pl.Path("Source_Skymaps")
    # Format to save the plots in
    plot_format: str = "pdf"

    # Source location mollweide plot
    skymap_none: pl.Path = Field(default=None)
    skymap_all: pl.Path = Field(default=None)
    skymap_obs: pl.Path = Field(default=None)
    skymap_sched: pl.Path = Field(default=None)
    skymap_comp: pl.Path = Field(default=None)

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "skymap_none",
        "skymap_all",
        "skymap_obs",
        "skymap_sched",
        "skymap_comp",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "skymap_none",
        "skymap_all",
        "skymap_obs",
        "skymap_sched",
        "skymap_comp",
    )(serialize_paths)


class SourceTrajPlots(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Plots directory
    directory: pl.Path = pl.Path("Source_Trajectories")
    # Format to save the plots in
    plot_format: str = "pdf"

    # Source location mollweide plot
    source_trajectories_full_sky: pl.Path = Field(default=None)
    source_trajectories_zoom: pl.Path = Field(default=None)
    source_trajectories_comp_full_sky: pl.Path = Field(default=None)
    source_trajectories_comp_zoom: pl.Path = Field(default=None)

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "source_trajectories_full_sky",
        "source_trajectories_zoom",
        "source_trajectories_comp_full_sky",
        "source_trajectories_comp_zoom",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "source_trajectories_full_sky",
        "source_trajectories_zoom",
        "source_trajectories_comp_full_sky",
        "source_trajectories_comp_zoom",
    )(serialize_paths)


class FlightPlots(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Plots directory
    directory: pl.Path = pl.Path("Flight")
    # Format to save the plots in
    plot_format: str = "pdf"

    tobs_sources: pl.Path = Field(default=None)
    tobs_priorities: pl.Path = Field(default=None)

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "tobs_sources",
        "tobs_priorities",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "tobs_sources",
        "tobs_priorities",
    )(serialize_paths)


class Plots(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Plots directory
    directory: pl.Path = pl.Path("Plots")

    detector: DetectorPlots = DetectorPlots()
    source_skymaps: SourceSkyPlots = SourceSkyPlots()
    source_trajectories: SourceTrajPlots = SourceTrajPlots()
    flight: FlightPlots = FlightPlots()

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _forward_local_paths = field_validator(
        "detector", "source_skymaps", "source_trajectories", "flight", mode="before"
    )(local_paths)
    _output_paths = field_serializer("directory")(serialize_paths)


class Observations(BaseModel):
    global_path: pl.Path = Field(default=None, exclude=True)
    # Path to Observations directory
    directory: pl.Path = pl.Path("Observations")
    # Path containing information about all sources
    all_file: pl.Path = pl.Path("all_output.json")
    # File holding information about all observable sources
    observable_file: pl.Path = pl.Path("observable_output.json")
    # File holding information about all scheduled sources
    scheduled_file: pl.Path = pl.Path("scheduled_output.json")
    # File holding information about a specific sources
    single_file: pl.Path = pl.Path("single_output.json")
    # File holding information about the next observation periods
    observation_period_file: pl.Path = pl.Path("observation_period_output.csv")
    # NuSpaceSim output file (TSPRPPT: Time Stamped Position Relative Point Source Tensor)
    nss_output_file: pl.Path = pl.Path("TSPRPST.h5")
    # Path to file containing the schedule
    schedule_file: pl.Path = pl.Path("schedule.csv")

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator(
        "all_file",
        "observable_file",
        "scheduled_file",
        "single_file",
        "observation_period_file",
        "nss_output_file",
        "schedule_file",
        mode="after",
    )(build_file)
    _output_paths = field_serializer(
        "directory",
        "all_file",
        "observable_file",
        "scheduled_file",
        "single_file",
        "observation_period_file",
        "nss_output_file",
        "schedule_file",
    )(serialize_paths)


class Output(BaseModel):
    # Path to directory containing all data files
    global_path: pl.Path = pl.Path("./")
    # Path to Output directory
    directory: pl.Path = pl.Path("Output")
    # Path to config file used for the run
    config_file: pl.Path = pl.Path("config.toml")
    # Path to log file
    log_file: pl.Path = pl.Path("log.log")
    # Path to directory containing all data files for previous observation
    previous_observation_path: pl.Path = pl.Path("2023-05-13/")

    plots: Plots = Plots()
    observations: Observations = Observations()

    _build_dir = field_validator("directory", mode="after")(build_dir)
    _build_file = field_validator("config_file", "log_file", mode="after")(build_file)
    _forward_local_paths = field_validator("plots", "observations", mode="before")(
        local_paths
    )

    _output_paths = field_serializer(
        "global_path",
        "directory",
        "config_file",
        "log_file",
        "previous_observation_path",
    )(serialize_paths)
