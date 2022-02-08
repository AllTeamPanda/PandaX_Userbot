# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import glob
import os
import sys
from pathlib import Path

from telethon import utils

import Panda

from .Config import Config
from .core.logger import logging
from .core.session import PandaBot
from .helpers.utils import install_pip
from .utils import loads, buka, setup_bot, join
from importlib import import_module
from Panda.modules import ALL_MODULES

LOGS = logging.getLogger("PandaUserbot")

print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)

cmdhr = Config.COMMAND_HAND_LER
pandaub = PandaBot

## Memulai ••••••••••√√√√√•••••••

try:
    LOGS.info("Memulai PandaUserbot")
    PandaBot.loop.run_until_complete(setup_bot())
    LOGS.info("Asistant Bot berhasil")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

## Install Modules ••••••√√√√√••••••

async def memulai():
    await loads("plugins")
    await loads("modules")
    await buka("VCPlugins")
    await buka("AsistenBot")
    PandaBot.loop.run_until_complete(join())


print("🛠 Sedang memperoses.....")
PandaBot.loop.run_until_complete(memulai())
print("Berhasil Mengaktifkan Userbot")

LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version 2021 [TELAH DIAKTIFKAN]")

if len(sys.argv) not in (1, 3, 4):
    PandaBot.disconnect()
else:
    PandaBot.run_until_disconnected()
