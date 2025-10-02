import pytest

from nuts.apps.init import init
from nuts.apps.make_config import build_make_config


def test_make_config(tmp_path):

    # Arrange
    temp_dir = tmp_path / "Tests"
    temp_dir.mkdir()

    catalogs_dir = temp_dir / "Catalogs"

    temp_file = temp_dir / "config.toml"

    # Act
    build_make_config(temp_file, str(catalogs_dir))

    # Assert
    # Check if the file was created
    assert temp_file.exists()

    # Ensure the file is not empty
    assert temp_file.stat().st_size > 0
