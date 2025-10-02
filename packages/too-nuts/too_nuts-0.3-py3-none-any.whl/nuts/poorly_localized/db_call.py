"""Gracedb api call.

https://gracedb.ligo.org
Pulls relevant information for a given GW event, if skymap is found
it will download it for the poorly localized module to use.

original author: Luke Kupari (luke-kupari@uiowa.edu)

.. autofunction:: gracedb_call

"""

import logging

import requests


def gracedb_call(gw_event: str):
    """Calls the gracedb api to get the skymap files for a given event

    Args:
        gw_event (str): name of the event to be searched for

    Returns:
        str: returns the correct url for the skymap file
    """
    logging.info("***************************************************")
    logging.info("Fetching files from GraceDB...")

    url = "https://gracedb.ligo.org/api/superevents/" + gw_event + "/files"
    response = requests.get(url)

    if response.status_code == 200:
        file_dict = response.json()
    else:
        logging.info(f"Failed to fetch files: {response.status_code}")
        return None

    keys = ["cwb.fits.gz", "bayestar.fits.gz", "olib.fits.gz"]

    for key in keys:
        if key in file_dict:
            logging.info(f"Found {key}: {file_dict[key]}")
            return_url = file_dict[key]
            break
    else:
        logging.info(
            "None of the expected keys were found. Available keys: %s",
            list(file_dict.keys()),
        )

    logging.info("***************************************************")
    return return_url
