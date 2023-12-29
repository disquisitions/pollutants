"""Module points"""
import os

import dask
import pandas as pd

import src.data.api
import src.elements.parameters as pr
import src.elements.service as sr
import src.elements.sequence as sq
import src.functions.objects
import src.functions.streams
import src.s3.upload


class Points:
    """
    Class Points
    Retrieves telemetric device's data points by date
    """

    def __init__(self, sequences: list[sq.Sequence], service: sr.Service, parameters: pr.Parameters, storage: str):
        """

        :param sequences:
        :param service:
        :param parameters:
        :param storage:
        """

        self.__sequences = sequences
        self.__service = service
        self.__parameters = parameters
        self.__storage = storage

        self.__api = src.data.api.API()
        self.__objects = src.functions.objects.Objects()
        self.__streams = src.functions.streams.Streams()
        self.__upload = src.s3.upload.Upload(service=self.__service, parameters=self.__parameters)

        self.__metadata = {'epoch_ms': 'The unix epoch time, in milliseconds, when the measure was recorded',
                           'measure': 'The unit of measure of the pollutant under measure',
                           'timestamp': 'The timestamp of the measure', 'date': 'The date the measure was recorded',
                           'sequence_id': 'The identification code of the sequence this record is part of.'}

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
    def __build(self, dictionary: dict, sequence_id: int) -> pd.DataFrame:
        """

        :param dictionary:
        :param sequence_id:
        :return:
        """

        data = pd.DataFrame(data=dictionary, columns=['epoch_ms', 'measure'])
        data.loc[:, 'timestamp'] = pd.to_datetime(data.loc[:, 'epoch_ms'].array, unit='ms', origin='unix')
        data.loc[:, 'date'] = data.loc[:, 'timestamp'].dt.date.array
        data.loc[: 'sequence_id'] = sequence_id

        return data

    @dask.delayed
    def __write(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> str:
        """

        :param blob:
        :param datestr:
        :param sequence:
        :return:
        """

        basename = os.path.join(self.__storage, str(sequence.pollutant_id), str(sequence.station_id))

        return self.__streams.write(blob=blob, path=os.path.join(basename, f'{datestr}.csv'))

    def __deliver(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> bool:
        """
        
        :param blob:
        :param datestr:
        :param sequence:
        :return:
        """

        key_name = f'{self.__parameters.points_}/{str(sequence.pollutant_id)}/{str(sequence.station_id)}/{datestr}.csv'

        return self.__upload.bytes(data=blob, metadata=self.__metadata, key_name=key_name)


    def exc(self, datestr: str):
        """

        :param datestr:
        :return:
        """

        computations = []
        for sequence in self.__sequences:
            url = self.__url(sequence_id=sequence.sequence_id, datestr=datestr)
            dictionary = self.__read(url=url)
            data = self.__build(dictionary=dictionary, sequence_id=sequence.sequence_id)
            message = self.__write(blob=data, datestr=datestr, station_id=sequence.station_id)
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
