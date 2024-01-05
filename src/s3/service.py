"""
Module service.py
"""

import boto3

import src.elements.profile as po
import src.elements.parameters as pr
import src.elements.service as sr
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

    def __init__(self, parameters: pr.Parameters, profile: po.Profile):
        """

        :param parameters: The S3 parameters settings for this project
        :param profile: The developer's Amazon Web Services Profile
        """

        self.__parameters: pr.Parameters = parameters

        # Profile/Auto-login
        boto3.setup_default_session(profile_name=profile.name)

        # The S3 resource, client, etc.
        self.__s3_resource: boto3.session.Session.resource = boto3.resource(
            service_name='s3', region_name=self.__parameters.region_name)
        self.__s3_client: boto3.session.Session.client = boto3.client(
            service_name='s3', region_name=self.__parameters.region_name)

    def exc(self) -> src.elements.service.Service:
        """

        :return:
        """

        # Hence, the collection
        return src.elements.service.Service(s3_resource=self.__s3_resource, s3_client=self.__s3_client)
