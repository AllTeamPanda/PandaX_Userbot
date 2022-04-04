from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl import functions, types
import asyncio
import time
import uuid
_cache = {}

async def get_update_linked_chat(event):
    if _cache.get("LINKED_CHATS") and _cache["LINKED_CHATS"].get(event.chat_id):
        _ignore = _cache["LINKED_CHATS"][event.chat_id]["linked_chat"]
    else:
        channel = await event.client(
            functions.channels.GetFullChannelRequest(event.chat_id)
        )
        _ignore = channel.full_chat.linked_chat_id
        if _cache.get("LINKED_CHATS"):
            _cache["LINKED_CHATS"].update({event.chat_id: {"linked_chat": _ignore}})
        else:
            _cache.update(
                {"LINKED_CHATS": {event.chat_id: {"linked_chat": _ignore}}}
            )
    return _ignore
