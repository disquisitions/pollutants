"""Module interface.py"""

import pandas as pd

import src.references.sequences
import src.references.stations
import src.references.substances
import src.elements.connector
import src.s3.bucket


class Interface:
    """
    Class Interface

    Rebuild, or retrieve the Amazon S3 data?  The Amazon S3 aspect is upcoming.
    """

    def __init__(self, parameters: src.elements.connector.Connector):
        """
        Constructor
        """

        self.__bucket_base_name = 'pollutants'
        self.__parameters = parameters

    def __bucket(self):

        bucket_name = self.__bucket_base_name + self.__parameters.bucket_base_name_affix
        src.s3.bucket.Bucket(parameters=self.__parameters).create(bucket_name=bucket_name)

    def exc(self) -> None:
        """

        :return:
        """

        self.__bucket()

        src.references.substances.Substances().exc()
        src.references.stations.Stations().exc()
        src.references.sequences.Sequences().exc()
