from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery


class AlertUser(object):
    def alert_user(self, func):
        async def wrapper(_, cb: CallbackQuery):
            if cb.from_user and not (
                cb.from_user.id == self.id or cb.from_user.id in self.SudoUsers()
            ):
                await cb.answer(
                    f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 ||𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁",
                    show_alert=True,
                )
            else:
                try:
                    await func(_, cb)
                except MessageNotModified:
                    pass

        return wrapper
