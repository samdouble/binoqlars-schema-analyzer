import uuid

from src.controllers.db import MainDbConnection


class LogsController:
    @staticmethod
    def create(json_object=None):
        database = MainDbConnection.instance().get_database()
        collection = database["logs"]
        return collection.insert_one(
            {
                "id": str(uuid.uuid4()),
                **(json_object or {}),
            }
        )
