import subprocess
import platform


class Sync:

    def __init__(self, restart: bool, profile: str):
        """
        DataSync incurs cost
        https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests
        """

        self.__restart: bool = restart
        self.__platform: str = platform.system().lower()
        self.__shell = False if self.__platform == 'windows' else True
        self.__profile = profile

    def exc(self, source: str, destination: str):
        """

        :return:
        """

        # {} source
        # s3://{} destination
        # profile
        message = subprocess.run(f'aws s3 sync {source} s3://{destination} --profile {self.__profile}',
                                 shell=self.__shell, capture_output=True)





