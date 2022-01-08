import time
from platform import python_version, uname

from telethon import version
import asyncio

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

plugin_category = "mansiez"

ilhammansizzz = "https://github.com/ilhammansiz/PandaX_Userbot"
support = "https://t.me/TEAMSquadUserbotSupport"
SUDO = gvarstatus("sudoenable")
SUDOuser = _sudousers_list()
User = gvarstatus("NAME")
Bot = gvarstatus("USERBOT")





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
    if Config.ALIVE_PIC:
        try:
            logo = Config.ALIVE_PIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/5650f059f41e278937f35.jpg"
            await alive.delete()
            msg = await pandaub.send_file(alive.chat_id, logo, caption=output)
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
