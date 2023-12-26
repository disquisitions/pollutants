import boto3
import botocore.exceptions

import src.elements.connector
import src.s3.profile


class Bucket:

    def __init__(self, parameters: src.elements.connector.Connector):
        """

        :param parameters:
        """

        profile = src.s3.profile.Profile().exc()
        boto3.setup_default_session(profile_name=profile)
        self.__parameters = parameters
        self.__s3_client = boto3.client('s3', region_name=self.__parameters.region_name)

    def create(self, bucket_name: str):
        """

        :param bucket_name:
        :return:
        """

        try:
            bucket_configuration = {
                'Location': {'Type': 'AvailabilityZone', 'Name': self.__parameters.availability_zone},
                'Bucket': {'Type': 'Directory', 'DataRedundancy': 'SingleAvailabilityZone'}
            }
            self.__s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=bucket_configuration)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def delete(self, bucket_name: str):
        """
        https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-delete.html

        :param bucket_name:
        :return:
        """

        # Apriori: aws s3 rm s3://... --recursive
        try:
            self.__s3_client.delete_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err
