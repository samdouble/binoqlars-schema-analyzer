from datetime import datetime
import time
from src.controllers.checks.checks_controller import ChecksController
from src.controllers.logs.logs_controller import LogsController

def handler(_event, _context):
    start_time = time.time()
    check = ChecksController.get_one()
    result = check.execute()
    end_time = time.time()

    # Log
    LogsController.create({
        "userId": check.user_id,
        "createdAt": datetime.today().replace(microsecond=0),
        "checkId": check.id,
        "executionTime": end_time - start_time,
        "result": result,
    })

    return result
