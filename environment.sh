#!/bin/bash

: << 'comment'
The set up herein is in line with the Dockerfile set up.  Both use the same
requirements.txt file to create an environment.
comment

# The environment in focus
prefix=/opt/miniconda3/envs/climate

: << 'delete'
  Delete the existing <climate> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <climate> via a requirements.txt file
rebuild
conda create -y --prefix $prefix -c conda-forge  python==3.11.6
conda install -y --prefix $prefix -c conda-forge --file requirements.txt
