"""
Module objects.py
"""
import logging
import boto3

import src.elements.parameters
import src.elements.service


class Objects:
    """
    Class Objects

    Will list all the S3 objects associated with this machine's active AWS CLI profile
    """

    def __init__(self, service: src.elements.service.Service):
        """
        Constructor
        """

        self.__parameters: src.elements.parameters.Parameters = service.parameters
        self.__s3_resource: boto3.session.Session.resource = service.s3_resource
        self.__bucket = self.__s3_resource.Bucket(name=self.__parameters.bucket_name)

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def filter(self, prefix: str):

        items = list(self.__bucket.objects.filter(Prefix=prefix))

        return len(items)

    def all(self):
        """

        :return:
        """

        items = list(self.__bucket.objects.all())

        return len(items)
