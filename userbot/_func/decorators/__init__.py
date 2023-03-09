import inspect
import logging
import os
from datetime import datetime
from traceback import format_exc
import pytz
from pyrogram import ContinuePropagation, StopPropagation, filters
from pyrogram.errors.exceptions.bad_request_400 import (
    MessageIdInvalid,
    MessageNotModified,
    MessageEmpty,
    UserNotParticipant
)
from pyrogram.handlers import MessageHandler

from ...Session.pyroclient import (
    app,
)

from ...config import Config



def listen(filter_s):
    """Simple Decorator To Handel Custom Filters"""
    def decorator(func):
        async def wrapper(client, message):
            try:
                await func(client, message)
            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            except UserNotParticipant:
                pass
            except MessageEmpty:
                pass
            except BaseException:
                logging.error(f"Exception - {func.__module__} - {func.__name__}")
                TZ = pytz.timezone(Config.TZ)
                datetime_tz = datetime.now(TZ)
                text = "**!ERROR WHILE HANDLING UPDATES!**\n\n"
                text += f"\n**Trace Back : ** `{str(format_exc())}`"
                text += f"\n**PandaUserbot-Name :** `{func.__module__}`"
                text += f"\n**Function Name :** `{func.__name__}` \n"
                text += datetime_tz.strftime(
                    "**Date :** `%Y-%m-%d` \n**Time :** `%H:%M:%S`"
                )
                text += "\n\n__You can Forward This to @PandaUserbot, If You Think This is A Error!__"
                try:
                    await client.send_message(Config.LOG_GRP, text)
                except BaseException:
                    logging.error(text)
            message.continue_propagation()
        if app:
            app.add_handler(MessageHandler(wrapper, filters=filter_s), group=0)
        return wrapper
    return decorator
