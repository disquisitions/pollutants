"""
Module setup.py
"""

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.functions.directories
import src.s3.bucket


class Setup:

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """
        
        :param service:
        :param s3_parameters:
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        # An instance for interacting with Amazon S3 buckets.
        bucket = src.s3.bucket.Bucket(
            service=self.__service, s3_parameters=self.__s3_parameters)

        if bucket.exists():
            return bucket.empty()
        else:
            return bucket.create()

    def __local(self) -> bool:
        """

        :return:
        """

        # An instance for interacting with local directories
        directories = src.functions.directories.Directories()

        # The warehouse
        return directories.cleanup(path=self.__configurations.warehouse)

    def exc(self) -> bool:
        """

        :return:
        """

        setup = self.__s3() & self.__local()

        return setup
