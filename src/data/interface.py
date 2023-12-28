"""Module interface.py"""
import logging
import os

import pandas as pd

import src.data.points
import src.elements.sequence
import src.functions.directories
import src.references.sequences


class Interface:
    """
    Class Interface
    """

    def __init__(self, hazards: list[int]):
        """

        :param hazards:
        """

        self.__hazards = hazards

        self.__directories = src.functions.directories.Directories()
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants', 'points')

    def __sequences(self) -> list[src.elements.sequence.Sequence]:
        """

        :return:
        """

        sequences = src.references.sequences.Sequences().exc()
        instances: pd.DataFrame = sequences.loc[sequences['pollutant_id'].isin(self.__hazards), :]
        structures: list[dict] = instances.to_dict(orient='records')

        return [src.elements.sequence.Sequence(**structure) for structure in structures]

    def exc(self, datestr_: list[str]):
        """

        :param datestr_:
        :return:
        """

        # The sequences associated with the pollutant in question
        # Retrieving data per date, but for several stations in parallel
        sequences = self.__sequences()
        points = src.data.points.Points(sequences=sequences, storage=self.__storage)
        for datestr in datestr_:
            messages = points.exc(datestr=datestr)
            logging.log(level=logging.INFO, msg=messages)
