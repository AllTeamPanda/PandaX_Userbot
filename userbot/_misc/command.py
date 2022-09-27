# Credits: @mrconfused
# FROM Panda-Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilhammansiz

import inspect
import re
from pathlib import Path
from typing import Dict, List, Union
from .Help import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from pathlib import Path
from time import gmtime, strftime
from traceback import format_exc


from telethon import events
from ..Var import Osdb, CMD_HANDLER, CMD_LIST, DEFAULT

from ..Session import (
    PandaBot,
    PandaBot2,
    PandaBot3,
    tgbot,
)



class userbot(object):
    def ilhammansiz_cmd(
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
            if PandaBot:
                if not disable_edited:
                    PandaBot.add_event_handler(
                        func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
                    )
                PandaBot.add_event_handler(
                    func, events.NewMessage(**args, outgoing=True, pattern=_reg)
                )
            if PandaBot2:
                if not disable_edited:
                    PandaBot2.add_event_handler(
                        func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
                    )
                PandaBot2.add_event_handler(
                    func, events.NewMessage(**args, outgoing=True, pattern=_reg)
                )
            if PandaBot3:
                if not disable_edited:
                    PandaBot3.add_event_handler(
                        func, events.MessageEdited(**args, outgoing=True, pattern=_reg)
                    )
                PandaBot3.add_event_handler(
                    func, events.NewMessage(**args, outgoing=True, pattern=_reg)
                )
            if allow_sudo:
                if PandaBot:
                    if not disable_edited:
                        PandaBot.add_event_handler(
                            func,
                            events.MessageEdited(
                                **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                            ),
                        )
                    PandaBot.add_event_handler(
                        func,
                        events.NewMessage(
                            **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                if PandaBot2:
                    if not disable_edited:
                        PandaBot2.add_event_handler(
                            func,
                            events.MessageEdited(
                                **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                            ),
                        )
                    PandaBot2.add_event_handler(
                        func,
                        events.NewMessage(
                            **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                    ),
                )
                if PandaBot3:
                    if not disable_edited:
                        PandaBot3.add_event_handler(
                            func,
                            events.MessageEdited(
                                **args, from_users=list(Osdb.SUDO_USERS), pattern=sudo_reg
                            ),
                        )
                    PandaBot3.add_event_handler(
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
            if PandaBot:
            PandaBot.add_event_handler(func, events.NewMessage(**args))
            if PandaBot2:
                PandaBot2.add_event_handler(func, events.NewMessage(**args))
            if PandaBot3:
                PandaBot3.add_event_handler(func, events.NewMessage(**args))
            return func
        return decorator


    def register(**args):
    """Register a new event."""
        pattern = args.get("pattern")
        disable_edited = args.get("disable_edited", False)
        ignore_unsafe = args.get("ignore_unsafe", False)
        unsafe_pattern = r"^[^/!#@\$A-Za-z]"
        groups_only = args.get("groups_only", False)
        trigger_on_fwd = args.get("trigger_on_fwd", False)
        disable_errors = args.get("disable_errors", False)
        insecure = args.get("insecure", False)
        args.get("own", False)

        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern

        if "disable_edited" in args:
            del args["disable_edited"]

        if "ignore_unsafe" in args:
            del args["ignore_unsafe"]

        if "groups_only" in args:
            del args["groups_only"]

        if "disable_errors" in args:
            del args["disable_errors"]

        if "trigger_on_fwd" in args:
            del args["trigger_on_fwd"]
        
        if "own" in args:
           del args["own"]
           args["incoming"] = True
           args["from_users"] = DEFAULT

        if "insecure" in args:
            del args["insecure"]

        if pattern and not ignore_unsafe:
            args["pattern"] = pattern.replace("^.", unsafe_pattern, 1)

        def decorator(func):
            async def wrapper(check):
                if check.edit_date and check.is_channel and not check.is_group:
                # Messages sent in channels can be edited by other users.
                # Ignore edits that take place in channels.
                    return
                if not trigger_on_fwd and check.fwd_from:
                    return

                if groups_only and not check.is_group:
                    await check.respond("`I don't think this is a group.`")
                    return

                if check.via_bot_id and not insecure and check.out:
                    return

                try:
                    await func(check)

                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except BaseException:

                # Check if we have to disable it.
                # If not silence the log spam on the console,
                # with a dumb except.

                    if not disable_errors:
                        date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                        text = "**!!! PandaUserbot ERROR REPOR !!!**\n\n"
                        link = "[Group Support](https://t.me/TeamSquadUserbotSupport)"
                        text += "Jika mau, Anda bisa melaporkan error ini, "
                        text += f"Cukup forward saja pesan ini ke {link}.\n\n"

                        ftext = "========== DISCLAIMER =========="
                        ftext += "\nFile ini HANYA diupload di sini,"
                        ftext += "\nkami hanya mencatat fakta error dan tanggal,"
                        ftext += "\nkami menghormati privasi Anda."
                        ftext += "\nJika mau, Anda bisa melaporkan error ini,"
                        ftext += "\ncukup forward saja pesan ini ke @TeamSquadUserbotSupport"
                        ftext += "\n================================\n\n"
                        ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                        ftext += "\nTanggal : " + date
                        ftext += "\nChat ID : " + str(check.chat_id)
                        ftext += "\nUser ID : " + str(check.sender_id)
                        ftext += "\n\nEvent Trigger:\n"
                        ftext += str(check.text)
                        ftext += "\n\nTraceback info:\n"
                        ftext += str(format_exc())
                        ftext += "\n\nError text:\n"
                        ftext += str(sys.exc_info()[1])
                        ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                        command = 'git log --pretty=format:"%an: %s" -10'

                        ftext += "\n\n\n10 commits Terakhir:\n"

                       bprocess = await asyncsubshell(
                        command, stdout=asyncsub.PIPE, stderr=asyncsub.PIPE
                        )
                        stdout, stderr = await process.communicate()
                        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

                        ftext += result

                        with open("error.log", "w+") as file:
                            file.write(ftext)
            if PandaBot:
                if not disable_edited:
                    PandaBot.add_event_handler(wrapper, events.MessageEdited(**args))
                PandaBot.add_event_handler(wrapper, events.NewMessage(**args))
            if PandaBot2:
                if not disable_edited:
                    PandaBot2.add_event_handler(wrapper, events.MessageEdited(**args))
                PandaBot2.add_event_handler(wrapper, events.NewMessage(**args))
            if PandaBot3:
                if not disable_edited:
                    PandaBot3.add_event_handler(wrapper, events.MessageEdited(**args))
                PandaBot3.add_event_handler(wrapper, events.NewMessage(**args))
                return wrapper

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

    def CMD_HELP:
        CMD_HELP = {}
        return CMD_HELP
    

    def callback(**args):
        """Assistant's callback decorator"""

        def decorator(func):
            if tgbot:
                tgbot.add_event_handler(func, events.CallbackQuery(**args))
            return func

        return decorator

    
