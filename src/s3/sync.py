import subprocess
import platform

class Sync:

    def __init__(self, restart: bool):
        """
        DataSync incurs cost
        https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests
        """

        self.__restart: bool = restart
        self.__platform: str = platform.system().lower()
        self.__shell = False if self.__platform == 'windows' else True


    def exc(self):
        """

        :return:
        """





