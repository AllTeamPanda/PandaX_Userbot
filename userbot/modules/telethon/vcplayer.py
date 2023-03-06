import logging

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import User
from ... import Config, PandaBot, udB
from ..._misc.managers import edit_delete, edit_or_reply

from ..._helper.VC.stream_helper import Stream
from ..._helper.VC.tg_downloader import tg_dl
from ..._helper.VC.vcp_helper import VCTools

plugin_category = "music"

logging.getLogger("pytgcalls").setLevel(logging.ERROR)

OWNER_ID = PandaBot.uid

vc_session = udB.get_key("VC_SESSION")

if vc_session:
    vc_client = TelegramClient(
        StringSession(vc_session), Config.APP_ID, Config.API_HASH
    )
else:
    vc_client = PandaBot

vc_client.__class__.__module__ = "telethon.client.telegramclient"
vc_player = VCTools(vc_client)




@vc_player.app.on_stream_end()
async def handler(_, update):
    await vc_player.handle_next(update)


ALLOWED_USERS = set()


@PandaBot.ilhammansiz_cmd(
    pattern="joinvc ?(\S+)? ?(?:-as)? ?(\S+)?",
    command=("joinvc", plugin_category),
    info={
        "header": "To join a Voice Chat.",
        "description": "To join or create and join a Voice Chat",
        "note": "You can use -as flag to join anonymously",
        "flags": {
            "-as": "To join as another chat.",
        },
        "usage": [
            "{tr}joinvc",
            "{tr}joinvc (chat_id)",
            "{tr}joinvc -as (peer_id)",
            "{tr}joinvc (chat_id) -as (peer_id)",
        ],
        "examples": [
            "{tr}joinvc",
            "{tr}joinvc -1001556371377",
            "{tr}joinvc -as -1001556371377",
            "{tr}joinvc -1001556371377 -as -1001556371377",
        ],
    },
)
async def joinVoicechat(event):
    "To join a Voice Chat."
    chat = event.pattern_match.group(1)
    joinas = event.pattern_match.group(2)

    await edit_or_reply(event, "Joining VC ......")

    if chat and chat != "-as":
        if chat.strip("-").isnumeric():
            chat = int(chat)
    else:
        chat = event.chat_id

    if vc_player.app.active_calls:
        return await edit_delete(
            event, f"You have already Joined in {vc_player.CHAT_NAME}"
        )

    try:
        vc_chat = await PandaBot.get_entity(chat)
    except Exception as e:
        return await edit_delete(event, f'ERROR : \n{e or "UNKNOWN CHAT"}')

    if isinstance(vc_chat, User):
        return await edit_delete(
            event, "Voice Chats are not available in Private Chats"
        )

    if joinas and not vc_chat.username:
        await edit_or_reply(
            event, "Unable to use Join as in Private Chat. Joining as Yourself..."
        )
        joinas = False

    out = await vc_player.join_vc(vc_chat, joinas)
    await edit_delete(event, out)



@PandaBot.ilhammansiz_cmd(
    pattern="leavevc",
    command=("leavevc", plugin_category),
    info={
        "header": "To leave a Voice Chat.",
        "description": "To leave a Voice Chat",
        "usage": [
            "{tr}leavevc",
        ],
        "examples": [
            "{tr}leavevc",
        ],
    },
)
async def leaveVoicechat(event):
    "To leave a Voice Chat."
    if vc_player.CHAT_ID:
        await edit_or_reply(event, "Leaving VC ......")
        chat_name = vc_player.CHAT_NAME
        await vc_player.leave_vc()
        await edit_delete(event, f"Left VC of {chat_name}")
    else:
        await edit_delete(event, "Not yet joined any VC")



@PandaBot.ilhammansiz_cmd(
    pattern="playlist",
    command=("playlist", plugin_category),
    info={
        "header": "To Get all playlist.",
        "description": "To Get all playlist for Voice Chat.",
        "usage": [
            "{tr}playlist",
        ],
        "examples": [
            "{tr}playlist",
        ],
    },
)
async def get_playlist(event):
    "To Get all playlist for Voice Chat."
    await edit_or_reply(event, "Fetching Playlist ......")
    playl = vc_player.PLAYLIST
    if not playl:
        await edit_delete(event, "Playlist empty", time=10)
    else:
        panda = ""
        for num, item in enumerate(playl, 1):
            if item["stream"] == Stream.audio:
                panda += f"{num}. 🔉  `{item['title']}`\n"
            else:
                panda += f"{num}. 📺  `{item['title']}`\n"
        await edit_delete(event, f"**Playlist:**\n\n{panda}\n**Enjoy the show**")



@PandaBot.ilhammansiz_cmd(
    pattern="vplay ?(-f)? ?([\S ]*)?",
    command=("vplay", plugin_category),
    info={
        "header": "To Play a media as video on VC.",
        "description": "To play a video stream on VC.",
        "flags": {
            "-f": "Force play the Video",
        },
        "usage": [
            "{tr}vplay (reply to message)",
            "{tr}vplay (yt link)",
            "{tr}vplay -f (yt link)",
        ],
        "examples": [
            "{tr}vplay",
            "{tr}vplay https://youtube.com/playlist?list=RDz-CyTv5TNx8&playnext=1",
            "{tr}vplay -f https://youtube.com/playlist?list=RDz-CyTv5TNx8&playnext=1",
        ],
    },
)
async def play_video(event):
    "To Play a media as video on VC."
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "Please Provide a media file to stream on VC", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "Join a VC and use play command")
    if not input_str:
        return await edit_or_reply(event, "No Input to play in vc")
    await edit_or_reply(event, "Playing in VC ......")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.video, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.video, force=False)
    if resp:
        await edit_delete(event, resp, time=30)


@PandaBot.ilhammansiz_cmd(
    pattern="play ?(-f)? ?([\S ]*)?",
    command=("play", plugin_category),
    info={
        "header": "To Play a media as audio on VC.",
        "description": "To play a audio stream on VC.",
        "flags": {
            "-f": "Force play the Audio",
        },
        "usage": [
            "{tr}play (reply to message)",
            "{tr}play (yt link)",
            "{tr}play -f (yt link)",
        ],
        "examples": [
            "{tr}play",
            "{tr}play https://youtube.com/playlist?list=RDz-CyTv5TNx8&playnext=1",
            "{tr}play -f https://youtube.com/playlist?list=RDz-CyTv5TNx8&playnext=1",
        ],
    },
)
async def play_audio(event):
    "To Play a media as audio on VC."
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "Please Provide a media file to stream on VC", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "Join a VC and use play command")
    if not input_str:
        return await edit_or_reply(event, "No Input to play in vc")
    await edit_or_reply(event, "Playing in VC ......")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.audio, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.audio, force=False)
    if resp:
        await edit_delete(event, resp, time=30)



@PandaBot.ilhammansiz_cmd(
    pattern="pause",
    command=("pause", plugin_category),
    info={
        "header": "To Pause a stream on Voice Chat.",
        "description": "To Pause a stream on Voice Chat",
        "usage": [
            "{tr}pause",
        ],
        "examples": [
            "{tr}pause",
        ],
    },
)
async def pause_stream(event):
    "To Pause a stream on Voice Chat."
    await edit_or_reply(event, "Pausing VC ......")
    res = await vc_player.pause()
    await edit_delete(event, res, time=30)



@PandaBot.ilhammansiz_cmd(
    pattern="resume",
    command=("resume", plugin_category),
    info={
        "header": "To Resume a stream on Voice Chat.",
        "description": "To Resume a stream on Voice Chat",
        "usage": [
            "{tr}resume",
        ],
        "examples": [
            "{tr}resume",
        ],
    },
)
async def resume_stream(event):
    "To Resume a stream on Voice Chat."
    await edit_or_reply(event, "Resuming VC ......")
    res = await vc_player.resume()
    await edit_delete(event, res, time=30)



@PandaBot.ilhammansiz_cmd(
    pattern="skip",
    command=("skip", plugin_category),
    info={
        "header": "To Skip currently playing stream on Voice Chat.",
        "description": "To Skip currently playing stream on Voice Chat.",
        "usage": [
            "{tr}skip",
        ],
        "examples": [
            "{tr}skip",
        ],
    },
)
async def skip_stream(event):
    "To Skip currently playing stream on Voice Chat."
    await edit_or_reply(event, "Skiping Stream ......")
    res = await vc_player.skip()
    await edit_delete(event, res, time=30)


