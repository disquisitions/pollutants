#!/bin/bash

: << 'environment'
The environment in focus
environment
prefix=/opt/miniconda3/envs/climate

: << 'delete'
Delete the existing <climate> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
Rebuild environment <climate> via a requirements.txt file
rebuild
conda create -y --prefix $prefix  python==3.11.7
conda install -y --prefix $prefix -c anaconda --file requirements.txt
