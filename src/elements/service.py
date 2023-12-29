"""
This is the data type Interface
"""

import typing

import boto3

import src.elements.parameters


class Service(typing.NamedTuple):
    """
    The data type class -> Service
    """

    s3_resource: boto3.session.Session.resource
    s3_client: boto3.session.Session.client
