
from .. import LOGS
from .client import bot, vcbot
from .pyroclient import pyrobot
import sys

from ..file import Database

def TelethonPyro():
    if Database.SESSION:
        try:
            bot.start()
            vcbot.start()
            bot.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)
     
    if Database.PyroSESSION:
        try:
            pyrobot.start()
            pyrobot.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)
