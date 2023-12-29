import typing

import pandas as pd

import src.elements.parameters as pr
import src.elements.service as sr

import src.s3.unload


class Read:

    def __init__(self, service: sr.Service, parameters: pr.Parameters):
        """

        :param service:
        :param parameters:
        """

        self.__service: sr.Service = service
        self.__parameters: pr.Parameters = parameters

        # S3 Unload Instance
        self.__unload = src.s3.unload.Unload(service=self.__service)

    def __read(self, filename: str) -> pd.DataFrame:
        """

        :param filename:
        :return:
        """

        key_name = f'{self.__parameters.references_}{filename}'
        buffer = self.__unload.exc(key_name=key_name)

        try:
            return pd.read_csv(filepath_or_buffer=buffer, header=0, encoding='utf-8')
        except ImportError as err:
            raise Exception(err) from err

    def exc(self) -> typing.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """

        :return:
          registry: DataFrame
          stations: DataFrame
          substances: DataFrame
        """

        registry = self.__read(filename='registry.csv')
        stations = self.__read(filename='stations.csv')
        substances = self.__read(filename='substances.csv')

        return registry, stations, substances
