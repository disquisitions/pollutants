"""Module interface.py"""
import logging
import os

import src.data.points
import src.data.depositories
import src.elements.sequence as sq
import src.functions.directories
import src.references.registry


class Interface:
    """
    Class Interface
    """

    def __init__(self, sequences: list[sq.Sequence]):
        """

        :param sequences
        """

        self.__sequences = sequences
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants', 'points')

    def exc(self, datestr_: list[str], restart: bool):
        """

        :param datestr_:
        :param restart
        :return:
        """

        if restart:
            src.functions.directories.Directories().cleanup(self.__storage)

        src.data.depositories.Depositories(
            sequences=self.__sequences, storage=self.__storage).exc()

        # Retrieving data per date, but for several stations in parallel
        points = src.data.points.Points(sequences=self.__sequences, storage=self.__storage)
        for datestr in datestr_:
            messages = points.exc(datestr=datestr)
            logging.log(level=logging.INFO, msg=messages)
