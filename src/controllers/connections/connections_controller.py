from src.controllers.db import MainDbConnection
from src.controllers.connections.connection import Connection

class ConnectionsController:

    @staticmethod
    def get_one(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['connections']
        json_connection = collection.find_one(filt)
        return Connection.from_json(json_connection)
