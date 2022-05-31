# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Recode by ilham mansiz


##
import sys
from importlib import import_module
from . import Botver, LOGS, bot, vcbot
from .database import ongrup, join, startbot, loadbot
from .modules import ALL_MODULES
from pytgcalls import idle
##


def start():
    bot.loop.run_until_complete(startbot())
    bot.loop.run_until_complete(loadbot())
    bot.loop.run_until_complete(join())
    bot.loop.run_until_complete(ongrup())

if __name__ == "__main__":
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
    
