"""Module interface.py"""
import logging
import os

import src.data.depositories
import src.data.points
import src.elements.parameters as pr
import src.elements.sequence as sq
import src.elements.service as sr
import src.functions.directories
import src.references.registry
import src.s3.sync


class Interface:
    """
    Class Interface
    """

    def __init__(self, service: sr.Service, parameters: pr.Parameters, sequences: list[sq.Sequence],
                 profile: str, warehouse: str, restart: bool):
        """

        :param service:
        :param parameters:
        :param sequences:
        :param profile
        :param warehouse:
        :param restart:
        """

        self.__service = service
        self.__parameters = parameters
        self.__sequences = sequences

        self.__sync = src.s3.sync.Sync(restart=restart, profile=profile)

        # Storage
        self.__storage = os.path.join(warehouse, 'pollutants', 'points')
        src.data.depositories.Depositories(
            sequences=self.__sequences, storage=self.__storage).exc()

    @staticmethod
    def __metadata() -> str:
        """

        :return: The metadata of the points
        """

        metadata = '"epoch_ms"="The milliseconds unix epoch time  when the measure was recorded",' + \
                   '"measure"="The unit of measure of the pollutant under measure",' + \
                   '"timestamp"="The timestamp of the measure",' + \
                   '"date"="The date the measure was recorded",' + \
                   '"sequence_id"="The identification code of the sequence this record is part of."'

        return metadata

    def __s3(self):
        """

        :return:
        """

        self.__sync.exc(source=self.__storage,
                        destination=f's3://{self.__parameters.bucket_name}/{self.__parameters.points_}',
                        metadata=self.__metadata())

    def exc(self, datestr_: list[str]):
        """

        :param datestr_:
        :return:
        """

        # Retrieving data per date, but for several stations & pollutants in parallel
        points = src.data.points.Points(
            service=self.__service, parameters=self.__parameters, sequences=self.__sequences, storage=self.__storage)
        for datestr in datestr_:
            messages = points.exc(datestr=datestr)
            logging.log(level=logging.INFO, msg=messages)

        self.__s3()
