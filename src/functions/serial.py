import yaml


class Serial:

    def __init__(self):
        """
        Constructor
        """
        pass

    @staticmethod
    def get_dictionary(uri: str) -> dict:
        """

        :param uri: The file string of a local YAML file; path + file name + extension
        :return:
        """

        with open(file=uri, mode='r') as stream:
            try:
                return yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err) from err
