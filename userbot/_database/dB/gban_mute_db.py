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


def gban(user, reason):
    ok = list_gbanned()
    ok.update({int(user): reason or "No Reason. "})
    return udB.set_key("GBAN", ok)


def ungban(user):
    ok = list_gbanned()
    if ok.get(int(user)):
        del ok[int(user)]
        return udB.set_key("GBAN", ok)


def is_gbanned(user):
    ok = list_gbanned()
    if ok.get(int(user)):
        return ok[int(user)]


def gmute(user):
    ok = list_gmuted()
    ok.append(int(user))
    return udB.set_key("GMUTE", ok)


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(int(user))
        return udB.set_key("GMUTE", ok)


def is_gmuted(user):
    return int(user) in list_gmuted()


def list_gmuted():
    return udB.get_key("GMUTE") or []
