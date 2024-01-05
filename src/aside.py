"""
Module aside.py
"""
import os

import platform
import sys

import logging


def main():
    """
    This is an experiments module.

    :return:
    """

    logger = logging.getLogger(__name__)

    logger.info('Operating System Name (posix or nt): %s', os.name)
    logger.info(msg=f'Platform: {platform.system()}')


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    main()