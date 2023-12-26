
class Config:

    def __init__(self):
        """

        """

        # S3 Express One Zone, which has 4 overarching regions
        # https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html
        region = 'eu-north-1'
        availability_zone = 'eun1-az3'
        regional_endpoint = 's3express-control.eu-north-1.amazonaws.com'
        zonal_endpoint = f's3express-eun1-az1.{region}.amazonaws.com'

        # bucket base
        bucket_base_name = 'pollutants/{pollutant_id}/{station_id}/{datestr}.csv'
        bucket_base_name_affix = f'--{availability_zone}--x-s3'
