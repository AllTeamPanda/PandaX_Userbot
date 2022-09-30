import os

import requests

from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import edit_or_reply, fetch_audio

from . import HELP


HELP(
    "shazam",
)

@ilhammansiz_on_cmd(
    ["shazam", "sreverse", "identify"],
    cmd_help={
        "help": "Reverse Search The Song!",
        "example": "{ch}shazam (reply to song)",
    },
)
async def shazamm(client, message):
    kek = await edit_or_reply(message, "`Shazaming In Progress!`")
    if not message.reply_to_message:
        await kek.edit("Reply To The Audio.")
        return
    if os.path.exists("panda.mp3"):
        os.remove("panda.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await kek.edit("**Searching For This Song In Panda DataBase.**")
    r = requests.post("https://starkapis.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await kek.edit(
            "`Seems Like Our Server Has Some Issues, Please Try Again Later!`"
        )
        return
    if xo.get("success") is False:
        await kek.edit("`Song Not Found IN Database. Please Try Again.`")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    zzz.get("sections")[3]
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    messageo = f"""<b>Song Shazamed.</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}
<u><b>Identified Using Panda - Get Your Userbot From</b></u>
"""
    await client.send_photo(message.chat.id, image, messageo, parse_mode="HTML")
    await kek.delete()
