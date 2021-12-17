from PandaX_Userbot.runx import Stark
from telethon.tl.types import InputMediaDice
import asyncio
import requests
from telethon import events, Button
import time
from Configs import Config
from . import mansiez

from collections import deque

@mansiez(pattern="/moon ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    event = await event.reply("🌗")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)



GAMBAR_OK = """
░▐▀▀▀▀▀▀▀▀▌▐▀▌▄▄▄▀▀▓▀
░▐▌▓▀▀▀▀▓▌▌▐▐▌▀▌▄▄▀░░
░▐▐▌▐▀▀▌▐▐▌▐▌▐▓▄▀░░░░
░▐▌▌▐▄▄▌▐▌▌▐▐▌▓▀▄░░░░
░▐▐▓▄▄▄▄▓▐▌▐▌▌▄▌▀▀▄░░
░▐▄▄▄▄▄▄▄▄▌▐▄▌▀▀▀▄▄▓▄
"""


GAMBAR_TENGKORAK = """
░░░░░░░░░░░░░▄▐░░░░
░░░░░░░▄▄▄░░▄██▄░░░
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█▄░░░░
░░░░░░░▐▌▀▄▀▄▀▐░░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░
"""

GAMBAR_KONTL = """
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠁⠉⠉⠉
"""


@Stark.on(events.NewMessage(pattern="[!?/]kntl"))
async def kntl(event):

    if event.is_group:
       await event.reply(GAMBAR_KONTL)

@Stark.on(events.NewMessage(pattern="[!?/]ok"))
async def ok(event):

    if event.is_group:
       await event.reply(GAMBAR_OK)


@Stark.on(events.NewMessage(pattern="[!?/]tengkorak"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(GAMBAR_TENGKORAK)

@Stark.on(events.NewMessage(pattern="[!?/]dice"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice(''))

@Stark.on(events.NewMessage(pattern="[!?/]dart"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice('🎯'))

@Stark.on(events.NewMessage(pattern="[!?/]ball"))
async def tengkorak(event):

    if event.is_group:
       await event.reply(file=InputMediaDice('🏀'))

@Stark.on(events.NewMessage(pattern="[!?/]ajg"))
async def tengkorak(event):

    if event.is_group:
        a = await event.reply("E anjeng kau kau bilang aku anak anjeng kau anjeng")
        await asyncio.sleep(0.5)
        await a.edit("Ngentot kau")

@Stark.on(events.NewMessage(pattern="[!?/]bom"))
async def tengkorak(event):

    if event.is_group:
        ilham = await event.reply("Ada bom lariiii...")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
        await asyncio.sleep(1)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
        await asyncio.sleep(0.5)
        await ilham.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵")


ANIMASI = """ Perintah Bot Animasi
- /kntl 
- /dice
- /dart
- /ball
- /ok 
- /tengkorak 
- /bom
/moon
"""




@Stark.on(events.callbackquery.CallbackQuery(data="animasi"))
async def _(event):
    await event.edit(ANIMASI, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbot")]])

@Stark.on(events.callbackquery.CallbackQuery(data="animasis"))
async def _(event):
    await event.edit(ANIMASI, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbott")]])



NOTE = """ Perintah Bot NOTES
- /save 
- /notes
- /clearnote
"""




@Stark.on(events.callbackquery.CallbackQuery(data="notes"))
async def _(event):
    await event.edit(NOTE, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbot")]])

@Stark.on(events.callbackquery.CallbackQuery(data="notess"))
async def _(event):
    await event.edit(NOTE, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbott")]])


