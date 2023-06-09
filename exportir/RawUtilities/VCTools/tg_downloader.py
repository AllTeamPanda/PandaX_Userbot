import asyncio
import io
import os
import pathlib
import time
from datetime import datetime

from telegraph import upload_file
from telethon.tl import types
from telethon.utils import get_extension
from userbot import *
from userbot.config import Config
from userbot._misc.managers import edit_or_reply
from userbot.helpers import progress

NAME = "untitled"

downloads = pathlib.Path(os.path.join(os.getcwd(), Config.TEMP_DIR))


async def tg_dl(event, reply, tgbot=False):
    "To download the replied telegram file"
    mone = await edit_or_reply(event, "`Downloading....`")
    name = NAME
    path = None
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
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
        if tgbot:
            progress_callback = None
        else:
            progress_callback = lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to download")
            )
        if (
            not reply.document
            and reply.photo
            and file_name
            and file_name.suffix
            or not reply.document
            and not reply.photo
        ):
            await reply.download_media(
                file=file_name.absolute(), progress_callback=progress_callback
            )
        elif not reply.document:
            file_name = await reply.download_media(
                file=downloads, progress_callback=progress_callback
            )
        else:
            dl = io.FileIO(file_name.absolute(), "a")
            await catub.fast_download_file(
                location=reply.document,
                out=dl,
                progress_callback=progress_callback,
            )
            dl.close()
        end = datetime.now()
        ms = (end - start).seconds
        await mone.edit(
            f"**•  Downloaded in {ms} seconds.**\n**•  Downloaded to :- **  `{os.path.relpath(file_name,os.getcwd())}`\n"
        )
        try:
            thumb = await reply.download_media(thumb=-1, file=downloads)
            thumb = f"https://graph.org{(upload_file(thumb))[0]}"
        except TypeError:
            try:
                nail_ = await event.client.get_profile_photos(PandaBot.me.id)
                thumb = await event.client.download_media(nail_[0], file=downloads)
            except Exception:
                thumb = (
                    "https://telegra.ph/file/c910a0ee1b10cfe0ef9db.jpg"
                )

        return [os.path.relpath(file_name, os.getcwd()), thumb]
    else:
        await mone.edit("`Reply to a message to download and stream.`")
        return False
