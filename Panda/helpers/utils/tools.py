import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        pandaevent = await edit_or_reply(
            event, f"`Transfiguration Time! Converting to ....`"
        )
    else:
        pandaevent = event
    pandamedia = None
    pandafile = os.path.join("./temp/", "meme.png")
    if os.path.exists(pandafile):
        os.remove(pandafile)
    if mediatype == "Photo":
        pandamedia = await reply.download_media(file="./temp")
        im = Image.open(pandamedia)
        im.save(pandafile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, pandafile, thumb=-1)
    elif mediatype == "Sticker":
        pandamedia = await reply.download_media(file="./temp")
        if pandamedia.endswith(".tgs"):
            await runcmd(
                f"lottie_convert.py --frame 0 -if lottie -of png '{pandamedia}' '{pandafile}'"
            )
        elif pandamedia.endswith(".webp"):
            im = Image.open(pandamedia)
            im.save(pandafile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, pandafile, thumb=-1)
        if not os.path.exists(pandafile):
            pandamedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(pandafile, 0.1)
            except:
                clip = clip.save_frame(pandafile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            pandamedia = await reply.download_media(file="./temp")
            im = Image.open(pandamedia)
            im.save(pandafile)
    if pandamedia and os.path.exists(pandamedia):
        os.remove(pandamedia)
    if os.path.exists(pandafile):
        return pandaevent, pandafile, mediatype
    return pandaevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
