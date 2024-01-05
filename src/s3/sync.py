import logging
import subprocess
import platform


class Sync:

    def __init__(self, restart: bool, profile: str):
        """
        DataSync incurs cost
        https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests
        """

        self.__restart: bool = restart
        self.__shell = False if platform.system().lower() == 'windows' else True
        self.__profile = profile

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, source: str, destination: str, metadata: dict):
        """

        :return:
        """

        if self.__restart:
            action = 'sync'
        else:
            action = 'cp'

        message = subprocess.run(
            f'aws s3 {action} {source} s3://{destination} --metadata {metadata} --profile {self.__profile}',
            shell=self.__shell, capture_output=True)
        self.__logger.info(message)
