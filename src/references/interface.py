"""Module interface.py"""
import logging

import pandas as pd

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.references.regenerate


class Interface:
    """
    Class Interface
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A collection of Amazon services
        :param s3_parameters: Amazon S3 parameters
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Sequences in focus
        self.__sequence_id_filter: list[int] = config.Config().sequence_id_filter

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

    def __excerpt(self, blob: pd.DataFrame) -> pd.DataFrame:
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
        excerpt = excerpt.copy().loc[excerpt['sequence_id'].isin(self.__sequence_id_filter), :]

        return excerpt

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # Retrieve (a) raw references data from Scottish Air & European Environment Information and
        # Observation Network depositories, or (b) structured references saved in Amazon S3?
        registry, stations, substances = src.references.regenerate.Regenerate(
            service=self.__service, s3_parameters=self.__s3_parameters).exc()

        # Merge and structure the references
        data = self.__integrate(registry=registry, stations=stations, substances=substances)
        excerpt = self.__excerpt(blob=data)

        return excerpt
