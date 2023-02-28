# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_stuff():
    return udB.get_key("ASST_CMDS") or {}


def add_cmd(cmd, msg, media, button):
    ok = get_stuff()
    ok.update({cmd: {"msg": msg, "media": media, "button": button}})
    return udB.set_key("ASST_CMDS", ok)


def rem_cmd(cmd):
    ok = get_stuff()
    if ok.get(cmd):
        ok.pop(cmd)
        return udB.set_key("ASST_CMDS", ok)


def cmd_reply(cmd):
    ok = get_stuff()
    if ok.get(cmd):
        okk = ok[cmd]
        return okk["msg"], okk["media"], okk["button"] if ok.get("button") else None
    return


def list_cmds():
    ok = get_stuff()
    return ok.keys()
