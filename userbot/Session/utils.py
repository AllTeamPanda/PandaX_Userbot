# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.

import ublackdev
import logging
import platform
import time
from pyrogram import __version__ as pyro_version
from telegraph import Telegraph
from ._var import Config
from ..versions import __version__ as botver
from .._helper import Helpers
from .._func import Methods
from .._database.classdb import Database

class Utils(Methods, Config, Database, Helpers):
    userbot_version = f"{botver}"
    assistant_version = f"v{botver}"
    python_version = str(platform.python_version())
    pyrogram_version = str(pyro_version)
    CMD_HELP = {}
    owner_name = "Ilham Mansiz"
    owner_id = f"{ublackdev.plist}"
    owner_username = "@diemmmmmmmmmm"
    Repo = "https://github.com/ilhammansiz/PandaX_Userbot.git"
    StartTime = time.time()
    logging.getLogger("pyrogram.syncer").setLevel(
        logging.CRITICAL
    )
    logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
    logging.basicConfig(format="%(asctime)s %(message)s")
    log = logging.getLogger("———")
    telegraph = Telegraph()
    telegraph.create_account(
        short_name=Config.TL_NAME if Config.TL_NAME else "Panda Userbot"
    )
