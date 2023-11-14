from src.controllers.actions.action import Action
from src.utils.email.functions import send

class EmailAction(Action):

    @classmethod
    def from_json(cls, json_object):
        new_instance = cls()
        new_instance.id = json_object["id"]
        new_instance.type = json_object["type"]
        new_instance.recipients = json_object["recipients"]
        return new_instance
    
    def execute(self):
        send()
