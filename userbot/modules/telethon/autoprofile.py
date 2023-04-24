import random

from telethon.tl.functions.account import UpdateProfileRequest

from . import *
plugin_category = "modules"

@pandaub.ilhammansiz_cmd(
    pattern="(auto|stop)name$",
    command=("auto|stop", plugin_category),
    info={
        "header": "Changes your name with time",
        "description": "Updates your profile name along with time. Set AUTONAME var in heroku with your profile name,",
        "note": "To stop this do '.end autoname'",
        "usage": "{tr}autoname",
    },
)
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
        udB.del_key("AUTONAME")
        await edit_or_reply(event, "`AUTONAME has been Stopped !`")
        return
    udB.set_key("AUTONAME", "True")
    await edit_or_reply(event, "`Started AUTONAME`")
    while True:
        getn = udB.get_key("AUTONAME")
        if not getn:
            return
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{OWNER_NAME}⚡ {DM} 🗓️"
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(1111)



@pandaub.ilhammansiz_cmd(
    pattern="(auto|stop)bio$",
    command=("auto|stop", plugin_category),
    info={
        "header": "Changes your name with time",
        "description": "Updates your profile bio along with time. Set AUTOBIO var in heroku with your profile name,",
        "note": "To stop this do '.end autobio'",
        "usage": "{tr}autobio",
    },
)
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
        udB.del_key("AUTOBIO")
        await edit_or_reply(event, "`AUTOBIO has been Stopped !`")
        return
    udB.set_key("AUTOBIO", "True")
    await edit_or_reply(event, "`Started AUTOBIO`")
    BIOS = [
        "Busy Today !",
        "USERBOT",
        "Enjoying Life!",
        "Unique as Always!" "Sprinkling a bit of magic",
        "Intelligent !",
    ]
    while True:
        getn = udB.get_key("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"📅{DM} | {BIOMSG} | ⌚️{HM}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(1111)
