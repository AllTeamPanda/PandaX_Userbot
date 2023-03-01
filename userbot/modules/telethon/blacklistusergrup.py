
from userbot import PandaBot, SqL
from . import edit_or_reply
from telethon import events
plugin_category = "plugins"
from ...helpers.utils import get_user_from_event


grupbclk = SqL.get_key("BLACKLISTGC") or []

@PandaBot.on(events.ChatAction)
async def joingrup(event):
    if event.user_joined:
        if i in grupbclk:
            await PandaBot.kick_participant(event.chat_id, i)



@PandaBot.ilhammansiz_cmd(
    pattern="addbalckuser$",
    command=("addbalckuser", plugin_category),
    info={
        "header": "To check bot's blacklist status",
        "options": "userblacklist",
        "usage": [
            "{tr}addbalckuser id",
        ],
    },
)
async def addblck(event):
    cmd = event.pattern_match.group(1)
    xxnx = await edit_or_reply(event, "prosesing..")
    gcblck = cmd
    output = await xxnx.edit(f"berhasil menambahkan pengguna anjeng {gcblck}")
    output += "**Bot is reloading to apply the changes. Please wait for a minute**"
    msg = await edit_or_reply(event, output)
    SqL.set_key("BLACKLISTGC", [gcblck])  
    await event.client.reload(msg)


