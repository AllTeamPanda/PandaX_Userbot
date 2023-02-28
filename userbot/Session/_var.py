import os

# todo
if os.uname()[1] == "localhost":
    response = os.system("pip3 install -r requirements.txt --no-cache-dir")
    if response == 0:
        print("Successfully Installed all requirements")
    else:
        print("Failed to install requirements")




class Config(object):
    """configuration class"""
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)

    # api id of your telegram account (required)
    API_ID = int(os.getenv("API_ID"))
    # api hash of your telegram account (required)
    API_HASH = os.getenv("API_HASH")
    # create a session using command [ python3 session.py ] or use repl.it (required)
    PyroSESSION = os.getenv("PyroSESSION")
    # ------------------
    # temporary download location (required)
    TEMP_DICT = os.getenv("TEMP_DICT", os.path.abspath(".") + "/downloads/")
    # official repo for updates
    UPSTREAM_REPO = os.getenv(
        "UPSTREAM_REPO", "https://github.com/ilhammansiz/PandaX_Userbot.git"
    )
    # ------------------
    # heroku api key (required -> if hosted on heroku)
    HEROKU_API_KEY = os.getenv("HEROKU_API")
    # heroku app name (required -> if hosted on heroku)
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    # database url (required)
    DB_URI = os.getenv("DATABASE_URL")
    # ------------------
    # these users can use your userbot
    SUDO_USERS = [
        int(x) for x in os.getenv("SUDO_USERS", "").split()
    ]  # splits on spaces
    # a group to store logs, etc (required)
    LOG_CHAT = PRIVATE_GROUP_BOT_API_ID
    # command handler, if you give (exclamation symbol = !) then you can do like this command: !ping => result: pong !
    PREFIX = os.getenv("PREFIX", ".")
    # for more info visit docs.pyrogram.org, workers section
    WORKERS = int(os.getenv("WORKERS", 8))
    # exclude official plugins from installing, give a space between plugin names
    NO_LOAD = [int(x) for x in os.getenv("NO_LOAD", "").split()]  # splits on spaces
    # default reason for afk plugin
    AFK_TEXT = os.getenv("AFK_TEXT", "I am busy Now !")
    # ------------------
    # add True to enable (default: False)
    PMPERMIT = os.getenv("PMPERMIT", False)
    # pmpermit pic (optional)
    PMPERMIT_PIC = os.getenv("PMPERMIT_PIC")
    # custom  pmpermit security text (optional)
    PMPERMIT_TEXT = os.getenv(
        "PMPERMIT_TEXT",
        "Hi tunggu sampai tuan saya membalas anda",
    )
    PM_LIMIT = int(os.getenv("PM_LIMIT", 4))
    TIME_ZONE = os.getenv("TIME_ZONE", "Asia/Jakarta")
    USER_NAME = os.getenv("USER_NAME")
    USER_BIO = os.getenv("USER_BIO")
    USER_PIC = os.getenv("USER_PIC", "")
    USER_ID = os.getenv("USER_ID")
    USER_USERNAME = os.getenv("USER_USERNAME")
    BOT_BIO = os.getenv("BOT_BIO")
    BOT_NAME = os.getenv("BOT_NAME", "PandaUserbot")
    BOT_PIC = os.getenv("BOT_PIC", "https://telegra.ph//file/ba8081afe4eb70270cf03.jpg")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_ID = os.getenv("BOT_ID")
    TOKEN = os.getenv("BOT_TOKEN")
    THUMB_PIC = os.getenv("THUMB_PIC", "https://telegra.ph//file/ba8081afe4eb70270cf03.jpg")
    TL_NAME = os.getenv("TL_NAME")
    HELP_EMOJI = os.getenv("HELP_EMOJI")
