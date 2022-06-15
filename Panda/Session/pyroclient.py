from pyrogram import Client
from pyrogram.types import *

from ..file import Database
from ..Version import __version__
from pytgcalls import PyTgCalls
import sys

loop = None

try:    
    if Database.PyroSESSION:
        pyrobot = Client(
        Database.PyroSESSION,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
    else:
         session_name = None
         pyrobot = session_name
    if Database.BOT_TOKEN is not None:
        pyrotgbot = Client(
           "SESSION",
           api_id=Database.APP_ID,
           api_hash=Database.API_HASH,
           loop=loop,
           app_version=__version__,
           sleep_threshold=180,
            ).start(bot_token=Database.BOT_TOKEN) 
except Exception as e:
    print(f"PyroSESSION {str(e)}")
    sys.exit()


pyrovcbot = PyTgCalls(pyrobot)
