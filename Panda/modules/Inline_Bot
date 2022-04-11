from .. import ALIVE_LOGO, CMD_HELP, INLINE_PIC, BOT_USERNAME, BOTLOG_CHATID, BOTLOG, INLINE_EMOJI, SUDO_USERS, DEVS
from ..Session import bot, tgbot
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name
from telethon.sync import custom, events
import re
from math import ceil


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{INLINE_EMOJI}", x, f"{INLINE_EMOJI}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⬅️", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("✖", b"close"),
                custom.Button.inline(
                    "➡️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        from ..modules.sql_helper.bot_blacklists import check_is_black_list
        from ..modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from ..misc import reply_id

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        firstname = user.first_name
        lastname = user.last_name
        owner = f"{firstname} {lastname}" if lastname else firstname
        logo = ALIVE_LOGO
        inlinelogo = INLINE_PIC
        tgbotusername = BOT_USERNAME
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        @tgbot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to, user_name, user_id, reply_msg, event.id, msg.id
                        )
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@PandaUserbot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=inlinelogo,
                    link_preview=False,
                    text=f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n✣ **Jumlah** `{len(dugmeler)}` Modules",
                    buttons=buttons,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Panda-Userbot",
                    url="https://t.me/TeamSquadUserbotSupport",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text="**Panda-UserBot**\n➖➖➖➖➖➖➖➖\n👤 **Owner Repo :** [Pocong](https://t.me/diemmmmmmmmmm)\n👥 **Support :** @TeamSquadUserbotSupport\n📐 **Repository :** [Panda-Userbot](https://github.com/ilhammansiz/PandaX_Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("𝐺𝑟𝑜𝑢𝑝", "https://t.me/TeamSquadUserbotSupport"),
                            custom.Button.url(
                                "𝑅𝑒𝑝𝑜", "https://github.com/ilhammansiz/PandaX_Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(match.group(4)))
                        )
                        note_data += markdown_note[prev : match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title=" Panda-Userbot ",
                    description="Panda-UserBot | Telethon",
                    url="https://t.me/TeamSquadUserbotSupport",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text=f"**Panda-UserBot**\n➖➖➖➖➖➖➖➖➖ **UserMode:** [{user.first_name}](tg://user?id={user.id})\n🐼 **Assistant:** {tgbotusername}\n➖➖➖➖➖➖➖➖\n**Support:** @TeamSquadUserbotSupport\n➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("𝐺𝑟𝑜𝑢𝑝", "https://t.me/TeamSquadUserbotSupport"),
                            custom.Button.url(
                                "𝑅𝑒𝑝𝑜", "https://github.com/ilhammansiz/PandaX_Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(looters)
                buttons = paginate_help(current_page_number, dugmeler, "helpme")
                text = f"**➕ Panda-Userbot Inline Menu **\n\n👤 **Owner** [{user.first_name}](tg://user?id={user.id})\n🗂 **Jumlah** `{len(dugmeler)}` Modules"
                await event.edit(
                    text,
                    file=inlinelogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in DEVS and SUDO_USERS:
                openlagi = custom.Button.inline("✖ Tutup", data="close")
                await event.edit(
                    " **Help Mode Button Ditutup!** "
                )
                await event.delete()
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")
                help_string = ""
                try:
                    for u in CMD_HELP[modul_name]:
                        help_string = f"Plugin Name-{modul_name}\n\n✘ Commands Available-\n\n"
                        help_string += str(CMD_HELP[modul_name])
                except BaseException:
                    pass
                if help_string == "":
                    reply_pop_up_alert = f"{modul_name} has no detailed help..."
                else:
                    reply_pop_up_alert = help_string
                reply_pop_up_alert += "\n© @PandaUserbot"
                buttons = [ 
                    [
                        Button.inline("« Bᴀᴄᴋ", data="reopen"),
                        Button.inline("Cʟᴏꜱᴇ", data="close"),
                    ],
                ]
                try:
                    if str(event.query.user_id) in SUDO_USERS:
                        await event.edit(
                            reply_pop_up_alert,
                            buttons=buttons,
                        )
                    else:
                         reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                         await event.answer(reply_pop_up_alert, cache_time=0)
                except BaseException:
                     pandaxx = f"Do .help {modul_name} to get the list of commands."
                     await event.edit(pandaxx, buttons=buttons)
    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. "
        )
