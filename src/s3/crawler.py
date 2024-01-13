"""
Module crawler.py
"""
import logging
import os

import boto3
import botocore.client
import botocore.exceptions

import src.elements.glue_parameters as gp
import src.elements.parameters as pr
import src.elements.profile as po
import src.functions.serial


class Crawler:
    """
    Class Crawler

    In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, parameters: pr.Parameters, profile: po.Profile):
        """

        :param parameters:
        :param profile:
        """

        self.__serial = src.functions.serial.Serial()

        # Amazon S3 (Simple Storage Service) parameters
        self.__parameters = parameters

        # Profile/Auto-login
        boto3.setup_default_session(profile_name=profile.name)
        self.__glue_client: botocore.client.BaseClient = boto3.client(
            service_name='glue', region_name=self.__parameters.region_name)

        # Crawler Parameters
        dictionary: dict = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'project', 'glue.yaml'))[
            'parameters']
        self.__glue_parameters: gp.GlueParameters = gp.GlueParameters(**dictionary)

        # Amazon Resource Name (ARN)
        self.__glue_arn: str = self.__get_dictionary(uri=os.path.join(os.getcwd(), 'resources', 'arn.yaml'))['arn']['glue']
        self.__glue_arn: str = self.__glue_arn.format(account_id=profile.account_id)

    def __get_dictionary(self, uri: str) -> dict:
        """

        :param uri:
        :return:
        """

        return self.__serial.get_dictionary(uri=uri)

    def create_crawler(self):
        """

        :return:
        """

        try:
            return self.__glue_client.create_crawler(
                Name=self.__glue_parameters.crawler_name,
                Role=self.__glue_arn,
                DatabaseName=self.__glue_parameters.database_name,
                Description=self.__glue_parameters.description,
                Targets={'S3Targets': [
                    {
                        'Path': f's3://{self.__parameters.bucket_name}'
                    },
                ]},
                TablePrefix=self.__glue_parameters.table_prefix,
                Schedule=self.__glue_parameters.schedule
            )
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def start_crawler(self):
        """

        :return:
        """

        try:
            self.__glue_client.start_crawler(Name=self.__glue_parameters.crawler_name)
            logging.log(level=logging.INFO, msg='The glue crawler is now running ...')
        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is already running ...')
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def delete_crawler(self, name: str):
        """

        :param name:
        :return:
        """

        try:
            self.__glue_client.delete_crawler(Name=name)
            return True
        except self.__glue_client.exceptions.EntityNotFoundException:
            return True
        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is running ...')
            return False
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err
