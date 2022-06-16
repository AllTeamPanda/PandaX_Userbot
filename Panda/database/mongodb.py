import motor.motor_asyncio
from .. import LOGS
import sys
from ..file import Database


def mongodb():
    if Database.MONGO_DB:
        try:
            motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)
     
