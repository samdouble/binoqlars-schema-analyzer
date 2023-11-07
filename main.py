import sys
from src.utils.db import get_database
from src.utils.secrets import get_secret
#from src.KeysObject import KeysObject

def handler():
    get_database()

    #all_keys = KeysObject()
    print(get_secret())

    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    handler()
