"""
Module service.py
"""
import os

import boto3
import botocore.client

import src.elements.s3_parameters as s3p
import src.elements.profile as po
import src.elements.service as sr
import src.functions.serial
import src.s3.parameters


class Service:
    """
    Class Service

    Auto-login via IAM Identity Centre Single Sign On; beware of
    machine prerequisite.  Re-visit, vis-à-vis cloud runs.
      * https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html


    A S3 resource service
      * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.\
            html#boto3.session.Session.resource
    """

    def __init__(self, s3_parameters: s3p.S3Parameters, profile: po.Profile):
        """

        :param s3_parameters: The S3 parameters settings for this project
        :param profile: The developer's Amazon Web Services (AWS) profile detail, which allows
                        for programmatic interaction with AWS.
        """

        # Profile
        self.__profile = profile

        # Profile/Auto-login
        # boto3.setup_default_session(profile_name=self.__profile.name)
        connector = boto3.session.Session()
        print(f'name: {connector.profile_name}')

        # The S3 resource, client, etc.
        self.__s3_resource: boto3.session.Session.resource = connector.resource(
            service_name='s3', region_name=s3_parameters.region_name)
        self.__s3_client: boto3.session.Session.client = connector.client(
            service_name='s3', region_name=s3_parameters.region_name)
        self.__secrets_manager = connector.client(
            service_name='secretsmanager', region_name=s3_parameters.region_name)
        self.__glue_client: botocore.client.BaseClient = connector.client(
            service_name='glue', region_name=s3_parameters.region_name)

    def __glue_arn(self) -> str:
        """

        :return:
        """

        # Amazon Resource Name (ARN)
        serial = src.functions.serial.Serial()
        glue_arn: str = serial.get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'arn.yaml'))['arn']['glue']

        return glue_arn.format(account_id=self.__profile.account_id)

    def exc(self) -> src.elements.service.Service:
        """

        :return:
            A collection of Amazon S3 (Simple Storage Service) services
        """

        # Hence, the collection
        return src.elements.service.Service(s3_resource=self.__s3_resource,
                                            s3_client=self.__s3_client,
                                            secrets_manager=self.__secrets_manager,
                                            glue_client=self.__glue_client,
                                            glue_arn=self.__glue_arn())
