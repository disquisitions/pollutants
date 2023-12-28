"""Module interface.py"""
import os.path

import pandas as pd

import src.elements.parameters
import src.elements.service
import src.references.registry
import src.references.stations
import src.references.substances
import src.s3.unload
import src.s3.upload


class Interface:
    """
    Class Interface

    Rebuild, or retrieve the Amazon S3 data?  The Amazon S3 aspect is upcoming.
    """

    def __init__(self, service: src.elements.service.Service, restart: bool = False):
        """

        :param service:
        :param restart:
        """

        self.__restart = restart
        self.__service = service

        # Amazon S3 Settings
        self.__parameters: src.elements.parameters.Parameters = self.__service.parameters

        # Amazon S3 interactions instances
        self.__unload = src.s3.unload.Unload(service=self.__service)
        self.__upload = src.s3.upload.Upload(service=self.__service)

    def __stations(self):
        """

        :return:
        """

        if self.__restart:
            data: pd.DataFrame
            metadata: dict
            data, metadata = src.references.stations.Stations().exc()
            self.__upload.bytes(data=data, metadata=metadata, key_name=f'{self.__parameters.references_}stations.csv')
        else:
            data = self.__unload.exc(key_name=f'{self.__parameters.references_}stations.csv')

        return data

    @staticmethod
    def __substances():

        return src.references.substances.Substances().exc()

    @staticmethod
    def __registry():

        src.references.registry.Registry().exc()

    def exc(self) -> None:
        """

        :return:
        """

        self.__registry()
        self.__stations()
        self.__substances()
