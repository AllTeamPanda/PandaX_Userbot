from telethon import events, Button
from PandaX_Userbot.runx import Stark
from Configs import Config
from PandaX_Userbot.status import is_admin
from telethon.utils import get_display_name
from PandaX_Userbot import petercordpanda_bot
from PandaX_Userbot.functions.asst_fns import *
from PandaX_Userbot.PandaVX import owner_and_sudos
from PandaX_v20 import *

X = "https://telegra.ph/file/695cb726224d2a7037399.jpg"

btn =[
    [Button.inline("📂 Notes 📂", data="notes"), Button.inline("🐼 Animation 🐼", data="animasi")],
    [Button.inline("🤡 Admin 🤡", data="admin"), Button.inline("🏷 Bans 🏷", data="bans")],
    [Button.inline(" 🔖Pins 🔖", data="pins"), Button.inline("📌 Pugres 📌", data="purges")],
    [Button.inline("🔐 Locks 🔐", data="locks"), Button.inline("🗂 Misc 🗂", data="misc")],
    [Button.inline("🧟‍♂️ Zombies 🧟‍♂️", data="zombies"), Button.inline("📨 Telegraph 📨", data="telegram")],
    [Button.inline("🎀 Tiny 🎀", data="tiny"), Button.inline("🃏 Covid 🃏", data="covid")],
    [Button.inline("🎎 ZonaDewasa 🎎", data="payudara"), Button.inline("🇮🇩 Country 🇮🇩", data="negara")],
    [Button.inline("🔊 TTS 🔊", data="tts"), Button.inline("🔋 Heroku 🔋", data="heroku")],
    [Button.inline("🚫 Close 🚫", data="closeit")]]

HELP_TEXT = f"""
**Hello 🙋 Saya Asistennya bot: [{petercordpanda_bot.me.first_name}](tg://user?id={petercordpanda_bot.uid})\nIni Tombol Menu Help Asisten PandaX_Userbot:**

/start - To Start Me ;)
/help - To Get Available Help Menu

__Made in__ @diemmmmmmmmmm\nSupport** @TeamSquadUserbotSupport**
"""


@Stark.on(events.NewMessage(pattern=("/help")))
async def alive(event):
  await Stark.send_message(event.chat, HELP_TEXT, file=X, buttons=btn)



@Stark.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
