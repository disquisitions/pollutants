"""Module main.py"""
import logging
import os
import sys

import pandas as pd


def main():
    """
    Entry point
    * In development
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)

    # Dates
    date = pd.Timestamp.today().date() - pd.Timedelta('1 day')
    if restart:
        values = pd.date_range(start=date - pd.Timedelta('28 days'), end=date, freq='D').to_list()
        datestr_ = [str(value.date()) for value in values]
    else:
        datestr_ = [str(date)]
    logger.info('Dates\n%s', datestr_)

    # Sequences
    sequences = src.references.interface.Interface(service=service, parameters=parameters, hazards=configurations.hazards).exc(
        restart=restart
    )
    logger.info('Sequences\n%s', sequences)

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
    import config
    import src.data.interface
    import src.functions.cache
    import src.references.interface
    import src.s3.parameters
    import src.s3.service
    import src.setup

    # Upcoming arguments
    restart = False

    # Parameters & Service
    parameters = src.s3.parameters.Parameters().exc()
    service = src.s3.service.Service(parameters=parameters).exc()

    # Setting-up
    configurations = config.Config()
    restart = src.setup.Setup(service=service, parameters=parameters, warehouse=configurations.warehouse).exc(
        restart=restart)

    main()
