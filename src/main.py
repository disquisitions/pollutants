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
    sequences = src.references.interface.Interface(service=service, parameters=parameters).exc(restart=restart)

    src.data.interface.Interface(
        parameters=parameters, sequences=sequences, profile=profile, restart=restart).exc(datestr_=datestr_)

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
    import src.algorithms.dates
    import src.data.interface
    import src.elements.profile
    import src.functions.cache
    import src.functions.profile
    import src.references.interface
    import src.s3.parameters
    import src.s3.service
    import src.setup

    # Upcoming arguments:
    # If restart then all the pollutants data retrieved thus far will be deleted from the cloud depository.
    restart = True

    # Parameters & Service
    parameters = src.s3.parameters.Parameters().exc()
    profile: src.elements.profile.Profile = src.functions.profile.Profile().exc()
    service = src.s3.service.Service(parameters=parameters, profile=profile).exc()

    # Setting-up
    configurations = config.Config()
    restart = src.setup.Setup(service=service, parameters=parameters, warehouse=configurations.warehouse).exc(
        restart=restart)

    main()
