# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


from .extdl import *
from .paste import *
flag = True
check = 0
while flag:
    try:
        from . import format as _format
        from . import tools as _pandatools
        from . import utils as _pandautils
        from .events import *
        from .format import htmlmentionuser, mentionuser, parse_pre

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
