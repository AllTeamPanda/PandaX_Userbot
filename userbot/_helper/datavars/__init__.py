# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.


from .botconfig import BOTDV, BotConfig
from .otherconfig import OTHERDV, OtherConfig
from .userconfig import USERDV, UserConfig


class DataVars(BotConfig, OtherConfig, UserConfig):
    DVLIST = BOTDV + OTHERDV + USERDV
