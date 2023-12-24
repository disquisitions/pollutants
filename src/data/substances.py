"""Module substances.py"""
import logging

import pandas as pd

import src.functions.objects
import src.data.vocabulary


class Substances:
    """
    Class Substances
    Reads-in the ...
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # The substances url (uniform resource locator)
        self.__url: str = 'https://www.scottishairquality.scot/sos-scotland/api/v1/phenomena'

        # The data source field names <labels>, their corresponding new names <names>,
        # and their expected data types <casts>
        labels = ['id', 'label']
        names = ['pollutant_id', 'uri']
        casts = [int, str]
        self.__rename = dict(zip(labels, names))
        self.__dtype = dict(zip(names, casts))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __structure(blob: dict) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        try:
            return pd.json_normalize(data=blob, max_level=1)
        except ImportError as err:
            raise Exception(err) from err

    def __casting(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        return blob.copy().astype(dtype=self.__dtype)

    @staticmethod
    def __extra_fields(blob: pd.DataFrame):

        definitions = src.data.vocabulary.Vocabulary().exc()
        data = blob.copy().drop(columns='uri').merge(definitions, how='left', on='pollutant_id')

        return data

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # Reading-in the JSON data of substances
        objects = src.functions.objects.Objects()
        dictionary: dict = objects.api(url=self.__url)

        # Hence, (a) structuring, (b) renaming fields in line with standards, (c) ensuring
        # the appropriate data type per field, and (d) adding fields that outline what each
        # <pollutant_id> denotes.
        data = self.__structure(blob=dictionary)
        data.rename(columns=self.__rename, inplace=True)
        data = self.__casting(blob=data)
        data = self.__extra_fields(blob=data)
        self.__logger.info('Substances\n %s', data.info())

        return data
