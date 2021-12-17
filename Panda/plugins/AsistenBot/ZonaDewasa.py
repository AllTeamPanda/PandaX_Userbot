import asyncio
import os
import urllib
from telethon import *
import requests
from Panda import PandaBot
from . import mansiez
bot = Stark
TMP_DOWNLOAD_DIRECTORY = "resources/downloads/"
Stark = PandaBot.tgbot
bot = PandaBot.tgbot

@mansiez(pattern="/tetek ?(.*)")
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(TMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Menemukan beberapa payudara besar untukmu 😂")
    await asyncio.sleep(0.5)
    await a.edit("Ini besar banget nih 😂")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()




@mansiez(pattern="/asupan ?(.*)")
async def _(event):
    try:
        response = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
        a = await event.reply("Menemukan beberapa jogetan asupan untukmu 😂")
        await asyncio.sleep(0.5)
        await a.edit("Ini lagi dikirim nih 😂")
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
        await a.delete()
    except Exception:
        await event.reply("**Tidak bisa menemukan video asupan.**")




@mansiez(pattern="/chika ?(.*)")
async def _(event):
    try:
        response = requests.get("https://tede-api.herokuapp.com/api/chika").json()
        a = await event.reply("Menemukan beberapa jogetan chika untukmu 😂")
        await asyncio.sleep(0.5)
        await a.edit("Ini lagi dikirim nih 😂")
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
        await a.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")



@mansiez(pattern="^/gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.reply("`Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.reply("`Mengirim Pesan Global... 📣`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")



Payudara = """
- /tetek - menemukan gambar tetek 
- /asupan menemukan asupan 🙂
- /chika liat lah🙂
"""

