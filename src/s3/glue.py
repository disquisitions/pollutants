"""
Module glue.py
"""
import boto3
import os

import src.functions.serial
import src.elements.glue_parameters as gp


class Glue:
    """
    Class Glue
    """

    def __init__(self):
        """
        Constructor

        In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
        """

        self.__serial = src.functions.serial.Serial()

    def __get_dictionary(self, uri: str) -> dict:
        """

        :param uri:
        :return:
        """

        return  self.__serial.get_dictionary(uri=uri)

    def exc(self):

        # Glue Parameters
        dictionary: dict = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'project', 'glue.yaml'))[
            'parameters']
        glue_parameters: gp.GlueParameters = gp.GlueParameters(**dictionary)

        # Amazon Resource Name (ARN)
        glue_arn: str = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'arn.yaml'))['arn']['glue']

        # Create a glue YAML for database, table, crawler, etc., names
        boto3.client('glue').create_crawler(
            Name=glue_parameters.crawler_name,
            Role=glue_arn,
            DatabaseName=glue_parameters.database_name,
            Description=glue_parameters.description,
            Targets={'S3Targets': [
                {
                    'Path': ''
                },
            ]},
            TablePrefix=glue_parameters.table_prefix
        )
