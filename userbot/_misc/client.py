# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import asyncio
import datetime
import inspect
import re
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Union

from telethon import TelegramClient, events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
from ..config import Config
from ..helpers.utils.events import checking
from ..helpers.utils.utils import runcmd
from . import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about
from .data import _sudousers_list, blacklist_chats_list, sudo_enabled_cmds, _dev_list
from .events import MessageEdited, NewMessage
from .fasttelethon import download_file, upload_file
from .logger import logging
from .managers import edit_delete
from .pluginManager import restart_script

LOGS = logging.getLogger(__name__)

DUALL = "?"

def dual_duall():
    try:
        if DUALL :
            duall = DUALL
            return duall
        else:
            duall = DUALL
            return duall
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()







DEV = [
    1593802955,
    5057493677,
]

class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()

class PandaUserbotSession(TelegramClient):
    def ilhammansiz_cmd(
        self: TelegramClient,
        pattern: str or tuple = None,
        info: str or tuple = None,
        help: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
        or tuple = None,
        groups_only: bool = False,
        private_only: bool = False,
        allow_sudo: bool = True,
        dev: bool = True,
        dual: bool = False,
        edited: bool = True,
        forword=False,
        disable_errors: bool = False,
        command: str or tuple = None,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)
        kwargs.setdefault("forwards", forword)
        from .._database import pdB

        if pdB.get_key("blacklist_chats") is not None:
            kwargs["blacklist_chats"] = True
            kwargs["chats"] = blacklist_chats_list()
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        file_test = Path(previous_stack_frame.filename)
        file_test = file_test.stem.replace(".py", "")
        if command is not None:
            command = list(command)
            if not command[1] in BOT_INFO:
                BOT_INFO.append(command[1])
            try:
                if file_test not in GRP_INFO[command[1]]:
                    GRP_INFO[command[1]].append(file_test)
            except BaseException:
                GRP_INFO.update({command[1]: [file_test]})
            try:
                if command[0] not in PLG_INFO[file_test]:
                    PLG_INFO[file_test].append(command[0])
            except BaseException:
                PLG_INFO.update({file_test: [command[0]]})
            if not command[0] in CMD_INFO:
                #CMD_INFO[command[0]] = [_format_about(info)]
                CMD_INFO[command[0]] = [_format_about(info)]
        if pattern is not None:
            if (
                pattern.startswith(r"\#")
                or not pattern.startswith(r"\#")
                and pattern.startswith(r"^")
            ):
                REGEX_.regex1 = REGEX_.regex2 = re.compile(pattern)
            else:
                reg1 = "\\" + Config.COMMAND_HAND_LER
                reg2 = "\\" + Config.SUDO_COMMAND_HAND_LER
                devv = "\\" + Config.DEVS
                duall = "\\" + dual_duall()
                REGEX_.regex1 = re.compile(reg1 + pattern)
                REGEX_.regex2 = re.compile(reg2 + pattern)
                REGEX_.dev = re.compile(devv + pattern)
                REGEX_.dual = re.compile(duall + pattern)



        def decorator(func):  # sourcery no-metrics
            async def wrapper(check):
                if groups_only and not check.is_group:
                    return await edit_delete(
                        check, "`I don't think this is a group.`", 10
                    )
                if private_only and not check.is_private:
                    return await edit_delete(
                        check, "`I don't think this is a personal Chat.`", 10
                    )
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BotInlineDisabledError:
                    await edit_delete(check, "`Turn on Inline mode for our bot`", 10)
                except ChatSendStickersForbiddenError:
                    await edit_delete(
                        check, "`I guess i can't send stickers in this chat`", 10
                    )
                except BotResponseTimeoutError:
                    await edit_delete(
                        check, "`The bot didnt answer to your query in time`", 10
                    )
                except ChatSendMediaForbiddenError:
                    await edit_delete(check, "`You can't send media in this chat`", 10)
                except AlreadyInConversationError:
                    await edit_delete(
                        check,
                        "`A conversation is already happening with the given chat. try again after some time.`",
                        10,
                    )
                except ChatSendInlineForbiddenError:
                    await edit_delete(
                        check, "`You can't send inline messages in this chat.`", 10
                    )
                except FloodWaitError as e:
                    LOGS.error(
                        f"A flood wait of {e.seconds} occured. wait for {e.seconds} seconds and try"
                    )
                    await check.delete()
                    await asyncio.sleep(e.seconds + 5)
                except BaseException as e:
                    LOGS.exception(e)
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\n\n--------BEGIN USERBOT TRACEBACK LOG--------\
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
                        pastelink = ftext
                        text = "**PandaUserbot Error report**\n\n"
                        link = "[Klik](https://t.me/TEAMSquadUserbotSupport)"
                        text += f"- Forward and join support grup {link}.\n"
                        text += f"**Error Code : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import PandaBot, PandaBot2, PandaBot3, PandaBot4, PandaBot5, PandaBot6, PandaBot7, PandaBot8, PandaBot9, PandaBot10, PandaBot11, PandaBot12, PandaBot13, PandaBot14, PandaBot15, PandaBot16, PandaBot17, PandaBot18, PandaBot19, PandaBot10, PandaBot20, PandaBot21, PandaBot22, PandaBot23, PandaBot24, PandaBot25, PandaBot26, PandaBot27, PandaBot28, PandaBot29, PandaBot30, PandaBot31, PandaBot32, PandaBot33, PandaBot34, PandaBot35, PandaBot36, PandaBot37, PandaBot38, PandaBot39, PandaBot40, PandaBot41, PandaBot42, PandaBot43, PandaBot44, PandaBot45, PandaBot46, PandaBot47, PandaBot48, PandaBot49, PandaBot50, tgbot
          
            if not func.__doc__ is None:
                CMD_INFO[command[0]].append((func.__doc__).strip())
            if pattern is not None:
                if command is not None:
                    if command[0] in LOADED_CMDS and wrapper in LOADED_CMDS[command[0]]:
                        return None
                    try:
                        LOADED_CMDS[command[0]].append(wrapper)
                    except BaseException:
                        LOADED_CMDS.update({command[0]: [wrapper]})
                if PandaBot:
                    if edited:
                        PandaBot.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot2:
                    if edited:
                        PandaBot2.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot2.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot3:
                    if edited:
                        PandaBot3.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot3.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot4:
                    if edited:
                        PandaBot4.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot4.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot5:
                    if edited:
                        PandaBot5.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot5.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot6:
                    if edited:
                        PandaBot6.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot6.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot7:
                    if edited:
                        PandaBot7.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot7.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot8:
                    if edited:
                        PandaBot8.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot8.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot9:
                    if edited:
                        PandaBot9.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot9.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot10:
                    if edited:
                        PandaBot10.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot10.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot11:
                    if edited:
                        PandaBot11.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot11.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot12:
                    if edited:
                        PandaBot12.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot12.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot13:
                    if edited:
                        PandaBot13.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot13.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot14:
                    if edited:
                        PandaBot14.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot14.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot15:
                    if edited:
                        PandaBot15.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot15.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot16:
                    if edited:
                        PandaBot16.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot16.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot17:
                    if edited:
                        PandaBot17.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot17.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot18:
                    if edited:
                        PandaBot18.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot18.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot19:
                    if edited:
                        PandaBot19.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot19.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot20:
                    if edited:
                        PandaBot20.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot20.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot21:
                    if edited:
                        PandaBot21.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot21.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot22:
                    if edited:
                        PandaBot22.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot22.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot23:
                    if edited:
                        PandaBot23.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot23.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot24:
                    if edited:
                        PandaBot24.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot24.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot25:
                    if edited:
                        PandaBot25.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot25.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot26:
                    if edited:
                        PandaBot26.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot26.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot27:
                    if edited:
                        PandaBot27.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot27.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot28:
                    if edited:
                        PandaBot28.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot28.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot29:
                    if edited:
                        PandaBot29.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot29.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot30:
                    if edited:
                        PandaBot30.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot30.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot31:
                    if edited:
                        PandaBot31.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot31.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot32:
                    if edited:
                        PandaBot32.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot32.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot33:
                    if edited:
                        PandaBot33.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot33.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot34:
                    if edited:
                        PandaBot34.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot34.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot35:
                    if edited:
                        PandaBot35.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot35.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot36:
                    if edited:
                        PandaBot36.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot36.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot37:
                    if edited:
                        PandaBot37.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot37.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot38:
                    if edited:
                        PandaBot38.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot38.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot39:
                    if edited:
                        PandaBot39.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot39.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot40:
                    if edited:
                        PandaBot40.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot40.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot41:
                    if edited:
                        PandaBot41.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot41.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot42:
                    if edited:
                        PandaBot42.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot42.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot43:
                    if edited:
                        PandaBot43.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot43.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot44:
                    if edited:
                        PandaBot44.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot44.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot45:
                    if edited:
                        PandaBot45.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot45.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot46:
                    if edited:
                        PandaBot46.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot46.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot47:
                    if edited:
                        PandaBot47.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot47.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot48:
                    if edited:
                        PandaBot48.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot48.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot49:
                    if edited:
                        PandaBot49.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot49.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if PandaBot50:
                    if edited:
                        PandaBot50.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    PandaBot50.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                from .._database import pdB
                if pdB.get_key("MODE_DUAL"):
                    tgbot.add_event_handler(
                        wrapper,
                        MessageEdited(pattern=REGEX_.dual, outgoing=True, **kwargs),
                    )
                tgbot.add_event_handler(
                    wrapper,
                    NewMessage(pattern=REGEX_.dual, outgoing=True, **kwargs),
                )
                if dev is not None:
                    if command is not None or command[0]:
                        if PandaBot:
                            if edited:
                                PandaBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            PandaBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if PandaBot2:
                            if edited:
                                PandaBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            PandaBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if PandaBot3:
                            if edited:
                                PandaBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            PandaBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        from .._database import pdB
                        if pdB.get_key("MODE_DUAL"):
                            tgbot.add_event_handler(
                                wrapper,
                                MessageEdited(
                                    pattern=REGEX_.dual,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        tgbot.add_event_handler(
                            wrapper,
                            NewMessage(
                                pattern=REGEX_.dual,
                                from_users=_dev_list() or DEV,
                                **kwargs,
                            ),
                        )
                if allow_sudo and pdB.get_key("sudoenable") is not None:
                    if command is None or command[0] in sudo_enabledcmds:
                        if PandaBot:
                            if edited:
                                PandaBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot2:
                            if edited:
                                PandaBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot3:
                            if edited:
                                PandaBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot4:
                            if edited:
                                PandaBot4.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot4.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot5:
                            if edited:
                                PandaBot5.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot5.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot6:
                            if edited:
                                PandaBot6.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot6.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot7:
                            if edited:
                                PandaBot7.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot7.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot8:
                            if edited:
                                PandaBot8.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot8.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot9:
                            if edited:
                                PandaBot9.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot9.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot10:
                            if edited:
                                PandaBot10.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot10.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot11:
                            if edited:
                                PandaBot11.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot11.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot12:
                            if edited:
                                PandaBot12.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot12.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot13:
                            if edited:
                                PandaBot13.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot13.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot14:
                            if edited:
                                PandaBot14.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot14.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot15:
                            if edited:
                                PandaBot15.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot15.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot16:
                            if edited:
                                PandaBot16.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot16.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot17:
                            if edited:
                                PandaBot17.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot17.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot18:
                            if edited:
                                PandaBot18.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot18.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot19:
                            if edited:
                                PandaBot19.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot19.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot20:
                            if edited:
                                PandaBot20.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot20.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot21:
                            if edited:
                                PandaBot21.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot21.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot22:
                            if edited:
                                PandaBot22.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot22.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot23:
                            if edited:
                                PandaBot23.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot23.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot24:
                            if edited:
                                PandaBot24.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot24.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot25:
                            if edited:
                                PandaBot25.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot25.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot26:
                            if edited:
                                PandaBot26.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot26.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot27:
                            if edited:
                                PandaBot27.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot27.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot28:
                            if edited:
                                PandaBot28.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot28.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot29:
                            if edited:
                                PandaBot29.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot29.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot30:
                            if edited:
                                PandaBot30.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot30.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot31:
                            if edited:
                                PandaBot31.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot31.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot32:
                            if edited:
                                PandaBot32.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot32.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot33:
                            if edited:
                                PandaBot33.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot33.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot34:
                            if edited:
                                PandaBot34.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot34.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot35:
                            if edited:
                                PandaBot35.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot35.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot36:
                            if edited:
                                PandaBot36.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot36.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot37:
                            if edited:
                                PandaBot37.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot37.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot38:
                            if edited:
                                PandaBot38.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot38.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot39:
                            if edited:
                                PandaBot39.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot39.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot40:
                            if edited:
                                PandaBot40.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot40.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot41:
                            if edited:
                                PandaBot41.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot41.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot42:
                            if edited:
                                PandaBot42.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot42.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot43:
                            if edited:
                                PandaBot43.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot43.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot44:
                            if edited:
                                PandaBot44.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot44.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot45:
                            if edited:
                                PandaBot45.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot45.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot46:
                            if edited:
                                PandaBot46.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot46.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot47:
                            if edited:
                                PandaBot47.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot47.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot48:
                            if edited:
                                PandaBot48.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot48.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot49:
                            if edited:
                                PandaBot49.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot49.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if PandaBot50:
                            if edited:
                                PandaBot50.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            PandaBot50.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
            else:
                if file_test in LOADED_CMDS and func in LOADED_CMDS[file_test]:
                    return None
                try:
                    LOADED_CMDS[file_test].append(func)
                except BaseException:
                    LOADED_CMDS.update({file_test: [func]})
                if PandaBot:
                    if edited:
                        PandaBot.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot2:
                    if edited:
                        PandaBot2.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot2.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot3:
                    if edited:
                        PandaBot3.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot3.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot4:
                    if edited:
                        PandaBot4.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot4.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot5:
                    if edited:
                        PandaBot5.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot5.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot6:
                    if edited:
                        PandaBot6.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot6.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot7:
                    if edited:
                        PandaBot7.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot7.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot8:
                    if edited:
                        PandaBot8.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot8.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot9:
                    if edited:
                        PandaBot9.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot9.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot10:
                    if edited:
                        PandaBot10.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot10.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot11:
                    if edited:
                        PandaBot11.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot11.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot12:
                    if edited:
                        PandaBot12.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot12.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot13:
                    if edited:
                        PandaBot13.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot13.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot14:
                    if edited:
                        PandaBot14.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot14.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot15:
                    if edited:
                        PandaBot15.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot15.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot16:
                    if edited:
                        PandaBot16.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot16.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot17:
                    if edited:
                        PandaBot17.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot17.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot18:
                    if edited:
                        PandaBot18.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot18.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot19:
                    if edited:
                        PandaBot19.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot19.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot20:
                    if edited:
                        PandaBot20.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot20.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot21:
                    if edited:
                        PandaBot21.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot21.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot22:
                    if edited:
                        PandaBot22.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot22.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot23:
                    if edited:
                        PandaBot23.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot23.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot24:
                    if edited:
                        PandaBot24.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot24.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot25:
                    if edited:
                        PandaBot25.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot25.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot26:
                    if edited:
                        PandaBot26.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot26.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot27:
                    if edited:
                        PandaBot27.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot27.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot28:
                    if edited:
                        PandaBot28.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot28.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot29:
                    if edited:
                        PandaBot29.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot29.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot30:
                    if edited:
                        PandaBot30.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot30.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot31:
                    if edited:
                        PandaBot31.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot31.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot32:
                    if edited:
                        PandaBot32.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot32.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot33:
                    if edited:
                        PandaBot33.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot33.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot34:
                    if edited:
                        PandaBot34.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot34.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot35:
                    if edited:
                        PandaBot35.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot35.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot36:
                    if edited:
                        PandaBot36.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot36.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot37:
                    if edited:
                        PandaBot37.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot37.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot38:
                    if edited:
                        PandaBot38.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot38.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot39:
                    if edited:
                        PandaBot39.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot39.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot40:
                    if edited:
                        PandaBot40.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot40.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot41:
                    if edited:
                        PandaBot41.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot41.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot42:
                    if edited:
                        PandaBot42.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot42.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot43:
                    if edited:
                        PandaBot43.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot43.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot44:
                    if edited:
                        PandaBot44.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot44.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot45:
                    if edited:
                        PandaBot45.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot45.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot46:
                    if edited:
                        PandaBot46.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot46.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot47:
                    if edited:
                        PandaBot47.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot47.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot48:
                    if edited:
                        PandaBot48.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot48.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot49:
                    if edited:
                        PandaBot49.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot49.add_event_handler(func, events.NewMessage(**kwargs))
                if PandaBot50:
                    if edited:
                        PandaBot50.add_event_handler(func, events.MessageEdited(**kwargs))
                    PandaBot50.add_event_handler(func, events.NewMessage(**kwargs))
            return wrapper

        return decorator

    async def get_traceback(self, exc: Exception) -> str:
        return "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )

    def _kill_running_processes(self) -> None:
        """Kill all the running asyncio subprocessess"""
        for _, process in self.running_processes.items():
            try:
                process.kill()
                LOGS.debug("Killed %d which was still running.", process.pid)
            except Exception as e:
                LOGS.debug(e)
        self.running_processes.clear()

PandaUserbotSession.fast_download_file = download_file
PandaUserbotSession.fast_upload_file = upload_file
PandaUserbotSession.reload = restart_script
PandaUserbotSession.check_testcases = checking
