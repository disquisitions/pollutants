import logging
import boto3
import botocore.exceptions

import src.elements.connector
import src.s3.profile


class Bucket:

    def __init__(self, parameters: src.elements.connector.Connector, bucket_name: str):
        """
        Via resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.\
                html#boto3.session.Session.resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/index.html

        :param parameters:
        """

        self.__parameters = parameters

        # The resource instance
        profile = src.s3.profile.Profile().exc()
        boto3.setup_default_session(profile_name=profile)
        self.__s3_resource = boto3.resource(service_name='s3', region_name=self.__parameters.region_name)
        self.__bucket = self.__s3_resource.Bucket(name=bucket_name)

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger: logging.Logger = logging.getLogger(__name__)

        self.__logger.info('Items\n%s', list(self.__s3_resource.buckets.all()))

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

        self.__logger.info(self.__bucket.name)

        try:
            state: dict = self.__bucket.meta.client.head_bucket(Bucket=self.__bucket.name)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

        if 'BucketRegion' in state.keys():
            return True or False
