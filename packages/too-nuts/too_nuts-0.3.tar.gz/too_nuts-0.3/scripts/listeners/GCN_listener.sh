#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate too

until python3 GCN_listener.py config.yml; do
    echo "GCN Listener crashed with exit code $?.  Respawning.." >&2
    sleep 1
done
