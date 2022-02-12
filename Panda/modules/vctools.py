from Panda import PandaBot
from ..core.managers import edit_delete, edit_or_reply

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
plugin_category = "modules"


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@PandaBot.ilhammansiz_cmd(
    pattern="stopvc(?: |$)(.*)",
    command=("stopvc", plugin_category),
    info={
        "header": "To give admin rights for a person",
        "description": "Stop Group Call in a group",
        "usage": [
            "{tr}stopvc",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await edit_or_reply(e, "Voice Chat Stopped")
    except Exception as ex:
        await edit_or_reply(e, f"`{ex}`")



@PandaBot.ilhammansiz_cmd(
    pattern="vcinvite(?: |$)(.*)",
    command=("vcinvite", plugin_category),
    info={
        "header": "To give admin rights for a person",
        "description": "Invite Group Call in a group",
        "usage": [
            "{tr}vcinvite",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(e):
    ok = await edit_or_reply(e, "Inviting Members to Voice Chat")
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
    await ok.edit(f"Invited {z} users")

@PandaBot.ilhammansiz_cmd(
    pattern="startvc(?: |$)(.*)",
    command=("startvc", plugin_category),
    info={
        "header": "To give admin rights for a person",
        "description": "startvc Group Call in a group",
        "usage": [
            "{tr}startvc",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await edit_or_reply(e, "Voice Chat Started")
    except Exception as ex:
        await edit_or_reply(e, f"`{ex}`")



@PandaBot.ilhammansiz_cmd(
    pattern="vctitle(?: |$)(.*)",
    command=("vctitle", plugin_category),
    info={
        "header": "To give admin rights for a person",
        "description": "vctitle Group Call in a group",
        "usage": [
            "{tr}vctitle",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(e):
    title = e.pattern_match.group(1).strip()
    if not title:
        return await edit_or_reply(e, "Silahkan Masukan Title untuk VCG"), time=5)
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"Berhasil Mengubah Judul VCG menjadi {title}")
    except Exception as ex:
        await edit_or_reply(e, f"`{ex}`")
