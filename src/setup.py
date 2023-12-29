
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

    def __setup(self, restart: bool) -> bool:
        """

        :param restart:
        :return:
        """

        n_references = self.__objects.filter(prefix=self.__parameters.references_)

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
