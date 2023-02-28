from asyncio.exceptions import CancelledError

from ... import PandaBot

import logging
from . import edit_or_reply
from ... import *
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "modules"


@PandaBot.ilhammansiz_cmd(
    pattern="restart$",
    command=("restart", plugin_category),
    info={
        "header": "Restarts the bot !!",
        "usage": "{tr}restart",
    },
    disable_errors=True,
)
async def _(event):
    "Restarts the bot !!"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    sandy = await edit_or_reply(
        event,
        "Restarted. `.ping` me or `.help` to check if I am online, actually it takes 1-2 min for restarting",
    )
    try:
        ulist = gvarstatus("restart_update")
        for i in ulist:
            delgvar("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        addgvar("restart_update", [ilham.chat_id, ilham.id])
    except Exception as e:
        LOGS.error(e)
    try:
        await PandaBot.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)
