class Connection:

    def __init__(self):
        pass
    
    @classmethod
    def from_json(cls, json_object):
        new_instance = cls()
        new_instance.id = json_object["id"]
        new_instance.type = json_object["type"]
        new_instance.key = json_object["key"]
        new_instance.database = json_object["database"]
        return new_instance
