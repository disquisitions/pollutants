#!/bin/bash

# Update conda
conda update -n base -c anaconda conda

# The environment in focus
prefix=/opt/miniconda3/envs/climate

: << 'delete'
  Delete the existing <climate> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <climate> via a requirements.txt file
rebuild
conda create -y --prefix $prefix  python>=3.11
conda install -y --prefix $prefix -c anaconda --file requirements.txt
