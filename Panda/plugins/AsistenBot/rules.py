from Panda import PandaBot
Stark = PandaBot.tgbot
from telethon import events, Button
from Configs import Config
Meong = """
 ➖➖➖➖➖➖➖➖➖➖
🎯 Rules :
 ➥  No spam either recent actions or group
 ➥  Keep discussions on-topic, related to PandaX-Userbot. 🤖
 ➥  Don't pm any person without prior permission especially to admins
 ➥  Use common sense. 
 ➥  Use polite language
➖➖➖➖➖➖➖➖➖➖➖➖
📌 Use Spam testing group for testing / checking out plugins.

📌 before asking any doubt check pinned message and channel recent posts and also .help and .info and send logs(this is must if your bot not working . if you don't know what is logs type #logs and send here.)

📌 be precise with your doubt and bug

 ➥  Use English while talking to me

 ➥ IF YOU WANT ANY FEATURE ADD IT IN BUGS POST (SENT AFTER EVERY MAJOR UPDATE in channel)) WHEN EVER I AM FREE I WILLL SEE IT AND REPLY YOU 
 ➥ By @diemmmmmmmmmm
"""
RULES = Meong

@Stark.on(events.NewMessage(pattern="^[!?/]rules"))
async def rules(event):

    msg = await event.get_reply_message()
    if not msg and event.is_group:
        await event.delete()
        await event.respond("Please read the rules before chatting here!", buttons=[
        [Button.url("Chat Rules", "t.me/{}?start=rules".format(Meong))
        ]])
        return
        
    re = (await event.get_reply_message()).id
    await event.delete()
    await Stark.send_message(event.chat_id, "Please read the rules before chatting here!", buttons=[
    [Button.url("Chat Rules", "t.me/{}?start=rules".format(Meong))
    ]], reply_to=re)
    return

    await event.reply(RULES)

@Stark.on(events.NewMessage(pattern="^/start rules"))
async def rules(event):

    if event.is_group:
       await event.reply("Please read the rules before chatting here!", buttons=[
       [Button.url("Chat Rules", "t.me/{}?start=rules".format(Meong))
       ]])
       return

    await event.reply(RULES)

@Stark.on(events.callbackquery.CallbackQuery(data="rules"))
async def _(event):

    await event.edit(RULES, buttons=[
    [Button.inline("« Bᴀᴄᴋ", data="helpp")]
    ])

@Stark.on(events.callbackquery.CallbackQuery(data="ruless"))
async def _(event):

    await event.edit(RULES, buttons=[
    [Button.inline("« Bᴀᴄᴋ", data="helpp")]
    ])
