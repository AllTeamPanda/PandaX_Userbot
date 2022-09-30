import logging

from pyrogram import filters

from Panda.sql_helper.autopost_sql import (
    add_new_autopost,
    check_if_autopost_in_db,
    del_autopost,
    get_autopost,
)
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd, listen
from Panda._func._helpers import edit_or_reply, get_text
from . import HELP


HELP(
    "autopost",
)

@ilhammansiz_on_cmd(
    ["autopost"],
    cmd_help={
        "help": "Add Channel To AutoPost List!",
        "example": "{ch}autopost @PandaUserbot",
    },
    chnnl_only=True,
)
async def autopost(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    chnnl = get_text(message)
    if not chnnl:
        await pablo.edit("`Provide Channel ID!`")
        return
    if str(chnnl).startswith("-100"):
        kk = str(chnnl).replace("-100", "")
    else:
        kk = chnnl
    if not kk.isnumeric():
        try:
            u_ = await client.get_chat(kk)
        except:
            await pablo.edit("`Invalid Chat ID / Username!`")
            return
        kk = str(u_.id).replace("-100", "")
    if check_if_autopost_in_db(message.chat.id, kk):
        await pablo.edit("Channel Already In DB")
        return
    add_new_autopost(message.chat.id, kk)
    await pablo.edit(f"`Added AutoPosting To This Channel From {chnnl}`")


@ilhammansiz_on_cmd(
    ["rmautopost"],
    cmd_help={
        "help": "Remove A Channel From Autopost List",
        "example": "{ch}rmautopost @TEAMSquadUserbotSupport",
    },
    chnnl_only=True,
)
async def rmautopost(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    chnnl = get_text(message)
    if not chnnl:
        await pablo.edit("`Provide Channel ID!`")
        return
    if str(chnnl).startswith("-100"):
        kk = str(chnnl).replace("-100", "")
    else:
        kk = chnnl
    if not kk.isnumeric():
        try:
            u_ = await client.get_chat(kk)
        except:
            await pablo.edit("`Invalid Chat ID / Username!`")
            return
        kk = str(u_.id).replace("-100", "")
    if not check_if_autopost_in_db(message.chat.id, kk):
        await pablo.edit("Channel Not In DB")
        return
    del_autopost(message.chat.id, kk)
    await pablo.edit(f"`Removed AutoPosting To This Channel From {chnnl}`")


@listen(
    (filters.incoming | filters.outgoing)
    & filters.channel
    & ~filters.edited
    & ~filters.service
)
async def autoposterz(client, message):
    chat_id = str(message.chat.id).replace("-100", "")
    if not get_autopost(int(chat_id)):
        
        return
    channels_set = get_autopost(int(chat_id))
    if not channels_set:
        
        return
    for chat in channels_set:
        try:
            await message.copy(int(chat["to_channel"]))
        except Exception as e:
            logging.error(
                f"[AUTOPOST] | {e} | {chat['to_channel']} | {message.chat.id}"
            )
    
