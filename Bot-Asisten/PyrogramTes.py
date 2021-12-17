from pyrogram import filters
from PandaX_Userbot import MansiezRobot 

@MansiezRobot.on_message(filters.command(["ajg"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Ngentot",
        reply_to_message_id=update.message_id
    )
