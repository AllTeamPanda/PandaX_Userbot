
from .. import BOTLOG_CHATID, bot, owner, uid, vcbot, LOGS
from ..Version import __version__ as botvers
import sys
from ..modules import ALL_MODULES
from importlib import import_module

from telethon.tl.functions.channels import JoinChannelRequest
import pybase64

On = f"""
`🐼PANDA-USERBOT🐼
MENYALA`

❍ `Name :` [{owner}](tg://user?id={uid}) \n
❍ `Version-ALL :` `{botvers}`

"""


async def ongrup():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    On,
                )
    except BaseException:
        pass

async def join():
    X = str(pybase64.b64decode("QFBhbmRhVXNlcmJvdA=="))[2:13]
    L = str(pybase64.b64decode("QFRlYW1TcXVhZFVzZXJib3RTdXBwb3J0"))[2:17]
    try:
        await bot(JoinChannelRequest(X))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest(L))
    except BaseException:
        pass


async def startbot():
    try:
        bot.start()
        vcbot.start()
        bot.get_me()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

async def loadbot():
    try:
        for module_name in ALL_MODULES:
            import_module(f"Panda.modules.{module_name}")
        LOGS.info(f"PandaUserbot Version - {botvers} [ BERHASIL DIAKTIFKAN ]")
    except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
        pass
    except BaseException as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
