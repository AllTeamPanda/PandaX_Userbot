
# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



from pyrogram.types import Message
from pyrogram.types import Chat

import asyncio
import math
import os
import shlex
import time
from math import ceil
from traceback import format_exc
from typing import Tuple
from os import remove

from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from ..Session.pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4
from ..Var import Config

import mimetypes

DEVLIST = [5057493677, 1593802955] 

def guess_mime_type(file_):
    """Get Mime Type Of A File From Url / Path"""
    s = mimetypes.guess_type(file_)
    if not s[0]:
        return None
    else:
        return s[0]



def extract_args(message, markdown=True):
    if not (message.text or message.caption):
        return ''

    text = message.text or message.caption

    text = text.markdown if markdown else text
    if ' ' not in text:
        return ''

    text = sub(r'\s+', ' ', text)
    text = text[text.find(' ') :].strip()
    return text


def extract_args_arr(message, markdown=True):
    return extract_args(message, markdown).split()

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def forward(message, chat_id):
    try:
        return message.forward(chat_id or 'me')
    except Exception as e:
        raise e


def get_messages(chat_id, msg_ids=None, client=pyrobot):
    try:
        ret = client.get_messages(chat_id=(chat_id or 'me'), message_ids=msg_ids)
        return [ret] if ret and isinstance(ret, Message) else ret
    except BaseException:
        return []


MARKDOWN_FIX_CHAR = '\u2064'

def send(client, chat, text, fix_markdown=False, reply_id=None):
    if fix_markdown:
        text += MARKDOWN_FIX_CHAR

    if len(text) < 4096:
        if not reply_id:
            client.send_message(chat.id if isinstance(chat, Chat) else chat, text)
        else:
            client.send_message(
                chat.id if isinstance(chat, Chat) else chat,
                text,
                reply_to_message_id=reply_id,
            )
        return

    file = open('temp.txt', 'w+')
    file.write(text)
    file.close()
    send_doc(client, chat, 'temp.txt')


def send_sticker(client, chat, sticker):
    try:
        client.send_sticker(chat.id if isinstance(chat, Chat) else chat, sticker)
    except BaseException:
        pass


def send_doc(client, chat, doc, caption='', fix_markdown=False):
    try:
        if len(caption) > 0 and fix_markdown:
            caption += MARKDOWN_FIX_CHAR
        client.send_document(
            chat.id if isinstance(chat, Chat) else chat, doc, caption=caption
        )
    except BaseException:
        pass

def send_log(text, fix_markdown=False):
    send(pyrobot, Config.LOG_GRP or 'me', text, fix_markdown=fix_markdown)


def send_log_doc(doc, caption='', fix_markdown=False, remove_file=False):
    send_doc(app, LOG_ID or 'me', doc, caption=caption, fix_markdown=fix_markdown)
    if remove_file:
        remove(doc)


def reply_msg(message: Message, message2: Message, delete_orig=False):
    try:
        message2.copy(chat_id=message.chat.id, reply_to_message_id=message.id)

        if delete_orig:
            message.delete()
    except Exception as e:
        raise e

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def edit_or_reply(message, text, parse_mode="md"):
    """Edit Message If Its From Self, Else Reply To Message, (Only Works For Sudo's)"""
    if not message:
        return await message.edit(text, parse_mode=parse_mode)
    if not message.from_user:
        return await message.edit(text, parse_mode=parse_mode)
    if message.from_user.id in Config.AFS:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)


async def is_admin_or_owner(message, user_id) -> bool:
    """Check If A User Is Creator Or Admin Of The Current Group"""
    if message.chat.type in ["private", "bot"]:
        # You Are Boss Of Pvt Chats.
        return True
    user_s = await message.chat.get_member(int(user_id))
    if user_s.status in ("creator", "administrator"):
        return True
    return False


def get_readable_time(seconds: int) -> int:
    """Get Time So That Human Can ReadIt"""
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


async def get_all_pros() -> list:
    """Get All Users , Sudo + Owners + Other Clients"""
    users = list(Config.SUDO_USERS)
    if pyrobot:
        ujwal = await pyrobot.get_me()
        users.append(ujwal.id)
    if pyrobot2:
        ujwal2 = await pyrobot2.get_me()
        users.append(ujwal2.id)
    if pyrobot3:
        ujwal3 = await pyrobot3.get_me()
        users.append(ujwal3.id)
    if pyrobot4:
        ujwal4 = await pyrobot3.get_me()
        users.append(ujwal4.id)
    return users


def paginate_help(page_number, loaded_modules, prefix, is_official=True):
    """Paginate Buttons"""
    number_of_rows = 6
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        InlineKeyboardButton(
            text="{} {} {}".format(
                Config.CUSTOM_HELP_EMOJI, x, Config.CUSTOM_HELP_EMOJI
            ),
            callback_data="us_plugin_{}|{}_{}".format(x, page_number, is_official),
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                InlineKeyboardButton(
                    text="⏪ Previous",
                    callback_data="{}_prev({})_{}".format(prefix, modulo_page, is_official),
                ),
                InlineKeyboardButton(text="Menu Utama", callback_data="backO_to_help_menu"),
                InlineKeyboardButton(
                    text="Next ⏩",
                    callback_data="{}_next({})_{}".format(prefix, modulo_page, is_official),
                ),
            )
        ]
    return pairs


def cb_wrapper(func):
    async def wrapper(client, cb):
        users = await get_all_pros()
        if cb.from_user.id not in users:
            await cb.answer(
                "Kamu tidak bisa mengakses Bot ini Deploy sendiri join @PandaUserbot ",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(client, cb)
            except MessageNotModified:
                await cb.answer("🤔🧐")
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"Tidak dapat Menginstal module silahkan Check Logs!",
                    cache_time=0,
                    show_alert=True,
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(client, inline_query):
        users = await get_all_pros()
        if inline_query.from_user.id not in users:
            await client.answer_inline_query(
                inline_query.id,
                cache_time=1,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="Sorry, Friend You Can't Use Me!",
                            input_message_content=InputTextMessageContent(
                                "Kamu tidak bisa mengakses Bot ini Deploy sendiri join @PandaUserbot"
                            ),
                        )
                    )
                ],
            )
        else:
            await func(client, inline_query)

    return wrapper


async def delete_or_pass(message):
    """Delete Message If Its From Self Else Just Pass"""
    if message.from_user.id in Config.AFS:
        return message
    return await message.delete()

def run_in_exc(f):
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(exc_, lambda: f(*args, **kwargs))
    return wrapper

def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Time Formatter"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    """Progress Bar For Showing Progress While Uploading / Downloading File - Normal"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


async def cb_progress(current, total, cb, start, type_of_ps, file_name=None):
    """Progress Bar For Showing Progress While Uploading / Downloading File - Inline"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await cb.edit_message_text(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit_message_text("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)


async def iter_chats(client):
    """Iter Your All Chats"""
    chats = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats


async def fetch_audio(client, message):
    """Fetch Audio From Videos Or Audio Itself"""
    c_time = time.time()
    if not message.reply_to_message:
        await message.edit("`Reply To A Video / Audio.`")
        return
    warner_stark = message.reply_to_message
    if warner_stark.audio is None and warner_stark.video is None:
        await message.edit("`Format Not Supported`")
        return
    if warner_stark.video:
        await message.edit("`Video Detected, Converting To Audio !`")
        warner_bros = await message.reply_to_message.download(
            progress=progress, progress_args=(message, c_time, f"`Downloading Audio!`")
        )
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a petercord.mp3"
        await runcmd(stark_cmd)
        final_warner = "panda.mp3"
    elif warner_stark.audio:
        await message.edit("`Download Started !`")
        final_warner = await message.reply_to_message.download(
            progress=progress, progress_args=(message, c_time, f"`Downloading Video!`")
        )
    await message.edit("`Almost Done!`")
    return final_warner
