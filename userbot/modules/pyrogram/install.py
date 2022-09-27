# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 

import os

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func.startup import load_modulesPyro as load_plugin
from userbot._func._helpers import edit_or_reply
from . import HELP


HELP(
    "install",
)

@ilhammansiz_on_cmd(
    ["install"],
    cmd_help={
        "help": "Install Custom Plugins In Userbot",
        "example": "{ch}install (replying to plugin (.py))",
    },
)
async def installer(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    if not message.reply_to_message:
        await pablo.edit("`Reply To A Plugin File To Install Plugin`")
        return
    if not message.reply_to_message.document:
        await pablo.edit("`Is It A Even A Document?`")
        return
    file_name = message.reply_to_message.document.file_name
    ext = file_name.split(".")[1]
    if os.path.exists(os.path.join("./userbot/modules/pyrogram/", file_name)):
        await pablo.edit("`This Plugin is Already Installed!`")
        return
    if not ext.lower() == "py":
        await pablo.edit("`Only Py Files :(`")
        return
    Escobar = await message.reply_to_message.download(file_name="./userbot/modules/pyrogram/")
    base_name = os.path.basename(Escobar)
    file_n = base_name.split(".")[0]
    try:
        load_plugin(file_n)
    except Exception as e:
        await pablo.edit(f"Error Installing Plugin.\n**Error** {e}")
        os.remove(Escobar)
        return
    await pablo.edit(f"`Sucessfully Installed {file_name}!`")

