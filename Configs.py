import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("BOT_TOKEN", None)
    LOGS_CHAT = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    BOT_US = os.environ.get("TG_BOT_USERNAME", None)
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", "Selamat Bergabung klik disini 👇🏻")
    RULES = os.environ.get("RULES", "ngentot")
    MAX_MESSAGE_SIZE_LIMIT = 4095
