"""
Module list.py
"""
import logging

import src.elements.service


class List:
    """
    Class List

    Will list all the S3 objects associated with this machine's active AWS CLI profile
    """

    def __init__(self, service: src.elements.service.Service):
        """
        Constructor
        """

        self.__service = service

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

    def exc(self):
        """

        :return:
        """

        return list(self.__service.s3_resource.buckets.all())
