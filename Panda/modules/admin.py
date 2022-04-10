# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.


from asyncio import sleep

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import (
    ChatAdminRequiredError,
    UserAdminInvalidError,
    UserIdInvalidError,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)

from .. import BOTLOG, BOTLOG_CHATID
from .. import CMD_HANDLER as cmd
from .. import CMD_HELP, DEVS, owner
from ..events import register
from ..misc import (
    _format,
    edit_delete,
    edit_or_reply,
    get_user_from_event,
    pandacute,
    cute,
    media_type,
)
from ..misc.logger import logging

# =================== CONSTANT ===================
PP_TOO_SMOL = "**Gambar Terlalu Kecil**"
PP_ERROR = "**Gagal Memproses Gambar**"
NO_ADMIN = "**Gagal dikarenakan Bukan Admin :)**"
NO_PERM = "**Tidak Mempunyai Izin!**"
NO_SQL = "**Berjalan Pada Mode Non-SQL**"
CHAT_PP_CHANGED = "**Berhasil Mengubah Profil Grup**"
INVALID_MEDIA = "**Media Tidak Valid**"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================


@pandacute(pattern="setgpic( -s| -d)$")
async def set_group_photo(event):
    "For changing Group dp"
    flag = (event.pattern_match.group(1)).strip()
    if flag == "-s":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await edit_delete(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await edit_delete(event, CHAT_PP_CHANGED)
            except PhotoCropSizeSmallError:
                return await edit_delete(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await edit_delete(event, PP_ERROR)
            except Exception as e:
                return await edit_delete(event, f"**ERROR : **`{str(e)}`")
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await edit_delete(event, f"**ERROR : **`{e}`")
        await edit_delete(event, "**Foto Profil Grup Berhasil dihapus.**", 30)


@pandacute(pattern="promote(?:\s|$)([\s\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cpromote(?:\s|$)([\s\S]*)")
async def promote(event):
    new_rights = ChatAdminRights(
        add_admins=False,
        change_info=True,
        invite_users=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if not user:
        return
    eventman = await edit_or_reply(event, "`Promoting...`")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await eventman.edit(NO_PERM)
    await edit_delete(eventman, "`Promoted Successfully!`", 30)


@pandacute(pattern="demote(?:\s|$)([\s\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cdemote(?:\s|$)([\s\S]*)")
async def demote(event):
    "To demote a person in group"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    eventman = await edit_or_reply(event, "`Demoting...`")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
        manage_call=None,
    )
    rank = "admin"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await eventman.edit(NO_PERM)
    await edit_delete(eventman, "`Demoted Successfully!`", 30)


@pandacute(pattern="ban(?:\s|$)([\s\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cban(?:\s|$)([\s\S]*)")
async def ban(bon):
    hantu = await bon.client.get_me()
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_or_reply(bon, NO_ADMIN)

    user, reason = await get_user_from_event(bon)
    if not user:
        return
    pocong = await edit_or_reply(bon, "`Processing Banned...`")
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await edit_or_reply(bon, NO_PERM)
    if reason:
        await pocong.edit(
            r"\\**#Banned_User**//"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
            f"**User ID:** `{str(user.id)}`\n"
            f"**Reason:** `{reason}`",
        )
    else:
        await pocong.edit(
            f"\\\\**#Banned_User**//\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n**User ID:** `{user.id}`\n**Action:** `Banned User by {hantu.first_name}`",
        )


@pandacute(pattern="unban(?:\s|$)([\s\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cunban(?:\s|$)([\s\S]*)")
async def nothanos(unbon):
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(unbon, NO_ADMIN)
    pocong = await edit_or_reply(unbon, "`Processing...`")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await edit_delete(pocong, "`Unban Berhasil Dilakukan!`")
    except UserIdInvalidError:
        await edit_delete(pocong, "`Sepertinya Terjadi ERROR!`")


@pandacute(pattern="mute(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cmute(?: |$)(.*)")
async def spider(spdr):
    try:
        from ..modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        return await edit_or_reply(spdr, NO_SQL)
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_or_reply(spdr, NO_ADMIN)
    pocong = await edit_or_reply(spdr, "`Processing...`")
    user, reason = await get_user_from_event(spdr)
    if not user:
        return
    self_user = await spdr.client.get_me()
    if user.id == self_user.id:
        return await edit_or_reply(pocong, "**Tidak Bisa Membisukan Diri Sendiri..（>﹏<）**"
        )
    if user.id in DEVS:
        return await pocong.edit("**Gagal Mute, Dia Adalah Pembuat Saya 🤪**")
    await pocong.edit(
        r"\\**#Muted_User**//"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`\n"
        f"**Action:** `Mute by {owner}`",
    )
    if mute(spdr.chat_id, user.id) is False:
        return await edit_delete(pocong, "**ERROR:** `Pengguna Sudah Dibisukan.`")
    try:
        await spdr.client(EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))
        if reason:
            await pocong.edit(
                r"\\**#Mute_User**//"
                f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
                f"**User ID:** `{user.id}`\n"
                f"**Reason:** `{reason}`",
            )
        else:
            await pocong.edit(
                r"\\**#Mute_User**//"
                f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
                f"**User ID:** `{user.id}`\n"
                f"**Action:** `Mute by {owner}`",
            )
    except UserIdInvalidError:
        return await edit_delete(pocong, "**Terjadi ERROR!**")


@pandacute(pattern="unmute(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cunmute(?: |$)(.*)")
async def unmoot(unmot):
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(unmot, NO_ADMIN)
    try:
        from ..modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        return await unmot.edit(NO_SQL)
    pocong = await edit_or_reply(unmot, "`Processing...`")
    user = await get_user_from_event(unmot)
    user = user[0]
    if not user:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await edit_delete(unmot, "**ERROR! Pengguna Sudah Tidak Dibisukan.**")
    try:
        await unmot.client(EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
        await edit_delete(pocong, "**Berhasil Melakukan Unmute!**")
    except UserIdInvalidError:
        return await edit_delete(pocong, "**Terjadi ERROR!**")


@cute()
async def muter(moot):
    try:
        from ..modules.sql_helper.gmute_sql import is_gmuted
        from ..modules.sql_helper.spam_mute_sql import is_muted
    except AttributeError:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                await moot.client(
                    EditBannedRequest(moot.chat_id, moot.sender_id, rights)
                )
    for i in gmuted:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@pandacute(pattern="ungmute(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cungmute(?: |$)(.*)")
async def ungmoot(un_gmute):
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(un_gmute, NO_ADMIN)
    try:
        from ..modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        return await edit_delete(un_gmute, NO_SQL)
    pocong = await edit_or_reply(un_gmute, "`Processing...`")
    user = await get_user_from_event(un_gmute)
    user = user[0]
    if not user:
        return
    await pocong.edit("`Membuka Global Mute Pengguna...`")
    if ungmute(user.id) is False:
        await pocong.edit("**ERROR!** Pengguna Sedang Tidak Di Gmute.")
    else:
        await edit_delete(un_gmute, "**Berhasil! Pengguna Sudah Tidak Dibisukan**")


@pandacute(pattern="gmute(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cgmute(?: |$)(.*)")
async def gspider(gspdr):
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(gspdr, NO_ADMIN)
    try:
        from ..modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        return await gspdr.edit(NO_SQL)
    pocong = await edit_or_reply(gspdr, "`Processing...`")
    user, reason = await get_user_from_event(gspdr)
    if not user:
        return
    self_user = await gspdr.client.get_me()
    if user.id == self_user.id:
        return await pocong.edit("**Tidak Bisa Membisukan Diri Sendiri..（>﹏<）**")
    if user.id in DEVS:
        return await pocong.edit("**Gagal Global Mute, Dia Adalah Pembuat Saya 🤪**")
    await pocong.edit("**Berhasil Membisukan Pengguna!**")
    if gmute(user.id) is False:
        await edit_delete(gspdr, "**ERROR! Pengguna Sudah Dibisukan.**")
    elif reason:
        await pocong.edit(
            r"\\**#GMuted_User**//"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Reason:** `{reason}`",
        )
    else:
        await pocong.edit(
            r"\\**#GMuted_User**//"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Action:** `Global Muted by {owner}`",
        )


@pandacute(pattern="zombies(?: |$)(.*)")
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**Grup Bersih, Tidak Menemukan Akun Terhapus.**"
    if con != "clean":
        await show.edit("`Mencari Akun Depresi...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = (
                f"**Menemukan** `{del_u}` **Akun Terhapus Dalam Grup Ini,"
                "\nBersihkan Itu Menggunakan Perintah** `.zombies clean`"
            )
        return await show.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await show.edit("**Maaf Kamu Bukan Admin!**")
    await show.edit("`Menghapus Akun Terhapus...`")
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await show.edit("`Tidak Memiliki Izin Banned Dalam Grup Ini`")
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"**Membersihkan** `{del_u}` **Akun Terhapus**"
    if del_a > 0:
        del_status = (
            f"**Membersihkan** `{del_u}` **Akun Terhapus** "
            f"\n`{del_a}` **Akun Admin Yang Terhapus Tidak Dihapus.**"
        )
    await show.edit(del_status)
    await sleep(2)
    await show.delete()
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            "**#ZOMBIES**\n"
            f"**Membersihkan** `{del_u}` **Akun Terhapus!**"
            f"\n**GRUP:** {show.chat.title}(`{show.chat_id}`)",
        )


@pandacute(pattern="admins$")
async def get_admin(show):
    info = await show.client.get_entity(show.chat_id)
    title = info.title or "Grup Ini"
    mentions = f"<b>👤 Daftar Admin Grup {title}:</b> \n"
    try:
        async for user in show.client.iter_participants(
            show.chat_id, filter=ChannelParticipantsAdmins
        ):
            if not user.deleted:
                link = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
                mentions += f"\n🧞‍♂️ {link}"
            else:
                mentions += f"\n👽 Akun Terhapus <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += f" {str(err)}" + "\n"
    await show.edit(mentions, parse_mode="html")


@pandacute(pattern="pin( loud|$)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cpin( loud|$)")
async def pin(event):
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await edit_delete(event, "`Reply Pesan untuk Melakukan Pin.`", 30)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "`Pinned Successfully!`")


@pandacute(pattern="unpin( all|$)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cunpin( all|$)")
async def pin(event):
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        return await edit_delete(
            event,
            "**Reply ke Pesan untuk melepas Pin atau Gunakan** `.unpin all` **untuk melepas pin semua**",
            45,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "all":
            await event.client.unpin_message(event.chat_id)
        else:
            return await edit_delete(
                event,
                "**Reply ke Pesan untuk melepas pin atau gunakan** `.unpin all`",
                45,
            )
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "`Unpinned Successfully!`")


@pandacute(pattern="kick(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.ckick(?: |$)(.*)")
async def kick(usr):
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(usr, NO_ADMIN)
    user, reason = await get_user_from_event(usr)
    if not user:
        return await edit_delete(usr, "**Tidak Dapat Menemukan Pengguna.**")
    xxnx = await edit_or_reply(usr, "`Processing...`")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        return await edit_delete(usr, f"{NO_PREM}\n{e}")
    if reason:
        await xxnx.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Telah Dikick Dari Grup**\n**Alasan:** `{reason}`"
        )
    else:
        await xxnx.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Telah Dikick Dari Grup**",
        )


@pandacute(pattern=r"undlt( -u)?(?: |$)(\d*)?")
async def _iundlt(event):
    catevent = await edit_or_reply(event, "`Searching recent actions...`")
    flag = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        if lim > 15:
            lim = int(15)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(5)
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"**{lim} Pesan yang dihapus di grup ini:**"
    if not flag:
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n☞ __{msg.old.message}__ **Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
            else:
                deleted_msg += f"\n☞ __{_media_type}__ **Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
        await edit_or_reply(catevent, deleted_msg)
    else:
        main_msg = await edit_or_reply(catevent, deleted_msg)
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"{msg.old.message}\n**Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
                )
            else:
                await main_msg.reply(
                    f"{msg.old.message}\n**Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}",
                    file=msg.old.media,
                )


CMD_HELP.update(
    {
        "admin": f"**Plugin : **`admin`\
        \n\n  ➕  **Syntax :** `{cmd}promote <username/reply> <nama title (optional)>`\
        \n  ➕  **Function : **Mempromosikan member sebagai admin.\
        \n\n  ➕  **Syntax :** `{cmd}demote <username/balas ke pesan>`\
        \n  ➕  **Function : **Menurunkan admin sebagai member.\
        \n\n  ➕  **Syntax :** `{cmd}ban <username/balas ke pesan> <alasan (optional)>`\
        \n  ➕  **Function : **Membanned Pengguna dari grup.\
        \n\n  ➕  **Syntax :** `{cmd}unban <username/reply>`\
        \n  ➕  **Function : **Unbanned pengguna jadi bisa join grup lagi.\
        \n\n  ➕  **Syntax :** `{cmd}mute <username/reply> <alasan (optional)>`\
        \n  ➕  **Function : **Membisukan Seseorang Di Grup, Bisa Ke Admin Juga.\
        \n\n  ➕  **Syntax :** `{cmd}unmute <username/reply>`\
        \n  ➕  **Function : **Membuka bisu orang yang dibisukan.\
        \n  ➕  **Function : ** Membuka global mute orang yang dibisukan.\
        \n\n  ➕  **Syntax :** `{cmd}all`\
        \n  ➕  **Function : **Tag semua member dalam grup.\
        \n\n  ➕  **Syntax :** `{cmd}admins`\
        \n  ➕  **Function : **Melihat daftar admin di grup.\
        \n\n  ➕  **Syntax :** `{cmd}setgpic <flags> <balas ke gambar>`\
        \n  ➕  **Function : **Untuk mengubah foto profil grup atau menghapus gambar foto profil grup.\
        \n  ➕  **Flags :** `-s` = **Untuk mengubah foto grup** atau `-d` = **Untuk menghapus foto grup**\
    "
    }
)


CMD_HELP.update(
    {
        "pin": f"**Plugin : **`pin`\
        \n\n  ➕  **Syntax :** `{cmd}pin` <reply chat>\
        \n  ➕  **Function : **Untuk menyematkan pesan dalam grup.\
        \n\n  ➕  **Syntax :** `{cmd}pin loud` <reply chat>\
        \n  •  **Function : **Untuk menyematkan pesan dalam grup (tanpa notifikasi) / menyematkan secara diam diam.\
        \n\n  •  **Syntax :** `{cmd}unpin` <reply chat>\
        \n  •  **Function : **Untuk melepaskan pin pesan dalam grup.\
        \n\n  •  **Syntax :** `{cmd}unpin all`\
        \n  •  **Function : **Untuk melepaskan semua sematan pesan dalam grup.\
    "
    }
)


CMD_HELP.update(
    {
        "undelete": f"**Plugin : **`undelete`\
        \n\n  ➕  **Syntax :** `{cmd}undlt` <jumlah chat>\
        \n  ➕  **Function : **Untuk mendapatkan pesan yang dihapus baru-baru ini di grup\
        \n\n  ➕  **Syntax :** `{cmd}undlt -u` <jumlah chat>\
        \n  ➕  **Function : **Untuk mendapatkan pesan media yang dihapus baru-baru ini di grup \
        \n  ➕  **Flags :** `-u` = **Gunakan flags ini untuk mengunggah media.**\
        \n\n  ➕  **NOTE : Membutuhkan Hak admin Grup** \
    "
    }
)


CMD_HELP.update(
    {
        "gmute": f"**Plugin : **`gmute`\
        \n\n  ➕  **Syntax :** `{cmd}gmute` <username/reply> <alasan (optional)>\
        \n  ➕  **Function : **Untuk Membisukan Pengguna di semua grup yang kamu admin.\
        \n\n  ➕  **Syntax :** `{cmd}ungmute` <username/reply>\
        \n  ➕  **Function : **Untuk Membuka global mute Pengguna di semua grup yang kamu admin.\
    "
    }
)


CMD_HELP.update(
    {
        "zombies": f"**Plugin : **`zombies`\
        \n\n  ➕  **Syntax :** `{cmd}zombies`\
        \n  ➕  **Function : **Untuk mencari akun terhapus dalam grup\
        \n\n  ➕  **Syntax :** `{cmd}zombies clean`\
        \n  ➕  **Function : **untuk menghapus Akun Terhapus dari grup.\
    "
    }
)
