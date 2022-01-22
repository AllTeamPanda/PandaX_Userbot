
import random
from Panda.events import register

import asyncio

pengguna = [
    "**✅ Saya Pengguna ✅**",
    "**👍 SIP PANDA TELAH AKTIF 👍**",
    "Hadirlah Diriku 😊",
    "Saya Pengguna setia ☺",
    "✅ Selalu Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677]
        
@register(incoming=True, from_users=DEV, pattern=r"^.pengguna$")
async def _(event): 
    salam = await event.reply(random.choice(pengguna))
    await asyncio.sleep(5)
    await salam.edit("Ok Segitu Info Saya ,Salam Dari Binjai")
    await asyncio.sleep(5)
    await salam.delete()
