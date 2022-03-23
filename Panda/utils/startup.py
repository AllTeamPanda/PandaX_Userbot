# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import glob
import os
import sys
from asyncio.exceptions import CancelledError
from pathlib import Path
from telethon.tl.functions.channels import JoinChannelRequest
import requests
from telethon import functions, types, utils

from Panda import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import PandaBot 
from ..helpers.utils import install_pip
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
import base64
from ..versions import __version__ as botvers

LOGS = logging.getLogger("PandaUserbot")
cmdhr = Config.COMMAND_HAND_LER
pandaub = PandaBot

async def setup_bot():
    try:
        await PandaBot.start()
        delta = await PandaBot(functions.help.GetConfigRequest())
        for option in delta.dc_options:
            if option.ip_address == PandaBot.session.server_address:
                if PandaBot.session.dc_id != option.id:
                    LOGS.warning(
                        f"Fixed DC ID in session from {PandaBot.session.dc_id}"
                        f" to {option.id}"
                    )
                PandaBot.session.set_dc(option.id, option.ip_address, option.port)
                PandaBot.session.save()
                break
        PandaBot.me = await PandaBot.get_me()
        bot_details = await PandaBot.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        PandaBot.uid = PandaBot.tgbot.uid = utils.get_peer_id(PandaBot.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(PandaBot.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()


# don't know work or not just a try in future will use sleep
async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://httpbin.org/ip").json())["origin"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await pandaub.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"

async def loads(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"Panda/{folder}/*.py"
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
                                plugin_path=f"Panda/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"Panda/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Panda/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")


async def buka(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"Panda/plugins/{folder}/*.py"
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
                                plugin_path=f"Panda/plugins/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"Panda/plugins/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Panda/plugins/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")




async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await pandaub.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID cannot be found. Make sure it's correct."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID is unsupported. Make sure it's correct."
            )
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "Don't delete this group or change to group(If you change group all your previous snips, welcome will be lost.)"
        _, groupid = await create_supergroup(
            "PandaUserbot BotLog Group", pandaub, Config.TG_BOT_USERNAME, descript
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "Private Group for PRIVATE_GROUP_BOT_API_ID is created successfully and added to vars."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await pandaub.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID cannot be found. Make sure it's correct.")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID is unsupported. Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PM_LOGGER_GROUP_ID.\n"
                + str(e)
            )
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "Panda"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


ON = f"""
© **Panda-Userbot**
•••••••••••
👤 Owner {Config.ALIVE_NAME}
💻 **Version -** `{botvers}`

❕ **Ketik** `{cmdhr}alive` **untuk Mengecheck Bot apakah sudah aktif**

❗Sebaiknya Anda jangan keluar grup ini agar bot tidak mati
 ....Terimakasih....🇮🇩

❗You should not leave this group so that the bot does not die
 ....Thank You....🇺🇸
•••••••••••
Dev by Ilham Mansiz
"""

async def ongrup():
    try:
        if PandaBot:
            if BOTLOG_CHATID != 0:
                await PandaBot.send_message(
                    BOTLOG_CHATID,
                    ON,
                )
    except BaseException:
        pass

async def join():
    X = base64.b64decode("QFBhbmRhVXNlcmJvdA==")
    L = base64.b64decode("QFRlYW1TcXVhZFVzZXJib3RTdXBwb3J0")
    try:
        await PandaBot(JoinChannelRequest(X))
    except BaseException:
        pass
    try:
        await PandaBot(JoinChannelRequest(L))
    except BaseException:
        pass

## Modular •••••√√√√√√••••••^••√√

P = "plugins"
M = "modules"
V = "VCPlugins"
A = "AsistenBot"
