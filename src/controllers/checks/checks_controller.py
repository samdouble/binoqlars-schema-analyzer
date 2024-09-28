from src.controllers.db import MainDbConnection
from src.controllers.checks.check import Check

class ChecksController:

    @staticmethod
    def get_one(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['checks']
        json_check = collection.find_one(filt)
        return Check.from_json(json_check)
