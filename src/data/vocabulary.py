"""Module vocabulary.py"""
import logging

import pandas as pd

import src.functions.streams


class Vocabulary:
    """
    Class Vocabulary
    Reads-in the air quality pollutants dictionary
    """

    def __init__(self):
        """
        Constructor
        """

        # The url (uniform resource locator) of the air quality pollutants dictionary
        self.__uri: str = 'https://dd.eionet.europa.eu/vocabulary/aq/pollutant/csv'

        # Its date fields
        self.__date_fields = ['AcceptedDate']

        # The data source field names <labels>, and their corresponding new names <names>; the new names are
        # in line with field-naming standards & defined ontology.
        labels = ['URI', 'Label', 'Notation', 'Status', 'AcceptedDate', 'recommendedUnit']
        names = ['uri', 'substance', 'notation', 'status', 'accepted_date', 'recommended_unit']
        self.__dtype = dict(zip(labels, [str] * len(labels)))
        self.__rename = dict(zip(labels, names))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __feature_engineering(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        data = blob.copy()

        # Deriving the <pollution_id>
        identifiers = data.copy().loc[:, 'uri'].str.rsplit(pat='/', n=1, expand=True)
        data.loc[:, 'pollution_id'] = identifiers.loc[:, 1].astype(dtype=int).array

        # Extracting the <recommended_unit_of_measure>
        units = data.copy().loc[:, 'recommended_unit'].str.rsplit(pat='/', n=1, expand=True)
        data.loc[:, 'recommended_unit_of_measure'] = units.loc[:, 1].array
        data.drop(columns='recommended_unit', inplace=True)

        return data

    def exc(self):
        """

        :return:
        """

        # Reads-in the details of each substance
        streams = src.functions.streams.Streams()
        data: pd.DataFrame = streams.api(uri=self.__uri, header=0, usecols=list(self.__dtype.keys()),
                                         dtype=self.__dtype, date_fields=self.__date_fields)

        # Hence, (a) renaming the fields in line with field naming conventions and ontology standards, and (b)
        # adding & dropping features
        data = data.copy().rename(columns=self.__rename)
        data = self.__feature_engineering(blob=data)
        self.__logger.info(data.info())
        self.__logger.info(data.head())
