"""Module stations.py"""
import logging

import pandas as pd

import src.functions.objects


class Stations:
    """
    Class Stations
    Reads-in the Scottish Air Quality Agency's inventory of telemetric devices
    """

    def __init__(self):
        """
        Constructor
        """

        # The stations url (uniform resource locator)
        self.__url = 'https://www.scottishairquality.scot/sos-scotland/api/v1/stations'

        # The data source field names, and their corresponding new names.
        self.__rename = dict(zip(['properties.id', 'properties.label'], ['station_id', 'station_label']))

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
            normalised = pd.json_normalize(data=blob, max_level=2)
        except ImportError as err:
            raise Exception(err) from err

        coordinates = pd.DataFrame(data=normalised['geometry.coordinates'].to_list(),
                                   columns=['longitude', 'latitude', 'height'])
        data = normalised.copy().drop(columns='geometry.coordinates').join(coordinates, how='left')
        data.drop(columns=['type', 'geometry.type', 'height'], inplace=True)

        return data

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # Reading-in the JSON data of telemetric device stations
        objects = src.functions.objects.Objects()
        dictionary: dict = objects.api(url=self.__url)

        # Hence, structuring, and renaming the fields in line with field naming conventions and ontology standards.
        data: pd.DataFrame = self.__structure(blob=dictionary)
        data.rename(columns=self.__rename, inplace=True)
        self.__logger.info('Stations\n %s', data.info())

        return data
