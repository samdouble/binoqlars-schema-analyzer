import json
from src.controllers.actions.action import Action
from src.controllers.actions.actions_controller import ActionsController
from src.controllers.connections.connections_controller import ConnectionsController
from src.controllers.db import MainDbConnection
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager

class Check:
    
    @classmethod
    def from_json(cls, json_object):
        new_instance = cls()
        new_instance.id = json_object["id"]
        new_instance.connection_id = json_object["connectionId"]
        new_instance.collection = json_object["collection"]
        new_instance.filter = json_object["filter"]
        new_instance.actions = json_object["actions"]
        return new_instance

    def _execute_actions(self):
        # Get referenced actions from the database
        actions = ActionsController.get({
            "id": {
                "$in": map(lambda a: a["id"], self.actions)
            },
        })
        # Execute actions
        for json_action in self.actions:
            action_id = json_action["id"]
            action = next(filter(lambda a: a.get_id() == action_id, actions))
            action.execute()

    def execute(self):
        is_validated = self.validate()
        if (not is_validated):
            self._execute_actions()

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
