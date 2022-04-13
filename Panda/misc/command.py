# Credits: @mrconfused
# FROM Panda-Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilhammansiz

import inspect
import re
from pathlib import Path
from typing import Dict, List, Union
from .HELP import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about


from telethon import events
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
from ..Osdb import Osdb

from .. import (
    bot,
    tgbot,
)


def Cutepanda(
    pattern: str = None,
    help: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
    or tuple = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    groups_only: bool = False,
    private_only: bool = False,
    dev: bool = True,
    dual: bool = False,
    edited: bool = True,
    disable_errors: bool = False,
    command: str or tuple = None,
    **args,
) -> callable:
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    args.setdefault("forwards", forword)
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(Osdb.BLACK_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats
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
            CMD_INFO[command[0]] = [_format_about(help)]
    if pattern is not None:
        global _reg
        global sudo_reg
        if pattern is not None:
            if (
                pattern.startswith(r"\#")
                or not pattern.startswith(r"\#")
                and pattern.startswith(r"^")
            ):
                _reg = sudo_reg = re.compile(pattern)
            else:
                _ = "\\" + Osdb.HANDLER
                sudo_ = "\\" + Osdb.SUDO_HANDLER
                _reg = re.compile(_ + pattern)
                sudo_reg = re.compile(sudo_ + pattern)
            

    def decorator(func):
        async def wrapper(check):
            if groups_only and not check.is_group:
                return await check.respond("`I don't think this is a group.`", 10)
            if private_only and not check.is_private:
               return await check.respond("`I don't think this is a personal Chat.`", 10)
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
            if edited:
                bot.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
                )
            bot.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=_reg)
                )
            if allow_sudo is not None:
                if command is not None or command[0]:
                    if edited:
                        bot.add_event_handler(
                            func,
                            events.MessageEdited(
                                **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                            ),
                        )
                    bot.add_event_handler(
                        func,
                        events.NewMessage(
                            **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                        ),
                    )
        else:
            if file_test in LOADED_CMDS and func in LOADED_CMDS[file_test]:
                return None
            try:
                LOADED_CMDS[file_test].append(func)
            except BaseException:
               LOADED_CMDS.update({file_test: [func]})
            if edited:
                bot.add_event_handler(func, events.MessageEdited(**args))
            bot.add_event_handler(func, events.NewMessage(**args))
        return wrapper

    return decorator







def pandacute(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(Osdb.BLACK_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global _reg
        global sudo_reg
        global t_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            _reg = sudo_reg = t_req = re.compile(pattern)
        else:
            _ = "\\" + Osdb.HANDLER
            sudo_ = "\\" + Osdb.SUDO_HANDLER
            _reg = re.compile(_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = _ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                LOADED_CMDS[file_test].append(cmd1)
            except BaseException:
                LOADED_CMDS.update({file_test: [cmd1]})

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(
                func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
            )
        bot.add_event_handler(
            func, events.NewMessage(**args, outgoing=True, pattern=_reg)
        )
        if allow_sudo:
            if not disable_edited:
                bot.add_event_handler(
                    func,
                    events.MessageEdited(
                        **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                    ),
                )
            bot.add_event_handler(
                func,
                events.NewMessage(
                    **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                ),
            )
        try:
            LOADED_CMDS[file_test].append(func)
        except Exception:
            LOADED_CMDS.update({file_test: [func]})
        return func

    return decorator

def cute(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        return func
    return decorator




def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def callback(**args):
    """Assistant's callback decorator"""

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
