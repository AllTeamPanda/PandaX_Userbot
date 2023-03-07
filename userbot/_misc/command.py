# Credits: @mrconfused
# FROM Panda-Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilhammansiz

import inspect
import re
from pathlib import Path

LOADED_CMDS = {}

from telethon import events
from ..config import Config

from ..Session import (
    vcbot,
)



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
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
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
            _ = "\\" + Config.COMMAND_HAND_LER
            sudo_ = "\\" + Config.SUDO_COMMAND_HAND_LER
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
            vcbot.add_event_handler(
                func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
            )
        vcbot.add_event_handler(
            func, events.NewMessage(**args, outgoing=True, pattern=_reg)
        )
        if allow_sudo:
            if not disable_edited:
                vcbot.add_event_handler(
                    func,
                    events.MessageEdited(
                        **args, from_users=list(Config.SUDO_USERS), pattern=sudo_reg
                    ),
                )
            vcbot.add_event_handler(
                func,
                events.NewMessage(
                    **args, from_users=list(Config.SUDO_USERS), pattern=sudo_reg
                ),
            )
        try:
            LOADED_CMDS[file_test].append(func)
        except Exception:
            LOADED_CMDS.update({file_test: [func]})
        return func

    return decorator
