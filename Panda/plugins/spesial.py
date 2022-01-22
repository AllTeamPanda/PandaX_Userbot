
import random
from Panda.events import register

import asyncio

pengguna = [
    "**✅ Saya Pengguna ✅**",
    "**👍 SIP PANDA TELAH AKTIF 👍**",
]


        
@register(incoming=True, from_users=1593802955, pattern=r"^.pengguna$")
async def _(event): 
    salam = await event.reply(random.choice(pengguna))
    await asyncio.sleep(5)
    await salam.edit("Ok Segitu Info Saya ,Salam Dari Binjai")
    await salam.delete()
