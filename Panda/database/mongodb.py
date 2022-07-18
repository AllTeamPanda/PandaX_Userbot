import motor.motor_asyncio
from ..file import Database


def mongodb():
    if Database.MONGO_DB:
        return motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
    else:
        return None
