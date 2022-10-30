import time
from platform import python_version
from telethon import Button, version
import asyncio
import sys
from userbot import PandaBot, SqL, StartTime, dual_duall, dual_mode, pandaversion, tgbot
pandaub = PandaBot
import random
from userbot import Config
from ...helpers.functions import get_readable_time
from pytgcalls import __version__
from ..._misc.data import _sudousers_list
from . import mention
from ...sql_helper.db import BaseDB
from telethon.tl.types import InputMessagesFilterVideo

Mongoredis = BaseDB()


custom_text = " 𝐏𝐚𝐧𝐝𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐁𝐎𝐓_𝐈𝐒_𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐏𝐚𝐧𝐝𝐚_𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞".split(
    " "
)
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or f"{random.choice(custom_text)}"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================

NAME = DEFAULTUSER


plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")

def SUDO():
    try:
        if SqL.getdb("sudoenable") is not None:
            SudoActive = SqL.setdb("sudoenable", "True")
            return SudoActive
        else:
            SudoActive = SqL.setdb("sudoenable", "False")
            return SudoActive
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



alive_logo = [
    f"https://telegra.ph/file/{_}.jpg"
    for _ in [
        "99dd9fbca84bc407ac4e8",
        "c13edd5c46ad875d57bd7",
        "d3c370234bf81c5bc2214",
        "50c6b49f05129eff150c0",
        "d27c36c92679d1fcaf662",
        "995641228cd4c93895464",
        "5d5c6e7c33046a14c0fea",
    ]
]

emoji_alive = "★ ♦ ♠ ♣ ¡ ! ‹ › ∞ ≈ × 🦌 🐘 🐨 🐼 🐧 🦇 🦃 🐲 💮 🌸 🌺 🌻 🌼 🏵 🌳 🌲 🌺 🎭 🌟 🌠 🌩 ⚡ 🔥 ☄️ ❄ 🛸 ✨ 🎑 ⚒️ 🛠 ⛏️ 🔨 ⚔️ 🗡 ⚙️ 🏹 🔮 🗿 ⚱️ ⚰️ ➡️ ↗️ ⬆️ ⬅️ ↘️ ⬇️ ✅ ☑️ ❓ ⁉️ ‼️ ❗🇲🇨 🇹🇷 🇩🇪".split(
    " "
)

SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or f"{random.choice(alive_logo)}"

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
                aliveess + "\n\n *`Logo Yang Disediakan Tidak Valid."
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

☉ {random.choice(emoji_alive)} 𝗢𝘄𝗻𝗲𝗿: @{PandaBot.me.username}
☉ {random.choice(emoji_alive)} Version: `𝚅{pandaversion}`
☉ {random.choice(emoji_alive)} 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻: `𝚅{version.__version__}`
☉ {random.choice(emoji_alive)} 𝗣𝘆𝘁𝗴𝗰𝗮𝗹𝗹𝘀: `𝚅{__version__}`
☉ {random.choice(emoji_alive)} 𝗣𝘆𝘁𝗵𝗼𝗻: `𝚅{python_version()}`\n
⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢
╭━─━─━─━─━─━─━─━─━╮
               𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲:

☉ {random.choice(emoji_alive)} 𝗗𝗕_𝗦𝗾𝗟: `{SqL.ping()}`
☉ {random.choice(emoji_alive)} 𝗦𝘂𝗱𝗼: {SUDO()}

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
