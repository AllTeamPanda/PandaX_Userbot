# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import sys


import Panda
from .core.session import PandaBot
from .utils import loads, buka, setup_bot, join, P, M, V, A

LOGS = Panda.core.logger.logging.getLogger("PandaUserbot")

print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)

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
    await loads(f"{P}")
    await loads(f"{M}")
    await buka(f"{V}")
    await buka(f"{A}")
    

print("🛠 Sedang memperoses.....")
PandaBot.loop.run_until_complete(memulai())
print("Berhasil Mengaktifkan Userbot")
PandaBot.loop.run_until_complete(join())

LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{Panda.__version__} [TELAH DIAKTIFKAN]")

if len(sys.argv) not in (1, 3, 4):
    PandaBot.disconnect()
else:
    PandaBot.run_until_disconnected()
