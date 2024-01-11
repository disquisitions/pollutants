"""Module parameters.py"""
import os

import src.elements.parameters
import src.functions.serial


class Parameters:
    """
    Class Parameters

    Description
    -----------

    This class reads-in the YAML file of this project repository's overarching Amazon S3 (Simple Storage Service)
    parameters.

    S3 Express One Zone, which has 4 overarching regions
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html
    """

    def __init__(self):
        """
        Constructor
        """

        self.__uri = os.path.join(os.getcwd(), 'resources', 'parameters.yaml')

    def __get_dictionary(self) -> dict:
        """

        :return:
            A dictionary, or excerpt dictionary, of YAML file contents
        """

        blob = src.functions.serial.Serial().get_dictionary(uri=self.__uri)

        return blob['parameters']

    @staticmethod
    def __build_collection(dictionary: dict) -> src.elements.parameters.Parameters:
        """

        :param dictionary:
        :return:
            A re-structured form of the parameters.
        """

        parameters = src.elements.parameters.Parameters(**dictionary)

        # Parsing variables
        location_constraint = parameters.location_constraint.format(region_name=parameters.region_name)
        parameters = parameters._replace(location_constraint=location_constraint)

        return parameters

    def exc(self) -> src.elements.parameters.Parameters:
        """

        :return:
            The re-structured form of the parameters.
        """

        dictionary = self.__get_dictionary()

        return self.__build_collection(dictionary=dictionary)
