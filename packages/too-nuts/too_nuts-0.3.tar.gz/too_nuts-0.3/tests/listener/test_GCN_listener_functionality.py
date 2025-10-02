"""Test module for the listener/GCN_listener.py module.
original author: Tobias Heibges
email: theibges@mines.edu
last edit by: Tobias Heibges
email: theibges@mines.edu
date: 2024-01-08
"""

import pathlib
import time as t

import pytest

from nuts.alert_listeners import GCN_listener
from nuts.config.config import ToOConfig

####################################################################################################
# Fixtures
####################################################################################################


# def test_run_GCN(config: ToOConfig):
#     """Test run of GCN listener

#     Assumption: First two returned alerts are status messages and are not saved

#     Args:
#         config (fixture): loads config file
#     """

#     gcn_listener = GCN_listener.GCN_listener(config)
#     alert_file = gcn_listener()
#     assert alert_file is None
