"""Module main.py"""
import logging
import os
import sys
import pandas as pd


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)

    # Dates
    date = pd.Timestamp.today().date() - pd.Timedelta('1 day')
    values = pd.date_range(start=date - pd.Timedelta('28 days'), end=date, freq='D').to_list()
    datestr_ = [str(value.date()) for value in values]
    logger.info(datestr_)

    # Pollutants - Sulphur Dioxide, Particulate Matter
    hazards = [1, 5]
    logger.info(hazards)

    # Try
    logger.info('Does the bucket <pollutants> exists? %s',
                src.s3.bucket.Bucket(bucket_name='pollutants').exists())
    logger.info('List of Buckets:\n%s',
                src.s3.list.List().exc())

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
    import src.functions.cache
    import src.s3.connector
    import src.elements.connector
    import src.s3.bucket
    import src.s3.list

    main()
