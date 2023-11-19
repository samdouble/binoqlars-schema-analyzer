from src.controllers.checks.check import Check

class PythonCheck(Check):

    def __init__(self, json_object):
        super().__init__(json_object)
        self.script = json_object["script"]

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object)

    def validate(self):
        print(self.script)
        # TODO Use something else than eval() here. Not safe.
        x = exec(self.script + "\nreturn_value = handler()")
        print(x)
        return True
