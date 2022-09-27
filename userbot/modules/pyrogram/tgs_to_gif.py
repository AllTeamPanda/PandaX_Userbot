# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 

import os
from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply, runcmd
from . import HELP


HELP(
    "tgs_to_gif",
)


@ilhammansiz_on_cmd(
    ["ttg"],
    cmd_help={
        "help": "Convert Tgs To Gif",
        "example": "{ch}ttg (Reply To Animated Sticker)",
    },
)
async def ttg_s(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    if not message.reply_to_message or not message.reply_to_message.sticker:
        await pablo.edit("Reply to A Animated Sticker...")
        return
    if message.reply_to_message.sticker.mime_type != "application/x-tgsticker":
        await pablo.edit("`Reply to A Animated Sticker...`")
        return
    lol = await message.reply_to_message.download("tgs.tgs")
    file_name = "tgs_to_gif.mp4"
    cmdo = f"lottie_convert.py {lol} {file_name}"
    await runcmd(cmdo)
    if not os.path.exists(file_name):
        return await pablo.edit("`Unable To Convert To Gif. Please Check If Sticker is Valid.`")
    await client.send_animation(message.chat.id, file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
    await pablo.delete()
