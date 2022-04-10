# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Recode by ilham mansiz


##
import sys
from importlib import import_module
from . import Botver, LOGS, bot, vcbot
from .database import ongrup, join
from .modules import ALL_MODULES
from pytgcalls import idle
##


try:
    bot.start()
    vcbot.start()
    user = bot.get_me()
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"Panda.modules.{module_name}")
    LOGS.info(f"PandaUserbot Version - {Botver} [ BERHASIL DIAKTIFKAN ]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

bot.loop.run_until_complete(join())
bot.loop.run_until_complete(ongrup())

idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
