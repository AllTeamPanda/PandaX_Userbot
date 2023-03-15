# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys


from .._database._var import Var, Database
from ..versions import __version__
import os
from .classstring import *
from .._misc.client import PandaUserbotSession, TelegramClient
from .._misc.botclient import PandaUserbotToken
from .._database import pyDatabase
DB = pyDatabase()

import sys
import logging

BOT_TOKEN = DB.get_key("BOT_TOKEN") or os.environ.get("BOT_TOKEN", None)
CEKBOT = "5293882146:AAFQIjmaC9ObBu98PAvctLu0QxkckfOJrz4"

LOGS = logging.getLogger("PandaUserbot")
loop = None


BOT_MODE = DB.get_key("MODE_DUAL")
DUAL_MODE = DB.get_key("DUAL_MODE")

##•••••••••••••••Recode by Ilham mansiz••||||•••
## Mode Userbot

try:
    if Var.STRING_SESSION:
        PandaBot = PandaUserbotSession(
            PandaSession(Var.STRING_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot = None
except Exception as e:
    print(f"STRING_SESSION- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION2") or Var.STRING_SESSION2:
        PandaBot2 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION2") or Var.STRING_SESSION2, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot2 = None
except Exception as e:
    print(f"STRING_SESSION2- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION3") or Var.STRING_SESSION3:
        PandaBot3 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION3") or Var.STRING_SESSION3, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot3 = None
except Exception as e:
    print(f"STRING_SESSION3- {str(e)}")
    sys.exit()


try:
    if Var.STRING_SESSION and DB.get_key("BOT_TOKEN") or Database.BOT_TOKEN:
        tgbot = PandaUserbotToken(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )

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


try:
    if Var.VC_SESSION:
        vcbot = TelegramClient(
            PandaSession(Var.VC_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vcbot = None
except Exception as e:
    print(f"STRING_SESSION- {str(e)}")
    sys.exit()



from pytgcalls import PyTgCalls

if Var.VC_SESSION:
    call_py = PyTgCalls(vcbot)
else:
    call_py = None
