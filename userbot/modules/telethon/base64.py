import asyncio
import base64
from . import PandaBot, edit_or_reply


plugin_category = "plugins"




@PandaBot.ilhammansiz_cmd(
    pattern="en(?: |$)(.*)",
    command=("encode", plugin_category),
    info={
        "header": "encode ",
        "usage": "{tr}en text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await edit_or_reply(event,
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@PandaBot.ilhammansiz_cmd(
    pattern="de(?: |$)(.*)",
    command=("decode", plugin_category),
    info={
        "header": "decode ",
        "usage": "{tr}de text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Decode..`")
    byt = ppk.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))






@PandaBot.ilhammansiz_cmd(
    pattern="enurl(?: |$)(.*)",
    command=("urlencode", plugin_category),
    info={
        "header": "url encode ",
        "usage": "{tr}en text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.urlsafe_b64encode(byt)
    atc = et.decode("ascii")
    await edit_or_reply(event,
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@PandaBot.ilhammansiz_cmd(
    pattern="urlde(?: |$)(.*)",
    command=("urldecode", plugin_category),
    info={
        "header": "urldecode ",
        "usage": "{tr}urlde text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Decode..`")
    byt = ppk.encode("ascii")
    try:
        et = base64.urlsafe_b64decode(byt)
        atc = et.decode("ascii")
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))


