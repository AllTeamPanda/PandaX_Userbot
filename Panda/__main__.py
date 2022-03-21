# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import sys
import Panda
from Panda import utils
LOGS = Panda.core.logger.logging.getLogger("PandaUserbot")
print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)
from .utils import P, M, V, A


## Memulai ••••••••••√√√√√•••••••

try:
    LOGS.info("Memulai PandaUserbot")
    LOGS.info("Asistant Bot berhasil")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

## Install Modules ••••••√√√√√••••••

async def memulai():
    await utils.loads(f"{P}")
    await utils.loads(f"{M}")
    await utils.buka(f"{V}")
    await utils.buka(f"{A}")
    

def start():
    Panda.PandaBot.loop.run_until_complete(Panda.utils.setup_bot())
    Panda.PandaBot.loop.run_until_complete(memulai())
    Panda.PandaBot.loop.run_until_complete(utils.join())
    Panda.PandaBot.loop.run_until_complete(Panda.utils.ongrup())
    LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{Panda.__version__} [TELAH DIAKTIFKAN]")

if __name__ == "__main__":
    start()
    try:
        Panda.PandaBot.run_until_disconnected()
    except ConnectionError:
        pass
