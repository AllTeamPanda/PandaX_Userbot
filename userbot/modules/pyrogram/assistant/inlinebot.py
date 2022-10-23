# ilham mansiz
# Panda Userbott
# Ported by ilham from Friday Userbot

import logging
import re
import string
from random import choice
import sys
from os import environ, execle
import platform
import re
import socket
import uuid
import psutil
from pyrogram import __version__
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
import requests
from pyrogram import __version__, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
from tinydb import Query, TinyDB
from userbot._func.startup import run_cmd
from userbot import pyrobot, pandaversion, CMD_HELP, pyrotgbot as bot, XTRA_CMD_LIST, CMD_LIST
from userbot import Config
from youtubesearchpython import SearchVideos
from userbot._func._helpers import (
    humanbytes,
    cb_wrapper,
    get_all_pros,
    paginate_help,
)
import os

import platform
import re
import socket
import sys
import uuid
from os import environ, execle

import psutil
from userbot._func.assistant_helpers import download_yt
from pyrogram.types import InputMediaAudio, InputMediaVideo

ilhammansiz = "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
Petercord_Userbot = pyrobot
db_m = TinyDB("./userbot/resources/secret.json")
db_s = TinyDB("./userbot/resources/not4u.json")

Petercord_version = pandaversion
REPO_ = Config.UPSTREAM_REPO
BRANCH_ = Config.U_BRANCH


@bot.on_inline_query()
async def owo(client, inline_query):
    string_given = inline_query.query.lower()
    if string_given.startswith("not4u"):
        if not ";" in string_given:
            return
        ok = string_given.split(" ", maxsplit=1)[1]
        user, msg = ok.split(";")
        fu = int(user) if user.isdigit() else user
        try:
            ui = await pyrobot.get_users(fu)
        except BaseException as e:
            logging.error(str(e))
            return
        owo = (
            f"@{ui.username}"
            if ui.username
            else f"[{ui.first_name}](tg://user?id={ui.id})"
        )
        chars = string.hexdigits
        randomc = "".join(choice(chars) for _ in range(4))
        stark_data = {"secret_code": randomc, "id": ui.id, "msg": msg}
        db_s.insert(stark_data)
        texts = f"Everyone Except {owo} Can Read This Message. \nClick Below To Check Message! \n**Note :** `Only He/She Can't Open It!`"
        ok_s = [
            (
                results.append(
                    title="OwO! Not For You",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Show Message !", callback_data=f"nu_{randomc}"
                                )
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(texts),
                )
            )
        ]
        await client.answer_inline_query(inline_query.id, cache_time=0, results=ok_s)
    elif string_given.startswith("yt"):
        results = []
        try:
            input = string_given.split(" ", maxsplit=1)[1]
        except:
            return
        search = SearchVideos(str(input), offset=1, mode="dict", max_results=50)
        rt = search.result()
        result_s = rt["search_result"]
        for i in result_s:
            url = i["link"]
            vid_title = i["title"]
            yt_id = i["id"]
            uploade_r = i["channel"]
            views = i["views"]
            thumb = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
            capt = f"""
**Video Title :** `{vid_title}`
**Link :** `{url}`
**Uploader :** `{uploade_r}`
**Views :** `{views}`
            """
            results.append(
                InlineQueryResultPhoto(
                    photo_url=thumb,
                    title=vid_title,
                    caption=capt,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Download - Audio",
                                    callback_data=f"ytdl_{url}_audio"
                                ),
                                InlineKeyboardButton(
                                    text="Download - Video",
                                    callback_data=f"ytdl_{url}_video"
                                )
                            ]
                        ]
                    ),
                )
            )
        await client.answer_inline_query(inline_query.id, cache_time=0, results=results)
    elif string_given.startswith("git"):
        try:
            input_ = string_given.split(" ", maxsplit=1)[1]
        except:
            return
        results = []
        r = requests.get("https://api.github.com/search/repositories", params={"q": input_})
        lool = r.json()
        if lool.get("total_count") == 0:
            return
        lol = lool.get("items")
        for X in lol:
            qw = X
            txt = f"""
<b>Name :</b> <i>{qw.get("name")}</i>
<b>Full Name :</b> <i>{qw.get("full_name")}</i>
<b>Link :</b> {qw.get("html_url")}
<b>Fork Count :</b> <i>{qw.get("forks_count")}</i>
<b>Open Issues :</b> <i>{qw.get("open_issues")}</i>
"""
            if qw.get("description"):
                txt += f'\n<b>Description :</b> <code>{qw.get("description")}</code>'
            if qw.get("language"):
                txt += f'\n<b>Language :</b> <code>{qw.get("language")}</code>'
            if qw.get("size"):
                txt += f'\n<b>Size :</b> <code>{qw.get("size")}</code>'
            if qw.get("score"):
                txt += f'\n<b>Score :</b> <code>{qw.get("score")}</code>'
            if qw.get("created_at"):
                txt += f'\n<b>Created At :</b> <code>{qw.get("created_at")}</code>'
            if qw.get("archived") == True:
                txt += f"\n<b>This Project is Archived</b>"

            results.append(
                InlineQueryResultArticle(
                   thumb_url="https://simpleicons.org/icons/github.svg",
                   url=qw.get("html_url"),
                   description=qw.get("description", "No Description"),
                   title = qw.get("name"),
                   input_message_content=InputTextMessageContent(txt, disable_web_page_preview=True)
                )
             )
        await client.answer_inline_query(inline_query.id, cache_time=0, results=results)
    elif string_given.startswith("whisper"):
        if not ";" in string_given:
            return
        ok = string_given.split(" ", maxsplit=1)[1]
        user, msg = ok.split(";")
        fu = int(user) if user.isdigit() else user
        try:
            ui = await pyrobot.get_users(fu)
        except BaseException as e:
            logging.error(str(e))
            return
        owo = (
            f"@{ui.username}"
            if ui.username
            else f"[{ui.first_name}](tg://user?id={ui.id})"
        )
        chars = string.hexdigits
        randomc = "".join(choice(chars) for _ in range(4))
        stark_data = {"secret_code": randomc, "id": ui.id, "msg": msg}
        db_m.insert(stark_data)
        texts = f"A Whisper Has Been Sent For {owo} . \nClick Below To Check Message! \n**Note :** `Only He/She Can Open It!`"
        ok_s = [
            (
                InlineQueryResultArticle(
                    title="Ssh! This is A Secret Message",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Show Message !", callback_data=f"sc_{randomc}"
                                )
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(texts),
                )
            )
        ]
        await client.answer_inline_query(inline_query.id, cache_time=0, results=ok_s)
    elif string_given.startswith("pmpandauserbot"):
        msg = (
              "❏ 𝐏𝐞𝐫𝐢𝐧𝐠𝐚𝐭𝐚𝐧!\n"
              "• Saya belum menyetujui anda untuk Cht.\n"
              "• Tunggu sampai sy menyetujui chat anda.\n"
              "• Jangan Spam Chat atau anda akan otomatis di blokir.\n"
              "┌━━━━━━━━━━━━\n"
              "├❏ 𝐏𝐞𝐬𝐚𝐧 𝐨𝐭𝐨𝐦𝐚𝐭𝐢𝐬 𝐁𝐲 𝐔𝐬𝐞𝐫𝐛𝐨𝐭\n"
              "└━━━━━━━━━━━━\n")
        bttn = [
            [
                InlineKeyboardButton(
                    text="☑️Terima☑️", callback_data=f"terimapm"
                )
            ],
            [
             InlineKeyboardButton(
                    text="❌Tolak❌", callback_data=f"tolakpm"
                )
            ],
        ]
       
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="Help Article!",
                        reply_markup=InlineKeyboardMarkup(bttn),
                        input_message_content=InputTextMessageContent(msg),
                    )
                )
            ],
        )
    elif string_given.startswith("help"):
        total_ = len(CMD_HELP)
        bttn = [
            [
                InlineKeyboardButton(
                    text="✅ Daftar Perintah ✅", callback_data=f"make_cmd_buttons"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔃 System 🔃", callback_data=f"make_ilham_bot"
                )
            ],
            [
             InlineKeyboardButton(
                    text="🚫 Close 🚫", callback_data=f"cleuse"
                )
            ],
        ]
        if Config.LOAD_UNOFFICIAL_PLUGINS:
            total_ = len(CMD_HELP)
        nice_text = f"**PandaUserbot Inline** \n\n**Version :** `{pandaversion}` \n**Pyrogram Version :** `{__version__}` \n**Modules :** {total_}"
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="Help Article!",
                        reply_markup=InlineKeyboardMarkup(bttn),
                        input_message_content=InputTextMessageContent(nice_text),
                    )
                )
            ],
        )

@bot.on_callback_query(filters.regex(pattern="ytdl_(.*)_(video|audio)"))
async def yt_dl_video(client, cb):
    url = cb.matches[0].group(1)
    audio_or_video = cb.matches[0].group(2)
    if audio_or_video == "video":
        file_name, downloaded_thumb, name, dur, u_date, uploader, views = await download_yt(url, as_video=True)
    else:
        file_name, downloaded_thumb, name, dur, u_date, uploader, views = await download_yt(url, as_video=False)
    if not os.path.exists(file_name):
        await cb.edit_message_text(file_name)
        return
    await cb.edit_message_text(f"`Downloaded : {name} | Now Uploading....`")
    import datetime
    f_size = humanbytes(os.stat(file_name).st_size)
    caption = f"""
**Title :** `{name}`
**Uploader :** `{uploader}`
**Views :** `{views}`
**Link :** `{url}`
**Duration :** `{datetime.timedelta(seconds=dur)}`
**File Size :** `{f_size}`
"""
    if audio_or_video == "video":
        file_ = InputMediaVideo(file_name, thumb=downloaded_thumb, supports_streaming=True, duration=dur, caption=caption)
    else:
        file_ = InputMediaAudio(file_name, performer=uploader, title=name, thumb=downloaded_thumb, duration=dur, caption=caption)
    await cb.edit_message_media(file_)
    if os.path.exists(file_name):
        os.remove(file_name)

@bot.on_callback_query(filters.regex(pattern="sc_(.*)"))
async def no_horny(client, cb):
    o = await get_all_pros()
    data_m = cb.matches[0].group(1)
    stark_moment = Query()
    sstark = db_m.search(stark_moment.secret_code == data_m)
    if sstark == []:
        await cb.answer(
            "OwO, It Seems Message Has Been Deleted From Server :(",
            cache_time=0,
            show_alert=True,
        )
        return
    id_s = sstark[0]["id"]
    o.append(int(id_s))
    if cb.from_user.id not in o:
        await cb.answer(
            "This Message Is Not For You, OwO ! Btw, This is A Bomb Making Secret.!",
            cache_time=0,
            show_alert=True,
        )
        return
    await cb.answer(sstark[0]["msg"], cache_time=0, show_alert=True)


@bot.on_callback_query(filters.regex(pattern="nu_(.*)"))
async def nothing_here(client, cb):
    data_m = cb.matches[0].group(1)
    stark_moment = Query()
    sstark = db_s.search(stark_moment.secret_code == data_m)
    if sstark == []:
        await cb.answer(
            "OwO, It Seems Message Has Been Deleted From Server :(",
            cache_time=0,
            show_alert=True,
        )
        return
    id_s = sstark[0]["id"]
    if cb.from_user.id == int(id_s):
        await cb.answer(
            "Everyone Except You Can Read This Message. Hehe!",
            cache_time=0,
            show_alert=True,
        )
        return
    await cb.answer(sstark[0]["msg"], cache_time=0, show_alert=True)
    

@bot.on_callback_query(filters.regex(pattern="make_ilham_bot"))
@cb_wrapper
async def cmd_buutton(client, cb):
    bttn = [
            [
                InlineKeyboardButton(
                    text="♻ Update Now ♻", callback_data=f"updTe_bot"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📳 Restart Now 📳", callback_data=f"restart_bot"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Back 🔙", callback_data=f"backO_to_help_menu"
                )
            ]
        ]
    await cb.edit_message_text("🎗 Data PandaUserbot 🎗", reply_markup=InlineKeyboardMarkup(bttn))

@bot.on_callback_query(filters.regex(pattern="backO_to_help_menu"))
@cb_wrapper
async def black_menu(client, cb):
    total_ = len(CMD_HELP)
    bttn = [
            [
                InlineKeyboardButton(
                    text="✅ Daftar Perintah ✅", callback_data=f"make_cmd_buttons"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎗 Data PandaUserbot 🎗", callback_data=f"make_ilham_bot"
                )
            ],
            [
             InlineKeyboardButton(
                    text="🚫 Close 🚫", callback_data=f"cleuse"
                )
            ],
        ]
    if Config.LOAD_UNOFFICIAL_PLUGINS:
        total_ = len(CMD_HELP)
    nice_text = f"**PandaUserbot Inline** \n\n**Version :** `{pandaversion}` \n**Pyrogram Version :** `{__version__}` \n**Modules :** {total_}"
    await cb.edit_message_text(nice_text, reply_markup=InlineKeyboardMarkup(bttn))

@bot.on_callback_query(filters.regex(pattern="make_cmd_buttons"))
@cb_wrapper
async def cmd_buutton(client, cb):
    bttn = [
            [
                InlineKeyboardButton(
                    text="📙 Modules 📙", callback_data=f"make_basic_button_True"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Back 🔙", callback_data=f"backO_to_help_menu"
                )
            ]
        ]
    if Config.LOAD_UNOFFICIAL_PLUGINS:
        len(CMD_HELP)
        bttn = [
                [
                    InlineKeyboardButton(
                        text="📙 Modules 📙",
                        callback_data=f"make_basic_button_True",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Back 🔙", callback_data=f"backO_to_help_menu"
                    )
                ]
            ]
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(bttn))

@bot.on_callback_query(filters.regex(pattern="restart_bot"))
@cb_wrapper
async def roaststart(client, cb):
    bttn = [
        [
                InlineKeyboardButton(
                    text="Back 🔙", callback_data=f"backO_to_help_menu"
                )
            ]
    ]
    await cb.edit_message_text("`Please Wait, Restarting... This May Take A While`", reply_markup=InlineKeyboardMarkup(bttn))
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    exit()

@bot.on_callback_query(filters.regex(pattern="updTe_bot"))
@cb_wrapper
async def update_it(client, cb):
    bttn = [
        [
                InlineKeyboardButton(
                    text="Back 🔙", callback_data=f"backO_to_help_menu"
                )
            ]
    ]
    await cb.edit_message_text("`Updating Please Wait!`", reply_markup=InlineKeyboardMarkup(bttn))
    try:
        repo = Repo()
    except GitCommandError:
        return await cb.edit_message_text(
            "`Invalid Git Command. Please Report This Bug To @PandaUserbot`",
            reply_markup=InlineKeyboardMarkup(bttn)
        )
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(Config.U_BRANCH, origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    if repo.active_branch.name != Config.U_BRANCH:
        return await cb.edit_message_text(
            f"`Seems Like You Are Using Custom Branch - {repo.active_branch.name}! Please Switch To {Config.U_BRANCH} To Make This Updater Function!`", reply_markup=InlineKeyboardMarkup(bttn))
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(Config.U_BRANCH)
    if not Config.HEROKU_URL:
        try:
            ups_rem.pull(Config.U_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
        await cb.edit_message_text("`Updated Sucessfully! Give Me A min To Restart!`", reply_markup=InlineKeyboardMarkup(bttn))
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        exit()
        return
    else:
        await cb.edit_message_text("`Heroku Detected! Pushing, Please Halt!`", reply_markup=InlineKeyboardMarkup(bttn))
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(Config.HEROKU_URL)
        else:
            remote = repo.create_remote("heroku", Config.HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except BaseException as error:
            return await cb.edit_message_text(f"**Updater Error** \nTraceBack : `{error}`", reply_markup=InlineKeyboardMarkup(bttn))

@bot.on_callback_query(filters.regex(pattern="sys_info"))
@cb_wrapper
async def fuck_arch_btw(client, cb):
    bttn = [
        [
                InlineKeyboardButton(
                    text="Back 🔙", callback_data=f"backO_to_help_menu"
                )
            ]
    ]
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    neat_msg = f"""**System Info**
    
**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatFork - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**Hostname :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
    """
    await cb.edit_message_text(neat_msg, reply_markup=InlineKeyboardMarkup(bttn))



@bot.on_callback_query(filters.regex(pattern="make_basic_button_(True|False)"))
@cb_wrapper
async def wow_nice(client, cb):
    nice = True
    if cb.matches[0].group(1) == "True":
        nice = True
    if nice is True:
        v_t = CMD_HELP
        bttn = paginate_help(0, CMD_HELP, "helpme", is_official=nice)
    else:
        v_t = CMD_LIST
        bttn = paginate_help(0, CMD_LIST, "helpme", is_official=nice)
    await cb.edit_message_text(
        f"Command List & Help \n**Total Commands :** `{len(v_t)}` \n**(C) @PandaUserbot**",
        reply_markup=InlineKeyboardMarkup(bttn),
    )


@bot.on_callback_query(filters.regex(pattern="cleuse"))
@cb_wrapper
async def close_it_please(client, cb):
    bttn = [
        [
                InlineKeyboardButton(
                    text="☑ Menu Awal ☑ ", callback_data=f"backO_to_help_menu"
                )
            ],
        [
                InlineKeyboardButton(
                    text="⛔ Hapus Semua ⛔", callback_data=f"mansiz"
                )
            ]
    ]
    await cb.edit_message_text("**Closed Help Menu**!", reply_markup=InlineKeyboardMarkup(bttn))


@bot.on_callback_query(filters.regex(pattern="mansiz"))
@cb_wrapper
async def close_it_please(client, cb):
    await cb.edit_message_text("Closed Menu")


@bot.on_callback_query(filters.regex(pattern="backme_(.*)_(True|False)"))
@cb_wrapper
async def get_back_vro(client, cb):
    total_ = len(CMD_HELP)
    page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "True":
        is_official = True
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(page_number, cmd_list, "helpme", is_official=is_official)
    nice_text = f"**PandaUserbot Inline** \n\n**Version :** `{pandaversion}` \n**Pyrogram Version :** `{__version__}` \n**Modules :** `{total_}`"
    await cb.edit_message_text(nice_text, reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_callback_query(filters.regex(pattern="us_plugin_(.*)_(True|False)"))
@cb_wrapper
async def give_plugin_cmds(client, cb):
    plugin_name, page_number = cb.matches[0].group(1).split("|", 1)
    is_official = True
    if cb.matches[0].group(2) == "True":
        is_official = True
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    help_string = f"**Modules :** `{plugin_name}` \n{cmd_list[plugin_name]}"
    help_string += "\n\n**(C) @PandaUserbot** ".format(plugin_name)
    await cb.edit_message_text(
        help_string,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Go Back",
                        callback_data=f"backme_{page_number}_{is_official}",
                    )
                ]
            ]
        ),
    )


@bot.on_callback_query(filters.regex(pattern="helpme_next\((.+?)\)_(True|False)"))
@cb_wrapper
async def give_next_page(client, cb):
    current_page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "True":
        is_official = True
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(
        current_page_number + 1, cmd_list, "helpme", is_official=is_official
    )
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_callback_query(filters.regex(pattern="helpme_prev\((.+?)\)_(True|False)"))
@cb_wrapper
async def give_old_page(client, cb):
    current_page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "True":
        is_official = True
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(
        current_page_number - 1, cmd_list, "helpme", is_official=is_official
    )
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
