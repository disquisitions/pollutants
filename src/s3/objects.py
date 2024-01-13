"""
Module objects.py
"""
import logging
import boto3
import botocore.exceptions

import src.elements.s3_parameters as s3p
import src.elements.service as sr


class Objects:
    """
    Class Objects

    Will list all the S3 objects associated with this machine's active AWS CLI profile
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """
        Constructor
        """

        self.__s3_parameters: s3p.S3Parameters = s3_parameters
        self.__s3_resource: boto3.session.Session.resource = service.s3_resource
        self.__s3_client = service.s3_client
        self.__bucket = self.__s3_resource.Bucket(name=self.__s3_parameters.bucket_name)

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def prefix_exist(self, key: str) -> bool:
        """

        :param key:
        :return:
        """

        try:
            dictionary = self.__s3_client.head_object(Bucket=self.__s3_parameters.bucket_name, Key=key)
            return True if dictionary else False
        except self.__s3_client.exceptions.NoSuchKey:
            return False
        except botocore.exceptions.ClientError:
            return False

    def filter(self, prefix: str) -> int:
        """
        Determines the number of items within a specified folder of the bucket

        :param prefix: The folder
        :return:
            The number of items within a specified folder of the bucket
        """

        items = list(self.__bucket.objects.filter(Prefix=prefix))

        return len(items)

    def all(self) -> int:
        """
        Determines the number of items within the bucket

        :return:
            The number of items within the bucket
        """

        items = list(self.__bucket.objects.all())

        return len(items)
