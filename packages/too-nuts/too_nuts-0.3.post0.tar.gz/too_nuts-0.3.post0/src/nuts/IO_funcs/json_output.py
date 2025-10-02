""" Output into a json file

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: save_json_out

"""

import json
import logging


def save_json_out(observations: list[dict], filename: str) -> str:
    """Write observations into a json file in output directory.

    :Author: Tobias Heibges (theibges@mines.edu)
    :Last edit by: Claire Guépin (claire.guepin@lupm.in2p3.fr)
    :Date: 2024-02-01

    Args:
        observations (list[dict]): list of observations
        filepath (str): path to file
        filename (str): Name of file, time of writing the file will be added

    Returns:
        str: full filename
    """
    logging.info(f"Number of sources {len(observations)}")
    json_string = json.dumps(observations)
    with open(filename, "w") as file:
        file.write(json_string)
    logging.info(f"Saved in {filename}")
    return filename
