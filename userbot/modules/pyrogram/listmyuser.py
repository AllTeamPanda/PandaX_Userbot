# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



import pyrogram

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply, edit_or_send_as_file
from . import HELP


HELP(
    "listmyuser",
)

@ilhammansiz_on_cmd(
    ["listmyusernames"],
    cmd_help={
        "help": "Get All Admin Channel / Chat List",
        "example": "{ch}listmyusernames",
    },
)
async def pabloescobar(client, message):
    pablo = await edit_or_reply(message, "`Please Wait!`")
    channels = await client.send(
        pyrogram.raw.functions.channels.GetAdminedPublicChannels()
    )
    C = channels.chats
    output_stre = ""
    for x in C:
        output_stre += f"{x.title}\n@{x.username}\n\n"
    output_str = f"""I am Admin In All These Groups And Channels
{output_stre}
"""
    await edit_or_send_as_file(
        output_str, pablo, client, "Your Admin Chats", "admin_chat"
    )
