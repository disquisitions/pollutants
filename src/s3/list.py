"""
Module list.py
"""
import logging

import src.s3.entities


class List(src.s3.entities.Entities):
    """
    Class List

    Will list all the S3 objects associated with this machine's active AWS CLI profile
    """

    def __init__(self):
        super(List, self).__init__()

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def exc(self):

        return list(super().resource().buckets.all())
