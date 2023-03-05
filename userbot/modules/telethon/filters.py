# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

plugin_category = "modules"

import os

from telegraph import upload_file as uf
from telethon.utils import pack_bot_file_id

from ..._database.dB.filter_db import add_filter, list_filter, rem_filter
from ..._misc.tools import format_btn, get_msg_button, mediainfo

from ... import PandaBot
from telethon import events
from pyPanda import get_string
from . import edit_or_reply
eor = edit_or_reply


@PandaBot.ilhammansiz_cmd(
    pattern="filter (.*)",
    command=("filter", plugin_category),
    info={
        "header": "To save filter for the given keyword.",
        "description": "If any user sends that filter then your bot will reply.",
        "option": {
            "{mention}": "To mention the user",
            "{title}": "To get chat name in message",
            "{count}": "To get group members",
            "{first}": "To use user first name",
            "{last}": "To use user last name",
            "{fullname}": "To use user full name",
            "{userid}": "To use userid",
            "{username}": "To use user username",
            "{my_first}": "To use my first name",
            "{my_fullname}": "To use my full name",
            "{my_last}": "To use my last name",
            "{my_mention}": "To mention myself",
            "{my_username}": "To use my username.",
        },
        "usage": "{tr}filter <keyword>",
    },
)
async def af(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    wt = await e.get_reply_message()
    chat = e.chat_id
    if not (wt and wrd):
        return await e.eor(get_string("flr_1"))
    btn = format_btn(wt.buttons) if wt.buttons else None
    if wt and wt.media:
        wut = mediainfo(wt.media)
        if wut.startswith(("pic", "gif")):
            dl = await wt.download_media()
            variable = uf(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "video":
            if wt.media.document.size > 8 * 1000 * 1000:
                return await e.eor(get_string("com_4"), time=5)
            dl = await wt.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        else:
            m = pack_bot_file_id(wt.media)
        if wt.text:
            txt = wt.text
            if not btn:
                txt, btn = get_msg_button(wt.text)
            add_filter(chat, wrd, txt, m, btn)
        else:
            add_filter(chat, wrd, None, m, btn)
    else:
        txt = wt.text
        if not btn:
            txt, btn = get_msg_button(wt.text)
        add_filter(chat, wrd, txt, None, btn)
    await e.eor(get_string("flr_4").format(wrd))
    PandaBot.add_handler(filter_func, events.NewMessage())


@PandaBot.ilhammansiz_cmd(
    pattern="stop ([\s\S]*)",
    command=("stop", plugin_category),
    info={
        "header": "To delete that filter . so if user send that keyword bot will not reply",
        "usage": "{tr}stop <keyword>",
    },
)
async def rf(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("flr_3"))
    rem_filter(int(chat), wrd)
    await e.eor(get_string("flr_5").format(wrd))


@PandaBot.ilhammansiz_cmd(
    pattern="filters$",
    command=("filters", plugin_category),
    info={
        "header": "To list all filters in that chat.",
        "description": "Lists all active (of your userbot) filters in a chat.",
        "usage": "{tr}filters",
    },
)
async def lsnote(e):
    if x := list_filter(e.chat_id):
        sd = "Filters Found In This Chats Are\n\n"
        return await e.eor(sd + x)
    await e.eor(get_string("flr_6"))
