"""Module substances.py"""
import logging

import pandas as pd

import src.functions.objects


class Substances:
    """
    Class Substances
    Reads-in the ...
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        self.__url: str = 'https://www.scottishairquality.scot/sos-scotland/api/v1/phenomena'

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

    def __structure(self, blob: dict) -> pd.DataFrame:

        try:
            normalised = pd.json_normalize(data=blob, max_level=1)
        except ImportError as err:
            raise Exception(err) from err

        return normalised.rename(columns=self.__rename)

    def __casting(self, blob: pd.DataFrame) -> pd.DataFrame:

        return blob.copy().astype(dtype=self.__dtype)

    def exc(self):
        """

        :return:
        """

        objects = src.functions.objects.Objects()
        dictionary: dict = objects.api(url=self.__url)

        data = self.__structure(blob=dictionary)
        data = self.__casting(blob=data)
        self.__logger.info(data.info())
