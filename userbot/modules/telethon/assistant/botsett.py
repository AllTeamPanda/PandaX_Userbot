# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot




from telethon import Button

from .... import Config
from .... import PandaBot, tgbot
from ...._misc.logger import logging
from ....helpers import reply_id
from ....helpers.utils import _format

from . import BOTLOG, BOTLOG_CHATID

pandaub = PandaBot

LOGS = logging.getLogger(__name__)

plugin_category = "plugins"

botusername = Config.BOT_USERNAME

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
    




