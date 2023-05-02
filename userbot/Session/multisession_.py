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
꧁༺ Panda Userbot ༻꧂\n\n
User - @{} 
Pyrogram Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


THON_ON = """
꧁༺ Panda Userbot ༻꧂\n\n
User - @{} 
Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


def Telethon():
    failed = 0
    if pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        try:
            PandaBot.connect()
            tgbot.start(bot_token=Database.BOT_TOKEN)
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
            if pdB.get_key("OWNER_ID") or [] or Var.OWNER_ID == 0:
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

    if pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        try:
            PandaBot4.connect()
            config = PandaBot4(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot4.session.server_address:
                    if PandaBot4.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot4.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot4.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot4.session.save()
                    break
            tgbot.get_me()
            PandaBot4.me = PandaBot4.get_me()
            PandaBot4.uid = tgbot.uid = utils.get_peer_id(PandaBot4.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot4.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot4.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION4 - {e}")
            sys.exit()

    if pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        try:
            PandaBot5.connect()
            config = PandaBot5(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot5.session.server_address:
                    if PandaBot5.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot5.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot5.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot5.session.save()
                    break
            tgbot.get_me()
            PandaBot5.me = PandaBot5.get_me()
            PandaBot5.uid = tgbot.uid = utils.get_peer_id(PandaBot5.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot5.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot5.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION5 - {e}")
            sys.exit()

    if pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        try:
            PandaBot6.connect()
            config = PandaBot6(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot6.session.server_address:
                    if PandaBot6.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot6.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot6.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot6.session.save()
                    break
            tgbot.get_me()
            PandaBot6.me = PandaBot6.get_me()
            PandaBot6.uid = tgbot.uid = utils.get_peer_id(PandaBot6.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot6.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot6.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION6 - {e}")
            sys.exit()

    if pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        try:
            PandaBot7.connect()
            config = PandaBot7(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot7.session.server_address:
                    if PandaBot7.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot7.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot7.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot7.session.save()
                    break
            tgbot.get_me()
            PandaBot7.me = PandaBot7.get_me()
            PandaBot7.uid = tgbot.uid = utils.get_peer_id(PandaBot7.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot7.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot7.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION7 - {e}")
            sys.exit()

    if pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        try:
            PandaBot8.connect()
            config = PandaBot8(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot8.session.server_address:
                    if PandaBot8.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot8.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot8.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot8.session.save()
                    break
            tgbot.get_me()
            PandaBot8.me = PandaBot8.get_me()
            PandaBot8.uid = tgbot.uid = utils.get_peer_id(PandaBot8.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot8.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot8.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION8 - {e}")
            sys.exit()

    if pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        try:
            PandaBot9.connect()
            config = PandaBot9(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot9.session.server_address:
                    if PandaBot9.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot9.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot9.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot9.session.save()
                    break
            tgbot.get_me()
            PandaBot9.me = PandaBot9.get_me()
            PandaBot9.uid = tgbot.uid = utils.get_peer_id(PandaBot9.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot9.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot9.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION9 - {e}")
            sys.exit()

    if pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        try:
            PandaBot10.connect()
            config = PandaBot10(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot10.session.server_address:
                    if PandaBot10.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot10.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot10.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot10.session.save()
                    break
            tgbot.get_me()
            PandaBot10.me = PandaBot10.get_me()
            PandaBot10.uid = tgbot.uid = utils.get_peer_id(PandaBot10.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot10.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot10.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION10 - {e}")
            sys.exit()

    if pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        try:
            PandaBot11.connect()
            config = PandaBot11(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot11.session.server_address:
                    if PandaBot11.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot11.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot11.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot11.session.save()
                    break
            tgbot.get_me()
            PandaBot11.me = PandaBot11.get_me()
            PandaBot11.uid = tgbot.uid = utils.get_peer_id(PandaBot11.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot11.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot11.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION11 - {e}")
            sys.exit()

    if pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        try:
            PandaBot12.connect()
            config = PandaBot12(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot12.session.server_address:
                    if PandaBot12.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot12.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot12.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot12.session.save()
                    break
            tgbot.get_me()
            PandaBot12.me = PandaBot12.get_me()
            PandaBot12.uid = tgbot.uid = utils.get_peer_id(PandaBot12.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot12.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot12.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION12 - {e}")
            sys.exit()

    if pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        try:
            PandaBot13.connect()
            config = PandaBot13(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot13.session.server_address:
                    if PandaBot13.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot13.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot13.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot13.session.save()
                    break
            tgbot.get_me()
            PandaBot13.me = PandaBot13.get_me()
            PandaBot13.uid = tgbot.uid = utils.get_peer_id(PandaBot13.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot13.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot13.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION13 - {e}")
            sys.exit()

    if pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        try:
            PandaBot14.connect()
            config = PandaBot14(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot14.session.server_address:
                    if PandaBot14.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot14.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot14.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot14.session.save()
                    break
            tgbot.get_me()
            PandaBot14.me = PandaBot14.get_me()
            PandaBot14.uid = tgbot.uid = utils.get_peer_id(PandaBot14.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot14.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot14.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION14 - {e}")
            sys.exit()

    if pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        try:
            PandaBot15.connect()
            config = PandaBot15(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot15.session.server_address:
                    if PandaBot15.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot15.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot15.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot15.session.save()
                    break
            tgbot.get_me()
            PandaBot15.me = PandaBot15.get_me()
            PandaBot15.uid = tgbot.uid = utils.get_peer_id(PandaBot15.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot15.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot15.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION15 - {e}")
            sys.exit()

    if pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        try:
            PandaBot16.connect()
            config = PandaBot16(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot16.session.server_address:
                    if PandaBot16.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot16.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot16.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot16.session.save()
                    break
            tgbot.get_me()
            PandaBot16.me = PandaBot16.get_me()
            PandaBot16.uid = tgbot.uid = utils.get_peer_id(PandaBot16.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot16.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot16.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION16 - {e}")
            sys.exit()

    if pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        try:
            PandaBot17.connect()
            config = PandaBot17(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot17.session.server_address:
                    if PandaBot17.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot17.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot17.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot17.session.save()
                    break
            tgbot.get_me()
            PandaBot17.me = PandaBot17.get_me()
            PandaBot17.uid = tgbot.uid = utils.get_peer_id(PandaBot17.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot17.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot17.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION17 - {e}")
            sys.exit()

    if pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        try:
            PandaBot18.connect()
            config = PandaBot18(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot18.session.server_address:
                    if PandaBot18.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot18.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot18.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot18.session.save()
                    break
            tgbot.get_me()
            PandaBot18.me = PandaBot18.get_me()
            PandaBot18.uid = tgbot.uid = utils.get_peer_id(PandaBot18.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot18.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot18.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION18 - {e}")
            sys.exit()

    if pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        try:
            PandaBot19.connect()
            config = PandaBot19(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot19.session.server_address:
                    if PandaBot19.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot19.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot19.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot19.session.save()
                    break
            tgbot.get_me()
            PandaBot19.me = PandaBot19.get_me()
            PandaBot19.uid = tgbot.uid = utils.get_peer_id(PandaBot19.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot19.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot19.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()

    if pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        try:
            PandaBot20.connect()
            config = PandaBot20(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot20.session.server_address:
                    if PandaBot20.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot20.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot20.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot20.session.save()
                    break
            tgbot.get_me()
            PandaBot20.me = PandaBot20.get_me()
            PandaBot20.uid = tgbot.uid = utils.get_peer_id(PandaBot20.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot20.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot20.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION20 - {e}")
            sys.exit()

    if pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        try:
            PandaBot21.connect()
            config = PandaBot21(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot21.session.server_address:
                    if PandaBot21.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot21.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot21.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot21.session.save()
                    break
            tgbot.get_me()
            PandaBot21.me = PandaBot21.get_me()
            PandaBot21.uid = tgbot.uid = utils.get_peer_id(PandaBot21.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot21.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot21.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION21 - {e}")
            sys.exit()

    if pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        try:
            PandaBot22.connect()
            config = PandaBot22(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot22.session.server_address:
                    if PandaBot22.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot22.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot22.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot22.session.save()
                    break
            tgbot.get_me()
            PandaBot22.me = PandaBot22.get_me()
            PandaBot22.uid = tgbot.uid = utils.get_peer_id(PandaBot22.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot22.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot22.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION22 - {e}")
            sys.exit()

    if pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        try:
            PandaBot23.connect()
            config = PandaBot23(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot23.session.server_address:
                    if PandaBot23.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot23.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot23.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot23.session.save()
                    break
            tgbot.get_me()
            PandaBot23.me = PandaBot23.get_me()
            PandaBot23.uid = tgbot.uid = utils.get_peer_id(PandaBot23.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot23.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot23.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION23 - {e}")
            sys.exit()

    if pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        try:
            PandaBot24.connect()
            config = PandaBot24(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot24.session.server_address:
                    if PandaBot24.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot24.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot24.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot24.session.save()
                    break
            tgbot.get_me()
            PandaBot24.me = PandaBot24.get_me()
            PandaBot24.uid = tgbot.uid = utils.get_peer_id(PandaBot24.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot24.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot24.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION24 - {e}")
            sys.exit()

    if pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        try:
            PandaBot25.connect()
            config = PandaBot25(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot25.session.server_address:
                    if PandaBot25.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot25.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot25.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot25.session.save()
                    break
            tgbot.get_me()
            PandaBot25.me = PandaBot25.get_me()
            PandaBot25.uid = tgbot.uid = utils.get_peer_id(PandaBot25.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot25.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot25.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION25 - {e}")
            sys.exit()

    if pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        try:
            PandaBot26.connect()
            config = PandaBot26(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot26.session.server_address:
                    if PandaBot26.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot26.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot26.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot26.session.save()
                    break
            tgbot.get_me()
            PandaBot26.me = PandaBot26.get_me()
            PandaBot26.uid = tgbot.uid = utils.get_peer_id(PandaBot26.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot26.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot26.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION26 - {e}")
            sys.exit()

    if pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        try:
            PandaBot27.connect()
            config = PandaBot27(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot27.session.server_address:
                    if PandaBot27.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot27.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot27.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot27.session.save()
                    break
            tgbot.get_me()
            PandaBot27.me = PandaBot27.get_me()
            PandaBot27.uid = tgbot.uid = utils.get_peer_id(PandaBot27.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot27.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot27.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION27 - {e}")
            sys.exit()

    if pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        try:
            PandaBot28.connect()
            config = PandaBot28(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot28.session.server_address:
                    if PandaBot28.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot28.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot28.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot28.session.save()
                    break
            tgbot.get_me()
            PandaBot28.me = PandaBot28.get_me()
            PandaBot28.uid = tgbot.uid = utils.get_peer_id(PandaBot28.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot28.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot28.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION28 - {e}")
            sys.exit()

    if pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        try:
            PandaBot29.connect()
            config = PandaBot29(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot29.session.server_address:
                    if PandaBot29.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot29.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot29.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot29.session.save()
                    break
            tgbot.get_me()
            PandaBot29.me = PandaBot29.get_me()
            PandaBot29.uid = tgbot.uid = utils.get_peer_id(PandaBot29.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot29.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot29.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION29 - {e}")
            sys.exit()

    if pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        try:
            PandaBot30.connect()
            config = PandaBot30(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot2.session.server_address:
                    if PandaBot30.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot30.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot30.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot30.session.save()
                    break
            tgbot.get_me()
            PandaBot30.me = PandaBot30.get_me()
            PandaBot30.uid = tgbot.uid = utils.get_peer_id(PandaBot30.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot30.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot30.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION30 - {e}")
            sys.exit()

    if pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        try:
            PandaBot31.connect()
            config = PandaBot31(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot31.session.server_address:
                    if PandaBot31.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot31.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot31.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot31.session.save()
                    break
            tgbot.get_me()
            PandaBot31.me = PandaBot31.get_me()
            PandaBot31.uid = tgbot.uid = utils.get_peer_id(PandaBot31.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot31.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot31.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION31 - {e}")
            sys.exit()

    if pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        try:
            PandaBot32.connect()
            config = PandaBot32(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot32.session.server_address:
                    if PandaBot32.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot32.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot32.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot32.session.save()
                    break
            tgbot.get_me()
            PandaBot32.me = PandaBot32.get_me()
            PandaBot32.uid = tgbot.uid = utils.get_peer_id(PandaBot32.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot32.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot32.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION32 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            PandaBot33.connect()
            config = PandaBot33(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot33.session.server_address:
                    if PandaBot33.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot33.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot33.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot33.session.save()
                    break
            tgbot.get_me()
            PandaBot33.me = PandaBot33.get_me()
            PandaBo33.uid = tgbot.uid = utils.get_peer_id(PandaBot33.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot33.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot33.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION33 - {e}")
            sys.exit()

    if pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        try:
            PandaBot34.connect()
            config = PandaBot34(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot34.session.server_address:
                    if PandaBot34.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot34.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot34.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot34.session.save()
                    break
            tgbot.get_me()
            PandaBot34.me = PandaBot34.get_me()
            PandaBot34.uid = tgbot.uid = utils.get_peer_id(PandaBot34.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot34.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot34.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION34 - {e}")
            sys.exit()

    if pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        try:
            PandaBot35.connect()
            config = PandaBot35(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot35.session.server_address:
                    if PandaBot35.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot35.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot35.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot35.session.save()
                    break
            tgbot.get_me()
            PandaBot35.me = PandaBot35.get_me()
            PandaBot35.uid = tgbot.uid = utils.get_peer_id(PandaBot35.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot35.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot35.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION35 - {e}")
            sys.exit()

    if pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        try:
            PandaBot36.connect()
            config = PandaBot36(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot36.session.server_address:
                    if PandaBot36.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot36.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot36.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot36.session.save()
                    break
            tgbot.get_me()
            PandaBot36.me = PandaBot36.get_me()
            PandaBo36.uid = tgbot.uid = utils.get_peer_id(PandaBot36.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot36.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot36.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION36 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        try:
            PandaBot37.connect()
            config = PandaBot37(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot37.session.server_address:
                    if PandaBot37.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot37.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot37.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot37.session.save()
                    break
            tgbot.get_me()
            PandaBot37.me = PandaBot37.get_me()
            PandaBot37.uid = tgbot.uid = utils.get_peer_id(PandaBot37.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot37.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot37.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION37 - {e}")
            sys.exit()

    if pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        try:
            PandaBot38.connect()
            config = PandaBot38(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot38.session.server_address:
                    if PandaBot38.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot38.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot38.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot38.session.save()
                    break
            tgbot.get_me()
            PandaBot38.me = PandaBot38.get_me()
            PandaBot38.uid = tgbot.uid = utils.get_peer_id(PandaBot38.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot38.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot38.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION38 - {e}")
            sys.exit()

    if pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        try:
            PandaBot39.connect()
            config = PandaBot39(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot39.session.server_address:
                    if PandaBot39.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot39.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot39.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot39.session.save()
                    break
            tgbot.get_me()
            PandaBot39.me = PandaBot39.get_me()
            PandaBot39.uid = tgbot.uid = utils.get_peer_id(PandaBot39.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot39.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot39.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION39 - {e}")
            sys.exit()

    if pdB.get_key("SESSION40") or Var.STRING_SESSION40 and Database.BOT_TOKEN:
        try:
            PandaBot40.connect()
            config = PandaBot40(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot40.session.server_address:
                    if PandaBot40.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot40.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot40.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot40.session.save()
                    break
            tgbot.get_me()
            PandaBot40.me = PandaBot40.get_me()
            PandaBo40.uid = tgbot.uid = utils.get_peer_id(PandaBot40.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot40.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot40.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION40 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION41") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        try:
            PandaBot41.connect()
            config = PandaBot41(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot41.session.server_address:
                    if PandaBot41.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot41.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot41.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot41.session.save()
                    break
            tgbot.get_me()
            PandaBot41.me = PandaBot41.get_me()
            PandaBot41.uid = tgbot.uid = utils.get_peer_id(PandaBot41.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot41.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot41.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION41 - {e}")
            sys.exit()

    if pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        try:
            PandaBot42.connect()
            config = PandaBot42(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot42.session.server_address:
                    if PandaBot42.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot42.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot42.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot42.session.save()
                    break
            tgbot.get_me()
            PandaBot42.me = PandaBot42.get_me()
            PandaBot42.uid = tgbot.uid = utils.get_peer_id(PandaBot42.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot42.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot42.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION42 - {e}")
            sys.exit()

    if pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        try:
            PandaBot43.connect()
            config = PandaBot43(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot43.session.server_address:
                    if PandaBot43.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot43.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot43.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot43.session.save()
                    break
            tgbot.get_me()
            PandaBot43.me = PandaBot43.get_me()
            PandaBot43.uid = tgbot.uid = utils.get_peer_id(PandaBot43.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot43.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot43.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION43 - {e}")
            sys.exit()

    if pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        try:
            PandaBot44.connect()
            config = PandaBot44(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot44.session.server_address:
                    if PandaBot44.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot44.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot44.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot44.session.save()
                    break
            tgbot.get_me()
            PandaBot44.me = PandaBot44.get_me()
            PandaBot44.uid = tgbot.uid = utils.get_peer_id(PandaBot44.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot44.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot44.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION44 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        try:
            PandaBot45.connect()
            config = PandaBot45(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot45.session.server_address:
                    if PandaBot45.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot45.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot45.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot45.session.save()
                    break
            tgbot.get_me()
            PandaBot45.me = PandaBot45.get_me()
            PandaBot45.uid = tgbot.uid = utils.get_peer_id(PandaBot45.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot45.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot45.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION45 - {e}")
            sys.exit()

    if pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        try:
            PandaBot46.connect()
            config = PandaBot46(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot46.session.server_address:
                    if PandaBot46.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot46.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot46.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot46.session.save()
                    break
            tgbot.get_me()
            PandaBot46.me = PandaBot46.get_me()
            PandaBot46.uid = tgbot.uid = utils.get_peer_id(PandaBot46.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot46.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot46.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION46 - {e}")
            sys.exit()

    if pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        try:
            PandaBot47.connect()
            config = PandaBot47(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot47.session.server_address:
                    if PandaBot47.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot47.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot47.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot47.session.save()
                    break
            tgbot.get_me()
            PandaBot47.me = PandaBot47.get_me()
            PandaBot47.uid = tgbot.uid = utils.get_peer_id(PandaBot47.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot47.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot47.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION47 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            PandaBot48.connect()
            config = PandaBot48(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot48.session.server_address:
                    if PandaBot48.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot48.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot48.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot48.session.save()
                    break
            tgbot.get_me()
            PandaBot48.me = PandaBot48.get_me()
            PandaBot48.uid = tgbot.uid = utils.get_peer_id(PandaBot48.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot48.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot48.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION48 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        try:
            PandaBot49.connect()
            config = PandaBot49(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot49.session.server_address:
                    if PandaBot49.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot49.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot49.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot49.session.save()
                    break
            tgbot.get_me()
            PandaBot49.me = PandaBot49.get_me()
            PandaBot49.uid = tgbot.uid = utils.get_peer_id(PandaBot49.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot49.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot49.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION49 - {e}")
            sys.exit()

    if pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        try:
            PandaBot50.connect()
            config = PandaBot50(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == PandaBot50.session.server_address:
                    if PandaBot50.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot50.session.dc_id}"
                            f" to {option.id}"
                    )
                    PandaBot50.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot50.session.save()
                    break
            tgbot.get_me()
            PandaBot50.me = PandaBot50.get_me()
            PandaBot50.uid = tgbot.uid = utils.get_peer_id(PandaBot50.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot50.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", PandaBot50.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION50 - {e}")
            sys.exit()

    if not pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION40") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION48") or Var.STRING_SESSION48 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        failed += 1
    return failed

def Pyrogram():
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION and Database.BOT_TOKEN:
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
    print(f"⚙️ Panda Userbot {pyrover} Telah Aktif")
    idle()
    
