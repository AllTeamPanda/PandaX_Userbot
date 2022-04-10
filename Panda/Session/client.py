from telethon.sessions import StringSession
from telethon import TelegramClient
from ..file import Database
from ..Version import __version__
from pytgcalls import PyTgCalls
import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

"""
if Database.SESSION:
    session_name = str(Database.SESSION)
    bot = TelegramClient(StringSession(session_name), Database.APP_ID, Database.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Database.APP_ID, Database.API_HASH)

"""
loop = None

try:    
    if Database.SESSION:
        session_name = str(Database.SESSION)
        bot = TelegramClient(
           session=StringSession(str(session_name)),
           api_id=Database.APP_ID,
           api_hash=Database.API_HASH,
           loop=loop,
           app_version=__version__,
           connection=ConnectionTcpAbridged,
           auto_reconnect=True,
           connection_retries=None,
            )
    else:
         session_name = "startup"
         bot = TelegramClient(session_name, Database.APP_ID, Database.API_HASH)
    if Database.BOT_TOKEN is not None:
        tgbot = TelegramClient(
           "SESSION",
           api_id=Database.APP_ID,
           api_hash=Database.API_HASH,
           loop=loop,
           app_version=__version__,
           connection=ConnectionTcpAbridged,
           auto_reconnect=True,
           connection_retries=None,
            ).start(bot_token=Database.BOT_TOKEN) 
except Exception as e:
    print(f"STRING_SESSION {str(e)}")
    sys.exit()


vcbot = PyTgCalls(bot)
