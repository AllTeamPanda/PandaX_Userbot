from platform import python_version

from telethon import version
from Panda import PandaBot
import heroku3
from telethon import events
from Panda import StartTime
import time
import datetime
from telethon import events, Button, custom
import re, os
bot = PandaBot
Stark = PandaBot.tgbot
from Panda.modules import mention

BOT = "𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕"
X = "https://telegra.ph/file/695cb726224d2a7037399.jpg"

ALIVEPANDA = f"""
Hᴇʟʟᴏ Tʜɪs ɪs Asisten of {mention}

Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ

Telethon Vᴇʀsɪᴏɴ : `{version.__version__}`

Python Version : `{python_version()}`

Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ.....

Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ
"""


PANDAALIVE =[
          [Button.url("PandaX_Userbot", "https://github.com/ilhammansiz/PandaX_Userbot"), Button.url("Deploy Panda", "https://heroku.com/deploy?template=https://github.com/ilhammansiz/PandaX_Userbott-Deploy")],
          [Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://t.me/UserbotTEAM_Tutorial"), Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "t.me/apiuserbutpetercord_bot")],
          [Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/UserbotTEAM_Tutorial"), Button.url("Rᴇᴅɪs", "https://redislabs.com")],
          [Button.url("Depolover", "t.me/diemmmmmmmmmm")]]


@Stark.on(events.NewMessage(pattern=("/alive")))
async def alive(event):
  await Stark.send_message(event.chat, ALIVEPANDA, file=X, buttons=PANDAALIVE)

@Stark.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await Stark.send_message(event.chat, "**PandaX_Userbot** \n\nDepolover :- @diemmmmmmmmmm", buttons=[[Button.url(" Rᴇᴘᴏ ", "https://github.com/ilhammansiz/PandaX_Userbot"), Button.url(" Dᴇᴘʟᴏʏ ", "https://heroku.com/deploy?template=https://github.com/IlhamMansiz/Pandapack")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Stark.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i> ꧁༺🐼 Panda Userbot 🐼༻꧂ </i></b>\n"
        "<b>➥ Timer:</b> <code>{}</code>\n"
        "<b>➥ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
