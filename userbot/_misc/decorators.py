# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery
from ..config import Config
from .data import _sudousers_list, pdB
from .._database._var import Var
Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 1593802955]


class check_owner:
    def __init__(self, func=None):
        self.func = func

    def __call__(self, *args, **kwargs):
        if not self.func:
            return self.__class__(args[0])

        async def wrapper(*args, **kwargs):
            c_q = args[0]
            if c_q.sender_id and (
                c_q.sender_id == Var.OWNER_ID
                or c_q.sender_id in _sudousers_list()
            ):
                

                try:
                    await self.func(c_q)
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds + 5)
                except MessageNotModifiedError:
                    pass
            else:
                await c_q.answer(
                    f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 ||𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁",
                    alert=True,
                )

        return wrapper(*args, **kwargs)
