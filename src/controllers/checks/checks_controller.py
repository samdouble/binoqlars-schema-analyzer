from src.controllers.checks.check import Check
from src.controllers.db import MainDbConnection


class ChecksController:
    @staticmethod
    def get_one(filt=None):
        database = MainDbConnection.instance().get_database()
        collection = database["checks"]
        json_check = collection.find_one(filt or {})
        return Check.from_json(json_check)
