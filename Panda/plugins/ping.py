import time

from datetime import datetime
from .. import StartTime, bot
from . import edit_or_reply, ilhammansiz_cmd
plugin_category = "plugins"

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time




@ilhammansiz_cmd(
    pattern="ping$",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "usage": ["{tr}ping"],
    },
)
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**P**")
    await xx.edit("**Po**")
    await xx.edit("**Pon**")
    await xx.edit("**Pong**")
    await xx.edit("**Pong!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await xx.edit(
        f"┏━《 𝗣 𝗔 𝗡 𝗗 𝗔 》━\n"
        f"┣➠ ▶ #PONG!!\n"
        f"┣➠ ▶ #Ping  `%sms`\n"
        f"┣➠ ⏰ **Uptime** `{uptime}` \n"
        f"┣➠ 👤 **Owner** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )




@ilhammansiz_cmd(
    pattern="pong$",
    command=("pong", plugin_category),
    info={
        "header": "check how long it takes to pong your userbot",
        "usage": ["{tr}pong"],
    },
)
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Gass!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🏓 **Ping!**\n`%sms`" % (duration))


