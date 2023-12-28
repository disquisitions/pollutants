"""
This is the data type Interface
"""

import typing

import boto3

import src.elements.parameters


class Service(typing.NamedTuple):
    """
    The data type class Interface
    """

    parameters: src.elements.parameters
    s3_resource: boto3.resource
