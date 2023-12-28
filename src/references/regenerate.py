
import logging

import pandas as pd

import src.elements.parameters
import src.elements.service
import src.references.registry
import src.references.stations
import src.references.substances
import src.s3.upload


class Regenerate:

    def __init__(self, service: src.elements.service.Service):
        """

        :param service:
        """

        self.__service = service

        # Amazon S3 Settings & Interactions Instances
        self.__parameters: src.elements.parameters.Parameters = self.__service.parameters
        self.__upload = src.s3.upload.Upload(service=self.__service)

    def __registry(self) -> pd.DataFrame:
        """

        :return:
        """

        key_name = f'{self.__parameters.references_}registry.csv'

        data: pd.DataFrame
        metadata: dict
        data, metadata = src.references.registry.Registry().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def __stations(self) -> pd.DataFrame:
        """

        :return:
        """

        key_name = f'{self.__parameters.references_}stations.csv'

        data: pd.DataFrame
        metadata: dict
        data, metadata = src.references.stations.Stations().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def __substances(self) -> pd.DataFrame:

        key_name = f'{self.__parameters.references_}substances.csv'

        data: pd.DataFrame
        metadata: dict
        data, metadata = src.references.substances.Substances().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def exc(self) -> (pd.DataFrame, pd.DataFrame, pd.DataFrame):

        registry: pd.DataFrame = self.__registry()
        stations: pd.DataFrame = self.__stations()
        substances: pd.DataFrame = self.__substances()

        return registry, stations, substances
