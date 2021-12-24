import time
from platform import python_version, uname

from telethon import version

from Panda import StartTime, pandaub, pandaversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "꧁༺ Panda Userbot ༻꧂"

from ..sql_helper.globals import gvarstatus, addgvar

# ================= CONSTANT =================
DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else uname().node
# ============================================
EMOJI = gvarstatus("EMOJI") or "🎨"

plugin_category = "mansiez"

ilhammansizzz = "https://github.com/ilhammansiz/PandaX_Userbot"
support = "https://t.me/TEAMSquadUserbotSupport"
SUDO = gvarstatus("sudoenable")

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
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if Config.ALIVE_PIC:
        panda_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        panda_caption += f"**🐼 PANDA USERBOT 🐼** \n"
        panda_caption += f"┏━━━━━━━━━━━━━━━━━\n"
        panda_caption += f"┣||{EMOJI} `Pengguna :` {DEFAULTUSER}\n"
        panda_caption += f"┣||{EMOJI} `Simbol   :`꧁༺ Panda Userbot ༻꧂\n"
        panda_caption += f"┣||{EMOJI} `Telethon :` Ver {version.__version__}\n"
        panda_caption += f"┣||{EMOJI} `Python   :` Ver {python_version()}\n"
        panda_caption += f"┣||{EMOJI} `Branch   :` {Config.UPSTREAM_REPO_BRANCH}\n"
        panda_caption += f"┣||{EMOJI} `Bot Ver  :` {pandaversion}\n"
        panda_caption += f"┣||{EMOJI} `Sudo     :` {SUDO}\n"
        panda_caption += f"┗━━━━━━━━━━━━━━━━━ \n"
        await event.client.send_file(
            event.chat_id, Config.ALIVE_PIC, caption=panda_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await event.delete()
        return
        await edit_or_reply(
            event,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**🐼 PANDA USERBOT 🐼** \n"
            f"┏━━━━━━━━━━━━━━━━━ \n"
            f"┣||{EMOJI} `Pengguna :` {DEFAULTUSER}\n"
            f"┣||{EMOJI} `Simbol   :`꧁༺ Panda Userbot ༻꧂\n"
            f"┣||{EMOJI} `Telethon :` Ver {version.__version__}\n"
            f"┣||{EMOJI} `Python   :` Ver {python_version()}\n"
            f"┣||{EMOJI} `Branch   :` {Config.UPSTREAM_REPO_BRANCH}\n"
            f"┣||{EMOJI} `Bot Ver  :` {pandaversion}\n"
            f"┣||{EMOJI} `Sudo     :` {SUDO}\n"
            f"┗━━━━━━━━━━━━━━━━━ \n",
        )
