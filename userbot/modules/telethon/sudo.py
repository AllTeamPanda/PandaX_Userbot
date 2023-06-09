from datetime import datetime

from telethon.utils import get_display_name

from ... import pandaub, SqL, udB
import logging

from ...config import Config
from ..._misc.tools import inline_mention
from ..._misc import CMD_INFO, PLG_INFO
from ..._misc.data import _sudousers_list, sudo_enabled_cmds
from . import edit_delete, edit_or_reply
from ...helpers.utils import get_user_from_event, mentionuser
from telethon.tl.types import User

plugin_category = "plugins"

LOGS = logging.getLogger(__name__)


async def _init() -> None:
    sudousers = _sudousers_list()
    Config.SUDO_USERS.clear()
    for user_d in sudousers:
        Config.SUDO_USERS.add(user_d)


    

def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


@pandaub.ilhammansiz_cmd(
    pattern="sudo (on|off)$",
    command=("sudo", plugin_category),
    info={
        "header": "To enable or disable sudo of your Catuserbot.",
        "description": "Initially all sudo commands are disabled, you need to enable them by addscmd\n Check `{tr}help -c addscmd`",
        "usage": "{tr}sudo <on/off>",
    },
)
async def chat_blacklist(event):
    "To enable or disable sudo of your PandaUserbot."
    input_str = event.pattern_match.group(1)
    sudousers = _sudousers_list()
    if input_str == "on":
        if SqL.get_key("sudoenable") is not None:
            return await edit_delete(event, "__Sudo is already enabled.__")
        SqL.set_key("sudoenable", "true")
        text = "__Enabled sudo successfully.__\n"
        if len(sudousers) != 0:
            text += (
                "**Bot is reloading to apply the changes. Please wait for a minute**"
            )
            msg = await edit_or_reply(
                event,
                text,
            )
            return await event.client.reload(msg)
        else:
            text += "**You haven't added anyone to your sudo yet.**"
            return await edit_or_reply(
                event,
                text,
            )
    if SqL.get_key("sudoenable") is not None:
        SqL.del_key("sudoenable")
        text = "__Disabled sudo successfully.__"
        if len(sudousers) != 0:
            text += (
                "**Bot is reloading to apply the changes. Please wait for a minute**"
            )
            msg = await edit_or_reply(
                event,
                text,
            )
            return await event.client.reload(msg)
        else:
            text += "**You haven't added any chat to blacklist yet.**"
            return await edit_or_reply(
                event,
                text,
            )
    await edit_delete(event, "It was turned off already")


@pandaub.ilhammansiz_cmd(
    pattern="addsudo(?: |$)(.*)",
    command=("addsudo", plugin_category),
    info={
        "header": "To add user as your sudo.",
        "usage": "{tr}addsudo <username/reply/mention>",
    },
)
async def add_sudo_user(ult):
    "To add user to sudo."
    inputs = ult.pattern_match.group(1).strip()
    if ult.reply_to_msg_id:
        replied_to = await ult.get_reply_message()
        id = replied_to.sender_id
        name = await replied_to.get_sender()
    elif inputs:
        try:
            id = await ult.client.parse_id(inputs)
        except ValueError:
            try:
                id = int(inputs)
            except ValueError:
                id = inputs
        try:
            name = await ult.client.get_entity(int(id))
        except BaseException:
            name = None
    elif ult.is_private:
        id = ult.chat_id
        name = await ult.get_chat()
    else:
        return await edit_delete(ult, "`Reply to a msg or add it's id/username.`", time=5)
    if name and isinstance(name, User) and (name.bot or name.verified):
        return await edit_delete(ult, "Bots can't be added as Sudo Users.")
    name = inline_mention(name) if name else f"`{id}`"
    if id == pandaub.uid:
        mmm = "You cant add yourself as Sudo User..."
    elif id in _sudousers_list():
        mmm = f"{name} `is already a SUDO User ...`"
    else:
        udB.set_key("sudoenable", "True")
        key = _sudousers_list()
        key.append(id)
        udB.set_key("sudousers_list", key)
        mmm = f"**Added** {name} **as SUDO User**"
    msg = await edit_delete(ult, mmm, time=5)
    await ult.client.reload(msg)


@pandaub.ilhammansiz_cmd(
    pattern="delsudo(?: |$)(.*)",
    command=("delsudo", plugin_category),
    info={
        "header": "To remove user from your sudo.",
        "usage": "{tr}delsudo <username/reply/mention>",
    },
)
async def _(ult):
    "To del user from sudo."
    inputs = ult.pattern_match.group(1).strip()
    if ult.reply_to_msg_id:
        replied_to = await ult.get_reply_message()
        id = replied_to.sender_id
        name = await replied_to.get_sender()
    elif inputs:
        try:
            id = await ult.client.parse_id(inputs)
        except ValueError:
            try:
                id = int(inputs)
            except ValueError:
                id = inputs
        try:
            name = await ult.client.get_entity(int(id))
        except BaseException:
            name = None
    elif ult.is_private:
        id = ult.chat_id
        name = await ult.get_chat()
    else:
        return await edit_delete(ult, "`Reply to a msg or add it's id/username.`", time=5)
    name = inline_mention(name) if name else f"`{id}`"
    if id not in _sudousers_list():
        mmm = f"{name} `wasn't a SUDO User ...`"
    else:
        key = _sudousers_list()
        key.remove(id)
        udB.set_key("sudousers_list", key)
        mmm = f"**Removed** {name} **from SUDO User(s)**"
    msg = await edit_delete(ult, mmm, time=5)
    await ult.client.reload(msg)


@pandaub.ilhammansiz_cmd(
    pattern="vsudo$",
    command=("vsudo", plugin_category),
    info={
        "header": "To list users for whom you are sudo.",
        "usage": "{tr}vsudo",
    },
)
async def _(ult):
    "To list Your sudo users"
    sudos = _sudousers_list()
    if not sudos:
        return await edit_delete(ult, "No SUDO User was assigned ...", time=5)
    msg = ""
    for i in sudos:
        try:
            name = await ult.client.get_entity(int(i))
        except BaseException:
            name = None
        if name:
            msg += f"• {inline_mention(name)} ( `{i}` )\n"
        else:
            msg += f"• `{i}` -> Invalid User\n"
    m = udB.get_key("sudoenable") or True
    if not m:
        m = ".sudo on"
    return await edit_delete(ult,
        f"**SUDO MODE : {m}\n\nList of SUDO Users :**\n{msg}", link_preview=False
    )
    

@pandaub.ilhammansiz_cmd(
    pattern="addscmd(s)? ((.|\n)*)",
    command=("addscmd", plugin_category),
    info={
        "header": "To enable cmds for sudo users.",
        "flags": {
            "-all": "Will enable all cmds for sudo users. (except few like eval, exec, profile).",
            "-full": "Will add all cmds including eval,exec...etc. compelete sudo.",
            "-p": "Will add all cmds from the given plugin names.",
        },
        "usage": [
            "{tr}addscmd -all",
            "{tr}addscmd -full",
            "{tr}addscmd -p <plugin names>",
            "{tr}addscmd <commands>",
        ],
        "examples": [
            "{tr}addscmd -p autoprofile botcontrols i.e, for multiple names use space between each name",
            "{tr}addscmd ping alive i.e, for multiple names use space between each name",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To enable cmds for sudo users."
    input_str = event.pattern_match.group(2)
    errors = ""
    sudocmds = sudo_enabled_cmds()
    if not input_str:
        return await edit_or_reply(
            event, "__Which command should i enable for sudo users . __"
        )
    input_str = input_str.split()
    if input_str[0] == "-all":
        pandaevent = await edit_or_reply(
            event, "__Enabling all safe cmds for sudo....__"
        )
        totalcmds = CMD_INFO.keys()
        flagcmds = (
            PLG_INFO["chain"]
            + PLG_INFO["autoprofile"]
            + PLG_INFO["evaluators"]
            + PLG_INFO["execmod"]
            + PLG_INFO["database"]
            + PLG_INFO["afk"]
            + PLG_INFO["lockchat"]
            + PLG_INFO["custom"]
            + PLG_INFO["carbon"]
            + PLG_INFO["corecmds"]
            + PLG_INFO["groupactions"]
            + PLG_INFO["sudo"]
            + PLG_INFO["transferchannel"]
            + ["climate"]
            + ["covid"]
        )
        loadcmds = list(set(totalcmds) - set(flagcmds))
        if len(sudocmds) > 0:
            SqL.del_key("sudo_enabled_cmds")
    elif input_str[0] == "-full":
        pandaevent = await edit_or_reply(
            event, "__Enabling compelete sudo for users....__"
        )
        loadcmds = CMD_INFO.keys()
        if len(sudocmds) > 0:
            SqL.del_key("sudo_enabled_cmds")
    elif input_str[0] == "-p":
        pandaevent = event
        input_str.remove("-p")
        loadcmds = []
        for plugin in input_str:
            if plugin not in PLG_INFO:
                errors += f"`{cmd}` __There is no such plugin in your PandaUserbot__.\n"
            else:
                loadcmds += PLG_INFO[plugin]
    else:
        pandaevent = event
        loadcmds = []
        for cmd in input_str:
            if cmd not in CMD_INFO:
                errors += (
                    f"`{cmd}` __There is no such command in your PandaUserbot__.\n"
                )
            elif cmd in sudocmds:
                errors += f"`{cmd}` __Is already enabled for sudo users__.\n"
            else:
                loadcmds.append(cmd)
    for cmd in loadcmds:
        SqL.set_key("sudo_enabled_cmds", cmd)
    result = (
        f"__Successfully enabled __ `{len(loadcmds)}` __ for PandaUserbot sudo.__\n"
    )
    output = (
        result + "**Bot is reloading to apply the changes. Please wait for a minute**\n"
    )
    if errors != "":
        output += "\n**Errors:**\n" + errors
    msg = await edit_or_reply(pandaevent, output)
    await event.client.reload(msg)


@pandaub.ilhammansiz_cmd(
    pattern="rmscmd(s)? ((.|\n)*)?",
    command=("rmscmd", plugin_category),
    info={
        "header": "To disable given cmds for sudo.",
        "flags": {
            "-all": "Will disable all enabled cmds for sudo users.",
            "-flag": "Will disable all flaged cmds like eval, exec...etc.",
            "-p": "Will disable all cmds from the given plugin names.",
        },
        "usage": [
            "{tr}rmscmd -all",
            "{tr}rmscmd -flag",
            "{tr}rmscmd -p <plugin names>",
            "{tr}rmscmd <commands>",
        ],
        "examples": [
            "{tr}rmscmd -p autoprofile botcontrols i.e, for multiple names use space between each name",
            "{tr}rmscmd ping alive i.e, for multiple commands use space between each name",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To disable cmds for sudo users."
    input_str = event.pattern_match.group(2)
    errors = ""
    sudocmds = sudo_enabled_cmds()
    if not input_str:
        return await edit_or_reply(
            event, "__Which command should I disable for sudo users . __"
        )
    input_str = input_str.split()
    if input_str[0] == "-all":
        pandaevent = await edit_or_reply(
            event, "__Disabling all enabled cmds for sudo....__"
        )
        flagcmds = sudocmds
    elif input_str[0] == "-flag":
        pandaevent = await edit_or_reply(
            event, "__Disabling all flagged cmds for sudo.....__"
        )
        flagcmds = (
            PLG_INFO["chain"]
            + PLG_INFO["autoprofile"]
            + PLG_INFO["evaluators"]
            + PLG_INFO["execmod"]
            + PLG_INFO["database"]
            + PLG_INFO["afk"]
            + PLG_INFO["lockchat"]
            + PLG_INFO["custom"]
            + PLG_INFO["carbon"]
            + PLG_INFO["corecmds"]
            + PLG_INFO["groupactions"]
            + PLG_INFO["sudo"]
            + PLG_INFO["transferchannel"]
            + ["climate"]
            + ["covid"]
        )
    elif input_str[0] == "-p":
        pandaevent = event
        input_str.remove("-p")
        flagcmds = []
        for plugin in input_str:
            if plugin not in PLG_INFO:
                errors += f"`{cmd}` __There is no such plugin in your PandaUserbot__.\n"
            else:
                flagcmds += PLG_INFO[plugin]
    else:
        pandaevent = event
        flagcmds = []
        for cmd in input_str:
            if cmd not in CMD_INFO:
                errors += (
                    f"`{cmd}` __There is no such command in your PandaUserbot__.\n"
                )
            elif cmd not in sudocmds:
                errors += f"`{cmd}` __Is already disabled for sudo users__.\n"
            else:
                flagcmds.append(cmd)
    count = 0
    for cmd in flagcmds:
        if SqL.set_key("sudo_enabled_cmds", cmd):
            count += 1
            SqL.set_key("sudo_enabled_cmds", cmd)
    result = f"__Successfully disabled __ `{count}` __ for PandaUserbot sudo.__\n"
    output = (
        result + "**Bot is reloading to apply the changes. Please wait for a minute**\n"
    )
    if errors != "":
        output += "\n**Errors:**\n" + errors
    msg = await edit_or_reply(pandaevent, output)
    await event.client.reload(msg)


@pandaub.ilhammansiz_cmd(
    pattern="vscmds( -d)?$",
    command=("vscmds", plugin_category),
    info={
        "header": "To show list of enabled cmds for sudo.",
        "description": "will show you the list of all enabled commands",
        "flags": {"-d": "To show disabled cmds instead of enabled cmds."},
        "usage": [
            "{tr}vscmds",
            "{tr}vscmds -d",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To show list of enabled cmds for sudo."
    input_str = event.pattern_match.group(1)
    sudocmds = sudo_enabled_cmds()
    clist = {}
    error = ""
    if not input_str:
        text = "**The list of sudo enabled commands are :**"
        result = "**SUDO ENABLED COMMANDS**"
        if len(sudocmds) > 0:
            for cmd in sudocmds:
                plugin = get_key(cmd)
                if plugin in clist:
                    clist[plugin].append(cmd)
                else:
                    clist[plugin] = [cmd]
        else:
            error += "__You haven't enabled any sudo cmd for sudo users.__"
        count = len(sudocmds)
    else:
        text = "**The list of sudo disabled commands are :**"
        result = "**SUDO DISABLED COMMANDS**"
        totalcmds = CMD_INFO.keys()
        cmdlist = list(set(totalcmds) - set(sudocmds))
        if cmdlist:
            for cmd in cmdlist:
                plugin = get_key(cmd)
                if plugin in clist:
                    clist[plugin].append(cmd)
                else:
                    clist[plugin] = [cmd]
        else:
            error += "__You have enabled every cmd as sudo for sudo users.__"
        count = len(cmdlist)
    if error != "":
        return await edit_delete(event, error, 10)
    pkeys = clist.keys()
    n_pkeys = [i for i in pkeys if i is not None]
    pkeys = sorted(n_pkeys)
    output = ""
    for plugin in pkeys:
        output += f"• {plugin}\n"
        for cmd in clist[plugin]:
            output += f"`{cmd}` "
        output += "\n\n"
    finalstr = (
        result
        + f"\n\n**SUDO TRIGGER: **`{Config.SUDO_COMMAND_HAND_LER}`\n**Commands:** {count}\n\n"
        + output
    )
    await edit_or_reply(event, finalstr, aslink=True, linktext=text)


pandaub.loop.create_task(_init())
