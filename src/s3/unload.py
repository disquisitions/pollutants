import io
import boto3

import src.elements.parameters as pr
import src.elements.service as sr


class Unload:

    def __init__(self, service: sr.Service, parameters: pr.Parameters):
        """

        :param service:
        """

        self.__parameters: pr.Parameters = parameters
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
