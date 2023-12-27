"""Module interface.py"""
import os.path

import src.references.sequences
import src.references.stations
import src.references.substances


class Interface:
    """
    Class Interface

    Rebuild, or retrieve the Amazon S3 data?  The Amazon S3 aspect is upcoming.
    """

    def __init__(self):
        """

        """

        # Local
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants', 'references')

    def exc(self) -> None:
        """

        :return:
        """

        src.references.substances.Substances().exc()
        src.references.stations.Stations().exc(storage=self.__storage)
        src.references.sequences.Sequences().exc()
