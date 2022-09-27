import os

import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    STRING_SESSION = os.environ.get(
        "SESSION", None)
    STRING_SESSION = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("SESSION", None)
    MONGO_URI = os.environ.get("MONGO_URI", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    REDIS_URI = os.environ.get("REDIS_URI", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
    REDISHOST = os.environ.get("REDISHOST", None)
    REDISPORT = os.environ.get("REDISPORT", None)
    REDISUSER = os.environ.get("REDISUSER", None)
    STRING_SESSION2 = os.environ.get("SESSION2") or None
    STRING_SESSION3 = os.environ.get("SESSION3") or None
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    DATABASE_URL = DB_URI



class Database(object):
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    SESSION = os.environ.get("SESSION", None)
    SESSION2 = os.environ.get("SESSION2", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    PyroSESSION = os.environ.get("PyroSESSION", None)
    MONGO_DB = Var.MONGO_URI
    PyroSESSION2 = os.environ.get("PyroSESSION2", None)
    PyroSESSION3 = os.environ.get("PyroSESSION3", None)
    PyroSESSION4 = os.environ.get("PyroSESSION4", None)
    DB_URIl = os.environ.get("DATABASES_URL", "mongodb+srv://petercord:b38DJZL3X6zhnHJ0@cluster0.e9xau.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

