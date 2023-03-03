# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def list_gbanned():
    return udB.get_key("GBAN") or {}


def gban(chat_id, reason):
    ok = list_gbanned()
    ok.update(chat_id: reason or "No Reason. ")
    return udB.set_key("GBAN", ok)


def ungban(chat_id):
    ok = list_gbanned()
    if ok.get(chat_id):
        del ok[chat_id]
        return udB.set_key("GBAN", ok)


def is_gbanned(chat_id):
    ok = list_gbanned()
    if ok.get(chat_id):
        return ok[chat_id]


def gmute(sender):
    ok = list_gmuted()
    ok.append(sender)
    return udB.set_key("GMUTE", ok)


def ungmute(sender):
    ok = list_gmuted()
    if sender in ok:
        ok.remove(sender)
        return udB.set_key("GMUTE", ok)


def is_gmuted(sender_id):
    return sender_id in list_gmuted()


def list_gmuted():
    return udB.get_key("GMUTE") or []
