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
        {'labels': ['id', 'label'], 'names': ['pollutant_id', 'uri'], cast: [int, str]}
        """

        self.__url: str = 'https://www.scottishairquality.scot/sos-scotland/api/v1/phenomena'

        self.__rename = dict(zip(['id', 'label'], ['pollutant_id', 'uri']))

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

    def exc(self):
        """

        :return:
        """

        objects = src.functions.objects.Objects()
        data: dict = objects.api(url=self.__url)
        self.__logger.info(data)

        self.__structure(blob=data)
