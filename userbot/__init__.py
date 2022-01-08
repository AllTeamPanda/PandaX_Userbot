#ilham mansiez


import logging
import os
import time
from os import environ
import motor.motor_asyncio
from pyrogram import Client

from .config_var import Config

# Note StartUp Time - To Capture Uptime.
start_time = time.time()
Petercord_version = "V-Mansiez.2021"

# Enable Logging For Pyrogram
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [Petercord_UserbotUB] - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)


mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_DB)

CMD_LIST = {}
XTRA_CMD_LIST = {}
sudo_id = Config.AFS

if not Config.STRINGSESSION:
    logging.error("No String Session Found! Petercord_Userbot is Exiting!")
    quit(1)

if not Config.API_ID:
    logging.error("No Api-ID Found! Petercord_Userbot is Exiting!")
    quit(1)

if not Config.API_HASH:
    logging.error("No ApiHash Found! Petercord_Userbot is Exiting!")
    quit(1)

if not Config.LOG_GRP:
    logging.error("No Log Group ID Found! Petercord_Userbot is Exiting!")
    quit(1)

PLUGINS = dict(
    root="Petercord_Userbot",
    include=[
        "vc." + Config.PLUGIN
    ]
)

# Clients - Upto 4 Clients is Supported!
if Config.STRINGSESSION:
    Petercord_Userbot = Client(
        Config.STRINGSESSION,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=PLUGINS,
        sleep_threshold=180,
    )
if Config.STRINGSESSION_2:
    Petercord_Userbot2 = Client(
        Config.STRINGSESSION_2,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=PLUGINS,
        sleep_threshold=180,
    )
else:
    Petercord_Userbot2 = None
if Config.STRINGSESSION_3:
    Petercord_Userbot3 = Client(
        Config.STRINGSESSION_3,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=PLUGINS,
        sleep_threshold=180,
    )
else:
    Petercord_Userbot3 = None
if Config.STRINGSESSION_4:
    Petercord_Userbot4 = Client(
        Config.STRINGSESSION_4,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=PLUGINS,
        sleep_threshold=180,
    )
else:
    Petercord_Userbot4 = None

if Config.BOT_TOKEN:
    bot = Client(
        "MyAssistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        sleep_threshold=180,
    )
else:
    bot = None
