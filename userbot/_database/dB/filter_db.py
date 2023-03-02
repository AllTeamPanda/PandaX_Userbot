# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_stuff():
    return udB.get_key("FILTERS") or {}


def add_filter(chat_id, keyword, reply, f_mesg_id):
    ok = get_stuff()
    if ok.get(chat_id):
        ok[chat_id].update({str(chat_id): {keyword: {"reply": reply, "f_mesg_id": f_mesg_id}}})
    else:
        ok.update({str(chat_id): {keyword: {"reply": reply, "f_mesg_id": f_mesg_id}}})
    udB.set_key("FILTERS", ok)


def rem_filter(chat_id, keyword):
    ok = get_stuff()
    if ok.get(chat_id) and ok[chat_id].get(keyword):
        ok[chat_id].pop(keyword)
        udB.set_key("FILTERS", ok)


def rem_all_filter(chat_id):
    ok = get_stuff()
    if ok.get(chat_id):
        ok.pop(chat_id)
        udB.set_key("FILTERS", ok)


def get_filter(chat_id):
    ok = get_stuff()
    if ok.get(chat_id):
        return ok[chat_id]


def list_filter(chat_id):
    ok = get_stuff()
    if ok.get(chat_id):
        return "".join(f"👉 `{z}`\n" for z in ok[chat_id])
