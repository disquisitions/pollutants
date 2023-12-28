
import os
import dask

import src.elements.sequence
import src.functions.directories


class Depositories:

    def __init__(self, storage: str):
        """

        """

        self.__storage = storage
        self.__directories = src.functions.directories.Directories()

    def __s3(self):
        """

        :return:
        """

    @dask.delayed
    def __local(self, sequence: src.elements.sequence.Sequence) -> bool:
        """

        :return:
        """

        return self.__directories.create(
            path=os.path.join(self.__storage, str(sequence.pollutant_id), str(sequence.station_id)))

    def exc(self, sequences: list[src.elements.sequence.Sequence], restart: bool):
        """

        :param sequences:
        :param restart:
        :return:
        """

        if restart:
            self.__directories.cleanup(self.__storage)

        computation = []
        for sequence in sequences:
            message = self.__local(sequence=sequence)
            computation.append(message)
