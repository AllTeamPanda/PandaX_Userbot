# ILHAM MANSIEZ
# PANDA USERBOT
# copyright catuserbot

import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from .... import tgbot

from ....config import Config
from ...._misc.logger import logging

LOGS = logging.getLogger(__name__)


@tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_true")))
async def age_verification_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Mengingat Itu Keputusan Bodoh, Aku Memilih Untuk Mengabaikannya.",
            alert=True,
        )
    await event.answer("Ya saya sudah 18+ sudah siap apapun hiks", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="Set `ALLOW_NSFW` = True di Heroku Vars untuk mengakses plugin ini",
            file="https://telegra.ph/file/85f3071c31279bcc280ef.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_false")))
async def age_verification_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Mengingat Itu Keputusan Bodoh, Aku Memilih Untuk Mengabaikannya.",
            alert=True,
        )
    await event.answer("Tidak Saya bocil😐", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="GO AWAY KID !",
            file="https://telegra.ph/file/08a3d412e29a1351b7aaa.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Mengingat Itu Keputusan Bodoh, Aku Memilih Untuk Mengabaikannya.",
            alert=True,
        )
    await event.answer("Unsure", alert=False)
    buttons = [
        (
            Button.inline(
                text="Ya Sudah bisa lama pun hiks", data="age_verification_true"
            ),
            Button.inline(
                text="Tidak Masih bocil gue 😐", data="age_verification_false"
            ),
        )
    ]
    try:
        await event.edit(
            text="**APAKAH ANDA CUKUP TUA UNTUK INI? ?**",
            file="https://telegra.ph/file/08a3d412e29a1351b7aaa.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass
