"""Module references.py"""
import collections

import pandas as pd

import src.data.sequences
import src.data.stations
import src.data.substances
import src.elements.references


class References:
    """
    Class References

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

        substances: pd.DataFrame = src.data.substances.Substances().exc()
        stations: pd.DataFrame = src.data.stations.Stations().exc()
        sequences: pd.DataFrame = src.data.sequences.Sequences().exc()

        return src.elements.references.References(
            substances=substances, stations=stations, sequences=sequences)
