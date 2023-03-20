# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from pyrogram import Client
from .classpyro import PyroClient
from .._database import pdB
from .._database._var import Database



if pdB.get_key("PyroSESSION") or Database.PyroSESSION:
    app = PyroClient()
else:
    app = None

