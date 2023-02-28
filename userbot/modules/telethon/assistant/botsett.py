# from https://github.com/sandy1709/catuserbot
# Recode by ILHAM MANSIEZ
# PANDA USERBOT
# TENTANG AKU DAN DIA



import re
from collections import defaultdict
from datetime import datetime
from typing import Optional, Union

from telethon import Button, events
from telethon.errors import UserIsBlockedError
from telethon.events import CallbackQuery, StopPropagation
from telethon.utils import get_display_name

from .... import Config
from .... import PandaBot, tgbot
from ...._misc import check_owner, pool
from ...._misc.logger import logging
from ....helpers import reply_id
from ....helpers.utils import _format

from .... import delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

pandaub = PandaBot

LOGS = logging.getLogger(__name__)

plugin_category = "plugins"
botusername = Config.TG_BOT_USERNAME


@tgbot.bot_cmd(
    pattern=f"^/start({botusername})?([\s]+)?$",
    incoming=True,
    func=lambda e: e.is_private,
)
async def bot_start(event):
    chat = await event.get_chat()
    user = await pandaub.get_me()
    reply_to = await reply_id(event)
    if chat.id != Config.OWNER_ID:
        start_msg = f"Hey 🙋 {_format.mentionuser(chat.first_name , chat.id)},\
                    \nSaya {_format.mentionuser(user.first_name , user.id)}' Assistant_bot.\
                    \nKamu Bisa Setting saya disini dan Daftar menu perintah Saya sebagai Asistantmu.\
                    \n\nPowered by @PandaUserbot"
        buttons = [
            (
                Button.inline("🌀 INFO 🌀", data="menubot"),
                Button.url(
                    "Deploy",
                    "https://t.me/PandaUserbot/13",
                ),
            )
        ]
    else:
        start_msg = f"Hey 🙋 {_format.mentionuser(chat.first_name , chat.id)},\
                    \nSaya {_format.mentionuser(user.first_name , user.id)}' Assistant_bot.\
                    \nKamu Bisa Setting saya disini dan Daftar menu perintah Saya sebagai Asistantmu.\
                    \n\nPowered by @PandaUserbot"
        buttons = [
            (
                Button.inline("🌀 INFO 🌀", data="menubot"),
                Button.url(
                    "Deploy",
                    "https://t.me/PandaUserbot",
                ),
            )
        ]
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Kesalahan**\nTerjadi Kesalahan pada bot saat loading.\
                \n`{str(e)}`",
            )
    

