from telethon import events, Button
from PandaX_Userbot import Stark, petercordpanda_bot as bot
from PandaX_Userbot.status import is_admin
import time
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from telethon.tl.types import ChannelParticipantsAdmins

import asyncio

PR_HELP = """
**✘ Need to delete lots of messages? That's what purges are for!**

‣ `/purge` - Reply to a msg to delete msgs from there.
‣ `/spurge` - Same as purge, but doesnt send the final confirmation message.
‣ `/del` - Deletes the replied to message.
"""

OWNER_ID = bot.uid
# Check if user has admin rights
async def is_administrator(user_id: int, message):
    admin = False
    async for user in Stark.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or OWNER_ID or SUDO_USERS:
            admin = True
            break
    return admin


@Stark.on(events.NewMessage(pattern="^/purge"))
async def purge(event):
    chat = event.chat_id
    msgs = []

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("You're not an admin!")
        return

    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to a message to select where to start purging from.")
        return

    try:
        msg_id = msg.id
        count = 0
        to_delete = event.message.id - 1
        await Stark.delete_messages(chat, event.message.id)
        msgs.append(event.reply_to_msg_id)
        for m_id in range(to_delete, msg_id - 1, -1):
            msgs.append(m_id)
            count += 1
            if len(msgs) == 100:
                await Stark.delete_messages(chat, msgs)
                msgs = []

        await Stark.delete_messages(chat, msgs)
        del_res = await Stark.send_message(
            event.chat_id, f"Fast Purged {count} messages."
        )

        await asyncio.sleep(4)
        await del_res.delete()

    except MessageDeleteForbiddenError:
        text = "Failed to delete messages.\n"
        text += "Messages maybe too old or I'm not admin! or dont have delete rights!"
        del_res = await respond(text, parse_mode="md")
        await asyncio.sleep(5)
        await del_res.delete()


@Stark.on(events.NewMessage(pattern="^/del$"))
async def delete_msg(event):

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("You're not an admin!")
        return

    chat = event.chat_id
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to some message to delete it.")
        return
    to_delete = event.message
    chat = await event.get_input_chat()
    rm = [msg, to_delete]
    await Stark.delete_messages(chat, rm)

@Stark.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command:CanDelMsgs!")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)



@Stark.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbot")]])

@Stark.on(events.callbackquery.CallbackQuery(data="purgess"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpbott")]])
