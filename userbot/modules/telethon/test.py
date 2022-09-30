from .. import pyrotgbot
from pyrogram import filters



@pyrotgbot.on_message(filters.command(["alive"]) & filters.incoming)
async def alive(client, message):
    client.me
    await message.reply(
        f"`Yo ! {message.from_user.first_name} , I am Alive. Need Help ? How Are You? 🤟`"
    )
