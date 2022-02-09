from . import mention
import random
from Panda.events import register
import asyncio

pengguna = [
    f"Perkenalkan Nama saya {mention}\nTerimah Kasih Ganteng 😏",
    f"Saya {mention} Pemuja owner 😂😏",
    f"Terimakasih buat owner 😊",
    f"Kamshamida owner ganteng 😂 ",
    f"✅ {mention} Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677]
        
@register(incoming=True, from_users=DEV, pattern=r"^.pengguna$")
async def _(event): 
    await event.reply(random.choice(pengguna))
    
    
    

