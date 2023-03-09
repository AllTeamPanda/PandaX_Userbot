# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


from userbot._func.decorators import listen
from pyrogram import filters
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


















@listen(filters.incoming & filters.private & ~filters.edited & ~filters.me & ~filters.service)
async def pmPermit(client, message):
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
async def approve_handler(client, message: Message):
    if not Config.PM_PSW:
        await app.send_edit(message, "`Pm Permit Is Disabled. Whats The Use Of Approving User?`")
        return
    if message.chat.type == "private":
        if int(message.chat.id) in OLD_MSG:
            await OLD_MSG[int(message.chat.id)].delete()
        user_ = await client.get_users(int(message.chat.id))
        firstname = user_.first_name
        if not app.is_user_approved(int(message.chat.id)):
            app.approve_user(int(message.chat.id))
        else:
            await message.edit("`User is Already Approved!`")
            await asyncio.sleep(3)
            await message.delete()
            return
        await message.edit(
            "Approved to pm [{}](tg://user?id={})".format(
                firstname, int(message.chat.id)
            )
        )
        await asyncio.sleep(3)
        await message.delete()
    elif message.chat.type == "supergroup":
        if not message.reply_to_message:
            await message.edit("`Reply To User To Approve Him !`")
            return
        user_ = await client.get_users(message.reply_to_message.from_user.id)
        firstname = user_.first_name
        if not app.is_user_approved(message.reply_to_message.from_user.id):
            app.approve_user(message.reply_to_message.from_user.id)
        else:
            await message.edit("`User is Already Approved!`")
            await asyncio.sleep(3)
            await message.delete()
            return
        await message.edit(
            "Approved to pm [{}](tg://user?id={})".format(
                firstname, message.reply_to_message.from_user.id
            )
        )
        await asyncio.sleep(3)
        await message.delete()
