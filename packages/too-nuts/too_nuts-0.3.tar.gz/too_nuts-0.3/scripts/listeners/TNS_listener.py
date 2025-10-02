#!/usr/bin/python
import sys
import time as t

import astropy.units as u

from nuts.config.config import ToOConfig
from nuts.config.load_config import ParseConfig
from nuts.parser import tns_download, tns_parser


def main(config: ToOConfig):
    update_period = config.params.tns.update_period
    while True:
        tns_filename = tns_download.search_tns(config)
        tns_events = tns_parser.read_TNS_table(tns_filename, config.files.tns_file)
        tns_parser.save_list(config, tns_events)
        t.sleep(update_period.to("s").value)


if __name__ == "__main__":
    config_path = sys.argv[1]
    config_parser = ParseConfig(config_path)
    main(config_parser.config)
