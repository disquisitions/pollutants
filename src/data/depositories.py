"""
Module depositories.py
"""
import os
import dask

import src.elements.sequence as sq
import src.functions.directories


class Depositories:
    """
    Class Depositories
    """

    def __init__(self, sequences: list[sq.Sequence], storage: str):
        """

        :param sequences:
        :param storage:
        """

        self.__sequences = sequences
        self.__storage = storage

        # Instances
        self.__directories = src.functions.directories.Directories()

    @dask.delayed
    def __local(self, sequence: sq.Sequence) -> bool:
        """

        :param sequence:
        :return:
        """

        return self.__directories.create(
            path=os.path.join(self.__storage, f'pollutant_{sequence.pollutant_id}', f'station_{sequence.station_id}'))

    def exc(self) -> list[str]:
        """

        :return:
        """

        computation = []
        for sequence in self.__sequences:
            message = self.__local(sequence=sequence)
            computation.append(message)
        messages = dask.compute(computation, scheduler='threads')[0]

        return messages
