# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import userbot
from userbot import LOGS, Database, Config

from .Session.multisession_ import *

cmdhr = Config.COMMAND_HAND_LER



from . import resources


"""
async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")
"""

def start():
    userbot.LOOP.run_until_complete(resources.memulai())
    userbot.LOOP.run_until_complete(resources.join())
    LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")
    if PandaBot:
        PandaBot.send_message(PRIVATE, THON_ON.format(PandaBot.me.username, userbot.__version__, cmdhr))
    if PandaBot2:
        PandaBot2.send_message(PRIVATE, THON_ON.format(PandaBot2.me.username, userbot.__version__, cmdhr))
    if PandaBot3:
        PandaBot3.send_message(PRIVATE, THON_ON.format(PandaBot3.me.username, userbot.__version__, cmdhr))
             


if __name__ == "__main__":
    if pdB.get_key("SESSION") or Database.SESSION:
        Telethon()
        resources.ClientMultiTelethon()
        start()
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION:
        Pyrogram()
        
    
if PandaBot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot.disconnect()
        else:
            PandaBot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot2:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot2.disconnect()
        else:
            PandaBot2.run_until_disconnected()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot3:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot3.disconnect()
        else:
            PandaBot3.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot4:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot4.disconnect()
        else:
            PandaBot4.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot5:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot5.disconnect()
        else:
            PandaBot5.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot6:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot6.disconnect()
        else:
            PandaBot6.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot6:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot6.disconnect()
        else:
            PandaBot6.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot7:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot7.disconnect()
        else:
            PandaBot7.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot7:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot7.disconnect()
        else:
            PandaBot7.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot8:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot8.disconnect()
        else:
            PandaBot8.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot8:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot8.disconnect()
        else:
            PandaBot8.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot9:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot9.disconnect()
        else:
            PandaBot9.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot10:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot10.disconnect()
        else:
            PandaBot10.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot11:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot11.disconnect()
        else:
            PandaBot11.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot12:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot12.disconnect()
        else:
            PandaBot12.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot13:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot13.disconnect()
        else:
            PandaBot13.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot14:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot14.disconnect()
        else:
            PandaBot14.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot15:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot15.disconnect()
        else:
            PandaBot15.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot16:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot16.disconnect()
        else:
            PandaBot16.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot17:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot17.disconnect()
        else:
            PandaBot17.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot18:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot18.disconnect()
        else:
            PandaBot18.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot19:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot19.disconnect()
        else:
            PandaBot19.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot20:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot20.disconnect()
        else:
            PandaBot20.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot21:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot21.disconnect()
        else:
            PandaBot21.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot22:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot22.disconnect()
        else:
            PandaBot22.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot23:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot23.disconnect()
        else:
            PandaBot23.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot24:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot24.disconnect()
        else:
            PandaBot24.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot25:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot25.disconnect()
        else:
            PandaBot25.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot26:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot26.disconnect()
        else:
            PandaBot26.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot27:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot27.disconnect()
        else:
            PandaBot27.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot28:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot28.disconnect()
        else:
            PandaBot28.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot29:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot29.disconnect()
        else:
            PandaBot29.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot30:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot30.disconnect()
        else:
            PandaBot30.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot31:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot31.disconnect()
        else:
            PandaBot31.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot32:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot32.disconnect()
        else:
            PandaBot32.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot33:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot33.disconnect()
        else:
            PandaBot33.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot34:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot35.disconnect()
        else:
            PandaBot35.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot36:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot36.disconnect()
        else:
            PandaBot36.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot37:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot37.disconnect()
        else:
            PandaBot37.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot38:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot38.disconnect()
        else:
            PandaBot38.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot39:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot39.disconnect()
        else:
            PandaBot39.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot40:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot40.disconnect()
        else:
            PandaBot40.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot41:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot41.disconnect()
        else:
            PandaBot41.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot42:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot42.disconnect()
        else:
            PandaBot42.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot43:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot43.disconnect()
        else:
            PandaBot43.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot44:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot44.disconnect()
        else:
            PandaBot44.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot45:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot45.disconnect()
        else:
            PandaBot45.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot46:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot46.disconnect()
        else:
            PandaBot46.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot47:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot47.disconnect()
        else:
            PandaBot47.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot48:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot48.disconnect()
        else:
            PandaBot48.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot49:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot49.disconnect()
        else:
            PandaBot49.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot50:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot50.disconnect()
        else:
            PandaBot50.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
