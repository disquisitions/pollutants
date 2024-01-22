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

    # Arguments
    arguments = src.glue.delete.arguments.Arguments()
    parser = argparse.ArgumentParser()

    parser.add_argument('item',
                        type=arguments.item,
                        help='The Amazon Glue item, i.e., <crawler> or <database> of interest.')
    parser.add_argument('instance', type=arguments.instance,
                        help='The name of the instance, i.e., crawler name or database name, '
                             'being deleted within a Glue item.')

    # Get the data parameters encoded by the input
    args = parser.parse_args()
    item = args.item
    instance = args.instance

    # Instances
    profile = src.functions.profile.Profile().exc()
    s3_parameters = src.s3.parameters.Parameters().exc()
    service = src.functions.service.Service(s3_parameters=s3_parameters, profile=profile).exc()

    main()
    