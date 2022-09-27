import asyncio


from pyrogram.types import CallbackQuery
from pyrogram.errors import FloodWait, MessageNotModified

from ..Var import Config
Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 1593802955]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWait as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModified:
                pass
        else:
            await c_q.answer(
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 || 𝐎𝐰𝐧𝐞𝐫: {Alive}\n\n𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁",
                alert=True,
            )

    return wrapper

