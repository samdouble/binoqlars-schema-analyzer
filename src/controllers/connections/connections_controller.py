from src.controllers.db import MainDbConnection

class ConnectionsController:

    @staticmethod
    def get_one(filter = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['connections']
        return collection.find_one(filter)
