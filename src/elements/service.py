"""
This is the data type Interface
"""

import typing

import boto3
import botocore.client


class Service(typing.NamedTuple):
    """
    The data type class -> Service

    Attributes
    ----------
    s3_resource: boto3.session.Session.resource
        The boto3.resource instance, with service & region name settings.
    s3_client: boto3.session.Session.client
        The boto3.client instance, with service & region name settings.
    """

    s3_resource: boto3.session.Session.resource
    s3_client: boto3.session.Session.client
    glue_client: botocore.client.BaseClient
    glue_arn: str
