import time
from platform import python_version

from telethon import version
import asyncio
from Panda import StartTime, pandaversion, PandaBot, SqL, Mongodb, redisalive
pandaub = PandaBot
from ..Config import Config
from ..helpers.functions import get_readable_time, check_data_base_heal_th
from pytgcalls import __version__
from ..core.data import _sudousers_list
from . import mention

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or "꧁༺ Panda Userbot ༻꧂"

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
        f"╭─⊸⌊`𝗢𝘄𝗻𝗲𝗿:` {NAME}\n"
        f"╭─⊸⌊`𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻:` 𝚅{version.__version__}\n"
        f"╭─⊸⌊`𝗣𝘆𝘁𝗵𝗼𝗻:` 𝚅{python_version()}\n"
        f"╭─⊸⌊`𝗣𝘆𝘁𝗴𝗰𝗮𝗹𝗹𝘀:` 𝚅{__version__}\n"
        f"╭─⊸⌊`𝗗𝗕_𝗦𝗾𝗟:` {check_data_base_heal_th()}\n"
        f"╭─⊸⌊`𝗠𝗼𝗻𝗴𝗼_𝗗𝗕:` {Mongodb.ping()}\n"
        f"╭─⊸⌊`𝗥𝗲𝗱𝗶𝘀_𝗗𝗕:` {redisalive()}\n"
        f"╭─⊸⌊`𝗩𝗲𝗿𝘀𝗶𝗼𝗻:` 𝚅{pandaversion}\n"
        f"╭─⊸⌊`𝗦𝘂𝗱𝗼:` {SUDO}\n"
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



