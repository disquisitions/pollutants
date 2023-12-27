
import boto3
import botocore.exceptions

import src.elements.connector


class Bucket:

    def __init__(self, parameters: src.elements.connector.Connector, bucket_name: str):
        """
        Via resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.resource
           * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/index.html

        :param parameters:
        """

        self.__parameters = parameters

        # Note, this is optional because the resource instance can build it automatically, via provided parameters
        endpoint_url = self.__parameters.root.format(bucket_name=bucket_name, region_name=self.__parameters.region_name)

        # The resource instance
        self.__s3_resource = boto3.resource(service_name='s3', region_name=self.__parameters.region_name,
                                            endpoint_url=endpoint_url)
        self.__bucket = self.__s3_resource.Bucket(name=bucket_name)

    def create(self, ):
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/create.html


        :return:
        """

        create_bucket_configuration = {
            'LocationConstraint': self.__parameters.location_constraint
        }

        try:
            self.__bucket.create(ACL='private',
                                 CreateBucketConfiguration=create_bucket_configuration)
            self.__bucket.wait_until_exists()
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def delete(self):
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/objects.html

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
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def exists(self) -> bool:
        """

        :return:
        """

        try:
            state: dict = self.__bucket.meta.client.head_bucket(Bucket=self.__bucket.name)
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

        if 'BucketRegion' in state.keys():
            return True
        else:
            return False
