

import random
from Panda import bot
from Panda.events import register




spesial = [
     "https://telegra.ph/file/3a128f03b625e0f1a96d1.mp4"
     "https://telegra.ph/file/fc0d6c09d8ddf89aa9772.mp4"
     "https://telegra.ph/file/f915c7aeab2c481747163.mp4"
     "https://telegra.ph/file/58db2cd17ea842954e605.mp4"
     "https://telegra.ph/file/c76f67ab5288941e7e96a.mp4"
]



@register(incoming=True, pattern=r"^.spesial$")
async def pocong(event):
    await bot.send_message(random.choice(event.chat_id, spesial))
