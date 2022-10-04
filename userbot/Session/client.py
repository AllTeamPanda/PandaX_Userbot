
# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

from .._misc.client import PandaUserbotSession, TelegramClient
from telethon.sessions import StringSession
from .._database._var import Var, Database
from telethon import TelegramClient
import os


from .._database import DatabaseCute
DB = DatabaseCute()

import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging

BOT_TOKEN = DB.getdb("BOT_TOKEN") or os.environ.get("BOT_TOKEN", None)
CEKBOT = "5293882146:AAFQIjmaC9ObBu98PAvctLu0QxkckfOJrz4"

LOGS = logging.getLogger("PandaUserbot")
loop = None


BOT_MODE = DB.getdb("MODE_DUAL")
DUAL_MODE = DB.getdb("DUAL_MODE")

##•••••••••••••••Recode by Ilham mansiz••||||•••
## Mode Userbot



try:
    if Var.STRING_SESSION:
        session = StringSession(str(Var.STRING_SESSION))
        PandaBot = PandaUserbotSession(
            session=session,
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
    else:
        PandaBot = None
except Exception as e:
    print(f"STRING_SESSION- {str(e)}")
    sys.exit()

try:
    if Var.STRING_SESSION2:
        session2 = StringSession(str(Var.STRING_SESSION3))
        PandaBot2 = PandaUserbotSession(
            session=session2,
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
    else:
        PandaBot2 = None
except Exception as e:
    print(f"STRING_SESSION2- {str(e)}")
    sys.exit()

try:
    if Var.STRING_SESSION3:
        session3 = StringSession(str(Var.STRING_SESSION3))
        PandaBot3 = PandaUserbotSession(
            session=session3,
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
    else:
        PandaBot3 = None
except Exception as e:
    print(f"STRING_SESSION3- {str(e)}")
    sys.exit()

try:
    if Database.BOT_TOKEN is not None:
        tgbot = PandaUserbotSession(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        ).start(bot_token=BOT_TOKEN)
    else:
        tgbot = None
except Exception as e:
    print(f"BOT-TOKEN- {str(e)}")
    sys.exit()


CEKBOT = "5293882146:AAFQIjmaC9ObBu98PAvctLu0QxkckfOJrz4"

if CEKBOT:
    cekbot = TelegramClient(
        "MyAssistant",
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
    )
else:
    cekbot = None





