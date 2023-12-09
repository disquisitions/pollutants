#!/bin/bash


conda remove --prefix /opt/miniconda3/envs/climate --all

: << 'yml'
Via an environment.yml file
yml
# conda env create --file environment.yml -p /opt/miniconda3/envs/climate


: << 'requirements'
Via a requirements.txt file
requirements

# Initiate an environment
conda create -y --prefix /opt/miniconda3/envs/climate python==3.11.7

# Install the
conda install -y --prefix /opt/miniconda3/envs/climate -c anaconda --file requirements.txt

# If a package is only available via pip
# conda activate climate
# pip install ... --no-cache-dir
# pip install ... --no-cache-dir
# conda deactivate
