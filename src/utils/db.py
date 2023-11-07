import os
from pymongo import MongoClient

def get_database():
    client = MongoClient(os.getenv("MONGODB_URL"))
    return client['app']
