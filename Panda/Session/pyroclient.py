from pyrogram import Client

from ..file import Database
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
    if Database.PyroSESSION2:
        pyrobot2 = Client(
        Database.PyroSESSION2,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
    else:
         session_name = None
         pyrobot2 = session_name
    if Database.PyroSESSION3:
        pyrobot3 = Client(
        Database.PyroSESSION3,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
    else:
         session_name = None
         pyrobot3 = session_name
    if Database.PyroSESSION4:
        pyrobot4 = Client(
        Database.PyroSESSION4,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
    else:
         session_name = None
         pyrobot4 = session_name
    if Database.BOT_TOKEN is not None:
        pyrotgbot = Client(
           "SESSION",
           api_id=Database.APP_ID,
           api_hash=Database.API_HASH,
           bot_token=Database.BOT_TOKEN,
           sleep_threshold=180,
            ) 
except Exception as e:
    print(f"PyroSESSION {str(e)}")
    sys.exit()


