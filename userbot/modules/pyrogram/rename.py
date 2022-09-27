# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import time

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply, get_text, progress

from . import HELP


HELP(
    "rename",
)

@ilhammansiz_on_cmd(
    ["rename", "rupload"],
    cmd_help={
        "help": "Rename File!",
        "example": "{ch}rename (reply to file) (new name)",
    },
)
async def rename(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    fname = get_text(message)
    if not fname:
        await pablo.edit("Please Give New Name For File With Extension")
        return
    if not message.reply_to_message:
        await pablo.edit("Please Reply To A File To Rename")
        return
    await pablo.edit("⚡️`Rename and upload in progress, please wait!`⚡️")
    file_name = None
    try:
        file_name = message.reply_to_message.document.file_name
    except:
        pass
    if file_name:
        Kk = fname.split(".")
        try:
            Kk[1]
        except:
            fuck = file_name.rpartition(".")[-1]
            fname = f"{fname}.{fuck}"
    EsCoBaR = await message.reply_to_message.download(fname)
    caption = ""
    if message.reply_to_message.caption:
        caption = message.reply_to_message.caption
    c_time = time.time()
    await client.send_document(
        message.chat.id,
        EsCoBaR,
        caption=caption,
        progress=progress,
        progress_args=(pablo, c_time, f"`Uploading {fname}`", EsCoBaR),
    )
    await pablo.edit(
        "File Renamed and Uploaded. By PandaUserBot. Get your PandaUserBot from @PandaUserbot"
    )

