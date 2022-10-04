import time
from platform import python_version
from telethon import Button, version
import asyncio
from userbot import PandaBot, SqL, StartTime, dual_duall, dual_mode, pandaversion, tgbot
pandaub = PandaBot

from userbot import Config
from ...helpers.functions import get_readable_time
from pytgcalls import __version__
from ..._misc.data import _sudousers_list
from . import mention
from ...sql_helper.db import BaseDB

Mongoredis = BaseDB()

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or "PandaX-Userbot"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================
EMOJI = SqL.getdb("EMOJI") or "🎨"
NAME = DEFAULTUSER

plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")

if SUDO:
    SudoActive = SqL.setdb("sudoenable", "True")
    return SudoActive
else:
    SudoActive = SqL.setdb("sudoenable", "False")
    return SudoActive


SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or "https://telegra.ph/file/462ea6cf2beab87ef2d9f.jpg"

usernames = Config.TG_BOT_USERNAME

@PandaBot.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def redis(alive):
    PandaBot.me = await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("꧁༺ Panda Userbot ༻꧂")
    await alive.edit("꧁༺ Userbot ༻꧂")
    await asyncio.sleep(1)
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=aliveess)
            if tgbot:
                await tgbot.send_file(alive.chat_id, logo, caption=aliveess, buttons=menu())
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(aliveess)
        await asyncio.sleep(100)
        await alive.delete()


aliveess = f"""
{CUSTOM_ALIVE_TEXT}

☉ 👤 𝗢𝘄𝗻𝗲𝗿: {PandaBot.me.username}
☉ 🛰 Version: `𝚅{pandaversion}`
☉ 👾 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻: `𝚅{version.__version__}`
☉ 🎙 𝗣𝘆𝘁𝗴𝗰𝗮𝗹𝗹𝘀: `𝚅{__version__}`
☉ 🐍 𝗣𝘆𝘁𝗵𝗼𝗻: `𝚅{python_version()}`\n
⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢
╭━─━─━─━─━─━─━─━─━╮
               𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲:

☉ 🐘 𝗗𝗕_𝗦𝗾𝗟: `{SqL.ping()}`
☉ 👥 𝗦𝘂𝗱𝗼: {SUDO}

╰━─━─━─━─━─━─━─━─━╯
⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢
"""


def menu():
    buttons = [
        (
            Button.url(
                "👤 Support 👤",
                "https://t.me/TEAMSquadUserbotSupport",
            ),
            Button.inline(
                f"💎 𝙸𝚗𝚏𝚘",
                data="check",
            ),
        ),   
        (
            Button.url(
                "❓Source Code❓",
                "https://github.com/ilhammansiz/PandaX_Userbot",
            ),
            Button.url(
                "#⃣Deploy#⃣",
                "https://t.me/PandaUserbot/13",
            ),
        ),
    ]
    return buttons
