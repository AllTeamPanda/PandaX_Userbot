# Copyright (C) 2020 Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


##•••••••••••From & import••••••••••••••••
from .Osdb import Osdb
import os
from .Session import *
from .Version import __version__

import logging
import os
import re
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sync import custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

##••••••••••••••••••••••••••



# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CATEGORY = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True
## •••••••••••••••••••

load_dotenv("config.env")

## Time
StartTime = time.time()

def STORAGE(n):
    return Storage(Path("data") / n)

repo = Repo()
branch = repo.active_branch.name

Botver = __version__
## 
BOT_VER = __version__

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "Anda HARUS memiliki python setidaknya versi 3.9."
        "Beberapa fitur tergantung versi python ini. Bot berhenti."
    )
    sys.exit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
)

if CONFIG_CHECK:
    LOGS.info(
        "Harap hapus baris yang disebutkan dalam tagar pertama dari file config.env"
    )
    sys.exit(1)


DEVS = [5057493677, 1593802955]

SUDO_USERS = Osdb.SUDO_USERS
BLACK_CHAT = Osdb.BLACK_CHAT
BLACKLIST_CHAT = Osdb.BLACKLIST_CHAT
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001159103924]
BOTLOG_CHATID = Osdb.BOTLOG_CHATID
BOTLOG = Osdb.BOTLOG
LOGSPAMMER = Osdb.LOGSPAMMER
LOAD = Osdb.LOAD
NO_LOAD = Osdb.NO_LOAD
PM_AUTO_BAN = Osdb.PM_AUTO_BAN
PM_LIMIT = Osdb.PM_LIMIT
HEROKU_APP_NAME = Osdb.HEROKU_APP_NAME
HEROKU_API_KEY = Osdb.HEROKU_API_KEY
WATCH_COUNTRY = Osdb.WATCH_COUNTRY
GIT_REPO_NAME = Osdb.GIT_REPO_NAME
GITHUB_ACCESS_TOKEN = Osdb.GITHUB_ACCESS_TOKEN
UPSTREAM_REPO_URL = Osdb.UPSTREAM_REPO_URL
S_PACK_NAME = Osdb.S_PACK_NAME
OCR_SPACE_API_KEY = Osdb.OCR_SPACE_API_KEY
REM_BG_API_KEY = Osdb.REM_BG_API_KEY
CHROME_DRIVER = Osdb.CHROME_DRIVER
GOOGLE_CHROME_BIN = Osdb.GOOGLE_CHROME_BIN
OPEN_WEATHER_MAP_APPID = Osdb.OPEN_WEATHER_MAP_APPID
WEATHER_DEFCITY = Osdb.WEATHER_DEFCITY
ANTI_SPAMBOT = Osdb.ANTI_SPAMBOT
ANTI_SPAMBOT_SHOUT = Osdb.ANTI_SPAMBOT_SHOUT
COUNTRY = Osdb.COUNTRY
TZ_NUMBER = Osdb.TZ_NUMBER
CLEAN_WELCOME = Osdb.CLEAN_WELCOME
ZIP_DOWNLOAD_DIRECTORY = Osdb.ZIP_DOWNLOAD_DIRECTORY
BITLY_TOKEN = Osdb.BITLY_TOKEN
BIO_PREFIX = Osdb.BIO_PREFIX
DEFAULT_BIO = Osdb.DEFAULT_BIO
LASTFM_API = Osdb.LASTFM_API
LASTFM_SECRET = Osdb.LASTFM_SECRET
LASTFM_USERNAME = Osdb.LASTFM_USERNAME
TEMP_DOWNLOAD_DIRECTORY = Osdb.TEMP_DOWNLOAD_DIRECTORY
DEEZER_ARL_TOKEN = Osdb.DEEZER_ARL_TOKEN
DEEP_AI = Osdb.DEEP_AI
BOT_TOKEN = Osdb.BOT_TOKEN
BOT_USERNAME = Osdb.BOT_USERNAME
HANDLER = Osdb.HANDLER
SUDO_HANDLER = Osdb.SUDO_HANDLER
LASTFM_PASSWORD_PLAIN = Osdb.LASTFM_PASSWORD_PLAIN
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass

ALIVE_TEKS_CUSTOM = os.environ.get("ALIVE_TEKS_CUSTOM", None)
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Panda")
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "⚡")
INLINE_EMOJI = os.environ.get("INLINE_EMOJI", "᪥")
ICON_HELP = os.environ.get("ICON_HELP", "❈")
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
)
INLINE_PIC = (
    os.environ.get("INLINE_PIC") or "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
)
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/6213d2673486beca02967.png"
)
QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
)
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)
TERM_ALIAS = os.environ.get("TERM_ALIAS", "PandaUserbot")
GROUP = os.environ.get("GROUP", "TeamSquadUserbotSupport")
CHANNEL = os.environ.get("CHANNEL", "PandaUserbot")
BYPASS_URL = os.environ.get("BYPASS_URL", "@bypassvip_bot")
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)


# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

CMD_HANDLER = HANDLER
WHITELIST = [5057493677, 1593802955]
DEFAULT = [1593802955]


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)


async def check_botlog_chatid() -> None:
    if not BOTLOG_CHATID and BOTLOG:
        LOGS.warning(
            "var BOTLOG_CHATID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var BOTLOG_CHATID"
        )
        sys.exit(1)


async def update_restart_msg(chat_id, msg_id):
    DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
    message = (
        f"**{BOT_VER} is back up and running!**\n\n"
        f"**User:** {DEFAULTUSER}"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from .modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            bot.loop.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass

with bot:
    try:
        user = bot.get_me()
        uid = user.id
        firstname = user.first_name
        lastname = user.last_name
        owner = f"{firstname} {lastname}" if lastname else firstname
    except BaseException as a:
        LOGS.info(f"{a}")


def main_menu():
    text=f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n✣ **Jumlah** `{len(CMD_HELP)}` Modules"
    buttons = [
        (
            Button.url(
                "Support",
                "https://t.me/TEAMSquadUserbotSupport",
            ),
            Button.inline(
                f"💎 𝙸𝚗𝚏𝚘",
                data="menuu",
            ),
        ),
    ]
    return text, buttons

def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{INLINE_EMOJI}", x, f"{INLINE_EMOJI}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⬅️", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("✖", b"close"),
                custom.Button.inline(
                    "➡️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        from ..modules.sql_helper.bot_blacklists import check_is_black_list
        from ..modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from ..misc import reply_id

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        firstname = user.first_name
        lastname = user.last_name
        owner = f"{firstname} {lastname}" if lastname else firstname
        logo = ALIVE_LOGO
        inlinelogo = INLINE_PIC
        tgbotusername = BOT_USERNAME
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        @tgbot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to, user_name, user_id, reply_msg, event.id, msg.id
                        )
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            string = query.lower()
            string.split()
            if event.query.user_id == uid and query.startswith("@PandaUserbot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=inlinelogo,
                    link_preview=False,
                    text=f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n✣ **Jumlah** `{len(dugmeler)}` Modules",
                    buttons=buttons,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Panda-Userbot",
                    url="https://t.me/TeamSquadUserbotSupport",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text="**Panda-UserBot**\n➖➖➖➖➖➖➖➖\n👤 **Owner Repo :** [Pocong](https://t.me/diemmmmmmmmmm)\n👥 **Support :** @TeamSquadUserbotSupport\n📐 **Repository :** [Panda-Userbot](https://github.com/ilhammansiz/PandaX_Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("𝐺𝑟𝑜𝑢𝑝", "https://t.me/TeamSquadUserbotSupport"),
                            custom.Button.url(
                                "𝑅𝑒𝑝𝑜", "https://github.com/ilhammansiz/PandaX_Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            elif string == "help":
               _result = main_menu()
               result = builder.photo(
                   file=inlinelogo,
                   text=_result[0],
                   buttons=_result[1],
                   link_preview=False,
               )
               await event.answer([result] if result else None)
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(match.group(4)))
                        )
                        note_data += markdown_note[prev : match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title=" Panda-Userbot ",
                    description="Panda-UserBot | Telethon",
                    url="https://t.me/TeamSquadUserbotSupport",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text=f"**Panda-UserBot**\n➖➖➖➖➖➖➖➖➖ **UserMode:** [{user.first_name}](tg://user?id={user.id})\n🐼 **Assistant:** {tgbotusername}\n➖➖➖➖➖➖➖➖\n**Support:** @TeamSquadUserbotSupport\n➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("𝐺𝑟𝑜𝑢𝑝", "https://t.me/TeamSquadUserbotSupport"),
                            custom.Button.url(
                                "𝑅𝑒𝑝𝑜", "https://github.com/ilhammansiz/PandaX_Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(looters)
                buttons = paginate_help(current_page_number, dugmeler, "helpme")
                text = f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n🗂 **Jumlah** `{len(dugmeler)}` Modules"
                await event.edit(
                    text,
                    file=inlinelogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"menuu")))
        async def on_plug_in_callback_query_handler(event):
            buttons = paginate_help(0, dugmeler, "helpme")
            text=f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n✣ **Jumlah** `{len(dugmeler)}` Modules"
              
            await event.edit(text, buttons=buttons),

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in DEVS and SUDO_USERS:
                openlagi = custom.Button.inline("✖ Tutup", data="close")
                await event.edit(
                    " **Help Mode Button Ditutup!** "
                )
                await event.delete()
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")
                help_string = ""
                try:
                    for i in CMD_HELP[modul_name]:
                        help_string = f"Plugin Name-{modul_name}\n\n✘ Commands Available-\n\n"
                        help_string += str(CMD_HELP[modul_name])
                except BaseException:
                    pass
                if help_string == "":
                    reply_pop_up_alert = f"{modul_name} has no detailed help..."
                else:
                    reply_pop_up_alert = help_string
                reply_pop_up_alert += "\n© @PandaUserbot"
                buttons = [ 
                    [
                        Button.inline("« Bᴀᴄᴋ", data="reopen"),
                        Button.inline("Cʟᴏꜱᴇ", data="close"),
                    ],
                ]
                try:
                    if str(event.query.user_id) in SUDO_USERS:
                        await event.edit(
                            reply_pop_up_alert,
                            buttons=buttons,
                        )
                    else:
                         reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                         await event.answer(reply_pop_up_alert, cache_time=0)
                except BaseException:
                     pandaxx = f"Do .help {modul_name} to get the list of commands."
                     await event.edit(pandaxx, buttons=buttons)
    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. "
        )
