from . import edit_or_reply, pandaub

plugin_category = "Plugins"


@pandaub.ilhammansiz_cmd(
    pattern="repo$",
    command=("repo", plugin_category),
    info={
        "header": "menunjukkan repo",
        "usage": "{tr}repo",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(
        event,
        "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [𝗣 𝗔 𝗡 𝗗 𝗔](https://github.com/ilhammansiz/PandaX_Userbot)\n\n [𝗢 𝗪 𝗡 𝗘 𝗥 𝗦](t.me/diemmmmmmmmmm)\n\n [GRUP SUPPORT](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n",
    )
