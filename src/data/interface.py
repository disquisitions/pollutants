
import logging
import os

import pandas as pd

import src.data.references
import src.elements.sequence
import src.functions.directories


class Interface:

    def __init__(self):
        """
        Constructor
        """

        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants')

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, pollutant_id: int, restart: bool = False):
        """

        :return:
        """

        path = os.path.join(self.__storage, str(pollutant_id))

        if restart:
            directories = src.functions.directories.Directories()
            directories.cleanup(path=path)
            directories.create(path=path)

        collection = src.data.references.References().exc()

        sequences = collection.sequences
        excerpt: pd.DataFrame = sequences.loc[sequences['pollutant_id'] == pollutant_id, :]
        self.__logger.info('Excerpt (Above)\n%s\n\n', excerpt.info())

        records = excerpt.to_dict(orient='records')
        self.__logger.info(records)

        instances = [src.elements.sequence.Sequence(**record) for record in records]
        self.__logger.info(instances)
