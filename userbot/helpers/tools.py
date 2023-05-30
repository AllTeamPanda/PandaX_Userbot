from html_telegraph_poster import TelegraphPoster
from .utils.utils import runcmd
import contextlib
import json
import os

def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None


async def post_to_telegraph(page_title, html_format_content):
    post_client = TelegraphPoster(use_api=True)
    auth_name = "PandaUserbot"
    post_client.create_api_token(auth_name)
    post_page = post_client.post(
        title=page_title,
        author=auth_name,
        author_url="https://t.me/TEAMSquadUserbotSupport",
        text=html_format_content,
    )
    return post_page["url"]


async def fileinfo(file):
    x, y, z, s = await runcmd(f"mediainfo '{file}' --Output=JSON")
    cat_json = json.loads(x)["media"]["track"]
    dic = {
        "path": file,
        "size": int(cat_json[0]["FileSize"]),
        "extension": cat_json[0]["FileExtension"],
        "type": "None",
        "format": "None",
        "audio": "None",
    }
    with contextlib.suppress(IndexError, KeyError):
        dic["format"] = cat_json[0]["Format"]
        dic["type"] = cat_json[1]["@type"]
        if "ImageCount" not in cat_json[0]:
            dic["duration"] = int(float(cat_json[0]["Duration"]))
            dic["bitrate"] = int(cat_json[0]["OverallBitRate"]) // 1000
        dic["height"] = int(cat_json[1]["Height"])
        dic["width"] = int(cat_json[1]["Width"])
        dic["audio"] = "Present" if cat_json[0]["AudioCount"] else "None"
    return dic
