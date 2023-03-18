# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import re
from telethon import Button
import json
import requests

def create_tl_btn(button: list):
    btn = []
    for z in button:
        if len(z) > 1:
            kk = [Button.url(x, y.strip()) for x, y in z]
            btn.append(kk)
        else:
            btn.append([Button.url(z[0][0], z[0][1].strip())])
    return btn


def get_msg_button(texts: str):
    btn = []
    for z in re.findall("\\[(.*?)\\|(.*?)\\]", texts):
        text, url = z
        urls = url.split("|")
        url = urls[0]
        if len(urls) > 1:
            btn[-1].append([text, url])
        else:
            btn.append([[text, url]])

    txt = texts
    for z in re.findall("\\[.+?\\|.+?\\]", texts):
        txt = txt.replace(z, "")

    return txt.strip(), btn


def format_btn(buttons: list):
    txt = ""
    for i in buttons:
        a = 0
        for i in i:
            if hasattr(i.button, "url"):
                a += 1
                if a > 1:
                    txt += f"[{i.button.text} | {i.button.url} | same]"
                else:
                    txt += f"[{i.button.text} | {i.button.url}]"
    _, btn = get_msg_button(txt)
    return btn




def translate(*args, **kwargs):
    headers = {
        "Referer": "https://translate.google.co.in",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/47.0.2526.106 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    x = requests.post(
        "https://translate.google.co.in/_/TranslateWebserverUi/data/batchexecute",
        headers=headers,
        data=_package_rpc(*args, **kwargs),
    ).text
    response = ""
    data = json.loads(json.loads(x[4:])[0][2])[1][0][0]
    subind = data[-2]
    if not subind:
        subind = data[-1]
    for i in subind:
        response += i[0]
    return response

def _get_value(stri):
    try:
        value = eval(stri.strip())
    except Exception as er:
        from .. import LOGS

        LOGS.debug(er)
        value = stri.strip()
    return value

def safe_load(file, *args, **kwargs):
    if isinstance(file, str):
        read = file.split("\n")
    else:
        read = file.readlines()
    out = {}
    for line in read:
        if ":" in line:  # Ignores Empty & Invalid lines
            spli = line.split(":", maxsplit=1)
            key = spli[0].strip()
            value = _get_value(spli[1])
            out.update({key: value or []})
        elif "-" in line:
            spli = line.split("-", maxsplit=1)
            where = out[list(out.keys())[-1]]
            if isinstance(where, list):
                value = _get_value(spli[1])
                if value:
                    where.append(value)
    return out


def mediainfo(media):
    xx = str((str(media)).split("(", maxsplit=1)[0])
    m = ""
    if xx == "MessageMediaDocument":
        mim = media.document.mime_type
        if mim == "application/x-tgsticker":
            m = "sticker animated"
        elif "image" in mim:
            if mim == "image/webp":
                m = "sticker"
            elif mim == "image/gif":
                m = "gif as doc"
            else:
                m = "pic as doc"
        elif "video" in mim:
            if "DocumentAttributeAnimated" in str(media):
                m = "gif"
            elif "DocumentAttributeVideo" in str(media):
                i = str(media.document.attributes[0])
                if "supports_streaming=True" in i:
                    m = "video"
                m = "video as doc"
            else:
                m = "video"
        elif "audio" in mim:
            m = "audio"
        else:
            m = "document"
    elif xx == "MessageMediaPhoto":
        m = "pic"
    elif xx == "MessageMediaWebPage":
        m = "web"
    return m

from telethon.tl import types
from telethon.utils import get_display_name

def make_mention(user, custom=None):
    if user.username:
        return f"@{user.username}"
    return inline_mention(user, custom=custom)


def inline_mention(user, custom=None, html=False):
    mention_text = get_display_name(user) or "Deleted Account" if not custom else custom
    if isinstance(user, types.User):
        if html:
            return f"<a href=tg://user?id={user.id}>{mention_text}</a>"
        return f"[{mention_text}](tg://user?id={user.id})"
    if isinstance(user, types.Channel) and user.username:
        if html:
            return f"<a href=https://t.me/{user.username}>{mention_text}</a>"
        return f"[{mention_text}](https://t.me/{user.username})"
    return mention_text
