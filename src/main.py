"""Module main.py"""
import logging
import os
import sys

def main():
    """
    Entry point
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('pollutants')


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
