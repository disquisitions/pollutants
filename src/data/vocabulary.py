"""Module vocabulary.py"""
import logging

import pandas as pd

import src.functions.streams


class Vocabulary:
    """
    Class Vocabulary
    Reads-in the reference ...
    """

    def __init__(self):
        """
        Constructor

        The application programming interface's <csv> data reading parameters.
        Field name updates: in line with field-naming standards & defined ontology.
        """

        self.__uri: str = 'https://dd.eionet.europa.eu/vocabulary/aq/pollutant/csv'
        self.__date_fields = ['AcceptedDate']

        labels = ['URI', 'Label', 'Definition', 'Notation', 'Status', 'AcceptedDate', 'recommendedUnit']
        names = ['uri', 'substance', 'definition', 'notation', 'status', 'accepted_date', 'recommended_unit']
        self.__dtype = dict(zip(labels, [str] * len(labels)))
        self.__rename = dict(zip(labels, names))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __features(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        data = blob.copy()

        identifiers = data.copy().loc[:, 'uri'].str.rsplit(pat='/', n=1, expand=True)
        data.loc[:, 'pollution_id'] = identifiers.loc[:, 1].array

        units = data.copy().loc[:, 'recommended_unit'].str.rsplit(pat='/', n=1, expand=True)
        data.loc[:, 'recommended_unit_of_measure'] = units.loc[:, 1].array

        return data

    def exc(self):
        """

        :return:
        """

        streams = src.functions.streams.Streams()
        data: pd.DataFrame = streams.api(uri=self.__uri, header=0, usecols=list(self.__dtype.keys()),
                                         dtype=self.__dtype, date_fields=self.__date_fields)

        data = data.copy().rename(columns=self.__rename)

        data = self.__features(blob=data)
        self.__logger.info(data.info())
        self.__logger.info(data.head())
