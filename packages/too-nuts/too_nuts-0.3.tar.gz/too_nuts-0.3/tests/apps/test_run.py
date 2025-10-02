from pathlib import Path

import pytest

from nuts.compute import Compute
from nuts.config.config import ToOConfig


@pytest.fixture
def temp_output_dir(tmp_path):
    temp_dir = tmp_path / "Tests"
    temp_dir.mkdir()
    return temp_dir


@pytest.fixture
def temp_output_config(config: ToOConfig, temp_output_dir: Path):
    config.output.directory = temp_output_dir
    config.output.config_file = temp_output_dir / "config.toml"
    config.output.log_file = temp_output_dir / "log.log"
    config.output.previous_observation_path = "2023-05-13"
    config.output.plots.directory = temp_output_dir / "Plots"
    config.output.plots.directory.mkdir()
    config.output.plots.detector.directory = temp_output_dir / "Plots/Detector"
    config.output.plots.detector.directory.mkdir()
    config.output.plots.detector.detector_location_mollweide = (
        temp_output_dir / "Plots/Detector/Detector_location_mollweide"
    )
    config.output.plots.detector.detector_location_hammer = (
        temp_output_dir / "Plots/Detector/Detector_map_hammer"
    )
    config.output.plots.detector.detector_location_aeqd = (
        temp_output_dir / "Plots/Detector/Detector_map_aeqd"
    )

    config.output.plots.source_skymaps.directory = (
        temp_output_dir / "Plots/Source_Skymaps"
    )
    config.output.plots.source_skymaps.directory.mkdir()
    config.output.plots.source_skymaps.skymap_none = (
        temp_output_dir / "Plots/Source_Skymaps/Sky_observable"
    )
    config.output.plots.source_skymaps.skymap_all = (
        temp_output_dir / "Plots/Source_Skymaps/Sources_all"
    )
    config.output.plots.source_skymaps.skymap_obs = (
        temp_output_dir / "Plots/Source_Skymaps/Sources_observable"
    )
    config.output.plots.source_skymaps.skymap_sched = (
        temp_output_dir / "Plots/Source_Skymaps/Sources_scheduled"
    )
    config.output.plots.source_skymaps.skymap_comp = (
        temp_output_dir / "Plots/Source_Skymaps/Sources_comp"
    )

    config.output.plots.source_trajectories.directory = (
        temp_output_dir / "Plots/Source_Trajectories"
    )
    config.output.plots.source_trajectories.directory.mkdir()
    config.output.plots.source_trajectories.source_trajectories_full_sky = (
        temp_output_dir / "Plots/Source_Trajectories/Traj_all"
    )
    config.output.plots.source_trajectories.source_trajectories_zoom = (
        temp_output_dir / "Plots/Source_Trajectories/Traj_fov"
    )
    config.output.plots.source_trajectories.source_trajectories_comp_full_sky = (
        temp_output_dir / "Plots/Source_Trajectories/Traj_Scheduled_all"
    )
    config.output.plots.source_trajectories.source_trajectories_comp_zoom = (
        temp_output_dir / "Plots/Source_Trajectories/Traj_Scheduled_fov"
    )

    config.output.observations.directory = temp_output_dir / "Observations"
    config.output.observations.directory.mkdir()
    config.output.observations.all_file = (
        temp_output_dir / "Observations/all_output.json"
    )
    config.output.observations.observable_file = (
        temp_output_dir / "Observations/observable_output.json"
    )
    config.output.observations.scheduled_file = (
        temp_output_dir / "Observations/scheduled_output.json"
    )
    config.output.observations.single_file = (
        temp_output_dir / "Observations/single_output.json"
    )
    config.output.observations.observation_period_file = (
        temp_output_dir / "Observations/observation_period_output.csv"
    )

    return config


# @pytest.fixture
# def short_database_config(temp_output_config: ToOConfig):
#    temp_output_config.files.database.cleaned = (
#        temp_output_config.output.directory / "Full_short.csv"
#    )
#    return temp_output_config


@pytest.fixture
def short_database_config(temp_output_config: ToOConfig):
    temp_output_config.files.database.cleaned = (
        temp_output_config.files.database.directory / "Full_short.csv"
    )
    return temp_output_config


def test_all(short_database_config: ToOConfig):
    print(short_database_config.output.directory)
    print(short_database_config.settings.calculation.start_time)
    print(short_database_config.settings.observation.lower_fov_cut)
    print(short_database_config.output.log_file)
    print(short_database_config.files.database.directory)
    print(short_database_config.files.database.cleaned)
    # Assert directories exist
    assert short_database_config.output.directory.exists()
    assert short_database_config.output.plots.directory.exists()

    # Run NuTS
    option = "obs_sched"
    compute = Compute(short_database_config)
    compute(option)

    # Assert all plot directories are not empty
    assert (
        len(list(short_database_config.output.plots.detector.directory.iterdir())) > 0
    )
    assert (
        len(
            list(
                (
                    short_database_config.output.plots.source_trajectories.directory
                ).iterdir()
            )
        )
        > 0
    )

    # list of source plots
    source_plots = [
        "Sky_observable_fov_Equatorial_0.pdf",
        "Sky_observable_fov_Galactic_0.pdf",
        "Sky_observable_sun_Equatorial_0.pdf",
        "Sky_observable_sun_Galactic_0.pdf",
        "Sky_observable_sun_moon_Equatorial_0.pdf",
        "Sky_observable_sun_moon_Galactic_0.pdf",
        "Sources_all_Equatorial_0.pdf",
        "Sources_all_Galactic_0.pdf",
        "Sources_observable_Equatorial_0.pdf",
        "Sources_observable_Galactic_0.pdf",
        "Sources_scheduled_Equatorial_0.pdf",
        "Sources_scheduled_Galactic_0.pdf",
        "Sources_comp_Equatorial_0.pdf",
        "Sources_comp_Galactic_0.pdf",
    ]
    for plot in source_plots:
        assert (
            short_database_config.output.plots.source_skymaps.directory / plot
        ).exists()

    # list of detector plots
    detector_plots = [
        "Detector_location_mollweide_0.pdf",
        "Detector_map_aeqd_0.pdf",
        "Detector_map_hammer_0.pdf",
    ]
    for plot in detector_plots:
        print(short_database_config.output.plots.detector.directory / plot)
        assert (short_database_config.output.plots.detector.directory / plot).exists()
