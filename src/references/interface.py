"""Module interface.py"""
import os.path

import src.elements.service
import src.functions.directories
import src.references.sequences
import src.references.stations
import src.references.substances


class Interface:
    """
    Class Interface

    Rebuild, or retrieve the Amazon S3 data?  The Amazon S3 aspect is upcoming.
    """

    def __init__(self, service: src.elements.service.Service):
        """

        """

        # Cloud/Local
        self.__service = service
        self.__bucket_name = 'pollutants'
        self.__key_root = 'references/'
        self.__storage = os.path.join(os.getcwd(), 'warehouse', 'pollutants', 'references')

        directories = src.functions.directories.Directories()
        directories.create(path=self.__storage)

    def exc(self) -> None:
        """

        :return:
        """

        src.references.substances.Substances().exc()
        src.references.stations.Stations(
            service=self.__service, storage=self.__storage,
            bucket_name=self.__bucket_name, key_root=self.__key_root).exc()
        src.references.sequences.Sequences().exc()
