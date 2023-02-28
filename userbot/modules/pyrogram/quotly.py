# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import asyncio

from pyrogram.types import Message

from ... import app, gen

app.CMD_HELP.update(
    {"quotly": ("quotly", {"q [reply to message]": "Make Image Of Your Texts."})}
)


@app.on_message(gen(["q"], allow=["sudo", "channel"]))
async def quotly_handler(_, m: Message):
    reply = m.reply_to_message
    if not reply:
        return await app.send_edit(m, "Reply to any users text message", delme=4)

    m = await app.send_edit(m, "Making a Quote . . .", text_type=["mono"])
    await reply.forward("@QuotLyBot")
    is_sticker = True
    while is_sticker:
        try:
            msg = await app.get_last_msg(message=m, chat_id="@QuotLyBot", limit=1)
            msg[0]["sticker"]["file_id"]
            is_sticker = False
        except:
            await asyncio.sleep(0.5)
    if msg_id := msg[0]["message_id"]:
        await asyncio.gather(
            m.delete(), app.copy_message(m.chat.id, "@QuotLyBot", msg_id)
        )
