"""Module interface.py"""
import os

import dask
import pandas as pd

import src.data.references
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

        # If restart, erase existing data
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants')
        self.__pollutant_id = pollutant_id
        self.__basename = os.path.join(self.__storage, str(self.__pollutant_id))
        if restart:
            self.__directories.cleanup(path=self.__basename)

        # The references
        self.__references = src.data.references.References().exc()

    def __sequences(self) -> list[src.elements.sequence.Sequence]:
        """

        :return:
        """

        instances: pd.DataFrame = self.__references.sequences.loc[
                                  self.__references.sequences['pollutant_id'] == self.__pollutant_id, :]
        structures: list[dict] = instances.to_dict(orient='records')

        return [src.elements.sequence.Sequence(**structure) for structure in structures]

    def __paths(self, sequences: list[src.elements.sequence.Sequence]):
        """

        :param sequences:
        :return:
        """

        # Ascertain the existence of each station's directory
        computation = [
            dask.delayed(self.__directories.create)(path=os.path.join(self.__basename, str(sequence.station_id))) for
            sequence in sequences]
        dask.compute(computation)

    def exc(self):
        """

        :return:
        """

        # The sequences associated with the pollutant in question
        sequences = self.__sequences()
        self.__paths(sequences=sequences)
