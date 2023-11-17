import json
from src.controllers.actions.actions_controller import ActionsController
from src.controllers.connections.connections_controller import ConnectionsController
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager

class PythonCheck:

    def __init__(self, json_object):
        super().__init__(json_object)
        self.script = json_object["script"]

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object)

    @classmethod
    def validate(self):
        print(self.script)
        x = eval(self.script)
        print(x)
        return True
