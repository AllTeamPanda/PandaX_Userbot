from ..misc import edit_or_reply, pandacute


@pandacute(pattern="repo$")
async def _(event):
    "animation command"
    event = await edit_or_reply(
        event,
        "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [Repositories](https://github.com/ilhammansiz/PandaX_Userbot)\n\n [Creator](t.me/diemmmmmmmmmm)\n\n [Grup Support](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n",
    )
