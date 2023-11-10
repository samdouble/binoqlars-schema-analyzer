from abc import ABC
import boto3
from botocore.exceptions import ClientError
import os

class SecretsManager(ABC):
    def get_secret(secret_name):
        session = boto3.session.Session(
            os.getenv('AWS_ACCESS_KEY_ID_'),
            os.getenv('AWS_SECRET_ACCESS_KEY_'),
        )
        client = session.client(
            service_name='secretsmanager',
            region_name='ca-central-1'
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            raise e

        secret = get_secret_value_response['SecretString']
        return secret
