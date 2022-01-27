# ILHAM MANSIEZ
# PANDA USERBOT

import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from ..Config import Config
Alive = Config.ALIVE_NAME



def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS and DEVS
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                f"𝗜𝗻𝗶 𝗺𝗲𝗻𝘂 𝗵𝗲𝗹𝗽 𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗣𝗲𝗻𝗴𝗴𝘂𝗻𝗮 {Alive}\n\n𝗗𝗲𝗽𝗹𝗼𝘆 𝗦𝗲𝗻𝗱𝗶𝗿𝗶  𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁𝗠𝘂.",
                alert=True,
            )

    return wrapper
