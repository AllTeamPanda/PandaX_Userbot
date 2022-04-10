# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



from distutils.util import strtobool as sb
import os

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
    
