## Copyright Ilham Mansiez
## Panda Userbot


import sys
import os
os.system("pip3 install --no-cache-dir -r filepanda.txt")

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
LOG_CHANNEL = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from Asisten.autobot import autobot, autousername, setbot, autogrup
from Asisten.autogrup import autopilot
from ..Var import Var
from .client import PandaUserbotSession
from telethon.sync import TelegramClient, custom, events
from pytgcalls import PyTgCalls

__version__ = "Ilham-Mansiz"

loop = None

if Var.STRING_SESSION:
    session = StringSession(str(Var.STRING_SESSION))
else:
    session = "pandauserbot"

try:
    PandaBot = PandaUserbotSession(
        session=session,
        api_id=Var.APP_ID,
        api_hash=Var.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )  
    call = PyTgCalls(PandaBot)
except Exception as e:
    print(f"STRING_SESSION - {str(e)}")
    sys.exit()



if not BOT_TOKEN:
    PandaBot.loop.run_until_complete(autobot())

if not LOG_CHANNEL:
    PandaBot.loop.run_until_complete(autogrup())


PandaBot.tgbot = tgbot = PandaUserbotSession(
    session="BOT_TOKEN",
    api_id=Var.APP_ID,
    api_hash=Var.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=BOT_TOKEN)

Bot = PandaBot
pandabot = PandaBot
Stark = PandaBot

