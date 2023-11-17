import json
from src.controllers.checks.check import Check
from src.controllers.connections.connections_controller import ConnectionsController
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager

class JsonCheck(Check):

    def __init__(self, json_object):
        super().__init__(json_object)
        self.filter = json_object["filter"]

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object)

    @classmethod
    def validate(self):
        connection = ConnectionsController.get_one({
            "id": self.connection_id,
        })

        connection_string = MongoDbAtlasSecretsManager.get_connection_string(connection.key)
        database_connection = MongoDbConnection(connection_string)
        database_client = database_connection.get_client()
        collection = database_client[connection.database][self.collection]
        filt = json.loads(self.filter)
        nb_results = collection.count_documents(filt)

        return nb_results == 0
