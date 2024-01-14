"""
Module database.py
"""

import botocore.client
import botocore.exceptions

import src.elements.service as sr


class Database:
    """
    Class Database

    In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_database.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, service: sr.Service):
        """

        :param service: A suite of services for interacting with Amazon Web Services
        """

        # Glue Client
        self.__glue_client: botocore.client.BaseClient = service.glue_client

    def delete_database(self, name: str):
        """

        :param name:
        :return:
        """

        self.__glue_client.delete_database(Name=name)
