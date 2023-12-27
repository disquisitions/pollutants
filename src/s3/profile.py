"""Module profile.py"""
import os
import yaml


class Profile:
    """
    Class Profile
    """

    def __init__(self):
        """
        Constructor
        """

        self.__uri = os.path.join(os.getcwd(), 'resources', 'profile.yaml')

    def __get_name(self) -> dict:
        """

        :return:
        """

        with open(file=self.__uri, mode='r') as stream:
            try:
                blob = yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err) from err

        return blob['profile']['name']

    def exc(self) -> str:
        """

        :return:
        """

        name = self.__get_name()

        return str(name)
