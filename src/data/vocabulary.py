import logging

import src.functions.streams

class Vocabulary:

    def __init__(self):
        """

        """

        self.__uri: str = 'https://dd.eionet.europa.eu/vocabulary/aq/pollutant/csv'

        # get <pollutant_id> from <uri>
        self.__fields = {'labels': ['URI', 'Label', 'Definition', 'Notation', 'Status', 'AcceptedDate', 'recommendedUnit'],
                         'name': ['uri', 'substance', 'definition', 'notation', 'status', 'accepted_date', 'recommended_unit'],
                         'type': str}
        self.__parse_dates = ['AcceptedDate']

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):

        streams = src.functions.streams.Streams()
        streams.api(uri=self.__uri)
