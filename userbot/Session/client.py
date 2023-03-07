# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#for session

# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
import base64
import ipaddress
import struct
import sys

from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession

from .._database._var import Var, Database

import os

from .._misc.client import PandaUserbotSession, TelegramClient
from .._misc.botclient import PandaUserbotToken
from .._database import pyDatabase
DB = pyDatabase()

import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
CEKBOT = "5293882146:AAFQIjmaC9ObBu98PAvctLu0QxkckfOJrz4"

LOGS = logging.getLogger("PandaUserbot")
loop = None


BOT_MODE = DB.get_key("MODE_DUAL")
DUAL_MODE = DB.get_key("DUAL_MODE")

##•••••••••••••••Recode by Ilham mansiz••||||•••
## Mode Userbot



_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}

# https://github.com/pyrogram/pyrogram/blob/master/docs/source/faq/what-are-the-ip-addresses-of-telegram-data-centers.rst

DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}


def PandaSession(session, logger=LOGS, _exit=True):
    if session:
        # Telethon Session
        if session.startswith(CURRENT_VERSION):
            if len(session.strip()) != 353:
                logger.exception("Wrong string session. Copy paste correctly!")
                sys.exit()
            return StringSession(session)

        # Pyrogram Session
        elif len(session) in _PYRO_FORM.keys():
            data_ = struct.unpack(
                _PYRO_FORM[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )
            if len(session) in [351, 356]:
                auth_id = 2
            else:
                auth_id = 3
            dc_id, auth_key = data_[0], data_[auth_id]
            return StringSession(
                CURRENT_VERSION
                + base64.urlsafe_b64encode(
                    struct.pack(
                        _STRUCT_PREFORMAT.format(4),
                        dc_id,
                        ipaddress.ip_address(DC_IPV4[dc_id]).packed,
                        443,
                        auth_key,
                    )
                ).decode("ascii")
            )
        else:
            logger.exception("Wrong string session. Copy paste correctly!")
            if _exit:
                sys.exit()
    logger.exception("No String Session found. Quitting...")
    if _exit:
        sys.exit()




try:
    if Var.STRING_SESSION:
        PandaBot = PandaUserbotSession(
            PandaSession(Var.STRING_SESSION, LOGS),
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
            PandaSession(Var.STRING_SESSION2, LOGS),
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
            PandaSession(Var.STRING_SESSION3, LOGS),
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
    if Var.STRING_SESSION and Database.BOT_TOKEN:
        tgbot = PandaUserbotToken(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        ).start(bot_token=Database.BOT_TOKEN)

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
    if Var.STRING_SESSION:
        vcbot = TelegramClient(
            PandaSession(Var.STRING_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
    else:
        vcbot = None
except Exception as e:
    print(f"STRING_SESSION- {str(e)}")
    sys.exit()



