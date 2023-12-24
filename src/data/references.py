import collections

import src.data.sequences
import src.data.stations
import src.data.substances
import src.elements.references


class References:

    def __init__(self):
        """

        """

    @staticmethod
    def exc():
        """

        :return:
        """

        src.data.substances.Substances().exc()
        src.data.stations.Stations().exc()
        src.data.sequences.Sequences().exc()
