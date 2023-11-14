from abc import ABC, abstractmethod

class Action(ABC):

    def __init__(self, json_object):
        self.id = json_object["id"]
    
    @classmethod
    def from_json(cls, json_object):
        from src.controllers.actions.action import EmailAction

        if (json_object["type"] == "Email"):
            return EmailAction(json_object)
        raise

    def get_id(self):
        return self.id

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
