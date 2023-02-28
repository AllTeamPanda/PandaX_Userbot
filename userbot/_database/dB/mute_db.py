# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_muted():
    return udB.get_key("MUTE") or {}


def mute(chat, id):
    ok = get_muted()
    if ok.get(chat):
        if id not in ok[chat]:
            ok[chat].append(id)
    else:
        ok.update({chat: [id]})
    return udB.set_key("MUTE", ok)


def unmute(chat, id):
    ok = get_muted()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    return udB.set_key("MUTE", ok)


def is_muted(chat, id):
    ok = get_muted()
    return bool(ok.get(chat) and id in ok[chat])
