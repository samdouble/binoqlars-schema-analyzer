import sys
from src.utils.db import get_database
from src.utils.secrets.MongoDbAtlasSecretsManager import MongoDbAtlasSecretsManager
#from src.KeysObject import KeysObject

def handler(event, context):
    print(event, context)

    print(get_database())

    #all_keys = KeysObject()
    print(MongoDbAtlasSecretsManager.get_connection_string())

    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
