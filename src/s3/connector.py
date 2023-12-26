import os
import yaml

import src.elements.connector


class Connector:

    def __init__(self):
        """

        """

        self.__uri = os.path.join(os.getcwd(), 'resources', 'connector.yaml')

    def __get_dictionary(self) -> dict:

        with open(file=self.__uri, mode='r') as stream:
            try:
                blob = yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err) from err

        return blob['parameters']

    def exc(self) -> src.elements.connector.Connector:

        dictionary = self.__get_dictionary()
        return src.elements.connector.Connector(**dictionary)
