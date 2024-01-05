"""
Module sync.py
"""
import logging
import platform
import subprocess

import src.elements.profile as po


class Sync:
    """

    Description
    -----------
    Transfers files to Amazon S3.  Note, DataSync incurs cost
        * https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests
    """

    def __init__(self, restart: bool, profile: po.Profile):
        """

        :param restart: Restart?  If yes, it means all previous cloud data
                        will be, has been, deleted during this run.
        :param profile: The developer's Amazon Web Services profile details
        """

        self.__restart: bool = restart
        self.__shell = False if platform.system().lower() == 'windows' else True
        self.__profile_name = profile.name

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, source: str, destination: str, metadata: str):
        """

        :param source: The local directory
        :param destination: The Amazon S3 destination
        :param metadata: The metadata dictionary
        :return:
        """

        if self.__restart:
            action = 'sync'
        else:
            action = 'cp'

        message = subprocess.run(f"""aws s3 {action} {source} {destination} """ +
                                 f"""--metadata {metadata} --profile {self.__profile_name}""",
                                 shell=self.__shell, capture_output=True)
        self.__logger.info(message)
