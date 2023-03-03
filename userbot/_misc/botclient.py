# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import datetime
import sys
import traceback

from telethon import TelegramClient, events
from ..config import Config
from ..helpers.utils.format import paste_text
from ..helpers.utils.utils import runcmd
from .logger import logging

LOGS = logging.getLogger(__name__)


class PandaUserbotToken(TelegramClient):
    def bot_cmd(
        self: TelegramClient,
        disable_errors: bool = False,
        edited: bool = False,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)

        def decorator(func):
            async def wrapper(check):
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except BaseException as e:
                    # Check if we have to disable error logging.
                    LOGS.exception(e)  # Log the error in console
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\nDisclaimer:\nThis file is pasted only here ONLY here,\
                                    \nwe logged only fact of error and date,\nwe respect your privacy,\
                                    \nyou may not report this error if you've\
                                    \nany confidential data here, no one will see your data\
                                    \n\n--------BEGIN USERBOT TRACEBACK LOG--------\
                                    \nDate: {date}\nGroup ID: {str(check.chat_id)}\
                                    \nSender ID: {str(check.sender_id)}\
                                    \n\nEvent Trigger:\n{str(check.text)}\
                                    \n\nTraceback info:\n{str(traceback.format_exc())}\
                                    \n\nError text:\n{str(sys.exc_info()[1])}"
                        new = {
                            "error": str(sys.exc_info()[1]),
                            "date": datetime.datetime.now(),
                        }
                        ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
                        command = 'git log --pretty=format:"%an: %s" -5'
                        ftext += "\n\n\nLast 5 commits:\n"
                        output = (await runcmd(command))[:2]
                        result = output[0] + output[1]
                        ftext += result
                        pastelink = paste_text(ftext)
                        text = "**PandaUserbot Error report**\n\n"
                        link = "[Klik](https://t.me/TEAMSquadUserbotSupport)"
                        text += "If you wanna you can report it"
                        text += f"- just forward this message {link}.\n"
                        text += (
                            "Nothing is logged except the fact of error and date\n\n"
                        )
                        text += f"**Error report : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import tgbot
            if tgbot:
                if edited is True:
                    tgbot.add_event_handler(func, events.MessageEdited(**kwargs))
                else:
                    tgbot.add_event_handler(func, events.NewMessage(**kwargs))

            return wrapper

        return decorator

