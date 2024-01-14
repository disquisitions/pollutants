"""
Module aside.py
"""
import logging
import os
import sys


def main():
    """
    This is an experiments module.

    :return:
    """

    logger = logging.getLogger(__name__)
    logger.info(msg='Crawl')

    # Crawl
    crawler = src.glue.crawler.Crawler(service=service, s3_parameters=s3_parameters)
    crawler.create_crawler()
    crawler.start_crawler()

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

    # Classes
    import src.elements.s3_parameters as s3p
    import src.elements.profile as po
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.profile
    import src.functions.service
    import src.glue.crawler
    import src.s3.parameters

    # Instances
    profile: po.Profile = src.functions.profile.Profile().exc()
    s3_parameters: s3p.S3Parameters = src.s3.parameters.Parameters().exc()
    service: sr.Service = src.functions.service.Service(s3_parameters=s3_parameters, profile=profile).exc()

    main()
