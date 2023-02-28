# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.

from .on_callback import OnCallbackQuery
from .on_inline import OnInlineQuery
from .on_message import OnMessage


class Decorators(
    OnMessage,
    OnInlineQuery,
    OnCallbackQuery,
):
    pass
