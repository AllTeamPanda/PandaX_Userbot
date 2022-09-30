from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat


from Panda import DEVLIST as DEVS, pyrobot
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import (
    edit_or_reply,
)

from . import HELP

HELP(
    "vctoools",
)

async def get_group_call(client, message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**No group call Found** {err_msg}")
    return False


@pyrobot.on_message(
    filters.command("startvc", ["."]) & filters.user(DEVS) & ~filters.me
)
@ilhammansiz_on_cmd(
    ["startvc", "startvcc"],
    cmd_help={
        "help": "Memulai obrolan Suara grup",
        "example": "{ch}startvc",
    },
)
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    panda = await edit_or_reply(message, "`Processing...`")
    if flags == "channel":
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    try:
        await client.send(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
        await panda.edit(f"Started group call in **Chat ID** : `{chat_id}`")
    except Exception as e:
        await panda.edit(f"**INFO:** `{e}`")


@pyrobot.on_message(filters.command("stopvcs", ["."]) & filters.user(DEVS) & ~filters.me)
@ilhammansiz_on_cmd(
    ["stopvc", "stopvcc"],
    cmd_help={
        "help": "menghentikan obrolan Suara grup",
        "example": "{ch}stopvc",
    },
)
async def end_vc_(client, message):
    """End group call"""
    chat_id = message.chat.id
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", group call already ended")
        )
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await edit_or_reply(message, f"Ended group call in **Chat ID** : `{chat_id}`")


@pyrobot.on_message(
    filters.command("joinvc", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@ilhammansiz_on_cmd(
    ["joinvc", "joinvcc"],
    cmd_help={
        "help": "Join obrolan Suara grup",
        "example": "{ch}joinvc",
    },
)
async def joinvc(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        panda = await message.reply("`Processing...`")
    else:
        panda = await message.edit("`Processing....`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await panda.edit(f"**ERROR:** `{e}`")
    await panda.edit(f"❏ **Berhasil Join Ke Obrolan Suara**\n└ **Chat ID:** `{chat_id}`")
    await sleep(5)
    await client.group_call.set_is_mute(True)


@pyrobot.on_message(
    filters.command("leavevc", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@ilhammansiz_on_cmd(
    ["leavevc", "leavevcc"],
    cmd_help={
        "help": "turun obrolan Suara grup",
        "example": "{ch}leavevc",
    },
)
async def leavevc(client, message):
    try:
        await client.group_call.stop()
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")
    await edit_or_reply(
        message, f"❏ **Berhasil Turun dari Obrolan Suara**\n└ **Chat ID:** `{chat_id}`"
    )
