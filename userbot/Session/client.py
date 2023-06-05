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





## SESSION MUTLTI 50

try:
    if DB.get_key("SESSION4") or Var.STRING_SESSION4:
        PandaBot4 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION4") or Var.STRING_SESSION4, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot4 = None
except Exception as e:
    print(f"STRING_SESSION4- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION5") or Var.STRING_SESSION5:
        PandaBot5 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION5") or Var.STRING_SESSION5, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot5 = None
except Exception as e:
    print(f"STRING_SESSION5- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION6") or Var.STRING_SESSION6:
        PandaBot6 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION6") or Var.STRING_SESSION6, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot6 = None
except Exception as e:
    print(f"STRING_SESSION6- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION7") or Var.STRING_SESSION7:
        PandaBot7 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION7") or Var.STRING_SESSION7, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot7 = None
except Exception as e:
    print(f"STRING_SESSION7- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION8") or Var.STRING_SESSION8:
        PandaBot8 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION8") or Var.STRING_SESSION8, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot8 = None
except Exception as e:
    print(f"STRING_SESSION8- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION9") or Var.STRING_SESSION9:
        PandaBot9 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION9") or Var.STRING_SESSION9, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot9 = None
except Exception as e:
    print(f"STRING_SESSION9- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION10") or Var.STRING_SESSION10:
        PandaBot10 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION10") or Var.STRING_SESSION10, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot10 = None
except Exception as e:
    print(f"STRING_SESSION10- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION11") or Var.STRING_SESSION11:
        PandaBot11 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION11") or Var.STRING_SESSION11, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot11 = None
except Exception as e:
    print(f"STRING_SESSION11- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION12") or Var.STRING_SESSION12:
        PandaBot12 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION12") or Var.STRING_SESSION12, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot12 = None
except Exception as e:
    print(f"STRING_SESSION12- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION13") or Var.STRING_SESSION13:
        PandaBot13 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION13") or Var.STRING_SESSION13, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot13 = None
except Exception as e:
    print(f"STRING_SESSION13- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION14") or Var.STRING_SESSION14:
        PandaBot14 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION14") or Var.STRING_SESSION14, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot14 = None
except Exception as e:
    print(f"STRING_SESSION14- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION15") or Var.STRING_SESSION15:
        PandaBot15 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION15") or Var.STRING_SESSION15, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot15 = None
except Exception as e:
    print(f"STRING_SESSION15- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION16") or Var.STRING_SESSION16:
        PandaBot16 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION16") or Var.STRING_SESSION16, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot16 = None
except Exception as e:
    print(f"STRING_SESSION16- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION17") or Var.STRING_SESSION17:
        PandaBot17 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION17") or Var.STRING_SESSION17, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot17 = None
except Exception as e:
    print(f"STRING_SESSION3- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION18") or Var.STRING_SESSION18:
        PandaBot18 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION18") or Var.STRING_SESSION18, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot18 = None
except Exception as e:
    print(f"STRING_SESSION18- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION19") or Var.STRING_SESSION19:
        PandaBot19 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION19") or Var.STRING_SESSION19, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot19 = None
except Exception as e:
    print(f"STRING_SESSION19- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION20") or Var.STRING_SESSION20:
        PandaBot20 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION20") or Var.STRING_SESSION20, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot20 = None
except Exception as e:
    print(f"STRING_SESSION20- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION21") or Var.STRING_SESSION21:
        PandaBot21 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION21") or Var.STRING_SESSION21, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot21 = None
except Exception as e:
    print(f"STRING_SESSION21- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION22") or Var.STRING_SESSION22:
        PandaBot22 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION22") or Var.STRING_SESSION22, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot22 = None
except Exception as e:
    print(f"STRING_SESSION22- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION23") or Var.STRING_SESSION23:
        PandaBot23 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION23") or Var.STRING_SESSION23, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot23 = None
except Exception as e:
    print(f"STRING_SESSION23- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION24") or Var.STRING_SESSION24:
        PandaBot24 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION24") or Var.STRING_SESSION24, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot24 = None
except Exception as e:
    print(f"STRING_SESSION42- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION25") or Var.STRING_SESSION25:
        PandaBot25 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION25") or Var.STRING_SESSION25, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot25 = None
except Exception as e:
    print(f"STRING_SESSION25- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION26") or Var.STRING_SESSION26:
        PandaBot26 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION26") or Var.STRING_SESSION26, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot26 = None
except Exception as e:
    print(f"STRING_SESSION26- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION27") or Var.STRING_SESSION27:
        PandaBot27 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION27") or Var.STRING_SESSION27, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot27 = None
except Exception as e:
    print(f"STRING_SESSION27- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION28") or Var.STRING_SESSION28:
        PandaBot28 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION28") or Var.STRING_SESSION28, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot28 = None
except Exception as e:
    print(f"STRING_SESSION28- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION29") or Var.STRING_SESSION29:
        PandaBot29 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION29") or Var.STRING_SESSION29, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot29 = None
except Exception as e:
    print(f"STRING_SESSION29- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION30") or Var.STRING_SESSION30:
        PandaBot30 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION30") or Var.STRING_SESSION30, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot30 = None
except Exception as e:
    print(f"STRING_SESSION30- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION31") or Var.STRING_SESSION31:
        PandaBot31 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION31") or Var.STRING_SESSION31, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot31 = None
except Exception as e:
    print(f"STRING_SESSION31- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION32") or Var.STRING_SESSION32:
        PandaBot32 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION32") or Var.STRING_SESSION32, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot32 = None
except Exception as e:
    print(f"STRING_SESSION32- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION33") or Var.STRING_SESSION33:
        PandaBot33 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION33") or Var.STRING_SESSION33, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot33 = None
except Exception as e:
    print(f"STRING_SESSION33- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION34") or Var.STRING_SESSION34:
        PandaBot34 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION34") or Var.STRING_SESSION34, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot34 = None
except Exception as e:
    print(f"STRING_SESSION34- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION35") or Var.STRING_SESSION35:
        PandaBot35 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION35") or Var.STRING_SESSION35, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot35 = None
except Exception as e:
    print(f"STRING_SESSION35- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION36") or Var.STRING_SESSION36:
        PandaBot36 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION36") or Var.STRING_SESSION36, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot36 = None
except Exception as e:
    print(f"STRING_SESSION2- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION37") or Var.STRING_SESSION37:
        PandaBot37 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION37") or Var.STRING_SESSION37, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot37 = None
except Exception as e:
    print(f"STRING_SESSION37- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION38") or Var.STRING_SESSION38:
        PandaBot38 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION38") or Var.STRING_SESSION38, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot38 = None
except Exception as e:
    print(f"STRING_SESSION38- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION39") or Var.STRING_SESSION39:
        PandaBot39 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION3") or Var.STRING_SESSION39, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot39 = None
except Exception as e:
    print(f"STRING_SESSION39- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION40") or Var.STRING_SESSION40:
        PandaBot40 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION40") or Var.STRING_SESSION40, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot40 = None
except Exception as e:
    print(f"STRING_SESSION40- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION41") or Var.STRING_SESSION41:
        PandaBot41 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION41") or Var.STRING_SESSION41, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot41 = None
except Exception as e:
    print(f"STRING_SESSION41- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION42") or Var.STRING_SESSION42:
        PandaBot42 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION42") or Var.STRING_SESSION42, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot42 = None
except Exception as e:
    print(f"STRING_SESSION42- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION43") or Var.STRING_SESSION43:
        PandaBot43 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION43") or Var.STRING_SESSION43, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot43 = None
except Exception as e:
    print(f"STRING_SESSION43- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION44") or Var.STRING_SESSION44:
        PandaBot44 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION44") or Var.STRING_SESSION44, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot44 = None
except Exception as e:
    print(f"STRING_SESSION44- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION45") or Var.STRING_SESSION45:
        PandaBot45 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION45") or Var.STRING_SESSION45, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot45 = None
except Exception as e:
    print(f"STRING_SESSION45- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION46") or Var.STRING_SESSION46:
        PandaBot46 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION40") or Var.STRING_SESSION46, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot46 = None
except Exception as e:
    print(f"STRING_SESSION46- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION47") or Var.STRING_SESSION47:
        PandaBot47 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION47") or Var.STRING_SESSION47, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot47 = None
except Exception as e:
    print(f"STRING_SESSION47- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION48") or Var.STRING_SESSION48:
        PandaBot48 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION48") or Var.STRING_SESSION48, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot48 = None
except Exception as e:
    print(f"STRING_SESSION48- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION49") or Var.STRING_SESSION49:
        PandaBot49 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION49") or Var.STRING_SESSION49, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot49 = None
except Exception as e:
    print(f"STRING_SESSION49- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION50") or Var.STRING_SESSION50:
        PandaBot50 = PandaUserbotSession(
            PandaSession(DB.get_key("SESSION50") or Var.STRING_SESSION50, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        PandaBot50 = None
except Exception as e:
    print(f"STRING_SESSION50- {str(e)}")
    sys.exit()

