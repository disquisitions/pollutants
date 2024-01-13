"""
Module aside.py
"""
import logging
import os
import platform
import sys


def main():
    """
    This is an experiments module.

    :return:
    """

    logger = logging.getLogger(__name__)

    # Environment
    logger.info(msg=f'Operating System Name (posix or nt): {os.name}')
    logger.info(msg=f'Platform: {platform.system()}')

    # Crawl
    src.s3.glue.Glue(parameters=parameters, profile=profile).exc()


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
    import src.elements.parameters as pr
    import src.elements.profile as po
    import src.functions.profile
    import src.s3.glue
    import src.s3.parameters

    # Instances
    profile: po.Profile = src.functions.profile.Profile().exc()
    parameters: pr.Parameters = src.s3.parameters.Parameters().exc()


    main()
