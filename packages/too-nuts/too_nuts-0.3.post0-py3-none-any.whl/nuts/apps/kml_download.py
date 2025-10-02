import click

from nuts.config.load_config import load_config
from nuts.IO_funcs.get_kml import get_kml_file


@click.command()
@click.argument("config_path", type=click.Path(exists=True))
def get_kml(config_path: str):
    build_get_kml(config_path)


def build_get_kml(config_path: str) -> None:
    """Download kml file from URL given in config."""
    config = load_config(config_path)
    get_kml_file(config)
    return None
