from ... import bot, pandaub

plugin_category = "plugins"


@pandaub.ilhammansiz_cmd(
    pattern="tmsg",
    command=("tmsg", plugin_category),
    info={
        "header": "Mengembalikan jumlah pesan total pengguna dalam obrolan saat ini",
        "usage": "{tr}tmsg username pengguna",
    },
)
async def _(event):
    k = await event.get_reply_message()
    if k:
        a = await event.client.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await event.client.get_messages(event.chat_id, 0, from_user=u)
    await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")
