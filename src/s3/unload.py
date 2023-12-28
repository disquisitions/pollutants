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
        self.__s3_resource: boto3.session.Session.resource = service.s3_resource

    def exc(self, key_name: str):
        """

        :param key_name: The S3 path of the data file, excluding the bucket name, including the file name..
        :return:
        """

        data = io.BytesIO()

        return self.__s3_resource.Bucket(name=self.__parameters.bucket_name).download_fileobj(
            Key=key_name, Fileobj=data)
