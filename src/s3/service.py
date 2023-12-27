"""
Module entities.py
"""
import logging

import boto3

import src.elements.parameters
import src.elements.service
import src.s3.parameters
import src.functions.profile


class Service:
    """
    Via resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.\
                html#boto3.session.Session.resource
           *
    """

    def __init__(self):
        """
        Re-visit profile in relation to cloud runs.

        """

        # Auto-login via IAM Identity Centre Single Sign On; beware of machine prerequisite.
        # https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html
        profile = src.functions.profile.Profile().exc()
        boto3.setup_default_session(profile_name=profile)

        # The parameters and the S3 resource
        self.__parameters: src.elements.parameters.Parameters = src.s3.parameters.Parameters().exc()
        self.__s3_resource = boto3.resource(service_name='s3', region_name=self.__parameters.region_name)

        # Hence, the collection
        self.service = src.elements.service.Service(
            parameters=self.__parameters, s3_resource=self.__s3_resource)
