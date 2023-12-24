import dask

import pandas as pd

import src.data.api
import src.functions.objects


class Points:

    def __init__(self, sequence_id_: list):
        """

        """

        self.__sequence_id_ = sequence_id_

        self.__api = src.data.api.API()
        self.__objects = src.functions.objects.Objects()

    @dask.delayed
    def __url(self, sequence_id: int, datestr: str) -> str:

        return self.__api.exc(sequence_id=sequence_id, datestr=datestr)

    @dask.delayed
    def __read(self, url: str) -> dict:

        content: dict = self.__objects.api(url=url)
        dictionary = content[0].__getitem__('data')

        return dictionary

    @dask.delayed
    def __build(self, dictionary: dict) -> pd.DataFrame:

        data = pd.DataFrame(data=dictionary, columns=['epoch_ms', 'measure'])
        data.loc[:, 'timestamp'] = pd.to_datetime(data.loc[:, 'epoch_ms'].array, unit='ms', origin='unix')
        data.loc[:, 'date'] = data.loc[:, 'timestamp'].dt.date.array

        return data

    def exc(self, datestr: str):

        computations = []
        for sequence_id in self.__sequence_id_:
            url = self.__url(sequence_id=sequence_id, datestr=datestr)
            dictionary = self.__read(url=url)
            data = self.__build(dictionary=dictionary)
            computations.append(data)
