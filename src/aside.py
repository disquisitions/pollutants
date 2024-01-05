"""
Module aside.py
"""
import json
import logging
import os
import platform
import sys


def main():
    """
    This is an experiments module.

    :return:
    """

    logger = logging.getLogger(__name__)

    # Environment
    logger.info('Operating System Name (posix or nt): %s', os.name)
    logger.info(msg=f'Platform: {platform.system()}')

    # Ensuring double quotes are retained
    text: str = json.dumps(dictionary)
    logger.info(f"""{text}""")


if __name__ == '__main__':
    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    dictionary = {'epoch_ms': 'The unix epoch time, in milliseconds, when the measure was recorded',
                  'measure': 'The unit of measure of the pollutant under measure',
                  'timestamp': 'The timestamp of the measure',
                  'date': 'The date the measure was recorded',
                  'sequence_id': 'The identification code of the sequence this record is part of.'}

    main()
