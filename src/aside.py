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
    crawler = src.glue.crawler.Crawler(service=service, parameters=parameters, profile=profile)
    database = src.glue.database.Database(service=service)

    crawler.delete_crawler(name='hygiene')
    database.delete_database(name='pollutants')

    crawler.create_crawler()
    crawler.start_crawler()


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
    import src.elements.service as sr
    import src.functions.profile
    import src.functions.service
    import src.glue.crawler
    import src.glue.database
    import src.s3.parameters
    
    # Instances
    profile: po.Profile = src.functions.profile.Profile().exc()
    parameters: pr.Parameters = src.s3.parameters.Parameters().exc()
    service: sr.Service = src.functions.service.Service(parameters=parameters, profile=profile).exc()

    main()
