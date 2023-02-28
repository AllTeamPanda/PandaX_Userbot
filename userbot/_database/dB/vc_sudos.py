# Copyright (C) 2021-2022 TeamUltroid
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from ... import udB


def get_vcsudos():
    return udB.get_key("VC_SUDOS") or []


def is_vcsudo(id):
    return id in get_vcsudos()


def add_vcsudo(id):
    sudos = get_vcsudos()
    sudos.append(id)
    return udB.set_key("VC_SUDOS", sudos)


def del_vcsudo(id):
    if is_vcsudo(id):
        sudos = get_vcsudos()
        sudos.remove(id)
        return udB.set_key("VC_SUDOS", sudos)
