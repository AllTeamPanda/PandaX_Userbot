# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import sys
import Panda

LOGS = Panda.core.logger.logging.getLogger("PandaUserbot")
print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)


## Memulai ••••••••••√√√√√•••••••

try:
    LOGS.info("Memulai PandaUserbot")
    Panda.core.session.PandaBot.loop.run_until_complete(Panda.utils.setup_bot())
    LOGS.info("Asistant Bot berhasil")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

## Install Modules ••••••√√√√√••••••

async def memulai():
    await Panda.utils.loads(f"{P}")
    await Panda.utils.loads(f"{M}")
    await Panda.utils.buka(f"{V}")
    await Panda.utils.buka(f"{A}")
    

print("🛠 Sedang memperoses.....")
Panda.core.session.PandaBot.loop.run_until_complete(memulai())
print("Berhasil Mengaktifkan Userbot")
Panda.core.session.PandaBot.loop.run_until_complete(Panda.utils.join())

LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{Panda.__version__} [TELAH DIAKTIFKAN]")

if len(sys.argv) not in (1, 3, 4):
    Panda.core.session.PandaBot.disconnect()
else:
    Panda.core.session.PandaBot.run_until_disconnected()
