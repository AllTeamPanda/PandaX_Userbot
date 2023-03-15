# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

import logging

LOGS = logging.getLogger(__name__)


# Admin checker by uniborg
async def is_admin(PandaBot, chat_id, userid):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await PandaBot(GetParticipantRequest(chat_id, userid))
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False
