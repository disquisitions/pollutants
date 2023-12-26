import boto3
import botocore.exceptions


class Bucket:

    def __init__(self):
        """

        """

        self.__s3_client = boto3.client('s3', region_name='')

    def create(self, bucket_name: str):

        try:
            bucket_configuration = {
                'Location': {'Type': 'AvailabilityZone', 'Name': ''},
                'Bucket': {'Type': 'Directory', 'DataRedundancy': 'SingleAvailabilityZone'}
            }
            self.__s3_client.create_bucket(Bucket='', CreateBucketConfiguration=bucket_configuration)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err
