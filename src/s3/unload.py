import io
import boto3

import src.elements.parameters
import src.elements.service


class Unload:

    def __init__(self, service: src.elements.service.Service):
        """

        :param service:
        """

        self.__parameters: src.elements.parameters.Parameters = service.parameters
        self.__s3_resource = service.s3_resource
        self.__s3_client = service.s3_client

    def exc(self, key_name: str):
        """

        :param key_name: The S3 path of the data file, excluding the bucket name, including the file name..
        :return:
        """

        blob = self.__s3_client.get_object(Bucket=self.__parameters.bucket_name, Key=key_name)
        buffer = io.StringIO(blob['Body'].read().decode('utf-8'))

        return buffer
