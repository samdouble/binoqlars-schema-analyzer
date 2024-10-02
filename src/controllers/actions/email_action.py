from src.controllers.actions.action import Action
from src.utils.email.functions import send


class EmailAction(Action):

    def __init__(self, json_object):
        super().__init__(json_object)
        self.type = json_object["type"]
        self.recipients = json_object["recipients"]

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object)

    def execute(self):
        return send(self.recipients)
