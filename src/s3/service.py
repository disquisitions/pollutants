"""
Module entities.py
"""
import logging

import boto3

import src.elements.parameters
import src.s3.parameters
import src.functions.profile


class Service:

    def __init__(self):
        """
        Re-visit profile in relation to cloud runs.

        """

        # Auto-login via IAM Identity Centre Single Sign On; beware of machine prerequisite.
        # https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html
        profile = src.functions.profile.Profile().exc()
        boto3.setup_default_session(profile_name=profile)

        # The parameters
        self.__parameters: src.elements.parameters.Parameters = src.s3.parameters.Parameters().exc()

        # The S3 resource
        self.__s3_resource = boto3.resource(service_name='s3', region_name=self.__parameters.region_name)

    def parameters(self) -> src.elements.parameters.Parameters:
        """

        :return:
        """

        return self.__parameters

    def resource(self):
        """

        :return:
        """

        return self.__s3_resource
