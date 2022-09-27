
from telethon import events
from .... import tgbot
from ....resources import is_admin
from datetime import timedelta
Stark = tgbot

@Stark.on(events.NewMessage(pattern="[!?/]spem"))
@is_admin
async def spam(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("That's not a user!")
       return
    ree = (await event.get_reply_message()).sender_id
    check = await Stark.get_permissions(event.chat_id, ree)

    if check.is_admin:
       await event.reply("He can be a spammer, but he is also an admin!")
       return
    elif check.is_creator:
       await event.delete()
       await event.reply("He is chat creator")
       return
    elif msg.sender.bot:
       await event.delete()
       await event.reply("Its a bot!")
       return

    re = (await event.get_reply_message()).sender_id
    user = await Stark.get_entity(ree)
    await event.delete()
    await Stark.edit_permissions(event.chat_id, re, timedelta(hours=1), send_messages=False)
    await Stark.send_message(event.chat_id, f"[{user.first_name}](tg://user?id={re}) it looks like you are spamming the chat!\nAnd so has been muted for 1 hour")

