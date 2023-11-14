from src.controllers.db import MainDbConnection
from src.controllers.actions.action import Action

class ActionsController:

    @staticmethod
    def get(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database["actions"]
        json_actions = list(collection.find(filt))
        print(json_actions[0], type(json_actions[0]))
        return map(lambda a: Action.from_json(a), json_actions)

    @staticmethod
    def get_one(filt = {}):
        database = MainDbConnection.instance().get_database()
        collection = database["actions"]
        json_action = collection.find_one(filt)
        return Action.from_json(json_action)
