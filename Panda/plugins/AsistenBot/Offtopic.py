from telethon import events
from Panda import PandaBot
client = PandaBot.tgbot
@client.on(events.NewMessage(pattern='/offtopic|/ot'))
async def handler(event):
  if event.chat_id == -1001448375234:
    try:
      ok = await event.get_reply_message()
      event.chat.username
      mad = f"@{ok.sender.username} You're going OffTopic\nYou'll now get a Warn and a Ban...\n\n➥ OffTopic [Message](https://t.me/{event.chat.username}/{ok.id}) \n➥ Reporter : @{event.sender.username}\n➥ If OffTopic message is deleted\nOffTopic message = {ok.message}"
      await client.send_message(event.chat_id, mad, link_preview=False)
    except:
      await event.reply("Tag a message and type #ot or #offtopic\n.\n.\n.")
  else:
     await event.reply("This command can't be used in this chat...")
