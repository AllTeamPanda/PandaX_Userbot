from telethon import events, Button
from Configs import Config
from Panda.status import is_admin
from telethon.utils import get_display_name
from Panda import PandaBot
bot = PandaBot.tgbot
X = "https://telegra.ph/file/695cb726224d2a7037399.jpg"
from Panda.modules import mention
owner = "https://t.me/diemmmmmmmmmm"
support = "https://t.me/TeamSquadUserbotSupport"
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

helpn =[
    [Button.inline("📂 Notes 📂", data="notess"), Button.inline("🐼 Animation 🐼", data="animasis")],
    [Button.inline("🤡 Admin 🤡", data="admins"), Button.inline("🏷 Bans 🏷", data="banss")],
    [Button.inline(" 🔖Pins 🔖", data="pinss"), Button.inline("📌 Pugres 📌", data="purgess")],
    [Button.inline("🔐 Locks 🔐", data="lockss"), Button.inline("🗂 Misc 🗂", data="miscs")],
    [Button.inline("🧟‍♂️ Zombies 🧟‍♂️", data="zombiess"), Button.inline("📨 Telegraph 📨", data="telegrams")],
    [Button.inline("🎀 Tiny 🎀", data="tinys"), Button.inline("🃏 Covid 🃏", data="covids")],
    [Button.inline("🎎 ZonaDewasa 🎎", data="payudaras"), Button.inline("🇮🇩 Country 🇮🇩", data="negaras")],
    [Button.inline("🔊 TTS 🔊", data="tts"), Button.inline("🔋 Heroku 🔋", data="herokus")],
    [Button.inline("🛠 Menu Utama 🛠", data="mainmenu")],
    [Button.inline("🚫 Close 🚫", data="closeit")]]

HELP_TEXT = f"""
**Hello 🙋\nSaya Asistennya bot: {mention}\nIni Tombol Menu Help Asisten PandaX_Userbot:**

Support** [UserBotSupport]({support})**
"""


@bot.on(events.NewMessage(pattern=("/help")))
async def alive(event):
  await Stark.send_message(event.chat, HELP_TEXT, file=X, buttons=btn)



@bot.on(events.callbackquery.CallbackQuery(data="helpp"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)


@bot.on(events.callbackquery.CallbackQuery(data="helpbot"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=helpn)
