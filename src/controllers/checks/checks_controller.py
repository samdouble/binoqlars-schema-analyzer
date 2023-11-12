from src.controllers.db import MainDbConnection

class ChecksController:

    @staticmethod
    def get_one(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['checks']
        return collection.find_one(filt)
