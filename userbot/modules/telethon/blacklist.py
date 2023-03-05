# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot



plugin_category = "modules"

from ..._database.dB.blacklist_db import (
    add_blacklist,
    get_blacklist,
    list_blacklist,
    rem_blacklist,
)
from telethon import events
from pyPanda import get_string
from ... import udB
from . import edit_or_reply, PandaBot

@PandaBot.ilhammansiz_cmd(
    pattern="blacklist$",
    command=("blacklist", plugin_category),
    info={
       "description": "blacklist the choosen word in that chat",
        "usage": [
            "{tr}blacklist <word/all words with a space>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def af(e):
    wrd = e.pattern_match.group(1).strip()
    chat = e.chat_id
    if not (wrd):
        return await edit_or_reply(e, get_string("blk_1"), time=5)
    wrd = e.text[11:]
    heh = wrd.split(" ")
    for z in heh:
        add_blacklist(int(chat), z.lower())
    PandaBot.add_handler(blacklist, events.NewMessage(incoming=True))
    await edit_or_reply(e, get_string("blk_2").format(wrd))


@PandaBot.ilhammansiz_cmd(
    pattern="remblacklist$",
    command=("remblacklist", plugin_category),
    info={
       "description": "Remove the word from blacklist",
        "usage": [
            "{tr}blacklist <word>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def rf(e):
    wrd = e.pattern_match.group(1).strip()
    chat = e.chat_id
    if not wrd:
        return await edit_or_reply(e, get_string("blk_3"), time=5)
    wrd = e.text[14:]
    heh = wrd.split(" ")
    for z in heh:
        rem_blacklist(int(chat), z.lower())
    await edit_or_reply(e, get_string("blk_4").format(wrd))



@PandaBot.ilhammansiz_cmd(
    pattern="listblacklist$",
    command=("listblacklist", plugin_category),
    info={
       "description": "List the word from blacklist",
        "usage": [
            "{tr}listblacklist <word>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def lsnote(e):
    if x := list_blacklist(e.chat_id):
        sd = get_string("blk_5")
        return await e.eor(sd + x)
    await e.eor(get_string("blk_6"))


async def blacklist(e):
    if x := get_blacklist(e.chat_id):
        text = e.text.lower().split()
        if any((z in text) for z in x):
            try:
                await e.delete()
            except BaseException:
                pass


if udB.get_key("BLACKLIST_DB"):
    PandaBot.add_handler(blacklist, events.NewMessage(incoming=True))
