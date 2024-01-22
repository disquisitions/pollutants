"""
Module arguments:
    Parses the input arguments
"""


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

        items = {'crawler', 'database'}
        assert items.intersection({name}), 'The item options are <crawler> & <database>'

        return name

    @staticmethod
    def instance(name: str) -> str:
        """

        :param name: The name of the instance, i.e., crawler name or database name, being
                     deleted within a Glue item
        :return:
        """

        assert isinstance(name, str), 'The instance name must be a string'

        return name
        