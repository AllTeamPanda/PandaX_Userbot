# Copyright (C) 2021-2022 Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

from distutils.util import strtobool as sb

import os    
import sys

from decouple import config
from dotenv import find_dotenv, load_dotenv
from validators.url import url

load_dotenv(find_dotenv())

CMD_LIST = {}
XTRA_CMD_LIST = {}


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True
AFF_LIST ={}

### Var
class Var(object):
    LOGGER = True
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    STRING_SESSION = os.environ.get(
        "SESSION", None)
    API_ID = APP_ID
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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    SESSION = STRING_SESSION
    LOG_CHANNEL = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API = os.environ.get("HEROKU_API", None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    VC_SESSION = config("VC_SESSION", default=None)

### Database
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

## Osdb

class Osdb(object):
    BOTLOG = sb(os.environ.get("BOTLOG", "True"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    BLACK_CHAT = {int(x) for x in os.environ.get("BLACK_CHAT", "").split()}
    BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001159103924]
    BOTLOG_CHATID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
    PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API", None)
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL", "https://github.com/ilhammansiz/PandaX_Userbot.git")
    S_PACK_NAME = os.environ.get("S_PACK_NAME", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    COUNTRY = str(os.environ.get("COUNTRY", "ID"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")
    BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
    DEEP_AI = os.environ.get("DEEP_AI", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    HANDLER = os.environ.get("HANDLER") or "."
    SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"+")
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    



## Ubot
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BLACK_CHAT = {int(x) for x in os.environ.get("BLACK_CHAT", "").split()}
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001159103924]
BOTLOG_CHATID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API", None)
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL", "https://github.com/ilhammansiz/PandaX_Userbot.git")
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)
DEEP_AI = os.environ.get("DEEP_AI", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
HANDLER = os.environ.get("HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"+")
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
CMD_HANDLER = HANDLER
WHITELIST = [5057493677, 1593802955]
DEFAULT = [1593802955]
DEVS = [5057493677, 1593802955]
ALIVE_TEKS_CUSTOM = os.environ.get("ALIVE_TEKS_CUSTOM", None)
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Panda")
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "⚡")
INLINE_EMOJI = os.environ.get("INLINE_EMOJI", "᪥")
ICON_HELP = os.environ.get("ICON_HELP", "❈")
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
)
INLINE_PIC = (
    os.environ.get("INLINE_PIC") or "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
)
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/6213d2673486beca02967.png"
)
QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
)
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)
TERM_ALIAS = os.environ.get("TERM_ALIAS", "PandaUserbot")
GROUP = os.environ.get("GROUP", "TeamSquadUserbotSupport")
CHANNEL = os.environ.get("CHANNEL", "PandaUserbot")
BYPASS_URL = os.environ.get("BYPASS_URL", "@bypassvip_bot")
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)
# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)
# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {
    int(x) for x in os.environ.get(
        "BLACKLIST_GCAST",
        "").split()}

# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001159103924]

CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

import os
from typing import Set
from ._database import pdB
SqL = pdB
from telethon.tl.types import ChatBannedRights
import heroku3
from dotenv import load_dotenv
from distutils.util import strtobool

if os.path.exists("local.env"):
    load_dotenv("local.env")

def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")





class Config(object):
    LOGGER = True
    STRING_SESSION3 = os.environ.get("SESSION3") or None  
    STRING_SESSION2 = os.environ.get("SESSION2") or None
    ALIVE_NAME = SqL.get_key("ALIVE_NAME") or os.environ.get("ALIVE_NAME", None)
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    DB_URI = os.environ.get("DATABASE_URL", None)
    PYROGRAM_SESSION = os.environ.get("PYROGRAM_SESSION", None)
    MONGO_URI = os.environ.get("MONGO_URI", None)
    STRING_SESSION = os.environ.get(
        "SESSION", None
    )
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    TG_BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    TZ = SqL.get_key("TZ") or os.environ.get("TZ", "Asia/Jakarta") 
    UPSTREAM_REPO = SqL.get_key("UPSTREAM_REPO") or os.environ.get(
        "UPSTREAM_REPO", "https://github.com/AllTeamPanda/PandaX_Userbot.git"
    ) 
    BOT_TOKEN = SqL.get_key("BOT_TOKEN") or TG_BOT_TOKEN 
    BOT_USERNAME = SqL.get_key("BOT_USERNAME") or TG_BOT_USERNAME
    AUTONAME = os.environ.get("AUTONAME", None)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    HEROKU_API_KEY = os.environ.get("HEROKU_API", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    MAX_FLOOD_IN_PMS = int(os.environ.get("MAX_FLOOD_IN_PMS", 5))
    PM_LOGGER_GROUP_ID = int(
        os.environ.get("PM_LOGGER_GROUP_ID")
        or os.environ.get("PM_LOGGR_BOT_API_ID")
        or 0
    )
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "pandauserbot")
    THUMB_IMAGE = os.environ.get(
        "THUMB_IMAGE", "https://telegra.ph/file/0c571ae6dcb68ea2bdf49.jpg"
    )
    PANDA_HELP_LOGO = os.environ.get(
        "PANDA_HELP_LOGO", None
    )
    UB_BLACK_LIST_CHAT = {
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    }
    NO_LOAD = [x for x in os.environ.get("NO_LOAD", "").split()]
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
    DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    HELP_TEXT_INLINE = os.environ.get("HELP_TEXT_INLINE", None)
    CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)
    NO_OF_ROWS_IN_HELP = int(os.environ.get("NO_OF_ROWS_IN_HELP", 5))
    NO_OF_COLUMNS_IN_HELP = int(os.environ.get("NO_OF_COLUMNS_IN_HELP", 2))
    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "✅")
    COMMAND_HAND_LER = SqL.get_key("COMMAND_HAND_LER") or os.environ.get("COMMAND_HAND_LER", r".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    # set this with required folder path to act as temparary folder
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    # For custom stickerpack names
    CUSTOM_STICKER_PACKNAME = os.environ.get("CUSTOM_STICKER_PACKNAME", None)
    # time to update autoprofile cmds
    CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
    # SpamWatch, CAS, SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    # is dual logging needed or not true or false
    DUAL_LOG = os.environ.get("DUAL_LOG", False)
    # progress bar progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "▰")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR", "▱")
    DEVS = os.environ.get("DEVS", "$")
    SUDO_ENABLED = False
    # API VARS FOR USERBOT
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture for screen shot
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Genius lyrics get this value from https://genius.com/developers both has
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    # Get your own API key from https://www.remove.bg/
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)  
    RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    DEEP_AI = os.environ.get("DEEP_AI", None)
    ALLOW_NSFW = os.environ.get("ALLOW_NSFW", "False")
    MAX_MESSAGE_SIZE_LIMIT = 4095
    LOAD = []  
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )   
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )    
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))    
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")    
    SUDO_USERS: Set[int] = set()
    LOGO = None
    LOG_GRP = PRIVATE_GROUP_BOT_API_ID
    COMMAND_HANDLER = COMMAND_HAND_LER
    SUDO_USERS = SUDO_USERS
    AFS = list(SUDO_USERS)
    CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "🐼")
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    FBAN_GROUP = int(os.environ.get("FBAN_GROUP", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/AllTeamPanda/PandaX_Userbot"
    )
    ALIVE_IMG = os.environ.get(
        "ALIVE_IMG", "https://telegra.ph/file/8f0e9e25427f9da09e08a.jpg"
    )
    PLUGINS_REPO = os.environ.get("PLUGINS_REPO", "https://github.com/AllTeamPanda/Plugins")
    if bool(PLUGINS_REPO and (PLUGINS_REPO.lower() != "false")):
        if not url(PLUGINS_REPO):
            PLUGINS_REPO = "https://github.com/AllTeamPanda/Plugins"
    else:
        PLUGINS_REPO = None
    VC_REPO = os.environ.get("VC_REPO", None)
    if bool(VC_REPO and (VC_REPO.lower() != "false")):
        if not url(VC_REPO):
            VC_REPO = "https://github.com/AllTeamPanda/VCPlayer"
    else:
        VC_REPO = None   
    U_BRANCH = "main"
    HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
    V_T_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
    TAG_LOGGER = os.environ.get("TAG_LOGGER", False)
    PM_PSW = bool(strtobool(str(os.environ.get("PM_PSW", True))))
    MAIN_NO_LOAD = [x for x in os.environ.get("MAIN_NO_LOAD", "").split(',')]
    XTRA_NO_LOAD = [x for x in os.environ.get("XTRA_NO_LOAD", "").split(',')]
    DISABLED_SUDO_CMD_S = os.environ.get("DISABLED_SUDO_CMD_S", None)
    ENABLE_WAIFU_FOR_ALL_CHATS = bool(strtobool(str(os.environ.get("ENABLE_WAIFU_FOR_ALL_CHATS", False))))
    CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH", "/usr/bin/chromedriver")
    CHROME_BIN_PATH = os.environ.get("CHROME_BIN_PATH", "/usr/bin/google-chrome-stable")
    TZ = os.environ.get("TZ", "Asia/Jakarta")
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    LOAD_UNOFFICIAL_PLUGINS = bool(strtobool(str(os.environ.get("LOAD_UNOFFICIAL_PLUGINS", True))))



class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
