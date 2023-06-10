import time
from platform import python_version
from telethon import Button, version
import asyncio
import sys
from userbot import HOSTED_ON, PandaBot, SqL, StartTime, pandaversion, tgbot
pandaub = PandaBot
from datetime import datetime
import random
from userbot import Config
from ...helpers.functions import get_readable_time

from ..._misc.data import _sudousers_list
from . import mention
from ...Session.multisession_ import Telethon


custom_text = " 𝐏𝐚𝐧𝐝𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐁𝐎𝐓_𝐈𝐒_𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐏𝐚𝐧𝐝𝐚_𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞".split(
    " "
)
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.get_key("CUSTOM_ALIVE_TEXT") or f"{random.choice(custom_text)}"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================

NAME = DEFAULTUSER


plugin_category = "plugins"

SUDO = SqL.get_key("sudoenable")

def SUDO():
    try:
        if SqL.get_key("sudoenable") is not None:        
            return "SudoUsers"
        else:
            return "No SudoUsers"
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



alive_logo = [
    f"https://telegra.ph/file/{_}.jpg"
    for _ in [
        "ecd71c1a58dd1788b174b",
        "50f3461be2fcbc2bc6918",
        "a84d82fb21e755d6e7e50",
        "f7bc0c04ea7486f18bcc4",
        "f504013cebca7d54f65e3",
        "7f2507df4e94cc2d53968",
        "5d5c6e7c33046a14c0fea",
        "0473bd52b7942bfb157d8",
    ]
]

emoji_alive = "★ ♦ ♠ ♣ ¡ ! ‹ › ∞ ≈ × 🦌 🐘 🐨 🐼 🐧 🦇 🦃 🐲 💮 🌸 🌺 🌻 🌼 🏵 🌳 🌲 🌺 🎭 🌟 🌠 🌩 ⚡ 🔥 ☄️ ❄ 🛸 ✨ 🎑 ⚒️ 🛠 ⛏️ 🔨 ⚔️ 🗡 ⚙️ 🏹 🔮 🗿 ⚱️ ⚰️ ➡️ ↗️ ⬆️ ⬅️ ↘️ ⬇️ ✅ ☑️ ❓ ⁉️ ‼️ ❗".split(
    " "
)

SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.get_key("ALIVE_PIC") or f"{random.choice(alive_logo)}"

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
    await get_readable_time((time.time() - StartTime))
    await alive.edit("꧁༺ Panda Userbot ༻꧂")
    await alive.edit("꧁༺ Userbot ༻꧂")
    await asyncio.sleep(1)
    if LOGO:
        try:
            logo = LOGO 
            await alive.delete()
            msg = await alive.client.send_file(alive.chat_id, logo, caption=aliveess)
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

☉ 𝐎𝐖𝐍𝐄𝐑: {NAME}
☉ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡: `𝚅{pandaversion}`
☉ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍: `𝚅{version.__version__}`
☉ 𝐏𝐘𝐓𝐇𝐎𝐍: `𝚅{python_version()}`\n
༻༺༻༺༻༺༻༺
⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢
╭━─━─━─━─━─━─━─━─━╮
       𝐒𝐓𝐀𝐓𝐔𝐒:

☉ 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄: `{SqL.name} {SqL.ping()}` 
☉ 𝐇𝐎𝐒𝐓𝐄𝐃_𝐎𝐍: [ {HOSTED_ON} ]
☉ 𝐒𝐔𝐃𝐎: {SUDO()}
╰━─━─━─━─━─━─━─━─━╯
⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢
༻༺༻༺༻༺༻༺
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
                "https://github.com/AllTeamPanda/PandaX_Userbot",
            ),
            Button.url(
                "#⃣Deploy#⃣",
                "https://t.me/PandaUserbot/13",
            ),
        ),
    ]
    return buttons
