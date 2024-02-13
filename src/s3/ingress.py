import glob
import os

import botocore.exceptions
import dask

import src.elements.s3_parameters as s3p
import src.elements.service as sr


class Ingress:

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters, metadata: dict):
        """

        :param service:
        :param s3_parameters:
        """

        self.__s3_client = service.s3_client
        self.__bucket_name = s3_parameters.bucket_name
        self.__metadata = metadata

    @dask.delayed
    def __ingress(self, file: str, key: str) -> str:
        """

        :param file:
        :param key:
        :return:
        """

        try:
            self.__s3_client.upload_file(Filename=file, Bucket=self.__bucket_name, Key=key,
                                         ExtraArgs={'Metadata': self.__metadata})
            return f'Uploading {key}'
        except botocore.exceptions.ClientError as err:
            raise Exception(err) from err

    def exc(self, path: str) -> list[str]:
        """

        :param path:
        :return:
        """

        files: list[str] = glob.glob(pathname=os.path.join(path, '**',  '*.csv'), recursive=True)
        keys = [file.split(self.__bucket_name)[1].replace(os.path.sep, '/')[1:] for file in files]

        computations = []
        for file, key in zip(files, keys):
            message = self.__ingress(file=file, key=key)
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
