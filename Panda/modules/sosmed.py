# Port by Koala 🐨/@manuskarakitann
# Copyright © @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot/>
# Sok²an ngentot sok pro
# Nyenyenye bacot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest

from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import edit_delete, edit_or_reply, pandacute


@pandacute(pattern="sosmed(?: |$)(.*)")
async def insta(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        link = xxnx
    elif event.is_reply:
        link = await event.get_reply_message()
    else:
        return await edit_delete(
            event,
            "**Berikan Link Sosmed atau Reply Link Sosmed Untuk di Download**",
        )
    xx = await edit_or_reply(event, "`Processing Download...`")
    chat = "@SaveAsbot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.send_message(chat, link)
            response = await response
        if response.text.startswith("Forward"):
            await xx.edit("Forward Private .")
        else:
            await xx.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client(DeleteHistoryRequest(peer=chat, max_id=0))
            await xx.delete()


@pandacute(pattern="dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await edit_delete(
            event, "`Mohon Berikan Link Deezloader yang ingin di download`"
        )
    else:
        await edit_or_reply(event, "`Sedang Mendownload Lagu...`")
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(event.chat_id, song, caption=details.text)
        await event.delete()


CMD_HELP.update(
    {
        "sosmed": f"**Plugin : **`sosmed`\
        \n\n  ➕  **Syntax :** `{cmd}sosmed` <link>\
        \n  ➕  **Function : **Download Media Dari Pinterest / Tiktok / Instagram.\
        \n\n  ➕  **Syntax :** `{cmd}dez` <link>\
        \n  ➕  **Function : **Download Lagu Via Deezloader\
    "
    }
)
