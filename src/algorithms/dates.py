"""
Module dates.py
"""
import logging

import datetime

import pandas as pd

import config


class Dates:
    """
    Class Dates

    This class calculates the list of dates for which data is required.
    """

    def __init__(self, restart: bool):
        """
        Constructor

        :param restart: Restart?
        """

        self.__restart = restart
        self.__configurations = config.Config()

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, ) -> list[str]:
        """

        :return:
        """

        # Settings
        ending = datetime.datetime.today()
        starting = datetime.datetime.today() - datetime.timedelta(days=self.__configurations.span)

        # A series of dates wherein each date is the date of the first day of a month
        if self.__restart:
            values = pd.date_range(start=starting, end=ending, freq='MS').to_list()
            datestr_ = [str(value.date()) for value in values]
        else:
            datestr_ = [str(ending.replace(day=1).date())]

        self.__logger.info('Dates\n%s', datestr_)

        return datestr_
