import collections


class Config:

    def __init__(self):
        """

        """

        # S3 Express One Zone, which has 4 overarching regions
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html
        region_code = 'eu-north-1'
        availability_zone = 'eun1-az3'
        regional_endpoint = f'https://s3express-control.{region_code}.amazonaws.com'
        zonal_endpoint = f'https://s3express-{availability_zone}.{region_code}.amazonaws.com'
        bucket_base_name_affix = f'--{availability_zone}--x-s3'

        # Data
        PartitionOfPoints = collections.namedtuple(
            typename='PartitionOfPoints', field_names=['bucket_base_name', 'bucket_base_name_affix',
                                                       'regional_endpoint', 'zonal_endpoint'])
        partition_of_points = PartitionOfPoints(
            bucket_base_name='pollutants/points/{pollutant_id}/{station_id}/{datestr}.csv',
            bucket_base_name_affix=bucket_base_name_affix,
            regional_endpoint=regional_endpoint,
            zonal_endpoint=zonal_endpoint)

        # References
        PartitionOfReferences = collections.namedtuple(
            typename='PartitionOfReferences', field_names=['bucket_base_name', 'bucket_base_name_affix',
                                                           'regional_endpoint', 'zonal_endpoint'])
        partition_of_references = PartitionOfReferences(
            bucket_base_name='pollutants/references/{filename}.csv',
            bucket_base_name_affix=bucket_base_name_affix,
            regional_endpoint=regional_endpoint,
            zonal_endpoint=zonal_endpoint)
