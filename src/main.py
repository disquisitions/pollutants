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

    date = pd.Timestamp.today().date() - pd.Timedelta('1 day')
    logger.info(date)
    dates = pd.date_range(start=date - pd.Timedelta('732 days'), end=date, freq='D')
    logger.info(dates)
    for i in dates:
        logger.info(str(i.date()))

    # Try
    pollutant_id = 1
    interface = src.data.interface.Interface(pollutant_id=pollutant_id, restart=True)

    interface.exc()

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
