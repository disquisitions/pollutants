"""Module interface.py"""
import logging

import src.data.depositories
import src.data.points
import src.elements.s3_parameters as s3p
import src.elements.sequence as sq


class Interface:
    """
    Class Interface
    """

    def __init__(self, s3_parameters: s3p.S3Parameters, sequences: list[sq.Sequence]):
        """

        :param s3_parameters: The S3 parameters settings for this project
        :param sequences: Each list item is the detail of a sequence, in collection form.
        """

        self.__s3_parameters = s3_parameters
        self.__sequences = sequences

    def exc(self, storage: str):
        """

        :return:
        """

        src.data.depositories.Depositories(
            sequences=self.__sequences, storage=storage).exc()

        # Retrieving data per date, but for several stations & pollutants in parallel
        points = src.data.points.Points(sequences=self.__sequences, storage=storage)
        messages = points.exc()
        logging.log(level=logging.INFO, msg=messages)
