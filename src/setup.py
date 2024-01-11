import logging

import src.elements.parameters as pr
import src.elements.service as sr
import src.s3.bucket
import src.s3.objects

import src.functions.directories


class Setup:

    def __init__(self, service: sr.Service, parameters: pr.Parameters, warehouse: str):
        """
        
        :param service:
        :param parameters:
        :param warehouse:
        """

        self.__service: sr.Service = service
        self.__parameters: pr.Parameters = parameters
        self.__warehouse = warehouse

        # An instance for dealing with local directories
        self.__directories = src.functions.directories.Directories()

        # An instance for dealing with the project's Amazon S3 bucket
        self.__bucket = src.s3.bucket.Bucket(
            service=self.__service, parameters=self.__parameters)
        self.__objects = src.s3.objects.Objects(
            service=self.__service, parameters=self.__parameters)

        # logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __setup(self, restart: bool) -> bool:
        """

        :param restart:
        :return:
        """

        if self.__bucket.exists() & self.__objects.prefix_exist(self.__parameters.references_):
            n_references = self.__objects.filter(prefix=self.__parameters.references_)
        else:
            n_references = 0
        self.__logger.info('There are %s reference documents within Amazon S3', n_references)

        # Ascertaining the states of depositories
        if not self.__bucket.exists():
            self.__bucket.create()
            self.__directories.cleanup(path=self.__warehouse)
            state = True
        elif (n_references != self.__parameters.n_references) | restart:
            self.__bucket.empty()
            self.__directories.cleanup(path=self.__warehouse)
            state = True
        else:
            state = restart

        return state

    def exc(self, restart: bool) -> bool:
        """

        :param restart:
        :return:
        """

        return self.__setup(restart=restart)
