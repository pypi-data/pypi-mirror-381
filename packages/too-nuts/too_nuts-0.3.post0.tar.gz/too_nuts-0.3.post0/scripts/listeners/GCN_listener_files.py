#!/usr/bin/python
import logging
import sys
import time as t

from too_parser.config.config import ToOConfig
from too_parser.config.load_config import ParseConfig
from too_parser.IO_funcs.too_database import DataBaseIO
from too_parser.parser import GCN_listener


def main(config: ToOConfig):
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG
    )

    # Initialize listener script
    listener = GCN_listener.GCN_listener(config)

    # Run the listener in an endless loop
    # COMMENT: unsure if this works perfectly, more real time testing required.

    # alert_file = "gcn_alert_text_2023-04-09T02" /00/12.txt"
    # too_event = listener.parse_alert("gcn_alert_text_2023-04-09T02/00/12.txt")
    too_event = listener.parse_alert(
        "/Users/tventers/Work/EUSO-SPB2/ToOSourceList/too-scource-parser/src/too_parser/Catalogs/GCN/gcn_alert_text_2023-04-10T21:54:33.txt"
    )
    # too_event = listener.parse_alert("../../src/too_parser/Catalogs/GCN/gcn_alert_text_2023-04-09T02_00_13.txt")
    print(config.files.db_gcn)
    if too_event is not None:
        GCN_database = DataBaseIO(config.files.db_gcn)
        try:
            GCN_database.read()
        except FileNotFoundError:
            print("FILE GCN.csv DOES NOT EXIST. CREATE FILE.")
        GCN_database.add_event(too_event)
        GCN_database.write()
    t.sleep(2)

    # while True:
    #    alert_file = listener()
    #    if alert_file is not None:
    #        too_event = listener.parse_alert(alert_file)
    #        if too_event is not None:
    #            GCN_database = DataBaseIO(config.files.db_gcn)
    #            try:
    #                GCN_database.read()
    #            except:
    #                print("FILE GCN.csv DOES NOT EXIST. CREATE FILE.")
    #            GCN_database.add_event(too_event)
    #            GCN_database.write()
    #    t.sleep(2)


if __name__ == "__main__":
    config_path = sys.argv[1]
    config_parser = ParseConfig(config_path)
    main(config_parser.config)
