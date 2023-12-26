"""Module connector.py"""
import os
import yaml

import src.elements.connector


class Connector:
    """
    Class Connector

    S3 Express One Zone, which has 4 overarching regions
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html
    """

    def __init__(self):
        """
        Constructor
        """

        self.__uri = os.path.join(os.getcwd(), 'resources', 'connector.yaml')

    def __get_dictionary(self) -> dict:

        with open(file=self.__uri, mode='r') as stream:
            try:
                blob = yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err) from err

        return blob['parameters']

    @staticmethod
    def __build_collection(dictionary: dict) -> src.elements.connector.Connector:

        parameters = src.elements.connector.Connector(**dictionary)

        zonal_root = parameters.zonal_root.format(availability_zone=parameters.availability_zone)
        root_affix = parameters.root_affix.format(region_name=parameters.region_name)
        bucket_base_name_affix = parameters.bucket_base_name_affix.format(availability_zone=parameters.availability_zone)
        parameters = parameters._replace(zonal_root=zonal_root, root_affix=root_affix,
                                         bucket_base_name_affix=bucket_base_name_affix)

        return parameters

    def exc(self) -> src.elements.connector.Connector:

        dictionary = self.__get_dictionary()

        return self.__build_collection(dictionary=dictionary)
