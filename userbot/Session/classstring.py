# Panda - UserBot
# Copyright (C) 2023-2024 Panda Userbot

# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz

from .._database._var import Var
from .._database import pdB
import base64
import ipaddress
import struct
import sys
import logging
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession
from ..versions import __version__

LOGS = logging.getLogger("PandaUserbot")
_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}
SESSION_STRING_FORMAT = ">BI?256sQ?"

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


def PyroSession(session_string, logger=LOGS, _exit=True):
    if session_string:
        # For Pyrogram Session
        if len(session_string) in _PYRO_FORM.keys():
            return session_string
            
        # For Telethon Session
        elif session_string.startswith(CURRENT_VERSION):
            if len(session_string):
                if session_string[0] != CURRENT_VERSION:
                    raise ValueError("Not a valid string")
                session_string = session_string[1:]
                ip_len = 4 if len(session_string) == 352 else 16
                data_ = struct.unpack(
                       _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(session_string)
                   )
                dc_id, auth_key = data_[0], data_[3]
                test_mode = False
                user_id = Var.OWNER_ID
                is_bot = False
                api_id = Var.APP_ID
                session_string = base64.urlsafe_b64encode(struct.pack(SESSION_STRING_FORMAT, dc_id, api_id, test_mode, auth_key, user_id, is_bot)).decode().rstrip("=")    
            return session_string
        else:
            logger.exception("Wrong string session. Copy paste correctly!")
            if _exit:
                sys.exit()
    logger.exception("No String Session found. Quitting...")
    if _exit:
        sys.exit()
