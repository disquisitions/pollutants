import boto3
import botocore.exceptions


class Buckets:

    def __init__(self):
        """

        """

        self.__resource = boto3.resource('s3')

    def create(self, bucket_name: str):

        bucket = self.__resource.Bucket(bucket_name)

        try:
            bucket.create(CreateBucketConfiguration={
                'LocationConstraint': self.__resource.meta.client.meta.region_name})
        except botocore.exceptions.ClientError as err:
            raise Exception(err.response) from err
