"""
Module database.py
"""

import boto3
import botocore.client
import botocore.exceptions

import src.elements.parameters as pr
import src.elements.profile as po


class Database:
    """
    Class Database

    In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_database.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, parameters: pr.Parameters, profile: po.Profile):
        """

        :param parameters:
        :param profile:
        """

        # Amazon S3 (Simple Storage Service) parameters
        self.__parameters = parameters

        # Profile/Auto-login
        boto3.setup_default_session(profile_name=profile.name)
        self.__glue_client: botocore.client.BaseClient = boto3.client(
            service_name='glue', region_name=self.__parameters.region_name)

    def delete_database(self, name: str):
        """

        :param name:
        :return:
        """

        self.__glue_client.delete_database(Name=name)
