import os
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.singleton import Singleton

@Singleton
class MainDbConnection:

    def __init__(self):
        self._connection = MongoDbConnection(os.getenv("MONGODB_URL"))

    def get_database(self):
        return self._connection['app']
