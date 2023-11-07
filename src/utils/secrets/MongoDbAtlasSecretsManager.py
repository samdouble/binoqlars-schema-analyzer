from src.utils.secrets.SecretsManager import SecretsManager

class MongoDbAtlasSecretsManager(SecretsManager):
    @classmethod
    def get_connection_string(cls):
        secret_name = 'datajitsu_6c98210f-ff3b-4d4a-8935-698fe2ad0287'
        secret = cls.get_secret(secret_name)
        print(secret)
        connection_string = secret['CONNECTION_STRING']
        return connection_string
