"""Module main.py"""
import logging
import os
import sys
import collections


def main():
    """
    Entry point
    """

    # Log
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Pollutants')

    # Try
    datestr = '2023-11-18'
    url: str = src.data.url.URL().exc(datestr=datestr)
    logger.info(url)
    sample = src.functions.objects.Objects().api(url=url)
    logger.info(sample.__getitem__('name'))
    logger.info(sample.__getitem__('data'))

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
    import src.functions.objects
    import src.functions.cache
    import src.data.url

    main()
