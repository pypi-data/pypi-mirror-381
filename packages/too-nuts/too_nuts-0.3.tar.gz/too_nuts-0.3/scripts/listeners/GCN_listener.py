#!/usr/bin/python
import logging
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

    # Initialize listener script
    listener = GCN_listener.GCN_listener(config)

    # Run the listener in an endless loop
    # COMMENT: unsure if this works perfectly, more real time testing required.
    while True:
        alert_file = listener()
        if alert_file is not None:
            too_event = listener.parse_alert(alert_file)
            if too_event is not None:
                GCN_database = DataBaseIO(config.files.db_gcn)
                try:
                    GCN_database.read()
                except FileNotFoundError:
                    print("FILE GCN.csv DOES NOT EXIST. CREATE FILE.")
                GCN_database.add_event(too_event)
                GCN_database.write()
        t.sleep(2)


if __name__ == "__main__":
    config_path = sys.argv[1]
    config_parser = ParseConfig(config_path)
    main(config_parser.config)
