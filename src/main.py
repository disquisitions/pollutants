"""Module main.py"""
import logging
import os
import sys
import pandas as pd


def main():
    """
    Entry point
    """

    # Log
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Pollutants')

    # Try
    pollutant_id = 1
    interface = src.data.interface.Interface()
    interface.exc(pollutant_id=pollutant_id)

    # Deleting __pycache__
    src.functions.cache.Cache().delete()
    

if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Modules
    import src.data.api
    import src.data.interface
    import src.functions.objects
    import src.functions.cache

    main()
