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
    
