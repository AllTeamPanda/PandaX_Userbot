from collections import deque

import asyncio
import requests
from telethon import events, Button
import time
from . import mansiez

@mansiez(pattern="&moon ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    event = await event.reply("🌗")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
