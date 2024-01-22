"""
Module arguments:
    Parses the input arguments
"""
import numpy as np


class Arguments:
    """
    Class Arguments
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def item(name: str) -> str:
        """
        
        :param name: The name of the glue item for which a connection is required
        :return: 
        """

        items = ['crawler', 'database']
        print(name in items)
        assert (name in items), 'The item options are <crawler> & <database>'

        return name

    @staticmethod
    def instance(name) -> str:
        """

        :param name: The name of the instance, i.e., crawler name or database name, being
                     deleted within a Glue item
        :return:
        """

        assert len(name) > 0 & len(name) < 256, 'The instance name length must be within (0  256)'

        return name
        