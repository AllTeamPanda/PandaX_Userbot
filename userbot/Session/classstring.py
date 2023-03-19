# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#for session

# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz

from .._database._var import Var
import base64
import ipaddress
import struct
import sys
import logging
LOGS = logging.getLogger("PandaUserbot")
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession
from telethon.crypto import AuthKey
from ..versions import __version__
_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}

# https://github.com/pyrogram/pyrogram/blob/master/docs/source/faq/what-are-the-ip-addresses-of-telegram-data-centers.rst

DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}

SESSION_STRING_FORMAT = ">BI?256sQ?"
_TELEHON_FORM = {353: ">B{}sH256s"}


OLD_SESSION_STRING_FORMAT = ">B{}sH256s"
OLD_SESSION_STRING_FORMAT_64 = ">B{}sH256s"
SESSION_STRING_SIZE = 351
SESSION_STRING_SIZE_64 = 356



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


def PyroSession(session_name, logger=LOGS, _exit=True):
    if session_name:
        # Pyrogram Session
        if session_name:
            return session_name

        # Telethon to pyro Session
        elif session_name: 
            if session_name:
                if session_name[0] != CURRENT_VERSION:
                    logger.exception("Wrong string session. Copy paste correctly!")
            session_name = session_name[1:]
            ip_len = 4 if len(session_name) == 352 else 16
            dc_id, ip, port, key = struct.unpack(
                _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(session_name))
            server_address = ipaddress.ip_address(ip).compressed

            if any(key):
                auth_key = AuthKey(key)
            
            auth_key = key
            api_id = False
            test_mode = key
            user_id = False
            is_bot = False
            FORMAT2 = base64.urlsafe_b64encode(
                    struct.pack(
                        OLD_SESSION_STRING_FORMAT,
                        dc_id,
                        api_id,
                        test_mode,
                        auth_key,
                        user_id,
                        is_bot,
                    )
                ).decode('ascii')
            
            FORMAT3 = base64.urlsafe_b64encode(
                    struct.pack(
                        OLD_SESSION_STRING_FORMAT_64,
                        dc_id,
                        api_id,
                        test_mode,
                        auth_key,
                        user_id,
                        is_bot,
                    )
                ).decode('ascii')

            FORMAT = base64.urlsafe_b64encode(
                    struct.pack(
                        SESSION_STRING_FORMAT,
                        dc_id,
                        api_id,
                        test_mode,
                        auth_key,
                        user_id,
                        is_bot,
                    )
                ).decode('ascii')

            return FORMAT, FORMAT2, FORMAT3
        else:
            logger.exception("Wrong string session. Copy paste correctly!")
            if _exit:
                sys.exit()
    logger.exception("No String Session found. Quitting...")
    if _exit:
        sys.exit()
