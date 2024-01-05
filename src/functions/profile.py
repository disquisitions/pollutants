"""Module profile.py"""
import os
import yaml

import src.elements.profile


class Profile:
    """
    Class Profile
    """

    def __init__(self):
        """
        Constructor
        """

        self.__uri = os.path.join(os.getcwd(), 'resources', 'profile.yaml')

    def __get_dictionary(self) -> dict:
        """

        :return:
        """

        with open(file=self.__uri, mode='r') as stream:
            try:
                blob = yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err) from err

        return blob['profile']

    def exc(self) -> src.elements.profile.Profile:
        """

        :return:
        """

        dictionary = self.__get_dictionary()

        return src.elements.profile.Profile(**dictionary)
