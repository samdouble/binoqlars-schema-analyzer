from src.controllers.db import MainDbConnection

class ConnectionsController:

    @staticmethod
    def get_one(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['connections']
        return collection.find_one(filt)
