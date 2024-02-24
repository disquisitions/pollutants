"""
Module setup.py
"""

import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.bucket
import src.s3.objects

import src.functions.directories


class Setup:

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters, warehouse: str):
        """
        
        :param service:
        :param s3_parameters:
        :param warehouse:
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters
        self.__warehouse = warehouse

        # An instance for dealing with local directories
        self.__directories = src.functions.directories.Directories()

        # An instance for dealing with the project's Amazon S3 bucket
        self.__bucket = src.s3.bucket.Bucket(
            service=self.__service, s3_parameters=self.__s3_parameters)

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        if self.__bucket.exists():
            return self.__bucket.empty()
        else:
            return self.__bucket.create()

    def __local(self) -> bool:
        """

        :return:
        """

        # The warehouse
        return self.__directories.cleanup(path=self.__warehouse)

    def exc(self) -> bool:
        """

        :return:
        """

        setup = self.__s3() & self.__local()

        return setup
