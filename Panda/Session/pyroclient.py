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
if Database.PyroSESSION2:
    pyrobot2 = Client(
        Database.PyroSESSION2,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot2 = None
if Database.PyroSESSION3:
    pyrobot3 = Client(
        Database.PyroSESSION3,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot3 = None
if Database.PyroSESSION4:
    pyrobot4 = Client(
        Database.PyroSESSION4,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot4 = None

if Database.BOT_TOKEN:
    pyrotgbot = Client(
        "MyAssistant",
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        bot_token=Database.BOT_TOKEN,
        sleep_threshold=180,
    )
else:
    pyrotgbot = None
