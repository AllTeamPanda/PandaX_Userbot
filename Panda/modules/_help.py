# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.

from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from .. import BOT_USERNAME
from .. import CMD_HANDLER as cmd
from .. import bot
from ..misc import edit_or_reply, pandacute, reply_id, Cutepanda
category = "help"

@Cutepanda(
    pattern="inline(?: |$)(.*)",
    command=("inline", category),
    help={
        "header": "Inline bot",
        "description": "Help via inline Bot",
        "usage": [
            "{tr}inline",
        ],
    },
)
async def _(event):
    reply_to_id = await reply_id(event)
    results = await event.client.inline_query(BOT_USERNAME, "help")
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    
