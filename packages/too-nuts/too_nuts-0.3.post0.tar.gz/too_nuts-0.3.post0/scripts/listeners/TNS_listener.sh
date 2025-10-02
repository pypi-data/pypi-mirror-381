#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate too_parser_dev

until python3 TNS_listener.py ../../src/too_parser/config/default_config.toml; do
    echo "TNS Listener crashed with exit code $?.  Respawning.." >&2
    sleep 1
done
