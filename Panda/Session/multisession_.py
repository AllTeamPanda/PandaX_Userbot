
from logging import getLogger

from .client import bot, vcbot
from .pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4, pyrotgbot
import sys
LOGS = getLogger(__name__)

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

    if Database.PyroSESSION2:
        try:
            pyrobot2.start()
            pyrobot2.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)

    if Database.PyroSESSION3:
        try:
            pyrobot3.start()
            pyrobot3.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)

    if Database.PyroSESSION4:
        try:
            pyrobot4.start()
            pyrobot4.get_me()
        except Exception as e:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)

