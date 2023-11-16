import uuid
from src.controllers.db import MainDbConnection

class ConnectionsController:

    @staticmethod
    def create(json_object = {}):
        database = MainDbConnection.instance().get_database()
        collection = database['logs']
        return collection.insert_one({
            "id": uuid.uuid4(),
            **json_object,
        })
