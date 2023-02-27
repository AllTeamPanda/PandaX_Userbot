# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


from pyrogram import Client
from .classbot import Pyrobot
from .._database._var import Database

loop = None
from .._database import DatabaseCute
DB = DatabaseCute()


if DB.getdb("PyroSESSION") or Database.PyroSESSION:
    pyrobot = Client(
        DB.getdb("PyroSESSION") or Database.PyroSESSION,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot = None
if DB.getdb("PyroSESSION2") or Database.PyroSESSION2:
    pyrobot2 = Client(
        DB.getdb("PyroSESSION2") or Database.PyroSESSION2,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot2 = None
if DB.getdb("PyroSESSION3") or Database.PyroSESSION3:
    pyrobot3 = Client(
        DB.getdb("PyroSESSION3") or Database.PyroSESSION3,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot3 = None
if DB.getdb("PyroSESSION4") or Database.PyroSESSION4:
    pyrobot4 = Client(
        DB.getdb("PyroSESSION4") or Database.PyroSESSION4,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot4 = None

if DB.getdb("PyroSESSION") or Database.PyroSESSION and DB.getdb("BOT_TOKEN") or Database.BOT_TOKEN:
    pyrotgbot = Pyrobot()
else:
    pyrotgbot = None

from .classpyro import SuperClient

if DB.getdb("PyroSESSION") or Database.PyroSESSION:
    app = SuperClient()
else:
    app = None
