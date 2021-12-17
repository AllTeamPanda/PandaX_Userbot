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
from .utils import load_module
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

LOGS = logging.getLogger("PandaUserbot")

print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)

cmdhr = Config.COMMAND_HAND_LER
pandaub = PandaBot

async def setup_bot():
    try:
        await pandaub.connect()
        config = await pandaub(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == pandaub.session.server_address:
                if pandaub.session.dc_id != option.id:
                    LOGS.warning(
                        f"Fixed DC ID in session from {pandaub.session.dc_id}"
                        f" to {option.id}"
                    )
                pandaub.session.set_dc(option.id, option.ip_address, option.port)
                pandaub.session.save()
                break
        await pandaub.start(bot_token=Config.TG_BOT_USERNAME)
        pandaub.me = await pandaub.get_me()
        pandaub.uid = pandaub.tgbot.uid = utils.get_peer_id(pandaub.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(pandaub.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()

def verifyLoggerGroup():
    if BOTLOG:
        try:
            entity = pandaub.loop.run_until_complete(pandaub.get_entity(BOTLOG_CHATID))
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified Logger group."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified Logger group."
                    )
        except ValueError:
            LOGS.error("Logger group ID cannot be found. " "Make sure it's correct.")
        except TypeError:
            LOGS.error("Logger group ID is unsupported. " "Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the logger group.\n"
                + str(e)
            )
        try:
            entity = pandaub.loop.run_until_complete(
                pandaub.get_entity(Config.PM_LOGGER_GROUP_ID)
            )
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Izin hilang untuk menambahkan pengguna untuk grup Pm Logger yang ditentukan."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Izin hilang untuk menambahkan pengguna untuk grup Pm Logger yang ditentukan."
                    )
        except ValueError:
            LOGS.error("Pm Logger group ID cannot be found. " "Make sure it's correct.")
        except TypeError:
            LOGS.error("Pm Logger group ID is unsupported. " "Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "Pengecualian terjadi saat mencoba memverifikasi grup Pm logger.\n"
                + str(e)
            )
    else:
        LOGS.info(
            "Kamu isi divars  PRIVATE_GROUP_BOT_API_ID in vars untuk fungsi userbot."
        )


def add_bot_to_logger_group():
    Config.TG_BOT_USERNAME 
    try:
        pandaub.loop.run_until_complete(
            pandaub(
                functions.messages.AddChatUserRequest(
                    chat_id=BOTLOG_CHATID,
                    user_id=Config.TG_BOT_USERNAME,
                    fwd_limit=1000000,
                )
            )
        )
        pandaub.loop.run_until_complete(
            pandaub(
                functions.messages.AddChatUserRequest(
                    chat_id=Config.PM_LOGGER_GROUP_ID,
                    user_id=Config.TG_BOT_USERNAME,
                    fwd_limit=1000000,
                )
            )
        )
    except BaseException:
        try:
            pandaub.loop.run_until_complete(
                pandaub(
                    functions.channels.InviteToChannelRequest(
                        channel=BOTLOG_CHATID,
                        users=[Config.TG_BOT_USERNAME],
                    )
                )
            )
            pandaub.loop.run_until_complete(
                pandaub(
                    functions.channels.InviteToChannelRequest(
                        channel=Config.PM_LOGGER_GROUP_ID,
                        users=[Config.TG_BOT_USERNAME],
                    )
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def startupmessage():
    try:
        if BOTLOG:
            Config.PANDAUBLOGO = await pandaub.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/08a3d412e29a1351b7aaa.jpg",
                caption="**🐼🐼BOT PANDA KAMU TELAH AKTIF SILAKAN JOIN GRUP.**",
                buttons=[
                    (Button.url("REPO", "https://github.com/ilhammansiz/PandaUserbot"),)
                ],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await pandaub.check_testcases()
            message = await pandaub.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**🐼🐼Ok Sekarang Bot menyala🐼🐼.**"
            await pandaub.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await pandaub.send_message(
                    msg_details[0],
                    f"{cmdhr}ping",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


if len(sys.argv) not in (1, 3, 4):
    pandaub.disconnect()
else:
    try:
        LOGS.info("Starting Panda")
        pandaub.loop.run_until_complete(setup_bot())
        LOGS.info("Startup Completed")
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()

verifyLoggerGroup()
add_bot_to_logger_group()

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

from importlib import import_module

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from Panda import LOGS, bot
from Panda.modules import ALL_MODULES


INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)


for module_name in ALL_MODULES:
    imported_module = import_module("Panda.modules." + module_name)




print("🛠 Sedang memperoses.....")
print("Yay BOT PANDA USERBOT MENYALA.!!!")
print(
    f"Mengaktifkan userbot {cmdhr}ping ⚙ BOT PANDA MENYALAH ⚙\
      \nIf you need assistance, head to https://t.me/TEAMSquadUserbotSupport"
)
print("Berhasil Mengaktifkan Userbot")

LOGS.info(f"🐼 PANDA-USERBOT 🐼\n⚙️ Version 2021 [TELAH DIAKTIFKAN]")

if len(sys.argv) not in (1, 3, 4):
    pandaub.disconnect()
else:
    pandaub.run_until_disconnected()
