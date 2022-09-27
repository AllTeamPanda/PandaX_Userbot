
import base64
from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import get_arg

from . import HELP


HELP(
    "base64",
)



@ilhammansiz_on_cmd(['en', 'encode'],
               cmd_help={
                'help': 'Base64.',
                'example': '{ch}en Mengkodekan textbase64'})
async def encode(client, message):
    ppk = get_arg(message)
    message.chat.id
    if not ppk:
        return await message.edit_text("`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await message.edit_text(
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@ilhammansiz_on_cmd(['de', 'de'],
               cmd_help={
                'help': 'Base64.',
                'example': '{ch}de Membuka textbase64'})
async def decode(client, message):
    ppk = get_arg(message)
    message.chat.id
    if not ppk:
        return await message.edit_text("`Give me Something to Decode..`")
    byt = ppk.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await message.edit_text(
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await message.edit_text("**ERROR :** " + str(p))
