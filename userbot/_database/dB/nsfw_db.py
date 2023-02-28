# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_stuff(key="NSFW"):
    return udB.get_key(key) or {}


def nsfw_chat(chat, action):
    x = get_stuff()
    x.update({chat: action})
    return udB.set_key("NSFW", x)


def rem_nsfw(chat):
    x = get_stuff()
    if x.get(chat):
        x.pop(chat)
        return udB.set_key("NSFW", x)


def is_nsfw(chat):
    x = get_stuff()
    if x.get(chat):
        return x[chat]


def profan_chat(chat, action):
    x = get_stuff("PROFANITY")
    x.update({chat: action})
    return udB.set_key("PROFANITY", x)


def rem_profan(chat):
    x = get_stuff("PROFANITY")
    if x.get(chat):
        x.pop(chat)
        return udB.set_key("PROFANITY", x)


def is_profan(chat):
    x = get_stuff("PROFANITY")
    if x.get(chat):
        return x[chat]
