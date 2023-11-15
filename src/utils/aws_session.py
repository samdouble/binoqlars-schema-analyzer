import boto3
import os
from src.utils.singleton import Singleton

@Singleton
class AwsSession:

    def __init__(self):
        self.session = boto3.session.Session(
            os.getenv('AWS_ACCESS_KEY_ID_'),
            os.getenv('AWS_SECRET_ACCESS_KEY_'),
        )

    def get_session(self):
        return self.session
