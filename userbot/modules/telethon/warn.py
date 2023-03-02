   
from ... import PandaBot, udB

from ..._misc.managers import edit_or_reply
from ..._database.dB.warn_db import add_warn, reset_warn, warns

from ...resources.tools import inline_mention
plugin_category = "modules"    



@PandaBot.ilhammansiz_cmd(
    pattern="warn(?:\s|$)([\s\S]*)",
    command=("warn", plugin_category),
    info={
        "header": "To warn a user.",
        "description": "will warn the replied user.",
        "usage": "{tr}warn <reason>",
    },
)
async def warn(e):
    pandaub = e.client
    reply = await e.get_reply_message()
    if len(e.text) > 5 and " " not in e.text[5]:
        return
    if reply:
        user = reply.sender_id
        reason = e.text[5:] if e.pattern_match.group(1).strip() else "unknown"
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await pandaub.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await edit_or_reply(e, "Reply To A User", time=5)
        try:
            reason = e.text.split(maxsplit=2)[-1]
        except BaseException:
            reason = "unknown"
    count, r = warns(e.chat_id, user)
    r = f"{r}|$|{reason}" if r else reason
    try:
        x = udB.get_key("SETWARN")
        number, action = int(x.split()[0]), x.split()[1]
    except BaseException:
        number, action = 3, "kick"
    if ("ban" or "kick" or "mute") not in action:
        action = "kick"
    if count + 1 >= number:
        if "ban" in action:
            try:
                await pandaub.edit_permissions(e.chat_id, user, view_messages=False)
            except BaseException:
                return await edit_or_reply(e, "`Something Went Wrong.`", time=5)
        elif "kick" in action:
            try:
                await pandaub.kick_participant(e.chat_id, user)
            except BaseException:
                return await edit_or_reply(e, "`Something Went Wrong.`", time=5)
        elif "mute" in action:
            try:
                await pandaub.edit_permissions(
                    e.chat_id, user, until_date=None, send_messages=False
                )
            except BaseException:
                return await edit_or_reply(e, "`Something Went Wrong.`", time=5)
        add_warn(e.chat_id, user, count + 1, r)
        c, r = warns(e.chat_id, user)
        ok = await pandaub.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"User {user} Got {action} Due to {count+1} Warns.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await edit_or_reply(text)
        return reset_warn(e.chat_id, ok.id)
    add_warn(e.chat_id, user, count + 1, r)
    ok = await pandaub.get_entity(user)
    user = inline_mention(ok)
    await edit_or_reply(
        e,
        f"**WARNING :** {count+1}/{number}\n**To :**{user}\n**Be Careful !!!**\n\n**Reason** : {reason}",
    )


@PandaBot.ilhammansiz_cmd(
    pattern="r(eset)?warns$",
    command=("resetwarns", plugin_category),
    info={
        "header": "To reset warns of the replied user",
        "usage": [
            "{tr}rwarns",
            "{tr}resetwarns",
        ],
    },
)
async def rwarn(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await edit_or_reply(e, "Reply To user")
    reset_warn(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = inline_mention(ok)
    await edit_or_reply(e, f"Cleared All Warns of {user}.")


@PandaBot.ilhammansiz_cmd(
    pattern="warns",
    command=("warns", plugin_category),
    info={
        "header": "To get users warns list.",
        "usage": "{tr}warns <reply>",
    },
)
async def twarns(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.from_id.user_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await edit_or_reply("Reply To A User", time=5)
    c, r = warns(e.chat_id, user)
    if c and r:
        ok = await e.client.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"User {user} Got {c} Warns.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await edit_or_reply(e, text)
    else:
        await edit_or_reply(e, "`No Warnings`")


@PandaBot.ilhammansiz_cmd(
    pattern="setwarn(?:\s|$)([\s\S]*)",
    command=("setwarn", plugin_category),
    info={
        "header": "To warn a user.",
        "description": "will warn the replied user.",
        "usage": "{tr}setwarn <reason>",
    },
)
async def warnset(e):
    ok = e.pattern_match.group(1).strip()
    if not ok:
        return await edit_or_reply("stuff")
    if "|" in ok:
        try:
            number, action = int(ok.split()[0]), ok.split()[1]
        except BaseException:
            return await edit_or_reply(get_string("schdl_2"), time=5)
        if ("ban" or "kick" or "mute") not in action:
            return await edit_or_reply(e, "`Only mute / ban / kick option suported`", time=5)
        udB.set_key("SETWARN", f"{number} {action}")
        await edit_or_reply(e, f"Done Your Warn Count is now {number} and Action is {action}")
    else:
        await edit_or_reply(e, "Incorrect Format", time=5)

