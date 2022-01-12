import time
from platform import python_version, uname

from telethon import version
import asyncio
import random
from Panda import StartTime, pandaub, pandaversion

from ..Config import Config
from ..helpers.functions import get_readable_time
from ..sql_helper.globals import gvarstatus

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "꧁༺ Panda Userbot ༻꧂"

from ..sql_helper.globals import gvarstatus
from ..core.data import _sudousers_list

# ================= CONSTANT =================
DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else uname().node
# ============================================
EMOJI = gvarstatus("EMOJI") or "🎨"
NAME = gvarstatus("NAME") or DEFAULTUSER

plugin_category = "Plugins"

ilhammansizzz = "https://github.com/ilhammansiz/PandaX_Userbot"
support = "https://t.me/TEAMSquadUserbotSupport"
SUDO = gvarstatus("sudoenable")
SUDOuser = _sudousers_list()
User = gvarstatus("NAME")
Bot = gvarstatus("USERBOT")

LOGO = Config.ALIVE_PIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/5650f059f41e278937f35.jpg"

spesial = [
     "https://telegra.ph/file/3a128f03b625e0f1a96d1.mp4"
     "https://telegra.ph/file/fc0d6c09d8ddf89aa9772.mp4"
     "https://telegra.ph/file/f915c7aeab2c481747163.mp4"
     "https://telegra.ph/file/58db2cd17ea842954e605.mp4"
     "https://telegra.ph/file/c76f67ab5288941e7e96a.mp4"
]

@pandaub.ilhammansiz_cmd(
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
    await pandaub.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("꧁༺ Panda Userbot ༻꧂")
    await alive.edit("꧁༺ Userbot ༻꧂")
    await alive.edit("🎰")
    await asyncio.sleep(2)
    output = (
        f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        f"┏━━━━━━━━━━━━━━━━━\n"
        f"┣||{EMOJI} `Pengguna :` {NAME}\n"
        f"┣||{EMOJI} `Simbol   :`༺🐼༻\n"
        f"┣||{EMOJI} `Telethon :` {version.__version__}\n"
        f"┣||{EMOJI} `Python   :` {python_version()}\n"
        f"┣||{EMOJI} `Branch   :` {Config.UPSTREAM_REPO_BRANCH}\n"
        f"┣||{EMOJI} `Bot Ver  :` {pandaversion}\n"
        f"┣||{EMOJI} `Sudo     :` {SUDO}\n"
        f"┣||{EMOJI} `ID Sudo  :` {SUDOuser}\n"
        f"┗━━━━━━━━━━━━━━━━━ \n")
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await pandaub.send_file(random.choice(alive.chat_id, logo, caption=output))
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
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()
