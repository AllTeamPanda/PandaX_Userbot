# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import userbot
from userbot import LOGS, Database, Config
import contextlib
from .Session.multisession_ import *

cmdhr = Config.COMMAND_HAND_LER



from . import resources


"""
async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")
"""

def start():
    userbot.LOOP.run_until_complete(resources.ClientMultiTelethon())
    userbot.LOOP.run_until_complete(resources.memulai())
    #userbot.LOOP.run_until_complete(resources.cloneplugins())
    #userbot.LOOP.run_until_complete(resources.clonevc())
    userbot.LOOP.run_until_complete(resources.join())
    LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")
    if PandaBot:
        PandaBot.send_message(PRIVATE, THON_ON.format(PandaBot.me.username, userbot.__version__, cmdhr, total))
    if PandaBot2:
        PandaBot2.send_message(PRIVATE, THON_ON.format(PandaBot2.me.username, userbot.__version__, cmdhr, total))
    if PandaBot3:
        PandaBot3.send_message(PRIVATE, THON_ON.format(PandaBot3.me.username, userbot.__version__, cmdhr, total))
             


if __name__ == "__main__":
    if pdB.get_key("SESSION") or Database.SESSION:
        usersss = Telethon()
        total = 50 - usersss
        start()
        LOGS.info(f"Total Clients = {total} Users")
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION:
        Pyrogram()
        
    
if PandaBot:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot.run_until_disconnected()
        else:
            PandaBot.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot2:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot2.run_until_disconnected()
        else:
            PandaBot2.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot3:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot3.run_until_disconnected()
        else:
            PandaBot3.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot4:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot4.run_until_disconnected()
        else:
            PandaBot4.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot5:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot5.run_until_disconnected()
        else:
            PandaBot5.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot6:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot6.run_until_disconnected()
        else:
            PandaBot6.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if PandaBot7:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot7.run_until_disconnected()
        else:
            PandaBot7.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if PandaBot8:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot8.run_until_disconnected()
        else:
            PandaBot8.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot9:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot9.run_until_disconnected()
        else:
            PandaBot9.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot10:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot10.run_until_disconnected()
        else:
            PandaBot10.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot11:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot11.run_until_disconnected()
        else:
            PandaBot11.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot12:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot12.run_until_disconnected()
        else:
            PandaBot12.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot13:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot13.run_until_disconnected()
        else:
            PandaBot13.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot14:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot14.run_until_disconnected()
        else:
            PandaBot14.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot15:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot15.run_until_disconnected()
        else:
            PandaBot15.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot16:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot16.run_until_disconnected()
        else:
            PandaBot16.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot17:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot17.run_until_disconnected()
        else:
            PandaBot17.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot18:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot18.run_until_disconnected()
        else:
            PandaBot18disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot19:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot19.run_until_disconnected()
        else:
            PandaBot19.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot20:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot21.run_until_disconnected()
        else:
            PandaBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot21:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot21.run_until_disconnected()
        else:
            PandaBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot22:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot22.run_until_disconnected()
        else:
            PandaBot22.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot23:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot23.run_until_disconnected()
        else:
            PandaBot23.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot24:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot24.run_until_disconnected()
        else:
            PandaBot24.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot25:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot25.run_until_disconnected()
        else:
            PandaBot25.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot26:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot26.run_until_disconnected()
        else:
            PandaBot26.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot27:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot27.run_until_disconnected()
        else:
            PandaBot27.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot28:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot28.run_until_disconnected()
        else:
            PandaBot28.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot29:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot29.run_until_disconnected()
        else:
            PandaBot29.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot30:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot30.run_until_disconnected()
        else:
            PandaBot30.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot31:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot31.run_until_disconnected()
        else:
            PandaBot31.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot32:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot32.run_until_disconnected()
        else:
            PandaBot32.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot33:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot33.run_until_disconnected()
        else:
            PandaBot33.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot34:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot34.run_until_disconnected()
        else:
            PandaBot34.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot36:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot36.run_until_disconnected()
        else:
            PandaBot36.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot37:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot37.run_until_disconnected()
        else:
            PandaBot37.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot38:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot38.run_until_disconnected()
        else:
            PandaBot38.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot39:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot39.run_until_disconnected()
        else:
            PandaBot39.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot40:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot40.run_until_disconnected()
        else:
            PandaBot40.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot41:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot41.run_until_disconnected()
        else:
            PandaBot41.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot42:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot42.run_until_disconnected()
        else:
            PandaBot42.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot43:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot43.run_until_disconnected()
        else:
            PandaBot43.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot44:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot44.run_until_disconnected()
        else:
            PandaBot44.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot45:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot45.run_until_disconnected()
        else:
            PandaBot45.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot46:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot46.run_until_disconnected()
        else:
            PandaBot46.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot47:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot47.run_until_disconnected()
        else:
            PandaBot47.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot48:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot48.run_until_disconnected()
        else:
            PandaBot48.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot49:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot49.run_until_disconnected()
        else:
            PandaBot49.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if PandaBot35:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot35.run_until_disconnected()
        else:
            PandaBot35.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
        
if PandaBot50:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                PandaBot50.run_until_disconnected()
        else:
            PandaBot50.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
