# Copyright (C) 2020 Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


##•••••••••••From & import••••••••••••••••
from .Osdb import Osdb
import os
from .Session import *
from .Version import __version__

import logging
import os
import re
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sync import custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

##••••••••••••••••••••••••••



# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CATEGORY = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True
## •••••••••••••••••••

load_dotenv("config.env")

## Time
StartTime = time.time()

def STORAGE(n):
    return Storage(Path("data") / n)

repo = Repo()
branch = repo.active_branch.name

Botver = __version__
## 
BOT_VER = __version__

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "Anda HARUS memiliki python setidaknya versi 3.9."
        "Beberapa fitur tergantung versi python ini. Bot berhenti."
    )
    sys.exit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
)

if CONFIG_CHECK:
    LOGS.info(
        "Harap hapus baris yang disebutkan dalam tagar pertama dari file config.env"
    )
    sys.exit(1)


DEVS = [5057493677, 1593802955]

SUDO_USERS = Osdb.SUDO_USERS
BLACK_CHAT = Osdb.BLACK_CHAT
BLACKLIST_CHAT = Osdb.BLACKLIST_CHAT
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001159103924]
BOTLOG_CHATID = Osdb.BOTLOG_CHATID
BOTLOG = Osdb.BOTLOG
LOGSPAMMER = Osdb.LOGSPAMMER
LOAD = Osdb.LOAD
NO_LOAD = Osdb.NO_LOAD
PM_AUTO_BAN = Osdb.PM_AUTO_BAN
PM_LIMIT = Osdb.PM_LIMIT
HEROKU_APP_NAME = Osdb.HEROKU_APP_NAME
HEROKU_API_KEY = Osdb.HEROKU_API_KEY
WATCH_COUNTRY = Osdb.WATCH_COUNTRY
GIT_REPO_NAME = Osdb.GIT_REPO_NAME
GITHUB_ACCESS_TOKEN = Osdb.GITHUB_ACCESS_TOKEN
UPSTREAM_REPO_URL = Osdb.UPSTREAM_REPO_URL
S_PACK_NAME = Osdb.S_PACK_NAME
OCR_SPACE_API_KEY = Osdb.OCR_SPACE_API_KEY
REM_BG_API_KEY = Osdb.REM_BG_API_KEY
CHROME_DRIVER = Osdb.CHROME_DRIVER
GOOGLE_CHROME_BIN = Osdb.GOOGLE_CHROME_BIN
OPEN_WEATHER_MAP_APPID = Osdb.OPEN_WEATHER_MAP_APPID
WEATHER_DEFCITY = Osdb.WEATHER_DEFCITY
ANTI_SPAMBOT = Osdb.ANTI_SPAMBOT
ANTI_SPAMBOT_SHOUT = Osdb.ANTI_SPAMBOT_SHOUT
COUNTRY = Osdb.COUNTRY
TZ_NUMBER = Osdb.TZ_NUMBER
CLEAN_WELCOME = Osdb.CLEAN_WELCOME
ZIP_DOWNLOAD_DIRECTORY = Osdb.ZIP_DOWNLOAD_DIRECTORY
BITLY_TOKEN = Osdb.BITLY_TOKEN
BIO_PREFIX = Osdb.BIO_PREFIX
DEFAULT_BIO = Osdb.DEFAULT_BIO
LASTFM_API = Osdb.LASTFM_API
LASTFM_SECRET = Osdb.LASTFM_SECRET
LASTFM_USERNAME = Osdb.LASTFM_USERNAME
TEMP_DOWNLOAD_DIRECTORY = Osdb.TEMP_DOWNLOAD_DIRECTORY
DEEZER_ARL_TOKEN = Osdb.DEEZER_ARL_TOKEN
DEEP_AI = Osdb.DEEP_AI
BOT_TOKEN = Osdb.BOT_TOKEN
BOT_USERNAME = Osdb.BOT_USERNAME
HANDLER = Osdb.HANDLER
SUDO_HANDLER = Osdb.SUDO_HANDLER
LASTFM_PASSWORD_PLAIN = Osdb.LASTFM_PASSWORD_PLAIN
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass

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

CMD_HANDLER = HANDLER
WHITELIST = [5057493677, 1593802955]
DEFAULT = [1593802955]


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)


async def check_botlog_chatid() -> None:
    if not BOTLOG_CHATID and BOTLOG:
        LOGS.warning(
            "var BOTLOG_CHATID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var BOTLOG_CHATID"
        )
        sys.exit(1)


async def update_restart_msg(chat_id, msg_id):
    DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
    message = (
        f"**PandaUserBot v{BOT_VER} is back up and running!**\n\n"
        f"**User:** {DEFAULTUSER}"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from .modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            bot.loop.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


with bot:
    try:
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
    except BaseException as a:
        LOGS.info(f"{a}")
