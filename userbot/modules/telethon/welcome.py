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

from ..._database.dB.greetings_db import (
    add_goodbye,
    add_thanks,
    add_welcome,
    delete_goodbye,
    delete_welcome,
    get_goodbye,
    get_welcome,
    must_thank,
    remove_thanks,
)
from ..._misc.tools import create_tl_btn, format_btn, get_msg_button, mediainfo

from pyPanda import get_string
from . import something, edit_or_reply, PandaBot

Note = "\n\nNote: `{mention}`, `{group}`, `{count}`, `{name}`, `{fullname}`, `{username}`, `{userid}` can be used as formatting parameters.\n\n"


@PandaBot.ilhammansiz_cmd(
    pattern="setwelcome$",
    command=("setwelcome", plugin_category),
    info={
       "description": "Set welcome message in the current chat.",
        "usage": [
            "{tr}setwelcome <message/reply to message>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def setwel(event):
    x = await edit_or_reply(event, get_string("com_1"))
    r = await event.get_reply_message()
    btn = format_btn(r.buttons) if (r and r.buttons) else None
    try:
        text = event.text.split(maxsplit=1)[1]
    except IndexError:
        text = r.text if r else None
    if r and r.media:
        wut = mediainfo(r.media)
        if wut.startswith(("pic", "gif")):
            dl = await r.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "video":
            if r.media.document.size > 8 * 1000 * 1000:
                return edit_or_reply(x, get_string("com_4"), time=5)
            dl = await r.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "web":
            m = None
        else:
            m = pack_bot_file_id(r.media)
        if r.text:
            txt = r.text
            if not btn:
                txt, btn = get_msg_button(r.text)
            add_welcome(event.chat_id, txt, m, btn)
        else:
            add_welcome(event.chat_id, None, m, btn)
        await eor(x, get_string("grt_1"))
    elif text:
        if not btn:
            txt, btn = get_msg_button(text)
        add_welcome(event.chat_id, txt, None, btn)
        await edit_or_reply(x, get_string("grt_1"))
    else:
        await edit_or_reply(x, get_string("grt_3"), time=5)



@PandaBot.ilhammansiz_cmd(
    pattern="clearwelcome$",
    command=("clearwelcome", plugin_category),
    info={
       "description": "delete welcome message in the current chat.",
        "usage": [
            "{tr}clearwelcome",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def clearwel(event):
    if not get_welcome(event.chat_id):
        return await edit_or_reply(event, get_string("grt_4"), time=5)
    delete_welcome(event.chat_id)
    await edit_or_reply(event, get_string("grt_5"), time=5)


@PandaBot.ilhammansiz_cmd(
    pattern="getwelcome$",
    command=("getwelcome", plugin_category),
    info={
       "description": "get welcome message in the current chat.",
        "usage": [
            "{tr}getwelcome",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def listwel(event):
    wel = get_welcome(event.chat_id)
    if not wel:
        return await edit_or_reply(event, get_string("grt_4"), time=5)
    msgg, med = wel["welcome"], wel["media"]
    if wel.get("button"):
        btn = create_tl_btn(wel["button"])
        return await something(event, msgg, med, btn)
    await event.reply(f"**Welcome Note in this chat**\n\n`{msgg}`", file=med)
    await event.delete()

@PandaBot.ilhammansiz_cmd(
    pattern="setgoodbye$",
    command=("setgoodbye", plugin_category),
    info={
       "description": "set goodbye message in the current chat.",
        "usage": [
            "{tr}setgoodbye <message/reply to message>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def setgb(event):
    x = await edit_or_reply(event, get_string("com_1"))
    r = await event.get_reply_message()
    btn = format_btn(r.buttons) if (r and r.buttons) else None
    try:
        text = event.text.split(maxsplit=1)[1]
    except IndexError:
        text = r.text if r else None
    if r and r.media:
        wut = mediainfo(r.media)
        if wut.startswith(("pic", "gif")):
            dl = await r.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "video":
            if r.media.document.size > 8 * 1000 * 1000:
                return await edit_or_reply(x, get_string("com_4"), time=5)
            dl = await r.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "web":
            m = None
        else:
            m = pack_bot_file_id(r.media)
        if r.text:
            txt = r.text
            if not btn:
                txt, btn = get_msg_button(r.text)
            add_goodbye(event.chat_id, txt, m, btn)
        else:
            add_goodbye(event.chat_id, None, m, btn)
        await edit_or_reply(x, "`Goodbye note saved`")
    elif text:
        if not btn:
            txt, btn = get_msg_button(text)
        add_goodbye(event.chat_id, txt, None, btn)
        await edit_or_reply(x, "`Goodbye note saved`")
    else:
        await edit_or_reply(x, get_string("grt_7"), time=5)


@PandaBot.ilhammansiz_cmd(
    pattern="delgoodbye$",
    command=("delgoodbye", plugin_category),
    info={
       "description": "del goodbye message in the current chat.",
        "usage": [
            "{tr}delgoodbye",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def clearwgb(event):
    if not get_goodbye(event.chat_id):
        return await edit_or_reply(event, get_string("grt_6"), time=5)
    delete_goodbye(event.chat_id)
    await edit_or_reply(event, "`Goodbye Note Deleted`", time=5)


@PandaBot.ilhammansiz_cmd(
    pattern="getgoodbye$",
    command=("getgoodbye", plugin_category),
    info={
       "description": "get goodbye message in the current chat.",
        "usage": [
            "{tr}getgoodbye",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def listgd(event):
    wel = get_goodbye(event.chat_id)
    if not wel:
        return await edit_or_reply(event, get_string("grt_6"), time=5)
    msgg = wel["goodbye"]
    med = wel["media"]
    if wel.get("button"):
        btn = create_tl_btn(wel["button"])
        return await something(event, msgg, med, btn)
    await event.reply(f"**Goodbye Note in this chat**\n\n`{msgg}`", file=med)
    await event.delete()


@ultroid_cmd(pattern="thankmembers (on|off)", groups_only=True)
async def thank_set(event):
    type_ = event.pattern_match.group(1).strip()
    if not type_ or type_ == "":
        await edit_or_reply(
            event,
            f"**Current Chat Settings:**\n**Thanking Members:** `{must_thank(event.chat_id)}`\n\nUse `{HNDLR}thankmembers on` or `{HNDLR}thankmembers off` to toggle current settings!",
        )
        return
    chat = event.chat_id
    if type_.lower() == "on":
        add_thanks(chat)
    elif type_.lower() == "off":
        remove_thanks(chat)
    await edit_or_reply(
        event,
        f"**Done! Thank you members has been turned** `{type_.lower()}` **for this chat**!",
    )
