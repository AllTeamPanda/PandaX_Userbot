
from pyrogram.errors import RPCError
from pyrogram.types import User

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot import pyrobot as app
from . import HELP


HELP(
    "whois",
)

infotext = (
    "**[{full_name}](tg://user?id={user_id})**\n"
    " > ID Pengguna: `{user_id}`\n"
    " > Nama Depan: `{first_name}`\n"
    " > Nama Belakang: `{last_name}`\n"
    " > Username: {username}\n"
    " > DC: {dc_id}\n"
    " > Status: {status}\n"
    " > Apakah Penipu: {scam}\n"
    " > Apakah Bot: {bot}\n"
    " > Apakah Premium : {premium}\n"
    " > Diverifikasi: {verifies}\n"
    " > Apakah Kontak: {contact}\n"
    " > Total Grup yang Sama: {common}"
)


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


@ilhammansiz_on_cmd(['whois', 'wh'],
               cmd_help={
                'help': 'Whois.',
                'example': '{ch}whois'})
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except RPCError:
            pass
    try:
        user = await app.get_users(get_user)
    except RPCError:
        await message.edit("Saya tidak tahu Pengguna itu.")
        return
    common = await app.get_common_chats(user.id)
    countpf = await app.get_chat_photos_count(user.id)
    async for pfp in app.get_chat_photos(user.id, 1):
        if pfp:
            await message.delete()
            await app.send_photo(
            message.chat.id,
            pfp.file_id,
            caption=infotext.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name or "",
                username=user.username or "",
                dc_id=user.dc_id or "1",
                status=user.status or "None",
                premium=user.is_premium,
                scam=user.is_scam,
                bot=user.is_bot,
                verifies=user.is_verified,
                contact=user.is_contact,
                common=len(common),
                fotouser=countpf or "None",
            ),
            reply_to_message_id=message.reply_to_message.id
            if message.reply_to_message
            else None,
            )
        else:
            await message.edit(
            infotext.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name or "",
                username=user.username or "",
                dc_id=user.dc_id or "1",
                status=user.status or "None",
                premium=user.is_premium,
                scam=user.is_scam,
                bot=user.is_bot,
                verifies=user.is_verified,
                contact=user.is_contact,
                common=len(common),
                ),
                disable_web_page_preview=True)


@ilhammansiz_on_cmd(['id', 'id'],
               cmd_help={
                'help': 'id',
                'example': '{ch}id'})
async def id(client, message):
    cmd = message.command
    chat_id = message.chat.id
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except RPCError:
            pass
    try:
        user = await client.get_users(get_user)
    except RPCError:
        await message.edit("Tidak menemukan user tersebut.")
        return
    text = "**User ID**: `{}`\n**Chat ID**: `{}`".format(user.id, chat_id)
    await message.edit(text)

@ilhammansiz_on_cmd(['grab', 'gr'],
               cmd_help={
                'help': 'Grab.',
                'example': '{ch}grab'})
async def grab(client, message):
    Panda = await message.edit("Processing")
    if not message.reply_to_message:
        return await message.edit("Tolong balas ke pengguna")
    elif message.reply_to_message:
        chat = message.chat.id
        get_user = message.reply_to_message.from_user.id
        user = await client.get_users(get_user)
        async for photo in app.get_chat_photos(user.id, limit=100): 
            await app.send_photo(chat, photo.file_id)
            await Panda.delete()
    else:
        await Panda.edit("Sepertinya ada yang salah")
        return
