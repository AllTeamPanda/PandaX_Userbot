import glob
import os
import sys
from asyncio.exceptions import CancelledError
from datetime import timedelta
from pathlib import Path

import requests
from telethon import Button, functions, types, utils

from Panda import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import PandaBot as pandaub
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

LOGS = logging.getLogger("PandaUserbot")
cmdhr = Config.COMMAND_HAND_LER


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


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.PANDAUBLOGO = await pandaub.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/3a52b78e38b4a084b0515.jpg",
                caption="**Bot PandaUserbot Telah aktif siap dipakai.**",
                buttons=[
                    (Button.url("Support", "https://t.me/TEAMSquadUserbotSupport"),)
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
            text = message.text + "\n\n**Ok Bot is Back and Alive.**"
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


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await pandaub.tgbot.get_me()
    try:
        await pandaub(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await pandaub(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder):
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
                LOGS.info(f"unable to load {shortname} because of error {e}")


from os import environ

# import logging
from pyrogram import Client

APP_ID = int(environ["APP_ID"])
API_HASH = environ["API_HASH"]
PROGRAM_SESSION = environ["PROGRAM_SESSION"]

PLUGINS = dict(
    root="Panda", include=["vc." + environ["PILIHAN_VCG"], "ping", "sysinfo"]
)

app = Client(PROGRAM_SESSION, APP_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig


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







async def autobot():
    await pandaub.start()
    if Config.TG_BOT_TOKEN:
        os.environ.get("TG_BOT_TOKEN", str(Config.TG_BOT_TOKEN))
        return
    if os.environ.get("TG_BOT_TOKEN):
        return
    LOGS.info("🛠 MEMBUAT BOT UNTUK ANDA DI @BotFather, HARAP TUNGU !!")
    who = await pandaub.get_me()
    name = "Panda_Userbot Assistant " + who.first_name
    if who.username:
        username = who.username + "_bot"
    else:
        username = "Panda_Userbot_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await pandaub(UnblockRequest(bf))
    await pandaub.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await pandaub.send_message(bf, "/start")
    await asyncio.sleep(1)
    await pandaub.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await pandaub.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
        )
        exit(1)
    await pandaub.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await pandaub.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await pandaub.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await pandaub.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
            )
            exit(1)
    await pandaub.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await pandaub.get_messages(bf, limit=1))[0].text
    await pandaub.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "PandaX_Userbot" + (str(who.id))[6:] + str(ran) + "_bot"
        await pandaub.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await pandaub.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            os.environ.get("TG_BOT_TOKEN", token)
            await pandaub.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await pandaub.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await pandaub.send_message(bf, "menu...")
            LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
        else:
            LOGS.info(
                f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        os.environ.get("TG_BOT_TOKEN", token)
        await pandaub.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await pandaub.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await pandaub.send_message(bf, "menu...")
        LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
    else:
        LOGS.info(
            f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
        )
        exit(1)
