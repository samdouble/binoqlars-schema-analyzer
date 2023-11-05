import sys
from lib.utils.db import get_database

def handler():
    get_database()
    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    handler()
