# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 


from io import BytesIO

from aiohttp import ClientSession
from userbot import pyrobot as app
from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply

from . import HELP


HELP(
    "carbon",
)
aiosession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@ilhammansiz_on_cmd(['carbon', 'cr'],
               cmd_help={
                'help': 'Carbon.',
                'example': '{ch}carbon reply ke textt'})
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    Panda = await edit_or_reply(message, "`Preparing Carbon...`")
    carbon = await make_carbon(text)
    await Panda.edit("`Uploading...`")
    ah = await app.get_me()
    await app.send_photo(
        message.chat.id,
        carbon,
        caption=f"**Carbonised by** {ah.mention}",
    )
    await Panda.delete()
    carbon.close()
