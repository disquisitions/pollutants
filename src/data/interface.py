"""Module interface.py"""
import logging
import os

import pandas as pd

import src.references.interface
import src.data.points
import src.elements.sequence
import src.functions.directories


class Interface:
    """
    Class Interface
    """

    def __init__(self, pollutant_id: int, restart: bool):
        """

        :param pollutant_id:
        :param restart:
        """

        # Directories deletion & creation instance
        self.__directories = src.functions.directories.Directories()

        # If case restart, erase the existing pollutant store
        self.__pollutant_id = pollutant_id
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants', str(self.__pollutant_id))
        if restart:
            self.__directories.cleanup(path=self.__storage)

        # The references
        self.__references = src.references.interface.Interface().exc()

    def __sequences(self) -> list[src.elements.sequence.Sequence]:
        """

        :return:
        """

        instances: pd.DataFrame = self.__references.sequences.loc[
                                  self.__references.sequences['pollutant_id'] == self.__pollutant_id, :]
        structures: list[dict] = instances.to_dict(orient='records')

        return [src.elements.sequence.Sequence(**structure) for structure in structures]

    def exc(self, datestr_: list[str]):
        """

        :param datestr_:
        :return:
        """

        # The sequences associated with the pollutant in question
        sequences = self.__sequences()
        points = src.data.points.Points(sequences=sequences, storage=self.__storage)

        # Ascertaining the existence of, or re-creating, directories
        [self.__directories.create(path=os.path.join(self.__storage, str(sequence.station_id)))
         for sequence in sequences]

        # Retrieving data per date, but for several stations in parallel
        for datestr in datestr_:
            messages = points.exc(datestr=datestr)
            logging.log(level=logging.INFO, msg=messages)
