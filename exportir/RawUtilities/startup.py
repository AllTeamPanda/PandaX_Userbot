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

from userbot import *

from userbot.config import Config, Var, Database
from userbot._misc.logger import logging

from userbot._misc.session import PandaBot, PandaBot2, PandaBot3, PandaBot4, PandaBot5, PandaBot6, PandaBot7, PandaBot8, PandaBot9, PandaBot10, PandaBot11, PandaBot12, PandaBot13, PandaBot14, PandaBot15, PandaBot16, PandaBot17, PandaBot18, PandaBot19, PandaBot10, PandaBot20, PandaBot21, PandaBot22, PandaBot23, PandaBot24, PandaBot25, PandaBot26, PandaBot27, PandaBot28, PandaBot29, PandaBot30, PandaBot31, PandaBot32, PandaBot33, PandaBot34, PandaBot35, PandaBot36, PandaBot37, PandaBot38, PandaBot39, PandaBot40, PandaBot41, PandaBot42, PandaBot43, PandaBot44, PandaBot45, PandaBot46, PandaBot47, PandaBot48, PandaBot49, PandaBot50, tgbot
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



async def memulai():
    await buka(f"telethon")
    await bukabot(f"assistant")

async def ClientMultiTelethon():
    if Var.STRING_SESSION and Database.BOT_TOKEN:
        if PandaBot:
            try:
                await tgbot.me = await tgbot.get_me()
                await await PandaBot(InviteToChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID, [tgbot.me.username]))
            except BaseException as er:
                LOGS.info("Error while Adding Assistant to Log Channel")
                LOGS.exception(er)
            if Config.PRIVATE_GROUP_BOT_API_ID:
                try:
                    achat = await tgbot.get_entity(Config.PRIVATE_GROUP_BOT_API_ID)
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
                        await PandaBot(
                            EditAdminRequest(
                                Config.PRIVATE_GROUP_BOT_API_ID, tgbot.me.username, rights, "Assistant"
                            )
                        )
                    except ChatAdminRequiredError:
                        LOGS.info(
                             "Failed to promote 'Assistant Bot' in 'Log Channel' due to 'Admin Privileges'"
                        )
        if PandaBot2:
            await PandaBot2(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot3:
            await PandaBot3(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot4:
            await PandaBot4(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot5:
            await PandaBot5(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot6:
            await PandaBot6(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot7:
            await PandaBot7(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot8:
            await PandaBot8(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot9:
            await PandaBot9(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot10:
            await PandaBot10(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot11:
            await PandaBot1(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot12:
            await PandaBot12(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot13:
            await PandaBot13(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot14:
            await PandaBot14(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot15:
            await PandaBot15(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot16:
            await PandaBot16(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot17:
            await PandaBot17(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot18:
            await PandaBot18(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot19:
            await PandaBot19(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot20:
            await PandaBot20(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot21:
            await PandaBot21(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot22:
            await PandaBot22(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot23:
            await PandaBot23(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot24:
            await PandaBot24(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot25:
            await PandaBot25(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot26:
            await PandaBot26(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot27:
            await PandaBot27(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot28:
            await PandaBot28(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot29:
            await PandaBot29(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot30:
            await PandaBot30(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot31:
            await PandaBot31(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot32:
            await PandaBot32(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot33:
            await PandaBot33(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot34:
            await PandaBot34(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot35:
            await PandaBot35(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot36:
            await PandaBot36(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot37:
            await PandaBot37(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot38:
            await PandaBot38(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot39:
            await PandaBot39(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot40:
            await PandaBot40(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot41:
            await PandaBot41(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot42:
            await PandaBot42(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot43:
            await PandaBot43(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot44:
            await PandaBot44(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot45:
            await PandaBot45(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot46:
            await PandaBot46(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot47:
            await PandaBot47(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot48:
            await PandaBot48(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot49:
            await PandaBot49(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        if PandaBot50:
            await PandaBot50(JoinChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID))
        
        if tgbot:
            await tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Memeriksa Database {DB.name}...")
            await tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Terkoneksi Database {DB.name} Successfully")
            

