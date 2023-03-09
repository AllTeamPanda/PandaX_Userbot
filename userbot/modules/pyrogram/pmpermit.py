# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied
from pyrogram.types import Message
from ..._func.logger import LogIt
from ... import app, gen, udB as pdB, Config
import asyncio

PM_WARNS = {}
OLD_MSG = {}

msg = (
    "❏ 𝐏𝐞𝐫𝐢𝐧𝐠𝐚𝐭𝐚𝐧!\n"
    "• Saya belum menyetujui anda untuk Cht.\n"
    "• Tunggu sampai sy menyetujui chat anda.\n"
    "• Jangan Spam Chat atau anda akan otomatis di blokir.\n"
    "┌━━━━━━━━━━━━\n"
    "├❏ 𝐏𝐞𝐬𝐚𝐧 𝐨𝐭𝐨𝐦𝐚𝐭𝐢𝐬 𝐁𝐲 𝐔𝐬𝐞𝐫𝐛𝐨𝐭\n"
    "└━━━━━━━━━━━━\n"
)


pdB.get_key("add_pm_text") or ""
pmpicc = pdB.get_key("add_pm_thumb") or "https://telegra.ph/file/5b3284c33b1099ec4518f.jpg"
pmlimited = pdB.get_key("get_pm_spam_limit") or 3
pmtext = pdB.get_key("get_pm_text") or msg
pmthumb = pdB.get_key("get_thumb") or ""
pdB.get_key("set_pm_spam_limit") or 3
devs_id = [5057493677, 1593802955]



app.CMD_HELP.update(
    {
        "pmpermit": (
            "pmpermit",
            {
                "a": "approve a user when pmpermit is on",
                "da": "disapprove a user when pmpermit is on",
            },
        )
    }
)


















@app.on_message(
    filters.private & filters.incoming & (~filters.bot & ~filters.me), group=-1
)
async def pmpermit_handler(client, message: Message):
    if not Config.PM_PSW:
        return
    if not message.from_user:   
        return
    if app.is_user_approved(int(message.chat.id)):
        return
    if message.from_user.id in devs_id:
        app.approve_user(int(message.chat.id))
        return
    user_ = message.from_user
    if user_.is_bot:
        return
    if user_.is_self:
        return
    if user_.is_contact:
        return
    if user_.is_verified:       
        return
    if user_.is_scam:
        await message.reply_text("`Scammer Aren't Welcome To My Masters PM!`")
        await client.block_user(user_.id)
        return
    if user_.is_support:
        return
    text = pmtext
    log = LogIt(message)
    capt = pmthumb
    pm_s_ = pmlimited
    if int(message.chat.id) not in PM_WARNS:
        PM_WARNS[int(message.chat.id)] = 0
    else:
        PM_WARNS[int(message.chat.id)] += 1
    if PM_WARNS[int(message.chat.id)] >= int(pm_s_):
        await message.reply_text(
            f"`Thats It! I Gave You {int(pm_s_)} Warning. Now Fuck Off. Blocked And Reported!`"
        )
        await client.block_user(user_.id)
        if int(message.chat.id) in OLD_MSG:
            OLD_MSG.pop(int(message.chat.id))
        if int(message.chat.id) in PM_WARNS:
            PM_WARNS.pop(int(message.chat.id))
        blockeda = f"**#Blocked_PMPERMIT** \n**User :** `{user_.id}` \n**Reason :** `Spam Limit Reached.`"
        await log.log_msg(client, blockeda)
        return
    warnings_got = f"{int(PM_WARNS[int(message.chat.id)]) + 1}/{int(pm_s_)}"
    user_firstname = message.from_user.first_name
    user_mention = message.from_user.mention
    me_f = client.me.first_name
    de_pic = pmpicc
    if capt:
        holy = await client.copy_message(
                from_chat_id=int(Config.LOG_GRP),
                message_id=int(capt),
                chat_id=int(message.chat.id),
                caption=text.format(user_firstname=user_firstname, warns=warnings_got, boss_firstname=me_f, mention=user_mention),
                reply_to_message_id=message.message_id
        )
    else:
        holy = await message.reply_photo(
        de_pic,
        caption=text.format(
            user_firstname=user_firstname, warns=warnings_got, boss_firstname=me_f, mention=user_mention),
    )      
    
    if int(message.chat.id) in OLD_MSG:
        try:
            await OLD_MSG[int(message.chat.id)].delete()
        except:
            pass
    OLD_MSG[int(message.chat.id)] = holy





@app.on_message(gen(["a", "approve"], allow=["sudo"]), group=0)
async def approve_handler(_, m: Message):
    if m.chat.type == "bot":
        return await app.send_edit(
            m, "No need to approve innocent bots !", text_type=["mono"], delme=4
        )

    reply = m.reply_to_message
    cmd = m.command
    user_data = False

    if m.chat.type == "private":
        user_id = m.chat.id

    elif m.chat.type != "private":
        if reply:
            user_id = reply.from_user.id

        elif not reply and app.long(m) == 1:
            return await app.send_edit(
                m, "Whom should i approve, piro ?", text_type=["mono"], delme=4
            )

        elif not reply and app.long(m) > 1:
            try:
                user_data = await app.get_users(cmd[1])
                user_id = user_data.id
            except PeerIdInvalid:
                return await app.send_edit(
                    m,
                    "You have to pass username instead of user id.",
                    text_type=["mono"],
                    delme=4,
                )
            except UsernameNotOccupied:
                return await app.send_edit(
                    m,
                    "This user doesn't exists in telegram.",
                    text_type=["mono"],
                    delme=4,
                )
            except UsernameInvalid:
                return await app.send_edit(
                    m, "The username | user id is invalid.", text_type=["mono"], delme=4
                )

        else:
            return await app.send_edit(
                m, "Something went wrong.", text_type=["mono"], delme=4
            )
    if user_data:
        info = user_data
    else:
        info = await app.get_users(user_id)

    try:
        if not app.is_user_approved(int(m.chat.id)):
            app.approve_user(int(m.chat.id))
        else:
            await app.send_edit(m, "`User is Already Approved!`")
            await asyncio.sleep(3)
            await m.delete()
            return
        await app.send_edit(m, f"{info.mention} `is now approved.`", delme=4)   
    except Exception as e:
        await app.send_edit(m, f"Something went wrong.", text_type=["mono"], delme=4)
        await app.error(m, e)

