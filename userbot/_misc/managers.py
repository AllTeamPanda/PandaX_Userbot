import asyncio
import os
from asyncio import sleep
from telethon.errors import MessageDeleteForbiddenError, MessageNotModifiedError
from telethon.tl.custom import Message
from telethon.tl.types import MessageService
from ..helpers.utils.format import md_to_text, paste_message
from .data import _sudousers_list, _dev_list
import logging
DEV = [5057493677, 1593802955]

LOGS = logging.getLogger("PandaUserbot")

# https://t.me/c/1220993104/623253
# https://docs.telethon.dev/en/latest/misc/changelog.html#breaking-changes
async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    deflink=False,
    noformat=False,
    linktext=None,
    caption=None,
    time=None,
    edit_time=None,
    **args,
):  # sourcery no-metrics
    sudo_users = _sudousers_list()
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096 and not deflink:
        parse_mode = parse_mode or "md"
        if event.sender_id in sudo_users:
            if reply_to:
                return await event.client.send_message(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    if not noformat:
        text = md_to_text(text)
    if aslink or deflink:
        linktext = linktext or "Message was to big so pasted to bin"
        response = await paste_message(text, pastetype="s")
        text = f"{linktext} [here]({response})"
        
        if reply_to:
            return await event.client.send_message(text, link_preview=link_preview)
        return await event.reply(text, link_preview=link_preview)
    await event.edit(text, link_preview=link_preview)
    return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await event.client.send_message(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in sudo_users:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)

    reply_toot = reply_to
    if event.out and not isinstance(event, MessageService):
        if edit_time:
            await sleep(edit_time)
        if args.get("file") and not event.media:
            await event.delete()
            ok = await event.client.send_message(
                event.chat_id,
                text,
                link_preview=link_preview,
                **args
            )
        else:
            try:
                ok = await event.edit(text, link_preview=link_preview, **args)
            except MessageNotModifiedError:
                ok = event
    else:
        ok = await event.client.send_message(
            event.chat_id, text, link_preview=link_preview, **args
        )

    if time:
        await sleep(time)
        return await ok.delete()
    return ok


async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None, **kwargs):
    sudo_users = _sudousers_list()
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 5
    if event.sender_id in sudo_users:
        reply_to = await event.get_reply_message()
        event = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    kwargs["time"] = kwargs.get("time", 8)
    return await event.delete()

eor = edit_or_reply
eod = edit_delete



async def _try_delete(event):
    try:
        return await event.delete()
    except (MessageDeleteForbiddenError):
        pass
    except BaseException as er:
        LOGS.error("Error while Deleting Message..")
        LOGS.exception(er)


setattr(Message, "eor", eor)
setattr(Message, "try_delete", _try_delete)
