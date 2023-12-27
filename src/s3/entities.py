import logging
import boto3

import src.elements.connector
import src.s3.connector
import src.s3.profile


class Entities:

    def __init__(self):
        """

        """

        # Auto-login via IAM Identity Centre Single Sign On; beware of machine prerequisite.
        # https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html
        profile = src.s3.profile.Profile().exc()
        boto3.setup_default_session(profile_name=profile)

        # The parameters
        self.__parameters: src.elements.connector.Connector = src.s3.connector.Connector().exc()
        print(self.__parameters)

        # The S3 resource
        self.__s3_resource = boto3.resource(service_name='s3', region_name=self.__parameters.region_name)

    def parameters(self) -> src.elements.connector.Connector:

        return self.__parameters

    def resource(self):

        return self.__s3_resource
