from abc import ABC, abstractclassmethod

from botocore.exceptions import ClientError

from src.utils.aws_session import AwsSession


class SecretsManager(ABC):
    @abstractclassmethod
    def get_connection_string(cls, secret_name):
        raise NotImplementedError()

    @classmethod
    def get_secret(cls, secret_name):
        client = AwsSession.instance().get_session().client(service_name="secretsmanager", region_name="ca-central-1")

        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            raise e

        return get_secret_value_response["SecretString"]
