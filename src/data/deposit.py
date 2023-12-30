import os

import pandas as pd

import src.elements.parameters as pr
import src.elements.service as sr
import src.elements.sequence as sq
import src.functions.streams
import src.s3.upload


class Deposit:

    def __init__(self, service: sr.Service, parameters: pr.Parameters, storage: str):
        """

        :param service:
        :param parameters:
        :param storage:
        """

        self.__service = service
        self.__parameters = parameters
        self.__storage = storage

        self.__upload = src.s3.upload.Upload(service=service, parameters=parameters)

        self.__streams = src.functions.streams.Streams()

        self.__metadata = {'epoch_ms': 'The unix epoch time, in milliseconds, when the measure was recorded',
                           'measure': 'The unit of measure of the pollutant under measure',
                           'timestamp': 'The timestamp of the measure',
                           'date': 'The date the measure was recorded',
                           'sequence_id': 'The identification code of the sequence this record is part of.'}

    def __local(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> str:
        """

        :param blob:
        :param datestr:
        :param sequence:
        :return:
            message -> {file stem}: succeeded
                       {file stem}: empty
        """

        basename = os.path.join(self.__storage, str(sequence.pollutant_id), str(sequence.station_id))

        return self.__streams.write(blob=blob, path=os.path.join(basename, f'{datestr}.csv'))

    def __s3(self,  blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> bool:
        """

        :param blob:
        :param datestr:
        :param sequence:
        :return:
            boolean -> Was the item uploaded?
        """

        key_name = f'{self.__parameters.points_}{str(sequence.pollutant_id)}/{str(sequence.station_id)}/{datestr}.csv'

        return self.__upload.bytes(data=blob, metadata=self.__metadata, key_name=key_name)

    def exc(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> str:
        """

        :param blob:
        :param datestr:
        :param sequence:
        :return:
        """

        if blob.empty:
            return f'{sequence.sequence_id} -> empty'
        else:
            local = self.__local(blob=blob, datestr=datestr, sequence=sequence)
            s3 = self.__s3(blob=blob, datestr=datestr, sequence=sequence)

            return f'{sequence.sequence_id} -> {local}|Uploaded: {s3}'
