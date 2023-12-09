<br>

Pollutants

<br>

### Remote & Local Environments

Building development environments.  Try

```shell
conda env create --file environment.yml -p /opt/miniconda3/envs/climate
```

or

```shell

# Initiate an environment
prefix=/opt/miniconda3/envs/climate
conda create -y --prefix $prefix python==3.11.7
conda install -y --prefix $prefix -c anaconda --file requirements.txt

# It is quite possible that one or more packages are only available via `pip`, hence the succeeding
# lines
conda activate climate
pip install ... --no-cache-dir
pip install ... --no-cache-dir
conda deactivate
```

<br>

### References

* [Docker Official Images: Python](https://hub.docker.com/_/python/)
* [Image Comparisons](https://pythonspeed.com/articles/base-image-python-docker-images/)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
