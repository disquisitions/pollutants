"""Module stations.py"""
import logging
import typing

import pandas as pd

import src.functions.objects


class Stations:
    """
    Class Stations
    Reads-in the Scottish Air Quality Agency's inventory of telemetric devices
    """

    def __init__(self):
        """
        :var:
          self.__url: The stations url (uniform resource locator)
          self.__rename: The original field names of the data, and their corresponding new names.
        """

        # Variables
        self.__url = 'https://www.scottishairquality.scot/sos-scotland/api/v1/stations'
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

    @staticmethod
    def __metadata() -> dict:
        """

        :return:
        """

        return {'station_id': 'The identification code of the telemetric device station.',
                'station_label': 'Address, etc., details of the station.',
                'longitude': 'The x geographic coordinate.',
                'latitude': 'The y geographic coordinate.'}

    def exc(self) -> typing.Tuple[pd.DataFrame, dict]:
        """

        :return
          data: A descriptive inventory of substances/pollutants.

          metadata: The metadata of <data>; for a data catalogue.
        """

        # Reading-in the JSON data of telemetric device stations
        objects = src.functions.objects.Objects()
        dictionary: dict = objects.api(url=self.__url)

        # Hence, structuring, and renaming the fields in line with field naming conventions and ontology standards.
        data: pd.DataFrame = self.__structure(blob=dictionary)
        data.rename(columns=self.__rename, inplace=True)

        return data, self.__metadata()
