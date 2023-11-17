from abc import ABC, abstractmethod
import json
from src.controllers.actions.actions_controller import ActionsController
from src.controllers.connections.connections_controller import ConnectionsController
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager

class Check(ABC):

    def __init__(self, json_object):
        self.id = json_object["id"]
        self.type = json_object["type"]
        self.user_id = json_object["userId"]
        self.connection_id = json_object["connectionId"]
        self.collection = json_object["collection"]
        self.actions = json_object["actions"]
    
    @classmethod
    def from_json(cls, json_object):
        from src.controllers.checks.json_check import JsonCheck
        from src.controllers.checks.python_check import PythonCheck

        if (json_object["type"] == "JSON"):
            return JsonCheck(json_object)
        elif (json_object["type"] == "Python"):
            return PythonCheck(json_object)
        raise

    def _execute_actions(self):
        # Get referenced actions from the database
        actions = ActionsController.get({
            "id": {
                "$in": list(map(lambda a: a["id"], self.actions))
            },
        })
        # Execute actions
        results = []
        for json_action in self.actions:
            action_id = json_action["id"]
            action = next(filter(lambda a: a.get_id() == action_id, actions))
            results.append(action.execute())
        return results

    def execute(self):
        is_validated = self.validate()
        if (not is_validated):
            return self._execute_actions()

    @abstractmethod
    def validate(self):
        pass
