from telethon import events
from pytgcalls import GroupCallFactory
from PandaX_Userbot import Stark
from . import mansiez
calls = GroupCallFactory(Stark, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON).get_group_call()
from telethon.tl.types import ChannelParticipantsAdmins
borg = Stark
import emoji
from googletrans import Translator



@mansiez(pattern="/join ?(.*)")
async def join_handler(event):
    chat = await event.get_chat()
    await calls.join(event.chat.id)


@mansiez(pattern="/tr ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            f"`.trt LanguageCode` as reply to a message.\nTry `.trc` to get all language codes",
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated**\nFrom {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await event.reply(output_str)
    except Exception as exc:
        await event.reply(str(exc))






@mansiez(pattern="/warn ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "⚠️ **You Have** `1/3` **Warnings** ⚠️\n\n__Watch out!__\n⚡ **Reason for warn:** Not given"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()



