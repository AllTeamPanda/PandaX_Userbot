import math
import os

import aiohttp
import urllib3
from Panda.sql_helper.globals import addgvar, delgvar, gvarstatus
from . import edit_delete, edit_or_reply, pandaub




@pandaub.ilhammansiz_cmd(
    pattern="getdb$",
    command=("getdb", plugin_category),
    info={
        "header": "Get Database",
        "usage": "{tr}getdb",
    },
)
async def getsql(event):
    var_ = event.pattern_match.group(1).upper()
    xxnx = await edit_or_reply(event, f"**Getting variable** `{var_}`")
    if var_ == "":
        return await xxnx.edit(
            f"**Invalid Syntax !!** \n\nKetik `{cmd}getdb NAMA_VARIABLE`"
        )
    try:
        sql_v = gvarstatus(var_)
        os_v = os.environ.get(var_) or "None"
    except Exception as e:
        return await xxnx.edit(f"**ERROR !!**\n\n`{e}`")
    await xxnx.edit(
        f"**OS VARIABLE:** `{var_}`\n**OS VALUE :** `{os_v}`\n------------------\n**SQL VARIABLE:** `{var_}`\n**SQL VALUE :** `{sql_v}`\n"
    )


@pandaub.ilhammansiz_cmd(
    pattern="setdb$",
    command=("setdb", plugin_category),
    info={
        "header": "set Database",
        "usage": "{tr}setdb",
    },
)
async def setsql(event):
    hel_ = event.pattern_match.group(1)
    var_ = hel_.split(" ")[0].upper()
    val_ = hel_.split(" ")[1:]
    valu = " ".join(val_)
    xxnx = await edit_or_reply(event, f"**Setting variable** `{var_}` **as** `{valu}`")
    if "" in (var_, valu):
        return await xxnx.edit(
            f"**Invalid Syntax !!**\n\n**Ketik** `{cmd}setsql VARIABLE_NAME value`"
        )
    try:
        addgvar(var_, valu)
    except Exception as e:
        return await xxnx.edit(f"**ERROR !!** \n\n`{e}`")
    await xxnx.edit(f"**Variable** `{var_}` **successfully added with value** `{valu}`")


@pandaub.ilhammansiz_cmd(
    pattern="deldb$",
    command=("deldb", plugin_category),
    info={
        "header": "Get Database",
        "usage": "{tr}deldb",
    },
)
async def delsql(event):
    var_ = event.pattern_match.group(1).upper()
    xxnx = await edit_or_reply(event, f"**Deleting Variable** `{var_}`")
    if var_ == "":
        return await xxnx.edit(
            f"**Invalid Syntax !!**\n\n**Ketik** `{cmd}delsql VARIABLE_NAME`"
        )
    try:
        delgvar(var_)
    except Exception as e:
        return await xxnx.edit(f"**ERROR !!**\n\n`{e}`")
    await xxnx.edit(f"**Deleted Variable** `{var_}`")
