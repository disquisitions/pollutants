import dask

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

        return self.__objects.api(url=url)

    def exc(self, datestr: str):

        computations = []
        for sequence_id in self.__sequence_id_:
            url = self.__url(sequence_id=sequence_id, datestr=datestr)
            dictionary = self.__read(url=url)
            computations.append(dictionary)
