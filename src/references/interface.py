"""Module interface.py"""
import logging

import pandas as pd

import src.elements.s3_parameters as s3p
import src.elements.sequence as sq
import src.elements.service as sr
import src.references.read
import src.references.regenerate
import config


class Interface:
    """
    Class Interface
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service:
        :param s3_parameters
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters
        self.__hazards: list[int] = config.Config().hazards

    @staticmethod
    def __integrate(registry: pd.DataFrame, stations: pd.DataFrame, substances: pd.DataFrame) -> pd.DataFrame:
        """
        Integrates the frames such that each record has the details of each distinct
        sequence identification code.

        :param registry:
        :param stations:
        :param substances:
        :return:
        """

        frame = registry.merge(stations, how='left', on='station_id')
        frame = frame.copy().merge(
            substances.copy()[['pollutant_id', 'substance', 'notation']], how='left', on='pollutant_id')

        return frame

    def __sequences(self, blob: pd.DataFrame) -> list[sq.Sequence]:
        """

        :param blob:
        :return:
        """

        data = blob.copy()

        # Here
        #  * Exclude records that do not have both coordinate values
        #  * Extract the records in focus
        conditionals = data['longitude'].isna() | data['latitude'].isna()
        excerpt: pd.DataFrame = data.copy().loc[~conditionals, :]
        excerpt = excerpt.copy().loc[excerpt['pollutant_id'].isin(self.__hazards), :]

        # Structuring
        structures: list[dict] = excerpt.to_dict(orient='records')

        return [src.elements.sequence.Sequence(**structure)
                for structure in structures]

    def exc(self, restart: bool) -> list[sq.Sequence]:
        """

        :param restart:
        :return:
        """

        # Retrieve (a) raw references data from Scottish Air & European Environment Information and
        # Observation Network depositories, or (b) structured references saved in Amazon S3?
        if restart:
            registry, stations, substances = src.references.regenerate.Regenerate(
                service=self.__service, parameters=self.__s3_parameters).exc()
        else:
            registry, stations, substances = src.references.read.Read(
                service=self.__service, parameters=self.__s3_parameters).exc()

        # Merge and structure the references
        data = self.__integrate(registry=registry, stations=stations, substances=substances)
        sequences = self.__sequences(blob=data)

        return sequences
