<br>

**Pollutants**

<br>



## Upcoming

Automate:

* subprocess.run()
  * Use system commands to securely transfer files to Amazon S3; via `aws s3 sync` or `aws s3 cp`, depending on the context.

* From local machine to GitHub to Amazon Elastic Container Registry (Via GitHub Actions) .  This requires a few more settings 
  * [OpenID](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
  * [News of Changes](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions#oidc)
  * [Cf. old approach](https://towardsaws.com/build-push-docker-image-to-aws-ecr-using-github-actions-8396888a8f9e), and 
   the approach used for the planets project.
  * [Cf. a rather different approach](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html),  which is infeasible because Terraform is not an open source product anymore.


## Remote & Local Environments

<br>

### Remote

Development within a container.  The environment's image is built via

```shell
docker build -t pollutants .
```

which names the new image `pollutants`.  Subsequently, use a container/instance of the image `pollutants` as a development environment via the command


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
&nbsp; &nbsp; type=bind,src="$(pwd)",target=/app pollutants

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



<br>

### Local

Building development environments.  Beforehand update the `base` **`conda`** environment

```shell
conda update -n base -c anaconda conda
```

An environment might be built via **environment.yml**

```shell
conda env create --file environment.yml -p /opt/miniconda3/envs/pollutants
```

or via **requirements.txt**

```shell
prefix=/opt/miniconda3/envs/pollutants
conda create -y --prefix $prefix python==3.11.7
conda install -y --prefix $prefix -c anaconda --file requirements.txt
```

In this case, it is quite possible that one or more packages are only available via `pip`, hence the directives

```shell
conda activate pollutants
pip install ... --no-cache-dir
conda deactivate
```

might be necessary.

<br>

## Development

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Subsequently, analyse via

```shell
python -m pylint --rcfile .pylintrc ...
```


<br>

## References

* [Docker Official Images: Python](https://hub.docker.com/_/python/)
* [Image Comparisons](https://pythonspeed.com/articles/base-image-python-docker-images/)
* [`man` reference](https://linux.die.net)
* [NumFocus Sponsored Projects](https://numfocus.org/sponsored-projects)
  * [pandas](https://pandas.pydata.org)
* Amazon Web Services
  * [Get started with Amazon S3 buckets and objects using an AWS SDK](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_Scenario_GettingStarted_section.html)
  * [Getting IAM Identity Center user credentials for the AWS CLI or AWS SDKs](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html)
  * [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)
  * [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)
  * [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
  * [Using temporary security credentials with the AWS SDKs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk)
  * [Switching to an IAM role (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html)

  * [AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html)
  * [Regional and Zonal Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html)
  * [Configuring Tokens](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso)

<br>

## Special

| focus          | resource                                                                                                            | client                                                                                                                      |
|:---------------|:--------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| create         | [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/create.html)          | [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)           |
| delete objects | [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/objects.html) | [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html#) |

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
