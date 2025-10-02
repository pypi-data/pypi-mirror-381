r""" Retrieving kml file

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: get_kml_file

"""

import logging
import pathlib as pl

import astropy.time as atime
import requests

from ..config.config import ToOConfig


def get_kml_file(
    config: ToOConfig,
) -> str:
    """Function to automatically download the newest kml file from the CSBF webpage

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Tobias Heibges (theibges@mines.edu)
    :Date: 2023-01-08

    Args:
        config (ToOConfig): Config file with directions on where to save the file
        url (str, optional): URL to download the kml file. Defaults to "https://pinwheel.balloonfacility.org/Trajectory/SPBKML729NT.kml".

    Returns:
        str: path to the newly created kml file
    """
    intime = atime.Time.now().isot
    output_filename = pl.Path(f"balloon_trajectory_{intime}.kml")
    kml_savepath = config.files.kml_dir / output_filename

    kml_file = requests.get(config.settings.detector.kml_url)
    with open(kml_savepath, "wb") as f:
        f.write(kml_file.content)

    logging.info(f"New KML file downloaded: {kml_savepath}")
    return kml_savepath, intime
