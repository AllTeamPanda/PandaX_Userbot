from pyrogram import Client
from pyrogram.types import *

from ..file import Database
from ..Version import __version__
from pytgcalls import PyTgCalls
import sys


try:    
    if Database.PyroSESSION:
        bot = Client(
        Database.PyroSESSION,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
    else:
         session_name = "startup"
         bot = Client(session_name, Database.APP_ID, Database.API_HASH)
    if Database.BOT_TOKEN is not None:
        tgbot = Client(
           "SESSION",
           api_id=Database.APP_ID,
           api_hash=Database.API_HASH,
           loop=loop,
           app_version=__version__,
           sleep_threshold=180,
            ).start(bot_token=Database.BOT_TOKEN) 
except Exception as e:
    print(f"STRING_SESSION {str(e)}")
    sys.exit()


vcbot = PyTgCalls(bot)
