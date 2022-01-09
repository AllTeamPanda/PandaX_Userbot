import random
from . import PandaBot

plugin_category = "Plugins"




spesial = [
     "https://telegra.ph/file/3a128f03b625e0f1a96d1.mp4"
     "https://telegra.ph/file/fc0d6c09d8ddf89aa9772.mp4"
     "https://telegra.ph/file/f915c7aeab2c481747163.mp4"
     "https://telegra.ph/file/58db2cd17ea842954e605.mp4"
     "https://telegra.ph/file/c76f67ab5288941e7e96a.mp4"
]



@PandaBot.ilhammansiz_cmd(
    pattern="spesial(?: |$)(.*)",
    command=("spesial", plugin_category),
    info={
        "header": "Gambar tetek 😂.",
        "description": "Menemukan tetek wkwk😂",
        "usage": "{tr}spesial ",
    },
)
async def pocong(event):
    await PandaBot.send_file(random.choice(event.chat_id, spesial))
