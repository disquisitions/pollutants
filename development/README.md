<br>

Notes

<br>

## Development Notes

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Subsequently, analyse via

```shell
python -m pylint --rcfile .pylintrc ...
```


### Snippets

Determining the operating system/platform $\ldots$

```python
import logging
import os
import platform

# Environment
logging.log(level=logging.INFO, msg=f'Operating System Name (posix or nt): {os.name}')
logging.log(level=logging.INFO, msg=f'Platform: {platform.system()}')
```


### References

* [Docker Official Images: Python](https://hub.docker.com/_/python/)
  * [A production set-up example](https://github.com/discourses/augmentation/blob/master/Dockerfile)
* [Image Comparisons](https://pythonspeed.com/articles/base-image-python-docker-images/)
* [`man` reference](https://linux.die.net)
* [NumFocus Sponsored Projects](https://numfocus.org/sponsored-projects)
  * [pandas](https://pandas.pydata.org)

* Amazon Web Services
  * [Getting IAM Identity Center user credentials for the AWS CLI or AWS SDKs](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html)
  * [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)
  * [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)
  * [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
  * [Using temporary security credentials with the AWS SDKs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk)
  * [Switching to an IAM role (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html)
  * [AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html)
  * [Regional and Zonal Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html)
  * [Configuring Tokens](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso)

* Amazon S3 (Simple Storage Service)
  * [Get started with Amazon S3 buckets and objects using an AWS SDK](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_Scenario_GettingStarted_section.html)
  * Cf. [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/create.html) & [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)
  * Cf. [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/objects.html) & [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html#)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
