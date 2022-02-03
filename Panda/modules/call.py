from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from telethon.tl.types import ChatAdminRights

from Panda.events import register
from Panda import PandaBot
NO_ADMIN = "`Sorry you are not admin :)`"

plugin_category = "modules"

async def get_call(event):
    geez = await event.client(getchat(event.chat_id))
    vcky = await event.client(getvc(geez.full_chat.call))
    return vcky.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@PandaBot.ilhammansiz_cmd(
    command=("startvc", plugin_category),
    info={
        "header": "Play the voice chat.",
        "description": "Memulai Voice Chat grup",
        "usage": ".startvc",
        "examples": [".startvc"],
    },
)
@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Voice Chat Started...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")

@PandaBot.ilhammansiz_cmd(
    command=("stopvc", plugin_category),
    info={
        "header": "End the voice chat.",
        "description": "Mengakhiri Voice Chat grup",
        "usage": ".stopvc",
        "examples": [".stopvc"],
    },
)
@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`Voice Chat Stopped...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")

@PandaBot.ilhammansiz_cmd(
    command=("vcinvite", plugin_category),
    info={
        "header": "Menginvite the voice chat.",
        "description": "Menginvite Voice Chat grup",
        "usage": ".vcinvite",
        "examples": [".vcinvite"],
    },
)
@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(e):
    await e.edit("`Inviting Members to Voice Chat...`")
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
    await e.edit(f"`Invited {z} users`")
