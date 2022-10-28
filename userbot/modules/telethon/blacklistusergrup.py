
from userbot import PandaBot, SqL
from . import edit_or_reply
from telethon import events
plugin_category = "plugins"
from ...helpers.utils import get_user_from_event, mentionuser


grupbclk = SqL.getdb("BLACKLISTGC") or ""

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
            "{tr}addbalckuser",
        ],
    },
)
async def addblck(event):
    xxnx = await edit_or_reply(event, "prosesing..")
    var = "BLACKLISTGC"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    if replied_user.id == event.client.uid:
        return await edit_or_reply(event, "__You can't add yourself to blacklist.")
    if event is None:
        return
    gcblck = replied_user.id
    blckgc = f"{BLACKLIST_GCAST} {gcblck}"
    if replied_user.id in grupbclk:
        return await edit_or_reply(event, "berhasil menambahkan pengguna lucknut")
    blacklistgrup = (
        blckgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    output = await xxnx.edit("berhasil menambahkan pengguna anjeng").format(gcblck)
    output += "**Bot is reloading to apply the changes. Please wait for a minute**"
    msg = await edit_or_reply(event, output)
    SqL.setdb("BLACKLISTGC", f"{blacklistgrup}")  
    await event.client.reload(msg)


