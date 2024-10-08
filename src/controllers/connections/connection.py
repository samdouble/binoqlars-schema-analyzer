from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def from_json(cls, json_object):
        new_instance = cls()
        new_instance.id = json_object["id"]
        new_instance.user_id = json_object["userId"]
        new_instance.type = json_object["type"]
        new_instance.database = json_object["database"]
        new_instance.key = json_object["key"]
        return new_instance
