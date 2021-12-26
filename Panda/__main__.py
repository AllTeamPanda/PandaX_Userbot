# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# PANDA USERBOT
# ILHAM MANSIEZ
# TENTANG AKU DAN DIA


import glob
import os
import sys
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils

import Panda
from Panda import BOTLOG, BOTLOG_CHATID

from .Config import Config
from .core.logger import logging
from .core.session import PandaBot, Bot, Stark
from .helpers.utils import install_pip
from .sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from .sql_helper.globals import gvarstatus
from .utils import load_module, load_modules
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

LOGS = logging.getLogger("PandaUserbot")

print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)

cmdhr = Config.COMMAND_HAND_LER
pandaub = PandaBot

async def setup_bot():
    try:
        await pandaub.start()
        await pandaub.start(bot_token=Config.TG_BOT_USERNAME)
        pandaub.me = await pandaub.get_me()
        pandaub.uid = pandaub.tgbot.uid = utils.get_peer_id(pandaub.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(pandaub.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()

PandaBot.loop.run_until_complete(setup_bot())

path = "Panda/plugins/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(shortname.replace(".py", ""))
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break
            else:
                os.remove(Path(f"Panda/plugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/{shortname}.py"))
            LOGS.info(f"Gagal membuka file {shortname} karena terjadi kesalahan {e}")


path = "Panda/plugins/VCPlugins/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(
                            shortname.replace(".py", ""),
                            plugin_path="Panda/plugins/VCPlugins",
                        )
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

            else:
                os.remove(Path(f"Panda/plugins/VCPlugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/VCPlugins/{shortname}.py"))
            LOGS.info(f"gagal membuka file {shortname} karena terjadi kesalahan {e}")
            LOGS.info(f"{e.args}")



#AsistenBot

path = "Panda/plugins/AsistenBot/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(
                            shortname.replace(".py", ""),
                            plugin_path="Panda/plugins/AsistenBot",
                        )
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

            else:
                os.remove(Path(f"Panda/plugins/AsistenBot/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/AsistenBot/{shortname}.py"))
            LOGS.info(f"gagal membuka file {shortname} karena terjadi kesalahan {e}")
            LOGS.info(f"{e.args}")

path = "Panda/modules/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_modules(
                            shortname.replace(".py", ""),
                            plugin_path="Panda/modules",
                        )
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

            else:
                os.remove(Path(f"Panda/modules/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/modules/{shortname}.py"))
            LOGS.info(f"gagal membuka file {shortname} karena terjadi kesalahan {e}")
            LOGS.info(f"{e.args}")

async def join():
    try:
        await PandaBot(JoinChannelRequest("@UserbotTEAM_Tutorial"))
    except BaseException:
        pass

    
PandaBot.loop.run_until_complete(join())
print("🛠 Sedang memperoses.....")
print("Yay BOT PANDA USERBOT MENYALA.!!!")
print(
    f"Mengaktifkan userbot {cmdhr}ping ⚙ BOT PANDA MENYALAH ⚙\
      \nIf you need assistance, head to https://t.me/TEAMSquadUserbotSupport"
)
print("Berhasil Mengaktifkan Userbot")

LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version 2021 [TELAH DIAKTIFKAN]")

if len(sys.argv) not in (1, 3, 4):
    pandaub.disconnect()
else:
    pandaub.run_until_disconnected()
