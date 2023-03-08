
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 

import asyncio

from ... import app, gen


app.CMD_HELP.update(
    {
        "ping": (
            "ping",
            {
                "gcast": "Global message too grup U.",
                "gcast": "text/reply",
                "gucast": "Global message too Private U.",
                "gcast": "text/reply",
            },
        )
    }
)

DEVS = [5057493677, 1593802955]


GCAST_BLACKLIST = [-1001718757023, -1001161992503]

@app.on_message(gen("gcast", allow=["sudo"]))
async def gcast_handler(_, message: Message):
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
        return await app.send_edit(message, "**Berikan Sebuah Pesan atau Reply**")
    await app.send_edit(message, "`Started global broadcast...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await client.send_message(chat, text)
                    done += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    error += 1
    await app.send_edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{error}` **Grup**"
    )


@app.on_message(gen("gucast", allow=["sudo"]))
async def gucast_handler(_, message: Message):
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
        return await app.send_edit(message, "**Berikan Sebuah Pesan atau Reply**")
    await app.send_edit(message, "`Started global broadcast to users...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private" and not dialog.chat.is_verified:
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    await client.send_message(chat, text)
                    done += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    error += 1
    await app.send_edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{error}` **chat**"
    )
