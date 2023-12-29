import logging
import typing

import pandas as pd

import src.elements.parameters as pr
import src.elements.service as sr
import src.references.registry
import src.references.stations
import src.references.substances
import src.s3.upload


class Regenerate:

    def __init__(self, service: sr.Service, parameters: pr.Parameters):
        """

        :param service:
        :param parameters:
        """

        self.__service: sr.Service = service
        self.__parameters: pr.Parameters = parameters

        # S3 Upload Instance
        self.__upload = src.s3.upload.Upload(service=self.__service)

    def __registry(self) -> pd.DataFrame:
        """

        :return:
        """

        key_name = f'{self.__parameters.references_}registry.csv'
        data, metadata = src.references.registry.Registry().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def __stations(self) -> pd.DataFrame:
        """

        :return:
        """

        key_name = f'{self.__parameters.references_}stations.csv'
        data, metadata = src.references.stations.Stations().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def __substances(self) -> pd.DataFrame:
        key_name = f'{self.__parameters.references_}substances.csv'
        data, metadata = src.references.substances.Substances().exc()
        self.__upload.bytes(data=data, metadata=metadata, key_name=key_name)

        return data

    def exc(self) -> typing.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """

        :return:
          registry: DataFrame
          stations: DataFrame
          substances: DataFrame
        """

        registry: pd.DataFrame = self.__registry()
        stations: pd.DataFrame = self.__stations()
        substances: pd.DataFrame = self.__substances()

        return registry, stations, substances
