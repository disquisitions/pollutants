"""
Module sync.py
"""
import logging
import platform
import subprocess


class Sync:
    """

    Description
    -----------
    Transfers files to Amazon S3. Note, DataSync incurs cost
        * https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests
    """

    def __init__(self, restart: bool):
        """

        :param restart: Restart? If yes, it means all previous cloud data
                        will be, has been, deleted during this run.
        """

        self.__restart: bool = restart
        self.__shell = False if platform.system().lower() == 'windows' else True

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
                                 f"""--metadata {metadata}""",
                                 shell=self.__shell, capture_output=True)
        self.__logger.info(message)
