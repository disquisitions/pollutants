import logging
import os
import sys

import argparse


def main():

    logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.elements.s3_parameters as s3p
    import src.elements.profile as po
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.profile
    import src.functions.service
    import src.glue.crawler
    import src.glue.database
    import src.glue.delete.arguments
    import src.s3.parameters

    arguments = src.glue.delete.arguments.Arguments()
    parser = argparse.ArgumentParser()


    # Instances
    profile = src.functions.profile.Profile().exc()
    s3_parameters = src.s3.parameters.Parameters().exc()
    service = src.functions.service.Service(s3_parameters=s3_parameters, profile=profile).exc()

    main()