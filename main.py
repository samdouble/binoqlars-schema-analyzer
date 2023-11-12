import json
from src.controllers.checks.checks_controller import ChecksController
from src.controllers.connections.connections_controller import ConnectionsController
from src.utils.database.mongodb_connection import MongoDbConnection
from src.utils.secrets.mongodbatlas_secrets_manager import MongoDbAtlasSecretsManager

def handler(_event, _context):
    check = ChecksController.get_one()
    print("Check", check)

    connection = ConnectionsController.get_one({
        "id": check["connectionId"],
    })
    print("Connection", connection)

    connection_string = MongoDbAtlasSecretsManager.get_connection_string(connection["key"])
    print("Connection string", connection_string)

    database_connection = MongoDbConnection(connection_string)
    database_client = database_connection.get_client()
    collection = database_client[connection["database"]][check["collection"]]
    filt = json.loads(check["filter"])
    result = collection.find_one(filt)
    print("Result", result)

    return result["date"] + " " + result["red"]["name"] + " vs " + result["blue"]["name"]
