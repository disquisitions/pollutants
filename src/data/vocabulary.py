import logging


class Vocabulary:

    def __init__(self):
        """

        """

        self.__uri: str = 'https://dd.eionet.europa.eu/vocabulary/aq/pollutant/csv'

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)
