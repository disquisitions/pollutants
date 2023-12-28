"""
Module: directories
"""
import os


class Directories:
    """
    For clearing & creating directories
    """

    def __init__(self):
        """
        """

    @staticmethod
    def cleanup(path: str) -> bool:
        """
        Clears a directory
        :param path:
        :return:
        """

        # Foremost, delete files
        __files = [os.remove(os.path.join(base, file))
                   for base, _, files in os.walk(path) for file in files]
        elements = [file for _, _, files in os.walk(path) for file in files]
        assert len(elements) == 0, f'Unable to delete all files within path {path}'

        # ... then, directories
        __directories = [os.removedirs(os.path.join(base, directory))
                         for base, directories, _ in os.walk(path, topdown=False)
                         for directory in directories
                         if os.path.exists(os.path.join(base, directory))]

        try:
            if os.path.exists(path=path):
                os.removedirs(path)
            return True
        except OSError as err:
            raise Exception(err) from err

    @staticmethod
    def create(path: str) -> bool:
        """
        :param path:
        :return:
        """

        try:
            if not os.path.exists(path):
                os.makedirs(path)
            return True
        except OSError as err:
            raise Exception(err) from err
