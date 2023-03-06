import re
from enum import Enum

from requests.exceptions import MissingSchema
from requests.models import PreparedRequest
from userbot.utils import runcmd
from yt_dlp import YoutubeDL


class Stream(Enum):
    audio = 1
    video = 2


yt_regex_str = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

yt_regex = re.compile(yt_regex_str)


def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except MissingSchema:
        return False


async def get_yt_stream_link(url, audio_only=False):
    if audio_only:
        return (
            await runcmd(f"yt-dlp --no-warnings --geo-bypass -f bestaudio -g {url}")
        )[0]
    return (await runcmd(f"yt-dlp --no-warnings --geo-bypass -f best -g {url}"))[0]


async def video_dl(url, title):
    path = f"temp/{title.replace(' ', '_')}.mp4"
    video_opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": False,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
            {"key": "FFmpegMetadata"},
        ],
        "outtmpl": path,
        "logtostderr": False,
        "quiet": True,
    }

    with YoutubeDL(video_opts) as ytdl:
        ytdl.extract_info(url)
    return path





import asyncio
import io
import os
import pathlib
import time
from datetime import datetime

from telethon.tl import types
from telethon.utils import get_extension
from userbot.config import Config
from userbot._misc.managers import edit_or_reply
from userbot.helpers import progress

NAME = "untitled"

downloads = pathlib.Path(os.path.join(os.getcwd(), Config.TMP_DOWNLOAD_DIRECTORY))


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix


async def tg_dl(event):
    "To download the replied telegram file"
    mone = await edit_or_reply(event, "`Downloading....`")
    name = NAME
    path = None
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    reply = await event.get_reply_message()
    if reply:
        start = datetime.now()
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        path = pathlib.Path(os.path.join(downloads, name))
        ext = get_extension(reply.document)
        if path and not path.suffix and ext:
            path = path.with_suffix(ext)
        if name == NAME:
            name += "_" + str(getattr(reply.document, "id", reply.id)) + ext
        if path and path.exists():
            if path.is_file():
                newname = f"{str(path.stem)}_OLD"
                path.rename(path.with_name(newname).with_suffix(path.suffix))
                file_name = path
            else:
                file_name = path / name
        elif path and not path.suffix and ext:
            file_name = downloads / path.with_suffix(ext)
        elif path:
            file_name = path
        else:
            file_name = downloads / name
        file_name.parent.mkdir(parents=True, exist_ok=True)
        c_time = time.time()
        if (
            not reply.document
            and reply.photo
            and file_name
            and file_name.suffix
            or not reply.document
            and not reply.photo
        ):
            await reply.download_media(
                file=file_name.absolute(),
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
        elif not reply.document:
            file_name = await reply.download_media(
                file=downloads,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
        else:
            dl = io.FileIO(file_name.absolute(), "a")
            await event.client.fast_download_file(
                location=reply.document,
                out=dl,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                ),
            )
            dl.close()
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            f"**•  Downloaded in {ms} seconds.**\n**•  Downloaded to :- **  `{os.path.relpath(file_name,os.getcwd())}`\n"
        )
        return os.path.relpath(file_name, os.getcwd())
    else:
        await mone.edit("`Reply to a message to download and stream.`")
        return False




import asyncio
from pathlib import Path

import requests
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    NodeJSNotInstalled,
    NotInGroupCallError,
    TooOldNodeJSVersion,
)
from pytgcalls.types import AudioPiped
from pytgcalls.types.stream import StreamAudioEnded
from telethon import functions
from telethon.errors import ChatAdminRequiredError
from yt_dlp import YoutubeDL

from .stream_helper import Stream, check_url, video_dl, yt_regex


class VCTools:
    def __init__(self, client) -> None:
        self.app = PyTgCalls(client, overload_quiet_mode=True)
        self.client = client
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []

    async def start(self):
        await self.app.start()

    def clear_vars(self):
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []

    async def join_vc(self, chat, join_as=None):
        if self.CHAT_ID:
            return f"Already in a group call on {self.CHAT_NAME}"
        if join_as:
            try:
                join_as_chat = await self.client.get_entity(int(join_as))
                join_as_title = f" as **{join_as_chat.title}**"
            except ValueError:
                return "Give Chat Id for joining as"
        else:
            join_as_chat = await self.client.get_me()
            join_as_title = ""
        try:
            await self.app.join_group_call(
                chat_id=chat.id,
                stream=AudioPiped("userbot/resources/resources_Silence01s.mp3"),
                join_as=join_as_chat,
                stream_type=StreamType().pulse_stream,
            )
        except NoActiveGroupCall:
            try:
                await self.client(
                    functions.phone.CreateGroupCallRequest(
                        peer=chat,
                        title="Cat VC",
                    )
                )
                await self.join_vc(chat=chat, join_as=join_as)
            except ChatAdminRequiredError:
                return "You need to become an admin to start VC, or ask one to start"
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return "Latest version of NodeJs is not installed"
        except AlreadyJoinedError:
            await self.app.leave_group_call(chat.id)
            await asyncio.sleep(3)
            await self.join_vc(chat=chat, join_as=join_as)
        self.CHAT_ID = chat.id
        self.CHAT_NAME = chat.title
        return f"Joined VC of **{chat.title}**{join_as_title}"

    async def leave_vc(self):
        try:
            await self.app.leave_group_call(self.CHAT_ID)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        self.CHAT_NAME = None
        self.CHAT_ID = None
        self.PLAYING = False
        self.PLAYLIST = []

    async def play_song(self, input, stream=Stream.audio, force=False):
        if yt_regex.match(input):
            with YoutubeDL({}) as ytdl:
                ytdl_data = ytdl.extract_info(input, download=False)
                title = ytdl_data.get("title", None)
            if title:
                playable = await video_dl(input, title)
            else:
                return "Error Fetching URL"
        elif check_url(input):
            try:
                res = requests.get(input, allow_redirects=True, stream=True)
                ctype = res.headers.get("Content-Type")
                if "video" not in ctype or "audio" not in ctype:
                    return "INVALID URL"
                name = res.headers.get("Content-Disposition", None)
                if name:
                    title = name.split('="')[0].split('"') or ""
                else:
                    title = input
                playable = input
            except Exception as e:
                return f"**INVALID URL**\n\n{e}"
        else:
            path = Path(input)
            if path.exists():
                if not path.name.endswith(
                    (".mkv", ".mp4", ".webm", ".m4v", ".mp3", ".flac", ".wav", ".m4a")
                ):
                    return "`File is invalid for Streaming`"
                playable = str(path.absolute())
                title = path.name
            else:
                return "`File Path is invalid`"
        print(playable)
        if self.PLAYING and not force:
            self.PLAYLIST.append({"title": title, "path": playable, "stream": stream})
            return f"Added to playlist.\n Position: {len(self.PLAYLIST)+1}"
        if not self.PLAYING:
            self.PLAYLIST.append({"title": title, "path": playable, "stream": stream})
            await self.skip()
            return f"Playing {title}"
        if force and self.PLAYING:
            self.PLAYLIST.insert(
                0, {"title": title, "path": playable, "stream": stream}
            )
            await self.skip()
            return f"Playing {title}"

    async def handle_next(self, update):
        if isinstance(update, StreamAudioEnded):
            await self.skip()



