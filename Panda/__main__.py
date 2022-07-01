# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Recode by ilham mansiz


##
from . import LOGS, Pyrogram, bot, pyrobot
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


async def main():
    for bots in bot:
        try:
            await bots.start()
            bots.me = await bots.get_me()
        except Exception:
            LOGS.info(str(e), exc_info=True)
            sys.exit(1)

## Telethon
def start():
    if bots:
        bots.loop.run_until_complete(main())
        bots.loop.run_until_complete(join())
        bots.loop.run_until_complete(ongrup())
    if pyrobot:
        pyrobot.loop.run_until_complete(Pyrogram())
        LOGS.info("PandaUserbot Pyrogram Telah Aktif")

##



if __name__ == "__main__":
    loadbot()
    start()
    idle()

if bot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            bots.disconnect()
        else:
            bots.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if pyrobot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            pyrobot.disconnect()
        else:
            pyrobot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)


