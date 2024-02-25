"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)

    # The dates
    datestr_ = src.algorithms.dates.Dates().exc()
    logger.info(datestr_)

    # Excerpt of metadata of sequences
    excerpt = src.references.interface.Interface(service=service, s3_parameters=s3_parameters).exc()

    # A parallel execution matrix: (metadata of sequences ⊗ dates), i.e., outer product
    sequences = src.algorithms.vectors.Vectors(
        excerpt=excerpt, datestr_=datestr_).exc()

    # Execute
    src.data.interface.Interface(service=service, s3_parameters=s3_parameters,
                                 sequences=sequences).exc(storage=storage)

    # Deleting __pycache__
    src.functions.cache.Cache().delete()


if __name__ == '__main__':
    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import config
    import src.algorithms.dates
    import src.algorithms.vectors
    import src.data.interface

    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service

    import src.references.interface
    import src.s3.s3_parameters
    import src.setup

    # S3 S3Parameters, Service Instance
    s3_parameters: s3p.S3Parameters = src.s3.s3_parameters.S3Parameters().exc()
    service: sr.Service = src.functions.service.Service(region_name=s3_parameters.region_name).exc()

    # Setting-up
    configurations = config.Config()
    setup: bool = src.setup.Setup(
        service=service, s3_parameters=s3_parameters).exc()

    # Storage: warehouse, Amazon S3 bucket, bucket prefix
    parts: list[str] = s3_parameters.points_.split(sep='/')
    parts: list[str] = [part for part in parts if part]
    parts: list[str] = [s3_parameters.bucket_name] + parts
    storage: str = os.path.join(configurations.warehouse, *parts)

    main()
