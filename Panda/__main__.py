# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Recode by ilham mansiz


##
import sys
from . import LOGS, TelethonPyro, bot
from .database import join, loadbot, ongrup
from pytgcalls import idle
from .file import Database
##

"""
try:
    bot.start()
    vcbot.start()
    user = bot.get_me()
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)
"""

if TelethonPyro:
    if Database.SESSION:
        based = "Telethon"
    else:
       Database.PyroSESSION:
        based = "Pyrogram"
    return based if Database.SESSION else based

LOGS.info("{based}")

def start():
    bot.loop.run_until_complete(loadbot())
    bot.loop.run_until_complete(join())
    bot.loop.run_until_complete(ongrup())

if __name__ == "__main__":
    TelethonPyro()
    start()
    idle()
    try:
        if len(sys.argv) not in (1, 3, 4):
            bot.disconnect()
        else:
            bot.run_until_disconnected()
    except Exception as e:
        LOGS.error(f"{e}")
        sys.exit()
    
