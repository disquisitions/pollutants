"""Module interface.py"""
import logging
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

    def __init__(self):
        """
        Constructor
        """

        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants')
        self.__references = src.data.references.References().exc()

        # Directories deletion & creation instance
        self.__directories = src.functions.directories.Directories()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __sequences(self, pollutant_id: int) -> list[src.elements.sequence.Sequence]:
        """

        :param pollutant_id:
        :return:
        """

        instances: pd.DataFrame = self.__references.sequences.loc[
                                  self.__references.sequences['pollutant_id'] == pollutant_id, :]
        structures: list[dict] = instances.to_dict(orient='records')

        return [src.elements.sequence.Sequence(**structure) for structure in structures]

    def exc(self, pollutant_id: int, restart: bool = False):
        """

        :param pollutant_id:
        :param restart:
        :return:
        """

        # The sequences associated with the pollutant in question
        sequences = self.__sequences(pollutant_id=pollutant_id)

        # The pollutant's top directory
        basename = os.path.join(self.__storage, str(pollutant_id))

        # If restart, erase existing data
        if restart:
            self.__directories.cleanup(path=basename)

        # Ascertain the existence of each station's directory
        computation = [dask.delayed(self.__directories.create)(path=os.path.join(basename, str(sequence.station_id)))
                       for sequence in sequences]
        dask.compute(computation)
