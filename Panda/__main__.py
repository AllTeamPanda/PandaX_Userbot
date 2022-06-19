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


def start():
    bot.loop.run_until_complete(loadbot())
    bot.loop.run_until_complete(join())
    bot.loop.run_until_complete(ongrup())

if __name__ == "__main__":
    TelethonPyro()
    start()
    idle()
    
