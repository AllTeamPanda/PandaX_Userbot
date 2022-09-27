# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 
from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply
from . import HELP


HELP(
    "joingrup",
)

@ilhammansiz_on_cmd(
    ["joingrup"],
    cmd_help={
        "help": "Untuk bergabung ke obrolan dengan username gc",
        "example": "{ch}joingrup @PandaUserbot",
    },
)
async def join(client, message):
    panda = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Berhasil Bergabung ke Chat ID** `{panda}`")
        await client.join_chat(panda)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@ilhammansiz_on_cmd(
    ["leavegrup", "kickme"],
    cmd_help={
        "help": "Untuk keluar ke obrolan gc",
        "example": "{ch}kickme ",
    },
)
async def leave(client, message):
    panda = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit_text(f"{client.me} has left this group, bye!!")
        await client.leave_chat(panda)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@ilhammansiz_on_cmd(
    ["leaveall"],
    cmd_help={
        "help": "keluar dari semua grup",
        "example": "{ch}leaveall",
    },
)
async def kickmeall(client, message):
    panda = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await panda.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )
