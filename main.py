from src.controllers.checks.checks_controller import ChecksController

def handler(_event, _context):
    check = ChecksController.get_one()
    print("Check", check)

    result = check.validate()

    return result["date"] + " " + result["red"]["name"] + " vs " + result["blue"]["name"]
