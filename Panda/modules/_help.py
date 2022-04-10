
from ..misc import pandacute, reply_id
from .. import BOT_USERNAME


@pandacute(pattern="inline")
async def _(event):
    reply_to_id = await reply_id(event)
    results = await event.client.inline_query(BOT_USERNAME, "helpmebot")
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    
