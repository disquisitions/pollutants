<br>

**Pollutants**

<br>

## Upcoming

Automation:

* From local machine to GitHub to Amazon Elastic Container Registry (Via GitHub Actions) .  This requires a few more settings 
  * [Open Identity](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services); also study the [news of changes](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions#oidc)
  * Re-visit the [old approach](https://towardsaws.com/build-push-docker-image-to-aws-ecr-using-github-actions-8396888a8f9e), and 
   the approach used for the planets project.  In relation the new approach [study this example](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html), which is infeasible because Terraform is not an open source product anymore.
* Amazon Glue & Data Catalogues
* Code Analysis & GitHub Actions

Usage Notes:

* Explanatory usage notes
* Resources files

Mathematics:

* [Manifolds](https://scikit-learn.org/stable/modules/manifold.html)

<br>

## Explanatory Notes

To delete an Amazon Glue Crawler

> ```shell
> python src/glue/delete/main.py {item} {instance}
> ``` 

wherein {item} is an Amazon Glue item, at present {item} = <span style="color: #722f37">crawler</span> or <span style="color: #722f37">database</span>, and {instance} is the name of a crawler or a database. 



<br>

## Remote & Local Environments

### Remote

Development within a container.  The environment's image is built via

```shell
docker build -t pollutants .
```

which names the new image `pollutants`.  Subsequently, use a container/instance of the image `pollutants` as a development environment via the command


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
> &nbsp; &nbsp; type=bind,src="$(pwd)",target=/app pollutants

wherein   `-p 10000:8888` maps the host port `1000` to container port `8888`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  Get the name of the running instance ``pollutants`` via

```shell
docker ps --all
```

A developer may attach an IDE (independent development environment) application to a running container.  In the case of IntelliJ IDEA

> Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** `operating system`
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

Similarly, Visual Studio Code as its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).

### Local

Beforehand update the `base` **`conda`** environment

```shell
conda update -n base -c anaconda conda
```

The local virtual environment can be built via **environment.yml**

```shell
conda env create --file environment.yml -p /opt/miniconda3/envs/pollutants
```

which uses the same **requirements.txt** as Dockerfile.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
