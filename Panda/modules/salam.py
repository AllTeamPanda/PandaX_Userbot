from time import sleep

from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import edit_or_reply, pandacute


@pandacute(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Dulu Biar Sopan**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@pandacute(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Hy kaa 🥺**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@pandacute(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@pandacute(pattern="L(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Astaghfirullah, Jawab salam dong**")
    sleep(2)
    await xx.edit("**Wa'alaikumsalam**")



CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\nㅤㅤ➕**Syntax** : {cmd}p\
        \n➕**Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\nㅤㅤ➕**Syntax** : {cmd}P\
        \n➕**Function : **salam Kenal dan salam\
        \n\nㅤㅤ➕**Syntax** : {cmd}l\
        \n➕**Function : **Untuk Menjawab salam\
        \n\nㅤㅤ➕**Syntax** :{cmd}L\
        \n➕**Function : **Untuk menjawab salam\
    "
    })
