"""Module points"""
import os

import dask
import pandas as pd

import src.data.api
import src.elements.sequence
import src.functions.objects
import src.functions.streams


class Points:
    """
    Class Points
    Retrieves telemetric device's data points by date
    """

    def __init__(self, sequences: list[src.elements.sequence.Sequence], path: str):
        """

        :param sequences:
        :param path:
        """

        self.__sequences = sequences
        self.__path = path

        self.__api = src.data.api.API()
        self.__objects = src.functions.objects.Objects()
        self.__streams = src.functions.streams.Streams()

    @dask.delayed
    def __url(self, sequence_id: int, datestr: str) -> str:
        """

        :param sequence_id:
        :param datestr:
        :return:
        """

        return self.__api.exc(sequence_id=sequence_id, datestr=datestr)

    @dask.delayed
    def __read(self, url: str) -> dict:
        """

        :param url:
        :return:
        """

        content: dict = self.__objects.api(url=url)
        dictionary = content[0].__getitem__('data')

        return dictionary

    @dask.delayed
    def __build(self, dictionary: dict) -> pd.DataFrame:
        """

        :param dictionary:
        :return:
        """

        data = pd.DataFrame(data=dictionary, columns=['epoch_ms', 'measure'])
        data.loc[:, 'timestamp'] = pd.to_datetime(data.loc[:, 'epoch_ms'].array, unit='ms', origin='unix')
        data.loc[:, 'date'] = data.loc[:, 'timestamp'].dt.date.array

        return data

    @dask.delayed
    def __write(self, blob: pd.DataFrame, datestr: str, station_id: int) -> str:
        """

        :param blob:
        :param datestr:
        :param station_id:
        :return:
        """

        basename = os.path.join(self.__path, str(station_id))

        return self.__streams.write(blob=blob, path=os.path.join(basename, f'{datestr}.csv'))

    def exc(self, datestr: str):
        """

        :param datestr:
        :return:
        """

        computations = []
        for sequence in self.__sequences:
            url = self.__url(sequence_id=sequence.sequence_id, datestr=datestr)
            dictionary = self.__read(url=url)
            data = self.__build(dictionary=dictionary)
            message = self.__write(blob=data, datestr=datestr, station_id=sequence.station_id)
            computations.append(message)
