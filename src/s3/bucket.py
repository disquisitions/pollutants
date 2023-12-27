import logging

import botocore.exceptions

import src.s3.entities
import src.s3.profile


class Bucket(src.s3.entities.Entities):

    def __init__(self, bucket_name: str):
        """
        Via resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.\
                html#boto3.session.Session.resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/index.html

        :param bucket_name:
        """

        super(Bucket, self).__init__()
        self.__parameters = super().parameters()
        self.__s3_resource = super().resource()

        # A bucket instance
        self.__bucket = self.__s3_resource.Bucket(name=bucket_name)

    def create(self):
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/create.html


        :return:
        """

        create_bucket_configuration = {
            'LocationConstraint': self.__parameters.location_constraint
        }

        try:
            self.__bucket.create(ACL=self.__parameters.access_control_list,
                                 CreateBucketConfiguration=create_bucket_configuration)
            self.__bucket.wait_until_exists()
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def delete(self) -> bool:
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/objects.html
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/delete.html
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/wait_until_not_exists.html

        :return:
        """

        # Foremost, delete the bucket's objects
        try:
            state = self.__bucket.objects.delete()
            if not state['Deleted']['DeleteMarker']:
                raise state['Errors']['Message']
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

        # Subsequently, delete the bucket
        try:
            self.__bucket.delete()
            self.__bucket.wait_until_not_exists()
            return True or False
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def exists(self) -> bool:
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/head_bucket.html#S3.Client.head_bucket
        https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/s3api/head-bucket.html

        :return:
        """

        try:
            state: dict = self.__bucket.meta.client.head_bucket(Bucket=self.__bucket.name)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

        if 'BucketRegion' in state.keys():
            return True or False
