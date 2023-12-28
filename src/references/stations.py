"""Module stations.py"""
import os

import pandas as pd

import src.elements.service
import src.functions.objects
import src.functions.streams
import src.s3.upload


class Stations:
    """
    Class Stations
    Reads-in the Scottish Air Quality Agency's inventory of telemetric devices
    """

    def __init__(self, service: src.elements.service.Service, storage: str, bucket_name: str, key_root: str):
        """

        :param service: For S3 ...
        :param storage: Local data depository.
        :param bucket_name: Amazon S3 bucket name.
        :param key_root: The key name prefix, i.e., the S3 path of the data file.
        """

        self.__service = service
        self.__storage = storage
        self.__bucket_name = bucket_name
        self.__key_root = key_root

        # The stations url (uniform resource locator)
        # The data source field names, and their corresponding new names.
        self.__url = 'https://www.scottishairquality.scot/sos-scotland/api/v1/stations'
        self.__rename = dict(zip(['properties.id', 'properties.label'], ['station_id', 'station_label']))

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

    def __write(self, blob: pd.DataFrame) -> str:
        """
        Locally

        :param blob:
        :return:
        """

        streams = src.functions.streams.Streams()
        pathstr = os.path.join(self. __storage, 'stations.csv')

        return streams.write(blob=blob, path=pathstr)

    def __deliver(self, blob: pd.DataFrame):
        """
        Deliver to Amazon S3

        :return:
        """

        metadata = {'station_id': 'The identification code of the telemetric device station.',
                    'station_label': 'Address, etc., details of the station.',
                    'longitude': 'The x geographic coordinate.', 'latitude': 'The y geographic coordinate.'}

        upload = src.s3.upload.Upload(service=self.__service)
        upload.bytes(data=blob, metadata=metadata, bucket_name=self.__bucket_name,
                     key_name=f'{self.__key_root}stations.csv')

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

        # Hence
        self.__write(blob=data)
        self.__deliver(blob=data)

        return data
