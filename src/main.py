"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point
    * In development
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Pollutants')

    # The dates
    datestr_ = src.algorithms.dates.Dates().exc(restart=restart)

    # Sequences
    sequences = src.references.interface.Interface(
        service=service, s3_parameters=s3_parameters).exc(restart=restart)
    src.data.interface.Interface(
        s3_parameters=s3_parameters, sequences=sequences, restart=restart).exc(datestr_=datestr_)

    # Deleting __pycache__
    src.functions.cache.Cache().delete()
    

if __name__ == '__main__':
    '''
    Setting-up
    '''
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    '''
    Modules
    '''
    import config
    import src.algorithms.dates
    import src.data.interface

    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service

    import src.references.interface
    import src.s3.parameters
    import src.setup

    '''
    Upcoming arguments:
    If restart then all the pollutants data retrieved thus far will be deleted from the cloud depository.
    '''
    restart = True

    '''
    S3 Parameters, Service Instance
    '''
    s3_parameters: s3p.S3Parameters = src.s3.parameters.Parameters().exc()
    service: sr.Service = src.functions.service.Service().exc()

    '''
    Setting-up
    '''
    configurations = config.Config()
    restart = src.setup.Setup(service=service, s3_parameters=s3_parameters, warehouse=configurations.warehouse).exc(
        restart=restart)

    main()
