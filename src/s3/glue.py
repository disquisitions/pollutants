"""
Module glue.py
"""
import logging
import os

import boto3
import botocore.client
import botocore.exceptions

import src.elements.glue_parameters as gp
import src.elements.parameters as pr
import src.functions.serial


class Glue:
    """
    Class Glue
    """

    def __init__(self, parameters: pr.Parameters):
        """
        Constructor

        In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
        """

        self.__serial = src.functions.serial.Serial()

        # Amazon S3 (Simple Storage Service) parameters
        self.__parameters = parameters

        # Glue Parameters
        dictionary: dict = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'project', 'glue.yaml'))[
            'parameters']
        self.__glue_parameters: gp.GlueParameters = gp.GlueParameters(**dictionary)

        # Amazon Resource Name (ARN)
        self.__glue_arn: str = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'arn.yaml'))['arn']['glue']

    def __get_dictionary(self, uri: str) -> dict:
        """

        :param uri:
        :return:
        """

        return self.__serial.get_dictionary(uri=uri)

    def __create_crawler(self, glue_client):
        """

        :param glue_client:
        :return:
        """

        try:
            glue_client.create_crawler(
                Name=self.__glue_parameters.crawler_name,
                Role=self.__glue_arn,
                DatabaseName=self.__glue_parameters.database_name,
                Description=self.__glue_parameters.description,
                Targets={'S3Targets': [
                    {
                        'Path': f's3://{self.__parameters.bucket_name}'
                    },
                ]},
                TablePrefix=self.__glue_parameters.table_prefix
            )
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def __start_crawler(self, glue_client):
        """

        :param glue_client:
        :return:
        """

        try:
            glue_client.start_crawler(Name=self.__glue_parameters.crawler_name)
            logging.log(level=logging.INFO, msg='The glue crawler is now running ...')
        except glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is already running ...')
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def exc(self):

        # Create a glue YAML for database, table, crawler, etc., names
        glue_client: botocore.client.BaseClient = boto3.client('glue')
        glue_client = self.__create_crawler(glue_client=glue_client)
        self.__start_crawler(glue_client=glue_client)
