import logging

import pandas as pd

import src.functions.streams

class Vocabulary:

    def __init__(self):
        """
        Constructor
        """

        self.__uri: str = 'https://dd.eionet.europa.eu/vocabulary/aq/pollutant/csv'

        # The application programming interface's <csv> data reading parameters
        labels = ['URI', 'Label', 'Definition', 'Notation', 'Status', 'AcceptedDate', 'recommendedUnit']
        self.__dtype = dict(zip(labels, [str] * len(labels)))
        self.__date_fields = ['AcceptedDate']

        # Field name updates: in line with field-naming standards & defined ontology
        names = ['uri', 'substance', 'definition', 'notation', 'status', 'accepted_date', 'recommended_unit']
        self.__rename = dict(zip(labels, names))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __structure(self, blob: pd.DataFrame) -> pd.DataFrame:
        """
        get <pollutant_id> from <uri>

        :param blob:
        :return:
        """

        return blob.copy().rename(columns=self.__rename)

    def exc(self):

        streams = src.functions.streams.Streams()
        data: pd.DataFrame = streams.api(uri=self.__uri, header=0, usecols=self.__dtype['labels'],
                                         dtype=self.__dtype, date_fields=self.__date_fields )
        self.__logger.info(data)

        data = self.__structure(blob=data)
        self.__logger.info(data)
