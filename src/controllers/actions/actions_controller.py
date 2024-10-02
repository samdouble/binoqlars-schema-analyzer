from src.controllers.actions.action import Action
from src.controllers.db import MainDbConnection


class ActionsController:
    @staticmethod
    def get(filt=None):
        database = MainDbConnection.instance().get_database()
        collection = database["actions"]
        json_actions = list(collection.find(filt or {}))
        return [Action.from_json(json_action) for json_action in json_actions]

    @staticmethod
    def get_one(filt=None):
        database = MainDbConnection.instance().get_database()
        collection = database["actions"]
        json_action = collection.find_one(filt or {})
        return Action.from_json(json_action)
