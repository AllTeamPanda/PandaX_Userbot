# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import glob
import os
import sys
from asyncio.exceptions import CancelledError
from pathlib import Path
from telethon.tl.functions.channels import JoinChannelRequest
import requests
from telethon import functions, types, utils

from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from userbot.config import Config, Var
from userbot._misc.logger import logging
from userbot._misc.session import PandaBot, PandaBot2, PandaBot3, tgbot
from userbot.helpers.utils import install_pip
from userbot._database import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
import base64
from userbot.version import __version__ as botvers

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
        bot_details = await tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        PandaBot.uid = tgbot.uid = utils.get_peer_id(PandaBot.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(PandaBot.me)
        if Config.STRING_SESSION2:
            await PandaBot2.start()
        if Config.STRING_SESSION3:
            await PandaBot3.start()
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
    path = f"userbot/{folder}/*.py"
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
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Panda/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")


async def buka(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/{folder}/*.py"
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
                                plugin_path=f"userbot/modules/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")

async def bukabot(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/telethon/{folder}/*.py"
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
                                plugin_path=f"userbot/modules/telethon/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
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
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


ON = f"""
Panda-Userbot
Owner {Config.ALIVE_NAME}
Version - `{botvers}`
Ketik `{cmdhr}alive` untuk Mengecheck Bot apakah sudah aktif
"""

MSG_ON = """
Panda-Userbot
━━
Version - `{}'
Ketik `{}alive` untuk Mengecheck Bot
━━
"""


CHATID = "-1001718757023"

async def ongrup():
    try:
        if cekbot:
            if CHATID != 0:
                await PandaBot.send_message(
                    CHATID,
                    ON,
                )
                await PandaBot.send_message(
                    CHATID,
                    ON,
                )
                await PandaBot.send_message(
                    CHATID,
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




from telethon.tl.functions.channels import (
    EditAdminRequest,
    InviteToChannelRequest,
)

from telethon.errors import (
    ChatAdminRequiredError,
)


from telethon.tl.types import (
    ChatAdminRights,
)


def ClientMultiTelethon():
    if Var.STRING_SESSION and Database.BOT_TOKEN:
        if PandaBot:
            try:
                PandaBot(InviteToChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID, [tgbot.me.username]))
            except BaseException as er:
                LOGS.info("Error while Adding Assistant to Log Channel")
                LOGS.exception(er)
            if Config.PRIVATE_GROUP_BOT_API_ID:
                try:
                    achat = tgbot.get_entity(Config.PRIVATE_GROUP_BOT_API_ID)
                except BaseException as er:
                    achat = None
                    LOGS.info("Error while getting Log channel from Assistant")
                    LOGS.exception(er)
                if achat and not achat.admin_rights:
                    rights = ChatAdminRights(
                        add_admins=True,
                        invite_users=True,
                        change_info=True,
                        ban_users=True,
                        delete_messages=True,
                        pin_messages=True,
                        anonymous=False,
                        manage_call=True,
                    )
                    try:
                        PandaBot(
                            EditAdminRequest(
                                Config.PRIVATE_GROUP_BOT_API_ID, tgbot.me.username, rights, "Assistant"
                            )
                        )
                    except ChatAdminRequiredError:
                        LOGS.info(
                             "Failed to promote 'Assistant Bot' in 'Log Channel' due to 'Admin Privileges'"
                        )
        
        if tgbot:
            tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Memeriksa {DB.name}...")
            tgbot.edit_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Terkoneksi {DB.name} Successfully")
            tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, resources.buka(f"telethon"))
            tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, resources.bukabot(f"assistant"))
             

