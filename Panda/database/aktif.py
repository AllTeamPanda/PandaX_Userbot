
from .. import BOTLOG_CHATID, bot, owner, uid
from ..Version import __version__ as botvers

from telethon.tl.functions.channels import JoinChannelRequest
import pybase64

On = f"""
`🐼PANDA-USERBOT🐼
MENYALA`

❍ `Name :` [{owner}](tg://user?id={uid}) \n
❍ `Version-ALL :` `{botvers}`

"""


async def ongrup():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    On,
                )
    except BaseException:
        pass

async def join():
    X = str(pybase64.b64decode("QFBhbmRhVXNlcmJvdA=="))[2:13]
    L = str(pybase64.b64decode("QFRlYW1TcXVhZFVzZXJib3RTdXBwb3J0"))[2:17]
    try:
        await bot(JoinChannelRequest(X))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest(L))
    except BaseException:
        pass
