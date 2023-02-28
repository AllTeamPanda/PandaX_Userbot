# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_stuff():
    return udB.get_key("ECHO") or {}


def add_echo(chat, user):
    x = get_stuff()
    if k := x.get(int(chat)):
        if user not in k:
            k.append(int(user))
        x.update({int(chat): k})
    else:
        x.update({int(chat): [int(user)]})
    return udB.set_key("ECHO", x)


def rem_echo(chat, user):
    x = get_stuff()
    if k := x.get(int(chat)):
        if user in k:
            k.remove(int(user))
        x.update({int(chat): k})
    return udB.set_key("ECHO", x)


def check_echo(chat, user):
    x = get_stuff()
    if (k := x.get(int(chat))) and int(user) in k:
        return True


def list_echo(chat):
    x = get_stuff()
    return x.get(int(chat))
