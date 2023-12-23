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
    sequence_id = 214
    datestr = '2023-11-18'
    url: str = src.data.api.API().exc(sequence_id=sequence_id, datestr=datestr)
    logger.info(url)
    sample = src.functions.objects.Objects().api(url=url)
    dictionary = sample[0].__getitem__('data')
    logger.info(pd.DataFrame(data=dictionary, columns=['epoch', 'measure']))

    # Additionally
    src.data.substances.Substances().exc()
    src.data.stations.Stations().exc()
    src.data.vocabulary.Vocabulary().exc()
    src.data.sequences.Sequences().exc()

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
    import src.data.substances
    import src.data.stations
    import src.data.vocabulary
    import src.data.sequences
    import src.data.api

    main()
