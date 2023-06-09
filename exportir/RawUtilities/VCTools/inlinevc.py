import re

from telethon import Button
from telethon.events import CallbackQuery
from telethon.tl.types import User
from userbot import *
from userbot._misc import check_owner

from .function import vc_player

vcimg = "https://telegra.ph/file/c910a0ee1b10cfe0ef9db.jpg"
erimg = "https://telegra.ph/file/c910a0ee1b10cfe0ef9db.jpg"


buttons = (
    [
        [
            Button.inline("👾 Join VC", data="joinvc"),
            Button.inline("🍃 Leave VC", data="leavevc"),
        ],
        [
            Button.inline("🎛 Player", data="playervc"),
            Button.inline("⚙️ Settings", data="settingvc"),
        ],
        [
            Button.inline("🗑 Close", data="vc_close"),
        ],
    ],
    [
        [
            Button.inline("⏮ Prev", data="previousvc"),
            Button.inline("⏸ Pause", data="pausevc"),
            Button.inline("⏭ Next", data="skipvc"),
        ],
        [
            Button.inline("Repeat ❌", data="repeatvc"),
            Button.inline("〣 Mainmenu", data="menuvc"),
        ],
        [
            Button.inline("🗑 Close", data="vc_close"),
        ],
    ],
)


# MAINMENU BUTTONS
@tgbot.on(CallbackQuery(data=re.compile(r"^joinvc$")))
@check_owner
async def joinvc(event):
    chat = event.chat_id
    if vc_player.app.active_calls:
        return await event.answer(f"You have already Joined in: {vc_player.CHAT_NAME}")

    try:
        vc_chat = await vc_player.client.get_entity(chat)
    except Exception as e:
        return await event.answer(f'ERROR : \n{e or "UNKNOWN CHAT"}')

    if isinstance(vc_chat, User):
        return await event.answer("Voice Chats are not available in Private Chats")

    out = await vc_player.join_vc(vc_chat, False)
    await event.answer(out)


@tgbot.on(CallbackQuery(data=re.compile(r"^leavevc$")))
@check_owner
async def leavevc(event):
    if vc_player.CHAT_ID:
        chat_name = vc_player.CHAT_NAME
        await vc_player.leave_vc()

        await event.answer(f"Left VC of {chat_name}")
    else:
        await event.answer("Not yet joined any VC")


@tgbot.on(CallbackQuery(data=re.compile(r"^playervc$")))
@check_owner
async def playervc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    playing = vc_player.PLAYING
    title = playing["title"]
    duration = playing["duration"]
    url = playing["url"]
    vcimg = playing["img"]
    msg = f"**🎧 Playing:** [{title}]({url})\n"
    msg += f"**⏳ Duration:** `{duration}`\n"
    msg += f"**💭 Chat:** `{vc_player.CHAT_NAME}`"
    await event.edit(msg, file=vcimg, buttons=buttons[1])


# PLAYER BUTTONS
@tgbot.on(CallbackQuery(data=re.compile(r"^menuvc$")))
@check_owner
async def playervc(event):
    await event.edit(file=vcimg, text="**| VC Menu |**", buttons=buttons[0])


@tgbot.on(CallbackQuery(data=re.compile(r"^previousvc$")))
@check_owner
async def previousvc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    if not vc_player.PREVIOUS:
        return await event.answer("No Previous track found.")
    prev = vc_player.PREVIOUS[-1]
    song_input = prev["path"]
    stream = prev["stream"]
    duration = prev["duration"]
    url = prev["url"]
    img = prev["img"]
    res = await vc_player.play_song(
        event,
        song_input,
        stream,
        force=True,
        prev=True,
        duration=duration,
        url=url,
        img=img,
    )
    if res and isinstance(res, list):
        try:
            await event.edit(file=res[0], text=res[1], buttons=buttons[1])
        except Exception:
            await event.edit(file=erimg, text=res[1], buttons=buttons[1])
    elif res and isinstance(res, str):
        await event.edit(file=vcimg, text=res, buttons=buttons[1])


@tgbot.on(CallbackQuery(data=re.compile(r"^resumevc$")))
@check_owner
async def resumevc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    res = await vc_player.resume()
    await event.answer(res)
    if not vc_player.PAUSED:
        eve = await event.get_message()
        buttons = [
            [Button.inline(k.text, data=k.data[2:1]) for k in i] for i in eve.buttons
        ]
        buttons[0].pop(1)
        buttons[0].insert(1, Button.inline("⏸ Pause", data="pausevc"))
        await event.edit(buttons=buttons)


@tgbot.on(CallbackQuery(data=re.compile(r"^pausevc$")))
@check_owner
async def pausevc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    res = await vc_player.pause()
    await event.answer(res)
    if vc_player.PAUSED:
        eve = await event.get_message()
        buttons = [
            [Button.inline(k.text, data=k.data[2:1]) for k in i] for i in eve.buttons
        ]
        buttons[0].pop(1)
        buttons[0].insert(1, Button.inline("▶️ Resume", data="resumevc"))
        await event.edit(buttons=buttons)


@tgbot.on(CallbackQuery(data=re.compile(r"^skipvc$")))
@check_owner
async def skipvc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    res = await vc_player.skip()
    if res and isinstance(res, list):
        try:
            await event.edit(file=res[0], text=res[1], buttons=buttons[1])
        except Exception:
            await event.edit(file=erimg, text=res[1], buttons=buttons[1])
    elif res and isinstance(res, str):
        await event.edit(file=vcimg, text=res, buttons=buttons[1])


@tgbot.on(CallbackQuery(data=re.compile(r"^repeatvc$")))
@check_owner
async def repeatvc(event):
    if not vc_player.PLAYING:
        return await event.answer("Play any audio or video stream first...", alert=True)
    if vc_player.REPEAT:
        vc_player.REPEAT = False
        buttons[1][1].pop(0)
        buttons[1][1].insert(0, Button.inline("Repeat ❌", data="repeatvc"))
    else:
        vc_player.REPEAT = True
        buttons[1][1].pop(0)
        buttons[1][1].insert(0, Button.inline("Repeat ✅", data="repeatvc"))

    await event.edit(buttons=buttons[1])


# SETTINGS BUTTONS
def fetch_button_layout(abtntext, bbtntext, cbtntext):
    return [
        [
            Button.inline("🎩 Auth Mode", data="amodeinfo"),
            Button.inline(abtntext, data="amode"),
        ],
        [
            Button.inline("🤖 Bot Mode", data="bmodeinfo"),
            Button.inline(bbtntext, data="bmode"),
        ],
        [
            Button.inline("🗑 Clean Mode", data="cmodeinfo"),
            Button.inline(cbtntext, data="cmode"),
        ],
        [
            Button.inline("⬅️ Back", data="backvc"),
            Button.inline("🗑 close", data="vc_close"),
        ],
    ]


def fetch_button_text():
    abtntext = "🏢 Public" if vc_player.PUBLICMODE else "🏠 Private"
    bbtntext = "✅ Enabled" if vc_player.BOTMODE else "❌ Disabled"
    cbtntext = "✅ Enabled" if vc_player.CLEANMODE else "❌ Disabled"
    return abtntext, bbtntext, cbtntext


@tgbot.on(CallbackQuery(data=re.compile(r"^settingvc$")))
@check_owner
async def settingvc(event):
    abtntext, bbtntext, cbtntext = fetch_button_text()
    buttons = fetch_button_layout(abtntext, bbtntext, cbtntext)
    await event.edit("** | Settings | **", buttons=buttons)


@tgbot.on(CallbackQuery(pattern="^(a|b|c)mode$"))
@check_owner
async def vc(event):
    mode = (event.pattern_match.group(1)).decode("UTF-8")
    abtntext, bbtntext, cbtntext = fetch_button_text()
    if mode == "a":
        vc_player.PUBLICMODE = not vc_player.PUBLICMODE
        abtntext = "🏢 Public" if vc_player.PUBLICMODE else "🏠 Private"
    elif mode == "b":
        vc_player.BOTMODE = not vc_player.BOTMODE
        bbtntext = "✅ Enabled" if vc_player.BOTMODE else "❌ Disabled"
    elif mode == "c":
        vc_player.CLEANMODE = not vc_player.CLEANMODE
        cbtntext = "✅ Enabled" if vc_player.CLEANMODE else "❌ Disabled"

    buttons = fetch_button_layout(abtntext, bbtntext, cbtntext)
    await event.edit("** | Settings | **", buttons=buttons)


@tgbot.on(CallbackQuery(pattern="(a|b|c)modeinfo$"))
@check_owner
async def vc(event):
    mode = (event.pattern_match.group(1)).decode("UTF-8")
    if mode == "a":
        text = "⁉️ What is This?\n\n🏢 Public: Anyone can use catuserbot vc player present in this group.\n\n🏠 Private: Only Owner of user bot and sudo users can use catuserbot vc player"
    elif mode == "b":
        text = "⁉️ What is This?\n\nWhen activated, Your assistant responds to the commands  with interactive buttons"
    elif mode == "c":
        text = "⁉️ What is This?\n\nWhen activated, Bot will delete its message after leaving vc to make your chat clean and clear."
    await event.answer(text, alert=True)


# COMMON BUTTONS
@tgbot.on(CallbackQuery(data=re.compile(r"^backvc$")))
@check_owner
async def vc(event):
    await event.edit("** | VC Menu | **", buttons=buttons[0])


@tgbot.on(CallbackQuery(data=re.compile(r"^vc_close$")))
@check_owner
async def vc(event):
    try:
        await event.delete()
    except Exception:
        await event.edit(
            "**| VC Player Closed |**",
            buttons=[[Button.inline("Open again", data="backvc")]],
        )
