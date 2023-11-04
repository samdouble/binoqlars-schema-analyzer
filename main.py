from abc import ABC
import sys
import lib.db

def handler(event, context):
    db.get_database()
    print("Hello World!")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'

if __name__ == "__main__":
    handler()
