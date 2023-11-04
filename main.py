import sys
from lib import db

def handler():
    db.get_database()
    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    handler()
