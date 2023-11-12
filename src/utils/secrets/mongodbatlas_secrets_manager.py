import json
from src.utils.secrets.secrets_manager import SecretsManager

class MongoDbAtlasSecretsManager(SecretsManager):

    @classmethod
    def get_connection_string(cls, secret_name):
        secret = cls.get_secret(secret_name)
        json_secret = json.loads(secret)
        connection_string = json_secret['CONNECTION_STRING']
        return connection_string
 