# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from telethon import functions, utils
from pyrogram import idle
from .._database._var import Var, Database
from logging import getLogger
from .._database import pdB
from .client import *

from .pyroclient import *
import sys
LOGS = getLogger(__name__)
import os

from pyrogram import __version__ as pyrover
PRIVATE = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID"))


cmdhr = os.environ.get("COMMAND_HAND_LER") or "."

MSG_ON = """
꧁༺ Panda Userbot ༻꧂

👿 Pengguna - @{}

⚙️ Pyrogram Version - `{}'
`[TELAH DIAKTIFKAN]`
°Ketik `{}alive` untuk Mengecheck Bot
"""


THON_ON = """
꧁༺ Panda Userbot ༻꧂

👿 Pengguna - @{}

⚙️ Version - `{}'
`[TELAH DIAKTIFKAN]`
°Ketik `{}alive` untuk Mengecheck Bot
"""


def Telethon():
    if Var.STRING_SESSION and Database.BOT_TOKEN:
        try:
            PandaBot.connect()
            tgbot.start(bot_token=Database.BOT_TOKEN)
            if Var.VC_SESSION:
                vcbot.start()
                call_py.start()
            config = PandaBot(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot.session.server_address:
                    if PandaBot.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot.session.save()
                    break
            tgbot.me = tgbot.get_me()
            PandaBot.me = PandaBot.get_me()
            PandaBot.uid = tgbot.uid = utils.get_peer_id(PandaBot.me)      
            if pdB.get_key("BOT_USERNAME"):
                pdB.set_key("BOT_USERNAME", tgbot.me.username)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION1 - {e}")
            sys.exit()
            

    if pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        try:
            PandaBot2.connect()
            config = PandaBot2(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot2.session.server_address:
                    if PandaBot2.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot2.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot2.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot2.session.save()
                    break
            tgbot.get_me()
            PandaBot2.me = PandaBot2.get_me()
            PandaBot2.uid = tgbot.uid = utils.get_peer_id(PandaBot2.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot2.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot2.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        try:
            PandaBot3.connect()
            config = PandaBot3(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot3.session.server_address:
                    if PandaBot3.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot3.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot3.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot3.session.save()
                    break
            tgbot.get_me()
            PandaBot3.me = PandaBot3.get_me()
            PandaBot3.uid = tgbot.uid = utils.get_peer_id(PandaBot3.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot3.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot3.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION3 - {e}")
            sys.exit()


def Pyrogram():
    if Database.PyroSESSION and Database.BOT_TOKEN:
        if pyrobot:
            pyrobot.start()
            print(f"⚙️ Panda Userbot {pyrover} Telah Aktif")
            idle()
"""
        if app.bot:
            print("Activating assistant.\n")
            app.bot.start()
            print("Assistant activated.\n")
            asistant = app.import_module("userbot/modules/pyrogram/asistant/", exclude=app.NoLoad())
            print(f"\n\n{asistant} modules Loaded Sucesfull\n\n")
        else:
            print("Assistant start unsuccessful, please check that you have given the bot token.\n")
            print("skipping assistant start !")
        
    if app:
        print("Activating assistant.\n")
        app.start()
        print("Assistant activated.\n")
    else:
        print("Assistant start unsuccessful, please check that you have given the bot token.\n")
        print("skipping assistant start !")
    print("Modules: Installing.\n\n")
    modules = app.import_module("userbot/modules/pyrogram/", exclude=app.NoLoad())
    print(f"\n\n{modules} modules Loaded Sucesfull\n\n")
"""
    
