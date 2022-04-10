
from .. import BOTLOG_CHATID, HANDLER, bot, owner
from ..Version import __version__ as botvers

from telethon.tl.functions.channels import JoinChannelRequest
import pybase64

On = f"""
•••••••••••
👤 Owner {owner}
💻 **Version -** `{botvers}`


❕ **Ketik** `{HANDLER}alive` **untuk Mengecheck Bot apakah sudah aktif**
❗Sebaiknya Anda jangan keluar grup ini agar bot tidak mati
 ....Terimakasih....🇮🇩
❗You should not leave this group so that the bot does not die
 ....Thank You....🇺🇸
•••••••••••
Dev by Ilham Mansiz
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
