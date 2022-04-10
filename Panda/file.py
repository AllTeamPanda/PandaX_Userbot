import os

class Database(object):
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    SESSION = os.environ.get("SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
 
