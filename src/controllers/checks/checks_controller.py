from src.controllers.db import MainDbConnection

class ChecksController:

    @staticmethod
    def get_one(filter = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['checks']
        return collection.find_one(filter)
