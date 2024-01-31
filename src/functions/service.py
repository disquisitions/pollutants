"""
Module service.py
"""

import boto3

import src.elements.s3_parameters as s3p
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

    def __init__(self):
        """
        The constructor.
        """

        # Profile/Auto-login
        # This session will retrieve the developer's <default> Amazon Web Services (AWS) profile
        # details, which allows for programmatic interaction with AWS.
        connector = boto3.session.Session()

        # The S3 resource, client, etc.
        self.__s3_resource: boto3.session.Session.resource = connector.resource(
            service_name='s3')
        self.__s3_client: boto3.session.Session.client = connector.client(
            service_name='s3')
        self.__secrets_manager = connector.client(
            service_name='secretsmanager')

    def exc(self) -> src.elements.service.Service:
        """

        :return:
            A collection of Amazon services
        """

        # Hence, the collection
        return src.elements.service.Service(s3_resource=self.__s3_resource,
                                            s3_client=self.__s3_client,
                                            secrets_manager=self.__secrets_manager)
