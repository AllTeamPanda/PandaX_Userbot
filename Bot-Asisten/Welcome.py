from PandaX_Userbot import Stark
from Configs import Config
from telethon import events, errors

from telethon import events, Button
from telethon.tl.functions.users import GetFullUserRequest
from datetime import timedelta
from PandaX_Userbot.Panda.database import Var
bot = Stark

PANDAALIVE =[
          [Button.url("PandaX_Userbot", "https://github.com/ilhammansiz/PandaX_Userbot"), Button.url("Deploy Panda", "https%3A%2F%2Fgithub.com%2Filhammansiz%2FPandaX_Userbot&template=https%3A%2F%2Fgithub.com%2Filhammansiz%2FPandaX_Userbot")],
          [Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://t.me/UserbotTEAM_Tutorial"), Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "t.me/apiuserbutpetercord_bot")],
          [Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/UserbotTEAM_Tutorial"), Button.url("Rᴇᴅɪs", "https://redislabs.com")],
          [Button.url("Depolover", "t.me/diemmmmmmmmmm")]]

PANDABYE =[[Button.url("Depolover", "t.me/diemmmmmmmmmm")]]

GOODBYE = """ Awas Kau masuk lagi Aku Asistan Kenapa keluar Masuk Kau"""

@Stark.on(events.CallbackQuery(pattern=r"check-bot-(\d+)"))
async def check(event):

    user_id = int(event.pattern_match.group(1))
    chat_id = event.chat_id
    if not event.sender_id == user_id:
        await event.answer("You can already speak freely!", alert=True)
        return
    if event.sender_id == user_id:
            await Stark.edit_permissions(chat_id, event.sender_id, send_messages=True)
            await event.answer("You are succesfully unmuted!")
            await event.edit(Var.WELCOME_TEXT, buttons=[
            [Button.url("Join Channel!", "t.me/UserbotTEAM_Tutorial".format(Config.BOT_US))]
            ], parse_mode="HTML", link_preview=False)


@Stark.on(events.ChatAction)
async def join(event):

    if event.user_joined:
        await Stark.edit_permissions(event.chat_id, event.user_id, send_messages=True)
        await event.reply(Var.WELCOME_TEXT, parse_mode="HTML", link_preview=False, buttons=PANDAALIVE)

@Stark.on(events.ChatAction)
async def lef(event):

    if  event.user_left or event.user_kicked:
        await Stark.edit_permissions(event.chat_id, event.user_id, send_messages=True)
        await event.reply(GOODBYE, parse_mode="HTML", link_preview=False, buttons=PANDABYE)



