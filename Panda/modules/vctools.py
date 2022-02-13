from Panda import PandaBot
from ..core.managers import edit_delete, edit_or_reply

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

plugin_category = "modules"
from Panda.events import register

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def stopvc(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("Voice Chat Stopped")
    except Exception as ex:
        await e.edit(f"`{ex}`")



@register(outgoing=True, pattern=r"^\.vcinvite$", groups_only=True)
async def vcinvite(e):
    ok = await e.edit("Inviting Members to Voice Chat")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"Invited {z} users")

@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def startvc(e):
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("Voice Chat Started")
    except Exception as ex:
        await e.edit(f"`{ex}`")


