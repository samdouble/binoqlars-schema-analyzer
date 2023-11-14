from abc import ABC, abstractmethod
from src.controllers.actions.action import EmailAction

class Action(ABC):
    
    @classmethod
    def from_json(cls, json_object):
        if (json_object["type"] == "Email"):
            return EmailAction.from_json(json_object)
        raise

    @abstractmethod
    def execute(self):
        pass
