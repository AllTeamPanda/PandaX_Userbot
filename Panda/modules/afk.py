# Copyright (C) 2022 TeamUltroid
# Thnks Man & Pocong Userbot
# Recode by @robotrakitangakbagus

import asyncio
from datetime import datetime

from telethon.tl import functions, types

from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import bash, pandacute, cute

USER_AFK = {}
afk_time = None
last_afk_message = {}
last_afk_msg = {}
afk_start = {}


@cute(outgoing=True)
async def set_not_afk(event):
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    user = await event.client.get_me()
    owner = user.first_name
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if "afk" not in current_message and "yes" in USER_AFK:
        try:
            if pic.endswith((".tgs", ".webp")):
                shite = await event.client.send_message(event.chat_id, file=pic)
                shites = await event.client.send_message(
                    event.chat_id,
                    f"**{owner} Kembali Online Untuk Parming**\n**Dari AFK :** `{total_afk_time}` **Yang Lalu**",
                )
            else:
                shite = await event.client.send_message(
                    event.chat_id,
                    f"**{owner} Pengangguran sok Sibuk Balik Lagi!**\n**Dari AFK :** `{total_afk_time}` **Yang Lalu**",
                    file=pic,
                )
        except BaseException:
            shite = await event.client.send_message(
                event.chat_id,
                f"**{owner} Kembali Online**\n**Dari AFK :** `{total_afk_time}` **Yang Lalu**",
            )

        await asyncio.sleep(6)
        await shite.delete()
        try:
            await shites.delete()
        except BaseException:
            pass
        USER_AFK = {}
        afk_time = None

        await bash("rm -rf *.webp")
        await bash("rm -rf *.tgs")


@cute(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    user = await event.client.get_me()
    owner = user.first_name
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason:
            message_to_reply = (
                   f"┌ ❏AFK!\n"
                + f"│┌ {owner} Sedang AFK\n"
                + f"│├ {total_afk_time} Yang Lalu \n"
                + f"└└ Karena : `{reason}`"
            )
        else:
            message_to_reply = (
                f"**✘ Maaf {owner} Sedang AFK** `{total_afk_time}` **Yang Lalu ✘**"
            )
        try:
            if pic.endswith((".tgs", ".webp")):
                msg = await event.reply(file=pic)
                msgs = await event.reply(message_to_reply)
            else:
                msg = await event.reply(message_to_reply, file=pic)
        except BaseException:
            msg = await event.reply(message_to_reply)
        await asyncio.sleep(2.5)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        try:
            if event.chat_id in last_afk_msg:
                await last_afk_msg[event.chat_id].delete()
        except BaseException:
            pass
        last_afk_message[event.chat_id] = msg
        try:
            if msgs:
                last_afk_msg[event.chat_id] = msgs
        except BaseException:
            pass


@pandacute(pattern="afk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    global USER_AFK
    global afk_time
    global last_afk_message
    global last_afk_msg
    global afk_start
    global afk_end
    global reason
    global pic
    user = await event.client.get_me()
    owner = user.first_name
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    last_afk_msg = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    pic = await event.client.download_media(reply) if reply else None
    if not USER_AFK:
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()
        USER_AFK = f"yes: {reason} {pic}"
        if reason:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await event.client.send_message(event.chat_id, file=pic)
                    await event.client.send_message(
                        event.chat_id,
                        f"\n ❏ 𝗔𝗙𝗞 !\n┌ {owner} 𝗟𝗮𝗴𝗶 𝗔𝗙𝗞! \n└ 𝗞𝗮𝗿𝗲𝗻𝗮 : `{reason}`",
                    )
                else:
                    await event.client.send_message(
                        event.chat_id,
                        f"\n ❏ 𝗔𝗙𝗞 !\n┌ {owner} 𝗟𝗮𝗴𝗶 𝗔𝗙𝗞! \n└ 𝗞𝗮𝗿𝗲𝗻𝗮 : `{reason}`",
                        file=pic,
                    )
            except BaseException:
                await event.client.send_message(
                    event.chat_id,
                    f"\n ❏ 𝗔𝗙𝗞 !\n┌ {owner} 𝗟𝗮𝗴𝗶 𝗔𝗙𝗞! \n└ 𝗞𝗮𝗿𝗲𝗻𝗮 : `{reason}`",
                )
        else:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await event.client.send_message(event.chat_id, file=pic)
                    await event.client.send_message(
                        event.chat_id, f"**✘ {owner} Telah AFK ✘**"
                    )
                else:
                    await event.client.send_message(
                        event.chat_id,
                        f"**✘ {owner} Telah AFK ✘**",
                        file=pic,
                    )
            except BaseException:
                await event.client.send_message(
                    event.chat_id, f"**✘ {owner} Telah AFK ✘**"
                )
        await event.delete()


CMD_HELP.update(
    {
        "afk": f"**Plugin : **`afk`\
        \n\n  ➕  **Syntax :** `{cmd}afk` <alasan> bisa <sambil reply sticker/foto/gif/media>\
        \n  ➕  **Function : **Memberi tahu kalau Master sedang afk bisa dengan menampilkan media keren ketika seseorang menandai atau membalas salah satu pesan atau dm Anda.\
        \n\n  ➕  **Syntax :** `{cmd}off`\
        \n  ➕  **Function : **Memberi tahu kalau Master sedang OFFLINE, dan menguubah nama belakang menjadi 【 OFF 】 \
    "
    }
)
