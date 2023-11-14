from abc import ABC, abstractmethod

class Action(ABC):
    
    @classmethod
    def from_json(cls, json_object):
        from src.controllers.actions.action import EmailAction

        if (json_object["type"] == "Email"):
            return EmailAction.from_json(json_object)
        raise

    @abstractmethod
    def execute(self):
        pass
