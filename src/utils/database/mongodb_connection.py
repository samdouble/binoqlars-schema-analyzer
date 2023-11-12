import os
from pymongo import MongoClient
from src.utils.database.connection import Connection

class MongoDbConnection(Connection):

    def __init__(self, connection_string):
        super().__init__()
        self._client = MongoClient(connection_string)

    def get_client(self):
        return self._client
