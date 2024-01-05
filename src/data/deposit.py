"""
Module deposit.py
"""
import os

import pandas as pd

import src.elements.sequence as sq
import src.functions.streams
import src.s3.upload


class Deposit:
    """
    Class Deposit
    """

    def __init__(self, storage: str):
        """

        :param storage: The local data depository
        """

        self.__storage = storage
        self.__streams = src.functions.streams.Streams()

    def __local(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> str:
        """

        :param blob:
        :param datestr:
        :param sequence:
        :return:
            message -> {file stem}: succeeded
                       {file stem}: empty
        """

        basename = os.path.join(self.__storage, f'pollutant_{sequence.pollutant_id}', f'station_{sequence.station_id}')

        return self.__streams.write(blob=blob, path=os.path.join(basename, f'{datestr}.csv'))

    def exc(self, blob: pd.DataFrame, datestr: str, sequence: sq.Sequence) -> str:
        """

        :param blob: A telemetric device's sequence data, in the form of a data frame.
        :param datestr: The date in focus; format YYYY-mm-dd
        :param sequence: The sequence's details, in collection form.
        :return:
        """

        if blob.empty:
            return f'{sequence.sequence_id} -> empty'
        else:
            local = self.__local(blob=blob, datestr=datestr, sequence=sequence)

            return f'{sequence.sequence_id} -> {local}'
