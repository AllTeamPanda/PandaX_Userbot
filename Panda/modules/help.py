
from .. import CMD_HELP
from ..misc import edit_delete, edit_or_reply, pandacute

modules = CMD_HELP
hemojis = {
    "bot": "🙇🏻"
}

@pandacute(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"`{args}` **Module yang lu cari gada tod.**")
    else:
        user = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += f"[ `{str(i)}` ]"
            string += f"᪥\t"
        await edit_or_reply(
            event,
            f"**👤 Owner:** [{user.first_name}](tg://user?id={user.id})\n\n"
            f"**🗂 Total Modules:** [ `{len(modules)}` ]\n\n"
            f"{string}"
            f"\n\nSupport @PandaUserbot",
        )
        
