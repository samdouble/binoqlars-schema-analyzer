from abc import ABC
from botocore.exceptions import ClientError
from src.utils.aws_session import AwsSession

class SecretsManager(ABC):
    def get_secret(secret_name):
        client = AwsSession.instance().get_session().client(
            service_name='secretsmanager',
            region_name='ca-central-1'
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            raise e

        return get_secret_value_response['SecretString']
