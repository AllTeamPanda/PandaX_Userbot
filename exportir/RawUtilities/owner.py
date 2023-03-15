# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from userbot import tgbot, PandaBot as pandaub
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import InlineQuery
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    PeerChannel,
)
from userbot._misc.data import _sudousers_list

def sudoers():
    return _sudousers_list()

def owner_and_sudos():
    return [str(pandaub.uid), *sudoers()]


def in_pattern(pat):
    def don(func):
        tgbot.add_event_handler(func, InlineQuery(pattern=pat))

    return don

async def admin_check(event):
    # Anonymous Admin Support
    if not event.sender_id and (
        isinstance(event.peer_id, PeerChannel)
        and str(event.peer_id.channel_id) in str(event.chat_id)
    ):
        return True
    if str(event.sender_id) in owner_and_sudos():
        return True
    try:
        perms = await event.client.get_permissions(event.chat_id, event.sender_id)
    except UserNotParticipantError:
        return False
    if isinstance(
        perms.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
    ):
        return True
    return False
