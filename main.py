import sys
from src.utils.db import get_database
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager
#from src.keys_object import KeysObject

def handler(_event, _context):
    database = get_database()
    print(database)

    #all_keys = KeysObject()
    print(MongoDbAtlasSecretsManager.get_connection_string())

    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
