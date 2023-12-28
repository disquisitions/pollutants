"""
Module upload.py
"""
import typing

import botocore.exceptions
import boto3

import src.elements.service
import src.elements.parameters


class Upload:
    """
    Cf. the Action sections of
          * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/index.html
          * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/object/index.html#S3.Object

        The second is derivable from the first via
          * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/Object.html
    """

    def __init__(self, service: src.elements.service.Service):
        """

        :param service:
        """

        self.__parameters: src.elements.parameters.Parameters = service.parameters
        self.__s3_resource: boto3.session.Session.resource = service.s3_resource

    def bytes(self, data: typing.Any, metadata: dict, bucket_name: str, key_name: str) -> bool:
        """

        :return:
        """

        # A bucket object
        bucket = self.__s3_resource.Bucket(name=bucket_name)

        try:
            bucket.put_object(
                ACL=self.__parameters.access_control_list,
                Body=data,
                Key=key_name, Metadata=metadata)
            return True or False
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err
