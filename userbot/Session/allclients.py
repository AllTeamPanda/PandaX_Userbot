# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from logging import getLogger
from .._database._var import Var, Database
from .client import PandaBot, PandaBot2, PandaBot3, PandaBot4, PandaBot5, PandaBot6, PandaBot7, PandaBot8, PandaBot9, PandaBot10, PandaBot11, PandaBot12, PandaBot13, PandaBot14, PandaBot15, PandaBot16, PandaBot17, PandaBot18, PandaBot19, PandaBot10, PandaBot20, PandaBot21, PandaBot22, PandaBot23, PandaBot24, PandaBot25, PandaBot26, PandaBot27, PandaBot28, PandaBot29, PandaBot30, PandaBot31, PandaBot32, PandaBot33, PandaBot34, PandaBot35, PandaBot36, PandaBot37, PandaBot38, PandaBot39, PandaBot40, PandaBot41, PandaBot42, PandaBot43, PandaBot44, PandaBot45, PandaBot46, PandaBot47, PandaBot48, PandaBot49, PandaBot50
from .._database import pdB
LOGS = getLogger(__name__)

try:
    if not pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        PandaBot = PandaBot
    if not pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        PandaBot = PandaBot2
    if not pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        PandaBot = PandaBot3
    if not pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        PandaBot = PandaBot4
    if not pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        PandaBot = PandaBot5
    if not pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        PandaBot = PandaBot6
    if not pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        PandaBot = PandaBot7
    if not pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        PandaBot = PandaBot8
    if not pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        PandaBot = PandaBot9
    if not pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        PandaBot = PandaBot10
    if not pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        PandaBot = PandaBot11
    if not pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        PandaBot = PandaBot12
    if not pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        PandaBot = PandaBot13
    if not pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        PandaBot = PandaBot14
    if not pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        PandaBot = PandaBot15
    if not pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        PandaBot = PandaBot16
    if not pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        PandaBot = PandaBot17
    if not pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        PandaBot = PandaBot18
    if not pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        PandaBot = PandaBot19
    if not pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        PandaBot = PandaBot20
    if not pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        PandaBot = PandaBot21
    if not pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        PandaBot = PandaBot22
    if not pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        PandaBot = PandaBot25
    if not pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        PandaBot = PandaBot24
    if not pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        PandaBot = PandaBot25
    if not pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        PandaBot = PandaBot26
    if not pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        PandaBot = PandaBot27
    if not pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        PandaBot = PandaBot28
    if not pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        PandaBot = PandaBot29
    if not pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        PandaBot = PandaBot30
    if not pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        PandaBot = PandaBot31
    if not pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        PandaBot = PandaBot32
    if not pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        PandaBot = PandaBot33
    if not pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        PandaBot = PandaBot34
    if not pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        PandaBot = PandaBot35
    if not pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        PandaBot = PandaBot36
    if not pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        PandaBot = PandaBot37
    if not pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        PandaBot = PandaBot38
    if not pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        PandaBot = PandaBot39
    if not pdB.get_key("SESSION40") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        PandaBot = PandaBot40
    if not pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        PandaBot = PandaBot42
    if not pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        PandaBot = PandaBot43
    if not pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        PandaBot = PandaBot44
    if not pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        PandaBot = PandaBot45
    if not pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        PandaBot = PandaBot46
    if not pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        PandaBot = PandaBot47
    if not pdB.get_key("SESSION48") or Var.STRING_SESSION48 and Database.BOT_TOKEN:
        PandaBot = PandaBot48
    if not pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        PandaBot = PandaBot49
    if not pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        PandaBot = PandaBot50
except Exception as e:
    LOGS.error(f"PandaBot - {e}")
