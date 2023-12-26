"""Module interface.py"""

import pandas as pd

import src.references.sequences
import src.references.stations
import src.references.substances
import src.elements.references


class Interface:
    """
    Class Interface

    Rebuild, or retrieve the Amazon S3 data?  The Amazon S3 aspect is upcoming.
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def exc() -> src.elements.references.References:
        """

        :return:
        """

        substances: pd.DataFrame = src.references.substances.Substances().exc()
        stations: pd.DataFrame = src.references.stations.Stations().exc()
        sequences: pd.DataFrame = src.references.sequences.Sequences().exc()

        return src.elements.references.References(
            sequences=sequences, stations=stations, substances=substances)
