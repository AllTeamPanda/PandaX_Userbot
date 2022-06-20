
from logging import getLogger
import pyrogram as pandapyro
from .client import bot, vcbot
from .pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4, pyrotgbot
import sys
LOGS = getLogger(__name__)

from ..file import Database

def Telethon():
    if Database.SESSION:
        try:
            bot.start()
            vcbot.start()
            bot.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)

 
async def Pyrogram():
    if pyrotgbot:
        await pyrotgbot.start()
        pyrotgbot.me = await pyrotgbot.get_me()
    if pyrobot:
        await pyrobot.start()
        pyrobot.me = await pyrobot.get_me()
        pyrobot.has_a_bot = True if bot else False
    if pyrobot2:
        await pyrobot2.start()
        pyrobot2.me = await pyrobot2.get_me()
        pyrobot2.has_a_bot = True if bot else False
    if pyrobot3:
        await pyrobot3.start()
        pyrobot3.me = await pyrobot3.get_me()
        pyrobot3.has_a_bot = True if bot else False
    if pyrobot4:
        await pyrobot4.start()
        pyrobot.me = await pyrobot4.get_me()
        pyrobot4.has_a_bot = True if bot else False
    
    await pandapyro.idle()
