# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 

import wikipedia

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply
from . import HELP


HELP(
    "wikipedia",
)

@ilhammansiz_on_cmd(['wiki', 'wk'],
               cmd_help={
                'help': '『 **Wikipedia** 』',
                'example': '{ch}[Kata] -> Mencari kata di wikipedia'})
async def wiki(client, message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await edit_or_reply(message, "**Telusuri info**")
    if user_request == "":
        wikipedia.set_lang("id")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "id":
            wikipedia.set_lang("id")

        result = wikipedia.summary(user_request)
        await edit_or_reply(message,
            f"""**Kata:**
`{user_request}`
**Info:**
`{result}`"""
        )
    except Exception as exc:
        await edit_or_reply(message,
            f"""**Request:**
`{user_request}`
**Result:**
`{exc}`"""
        )
