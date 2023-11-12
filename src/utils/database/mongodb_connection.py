import os
from pymongo import MongoClient
from utils.database.connection import Connection

class MongoDbConnection(Connection):

    def __init__(self, connection_string):
        super().__init__()
        self.client = MongoClient(connection_string)
