from src.controllers.connections.connection import Connection
from src.controllers.db import MainDbConnection


class ConnectionsController:
    @staticmethod
    def get_one(filt=None):
        database = MainDbConnection.instance().get_database()
        collection = database["connections"]
        json_connection = collection.find_one(filt or {})
        return Connection.from_json(json_connection)
