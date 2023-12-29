"""
Module objects.py
"""
import logging
import boto3

import src.elements.parameters as pr
import src.elements.service as sr


class Objects:
    """
    Class Objects

    Will list all the S3 objects associated with this machine's active AWS CLI profile
    """

    def __init__(self, service: sr.Service, parameters: pr.Parameters):
        """
        Constructor
        """

        self.__parameters: pr.Parameters = parameters
        self.__s3_resource: boto3.session.Session.resource = service.s3_resource
        self.__bucket = self.__s3_resource.Bucket(name=self.__parameters.bucket_name)

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def filter(self, prefix: str):

        items = list(self.__bucket.objects.filter(Prefix=prefix))
        self.__logger.info(items)

        return len(items)

    def all(self):
        """

        :return:
        """

        items = list(self.__bucket.objects.all())
        self.__logger.info(items)

        return len(items)
