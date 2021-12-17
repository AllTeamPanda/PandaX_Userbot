from Panda import bot, pandaub

plugin_category = "mansiez"


@pandaub.ilhammansiz_cmd(
    pattern="gcast(?: |$)(.*)",
    command=("gcast", plugin_category),
    info={
        "header": "Promosi kesemua grup yang dimasuki ",
        "usage": "{tr}gcast text/media",
    },
)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan Saya Text Untuk Di Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`• 📢 Global Broadcast Di Prosess Cok...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **Grup, Broadcast Gagal Terkirim =** `{er}`**Grup**╰✠╼━━━━━━❖━━━━━━━✠╯**"
    )
