"""Module interface.py"""

import pandas as pd

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
        Constructor
        """

        self.__bucket_base_name = 'pollutants/references/'

    @staticmethod
    def exc() -> None:
        """

        :return:
        """

        src.references.substances.Substances().exc()
        src.references.stations.Stations().exc()
        src.references.sequences.Sequences().exc()
