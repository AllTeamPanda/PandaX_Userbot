# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Recode by ilham mansiz


##
import pyrogram as pandapyro
from . import TelethonPyro, bot, LOGS, pyrotgbot
from .database import join, loadbot, ongrup
from pytgcalls import idle
import sys
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

## Telethon
def start():
    if bot:
        bot.loop.run_until_complete(join())
        bot.loop.run_until_complete(ongrup())
##

## Asisten Pyrogram

def run_bot():
    if pyrotgbot:
        await pyrotgbot.start()
        pyrotgbot.me = await pyrotgbot.get_me()
    await pandapyro.idle()


if __name__ == "__main__":
    TelethonPyro()
    loadbot()
    start()
    run_bot()
    idle()

if bot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            bot.disconnect()
        else:
            bot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
