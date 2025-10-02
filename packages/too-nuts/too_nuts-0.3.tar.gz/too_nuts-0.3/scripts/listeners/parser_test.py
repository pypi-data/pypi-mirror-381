#!/usr/bin/python
import logging
import os
import sys
import time as t

from nuts.config.config import ToOConfig
from nuts.config.load_config import ParseConfig
from nuts.IO_funcs.too_database import DataBaseIO
from nuts.parser import GCN_listener


def main(config: ToOConfig):
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG
    )

    database = DataBaseIO("./GCN.csv")
    database.read()

    # Initialize listener script
    listener = GCN_listener.GCN_listener(config)

    alert_file = "./GCN_Alerts/"
    dir_files = os.listdir(alert_file)
    for file in dir_files:
        print(file)
        print(alert_file + file)
        too_event = listener.parse_alert(alert_file + file)
        database.add_event(too_event)

    database.write()


if __name__ == "__main__":
    config_path = sys.argv[1]
    config_parser = ParseConfig(config_path)
    main(config_parser.config)
