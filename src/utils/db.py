import os
from pymongo import MongoClient

def get_database():
    client = MongoClient(os.getenv("MONGODB_URL"))
    database = client['app']
    collection = database['connections']
    return collection.find_one()
