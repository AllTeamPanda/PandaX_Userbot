import logging
import platform
import time

from pyrogram import __version__ as pyro_version
from telegraph import Telegraph

from .._database.classdb import Database
from ..helpers import Helpers
from .._func import Methods
from ..Var import Config
from ..versions import __version__ as botver
import ublackdev 

class Utils(Methods, Config, Database, Helpers):
    # versions /

    userbot_version = f"{botver}"
    assistant_version = f"v{botver}"
    python_version = str(platform.python_version())
    pyrogram_version = str(pyro_version)

    # containers /

    CMD_HELP = {}

    # owner details /

    owner_name = "Ilham Mansiz"
    owner_id = f"{ublackdev.plist}"
    owner_username = "@diemmmmmmmmmm"

    # other /

    Repo = "https://github.com/ilhammansiz/PandaX_Userbot.git"
    StartTime = time.time()

    # debugging /

    logging.getLogger("pyrogram.syncer").setLevel(
        logging.CRITICAL
    )  # turn off pyrogram logging
    logging.getLogger("pyrogram").setLevel(logging.CRITICAL)

    logging.basicConfig(format="%(asctime)s %(message)s")
    log = logging.getLogger("———")

    # telegraph /

    telegraph = Telegraph()
    telegraph.create_account(
        short_name=Config.TL_NAME if Config.TL_NAME else "Asterix Userbot"
    )
