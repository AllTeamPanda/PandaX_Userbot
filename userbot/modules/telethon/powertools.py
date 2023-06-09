
# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz

import os
from time import sleep

from ... import PandaBot

from ..._misc.logger import logging
from ..._misc.managers import edit_or_reply
from ... import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP_NAME

LOGS = logging.getLogger(__name__)
plugin_category = "modules"
catub = PandaBot
HEROKU_APP = HEROKU_APP_NAME




@PandaBot.ilhammansiz_cmd(
    pattern="shutdown$",
    command=("shutdown", plugin_category),
    info={
        "header": "Shutdowns the bot !!",
        "description": "To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use @hk_heroku_bot",
        "usage": "{tr}shutdown",
    },
)
async def _(event):
    "Shutdowns the bot"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down")
    await edit_or_reply(event, "`Turning off bot now ...Manually turn me on later`")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        os._exit(143)


@PandaBot.ilhammansiz_cmd(
    pattern="sleep( [0-9]+)?$",
    command=("sleep", plugin_category),
    info={
        "header": "Userbot will stop working for the mentioned time.",
        "usage": "{tr}sleep <seconds>",
        "examples": "{tr}sleep 60",
    },
)
async def _(event):
    "To sleep the userbot"
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "Syntax: `.sleep time`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "You put the bot to sleep for " + str(counter) + " seconds",
        )
    event = await edit_or_reply(event, f"`ok, let me sleep for {counter} seconds`")
    sleep(counter)
    await event.edit("`OK, I'm awake now.`")


@PandaBot.ilhammansiz_cmd(
    pattern="notify (on|off)$",
    command=("notify", plugin_category),
    info={
        "header": "To update the your chat after restart or reload .",
        "description": "Will send the ping cmd as reply to the previous last msg of (restart/reload/update cmds).",
        "usage": [
            "{tr}notify <on/off>",
        ],
    },
)
async def set_pmlog(event):
    "To update the your chat after restart or reload ."
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "__Notify was already disabled__")
        delgvar("restartupdate")
        return await edit_or_reply(event, "__Notify was disabled successfully.__")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "__Notify was enabled successfully.__")
    await edit_delete(event, "__Notify was already enabled.__")
