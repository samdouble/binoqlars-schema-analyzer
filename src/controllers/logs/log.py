from datetime import datetime
import uuid

class Log:
    
    @classmethod
    def __init__(self, json_object):
        self.id = uuid.uuid4()
        self.created_at = datetime.today().replace(microsecond=0)
        self.json_object = json_object
