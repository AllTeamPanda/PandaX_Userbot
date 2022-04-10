# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
import random
from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import pandacute
from telethon.tl.types import InputMessagesFilterVideo


@pandacute(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Asupan_Pocong", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"nih asupan biar ga lemess 🥵",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@pandacute(pattern="wibu$")
async def _(event):
    try:
        wibukntl = [
            wibu
            async for wibu in event.client.iter_messages(
                "@pocongwibu", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wibukntl),
            caption=f"nih buat lo vvibu bau bawang",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@pandacute(pattern="chika$")
async def _(event):
    try:
        response = requests.get("https://api-alphabot.herokuapp.com/api/asupan/chika?apikey=Alphabot").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)

CMD_HELP.update(
    {
        "wibu": f"**Plugin : **`Wibu`\
        \n\n  •  **Syntax :** `{cmd}wibu`\
        \n  •  **Function : **Mengirim secara random video anime\
    "
    }
)
