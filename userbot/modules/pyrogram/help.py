# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import os

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import BotInlineDisabled
from pyrogram.types import CallbackQuery, Message

from ... import app, gen


app.CMD_HELP.update(
    {
        "help": (
            "help",
            {
                "help [ module name ]": "Get commands info of that plugin.",
                "help": "Get your inline help dex.",
                "inline": "Toggle inline mode to On or Off of your bot through @BotFather",
                "mods": "Get list of available module names",
                "plugs": "Get list of available plugin names",
            },
        )
    }
)


helpdex_ids = app.getdv("DELETE_DEX_ID")


@app.bot.on_callback_query(filters.regex("delete-dext"))
@app.alert_user
async def delete_helpdex(_, cb: CallbackQuery):
    if not helpdex_ids:
        await cb.answer(
            "This message is expired, hence it can't be deleted !",
            show_alert=True,
        )
    else:
        try:
            app.deldv("DELETE_DEX_ID")  # empty var
        except Exception as e:
            app.log.error(e)


import struct
import base64

from pyrogram import filters
from pyrogram.types import CallbackQuery
from pyrogram.errors import PeerIdInvalid



@app.bot.on_callback_query(filters.regex("delete-dex"))
@app.alert_user
async def delete_helpmenu_callback(_, cb: CallbackQuery):
    try:
        if cb.inline_message_id:
            dc_id, message_id, chat_id, query_id = struct.unpack(
                "<iiiq",
                base64.urlsafe_b64decode(
                    cb.inline_message_id + '=' * (
                        len(cb.inline_message_id) % 4
                    )
                )
            )

            return await app.delete_messages(
                chat_id=int(str(-100) + str(chat_id)[1:]),
                message_ids=message_id
            )
        else:
            if cb.message:
                return await cb.message.delete()

        await cb.answer(
            "Message Expired !",
            show_alert=True
        )

    except (PeerIdInvalid, KeyError, ValueError):
        await app.delete_messages(
            chat_id=chat_id,
            message_ids=message_id
        )
        print(chat_id, message_id)
    except Exception as e:
        await app.error(e)


@app.on_message(gen("help", allow=["sudo"]))
async def helpdex_handler(_, m: Message):
    args = m.command if app.long(m) > 1 else False

    try:
        if args is False:
            m = await app.send_edit(m, ". . .", text_type=["mono"])
            result = await app.get_inline_bot_results(app.bot.username, "#t5r4o9nn6")
            if result:
                await m.delete()
                info = await app.send_inline_bot_result(
                    m.chat.id,
                    query_id=result.query_id,
                    result_id=result.results[0].id,
                    disable_notification=True,
                )

            else:
                await app.send_edit(
                    m,
                    "Please check your bots inline mode is on or not . . .",
                    delme=3,
                    text_type=["mono"],
                )
        elif args:

            module_help = await app.data(args[1])
            if not module_help:
                await app.send_edit(
                    m,
                    f"Invalid module name specified, use `{app.PREFIX}mods` to get list of modules",
                    delme=3,
                )
            else:
                await app.send_edit(
                    m, f"**MODULE:** {args[1]}\n\n" + "".join(module_help)
                )
        else:
            await app.send_edit(m, "Try again later !", text_type=["mono"], delme=3)
    except BotInlineDisabled:
        await app.toggle_inline(m)
        await help_menu(client, m)
    except Exception as e:
        await app.error(m, e)


# get all module name
@app.on_message(gen("mods", allow=["sudo"]))
async def allmodules_handler(_, m: Message):
    store = []
    store.clear()
    for x in os.listdir("userbot/modules/pyrogram/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit(m, "**MODULES OF USERBOT🤖:**\n\n" + "".join(store))


# get all plugins name
@app.on_message(gen("plugs", allow=["sudo"]))
async def allplugins_handler(_, m: Message):
    store = []
    store.clear()
    for x in os.listdir("userbot/modules/pyrogram/asistant/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit(m, "**PLUGINS OF BOT:**\n\n" + "".join(store))


@app.on_message(gen("inline", allow=["sudo"]))
async def toggleinline_handler(_, m: Message):
    return await app.toggle_inline(m)
