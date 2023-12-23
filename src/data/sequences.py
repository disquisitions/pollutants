import src.functions.objects
import logging
import pandas as pd


class Sequences:

    def __init__(self):
        """

        """

        self.__url = 'https://www.scottishairquality.scot/sos-scotland/api/v1/timeseries'

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __structure(blob: dict) -> pd.DataFrame:

        try:
            return pd.json_normalize(data=blob, max_level=2)
        except ImportError as err:
            raise Exception(err) from err

    def exc(self):

        objects = src.functions.objects.Objects()
        dictionary = objects.api(url=self.__url)

        data = self.__structure(blob=dictionary)
        self.__logger.info(data.info())
        self.__logger.info(data.head())
