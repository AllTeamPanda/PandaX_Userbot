import time
from platform import python_version

from telethon import version
import asyncio
from Panda import StartTime, pandaversion, PandaBot, SqL, Md
pandaub = PandaBot
from ..Config import Config
from ..helpers.functions import get_readable_time, check_data_base_heal_th
from pytgcalls import __version__
from ..core.data import _sudousers_list
from . import mention

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = Md.getdb("CUSTOM_ALIVE_TEXT") = SqL.getdb("CUSTOM_ALIVE_TEXT") or "꧁༺ Panda Userbot ༻꧂"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================
EMOJI = SqL.getdb("EMOJI") or "🎨"
NAME = DEFAULTUSER

plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")
SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or "https://telegra.ph/file/37b52b38dffb858cccf49.jpg"



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
    await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("꧁༺ Panda Userbot ༻꧂")
    await alive.edit("꧁༺ Userbot ༻꧂")
    await asyncio.sleep(1)
    output = (
        f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        f"⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢\n"
        f"╭─⊸⌊🚹 `Pengguna:` {NAME}\n"
        f"╭─⊸⌊✍ `Telethon:` v{version.__version__}\n"
        f"╭─⊸⌊🐍 `Python:` v{python_version()}\n"
        f"╭─⊸⌊👾 `Pytgcalls:` v{__version__}\n"
        f"╭─⊸⌊💻 `Database:` {check_data_base_heal_th()}\n"
        f"╭─⊸⌊🚀 `Version:` v{pandaversion}\n"
        f"╭─⊸⌊✅ `Sudo:` {SUDO}\n"
        f"╭─⊸⌊👥 `ID Sudo:` {SUDOuser}\n"
        f"⟣✧✧✧✧✧✧✧✧✧✧✧✧✧✧⟢")
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=output)
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



