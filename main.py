import sys
from lib.utils.db import get_database
from lib import KeysObject

def handler():
    get_database()

    all_keys = KeysObject()

    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    handler()
