import asyncio
import contextlib
import logging

from telethon import Button, TelegramClient, types
from telethon.sessions import StringSession
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.messages import AddChatUserRequest
from userbot import *
from userbot._misc.managers import edit_or_reply
from userbot.helpers import _pandautils
from userbot._database._var import Var, Database

from .vcclient import VCTools

LOGS = logging.getLogger(__name__)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

if Var.VC_STRING_SESSION:
    vc_client = vclient
else:
    vc_client = PandaBot
if Var.VC_STRING_SESSION2:
    vc_client2 = vclient2
else:
    vc_client2 = PandaBot2
if Var.VC_STRING_SESSION3:
    vc_client3 = vclient3
else:
    vc_client3 = PandaBot3
if Var.VC_STRING_SESSION4:
    vc_client4 = vclient4
else:
    vc_client4 = PandaBot4
if Var.VC_STRING_SESSION5:
    vc_client5 = vclient5
else:
    vc_client5 = PandaBot5
if Var.VC_STRING_SESSION6:
    vc_client6 = vclient6
else:
    vc_client6 = PandaBot6
if Var.VC_STRING_SESSION7:
    vc_client7 = vclient7
else:
    vc_client7 = PandaBot7
if Var.VC_STRING_SESSION8:
    vc_client8 = vclient8
else:
    vc_client8 = PandaBot8
if Var.VC_STRING_SESSION9:
    vc_client9 = vclient9
else:
    vc_client9 = PandaBot9
if Var.VC_STRING_SESSION10:
    vc_client10 = vclient10
else:
    vc_client10 = PandaBot10
if Var.VC_STRING_SESSION11:
    vc_client11 = vclient11
else:
    vc_client11 = PandaBot11
if Var.VC_STRING_SESSION12:
    vc_client12 = vclient12
else:
    vc_client12 = PandaBot12
if Var.VC_STRING_SESSION13:
    vc_client13 = vclient13
else:
    vc_client13 = PandaBot13
if Var.VC_STRING_SESSION14:
    vc_client14 = vclient14
else:
    vc_client14 = PandaBot14
if Var.VC_STRING_SESSION15:
    vc_client15 = vclient15
else:
    vc_client15 = PandaBot15
if Var.VC_STRING_SESSION16:
    vc_client16 = vclient16
else:
    vc_client16 = PandaBot16
if Var.VC_STRING_SESSION17:
    vc_client17 = vclient17
else:
    vc_client17 = PandaBot17
if Var.VC_STRING_SESSION18:
    vc_client18 = vclient18
else:
    vc_client18 = PandaBot18
if Var.VC_STRING_SESSION19:
    vc_client19 = vclient19
else:
    vc_client19 = PandaBot19
if Var.VC_STRING_SESSION20:
    vc_client20 = vclient20
else:
    vc_client20 = PandaBot20
if Var.VC_STRING_SESSION21:
    vc_client21 = vclient21
else:
    vc_client21 = PandaBot21
if Var.VC_STRING_SESSION22:
    vc_client22 = vclient22
else:
    vc_client22 = PandaBot22
if Var.VC_STRING_SESSION23:
    vc_client23 = vclient23
else:
    vc_client23 = PandaBot23
if Var.VC_STRING_SESSION24:
    vc_client24 = vclient24
else:
    vc_client24 = PandaBot24
if Var.VC_STRING_SESSION25:
    vc_client25 = vclient25
else:
    vc_client25 = PandaBot25
if Var.VC_STRING_SESSION26:
    vc_client26 = vclient26
else:
    vc_client26 = PandaBot26
if Var.VC_STRING_SESSION27:
    vc_client27 = vclient27
else:
    vc_client27 = PandaBot27
if Var.VC_STRING_SESSION28:
    vc_client28 = vclient28
else:
    vc_client28 = PandaBot28
if Var.VC_STRING_SESSION29:
    vc_client29 = vclient29
else:
    vc_client29 = PandaBot29
if Var.VC_STRING_SESSION30:
    vc_client30 = vclient30
else:
    vc_client30 = PandaBot30
if Var.VC_STRING_SESSION31:
    vc_client31 = vclient31
else:
    vc_client31 = PandaBot31
if Var.VC_STRING_SESSION32:
    vc_client32 = vclient32
else:
    vc_client32 = PandaBot32
if Var.VC_STRING_SESSION33:
    vc_client34 = vclient34
else:
    vc_client34 = PandaBot34
if Var.VC_STRING_SESSION35:
    vc_client35 = vclient35
else:
    vc_client35 = PandaBot35
if Var.VC_STRING_SESSION36:
    vc_client36 = vclient36
else:
    vc_client36 = PandaBot36
if Var.VC_STRING_SESSION37:
    vc_client37 = vclient37
else:
    vc_client37 = PandaBot37
if Var.VC_STRING_SESSION38:
    vc_client38 = vclient38
else:
    vc_client38 = PandaBot38
if Var.VC_STRING_SESSION39:
    vc_client39 = vclient39
else:
    vc_client39 = PandaBot39
if Var.VC_STRING_SESSION40:
    vc_client40 = vclient40
else:
    vc_client40 = PandaBot40
if Var.VC_STRING_SESSION41:
    vc_client41 = vclient41
else:
    vc_client41 = PandaBot41
if Var.VC_STRING_SESSION42:
    vc_client42 = vclient42
else:
    vc_client42 = PandaBot42
if Var.VC_STRING_SESSION43:
    vc_client43 = vclient43
else:
    vc_client42 = PandaBot42
if Var.VC_STRING_SESSION43:
    vc_client43 = vclient43
else:
    vc_client43 = PandaBot43
if Var.VC_STRING_SESSION44:
    vc_client44 = vclient44
else:
    vc_client44 = PandaBot44
if Var.VC_STRING_SESSION45:
    vc_client45 = vclient45
else:
    vc_client45 = PandaBot45
if Var.VC_STRING_SESSION26:
    vc_client46 = vclient46
else:
    vc_client46 = PandaBot46
if Var.VC_STRING_SESSION47:
    vc_client47 = vclient47
else:
    vc_client47 = PandaBot47
if Var.VC_STRING_SESSION48:
    vc_client48 = vclient48
else:
    vc_client48 = PandaBot48
if Var.VC_STRING_SESSION49:
    vc_client49 = vclient49
else:
    vc_client49 = PandaBot49
if Var.VC_STRING_SESSION50:
    vc_client50 = vclient50
else:
    vc_client50 = PandaBot50
    

    
    
    

vc_player = VCTools(vc_client)
vc_player2 = VCTools(vc_client2)
vc_player3 = VCTools(vc_client3)
vc_player4 = VCTools(vc_client4)
vc_player5 = VCTools(vc_client5)
vc_player6 = VCTools(vc_client6)
vc_player7 = VCTools(vc_client7)
vc_player8 = VCTools(vc_client8)
vc_player9 = VCTools(vc_client9)
vc_player10 = VCTools(vc_client10)
vc_player11 = VCTools(vc_client11)
vc_player12 = VCTools(vc_client12)
vc_player13 = VCTools(vc_client13)
vc_player14 = VCTools(vc_client14)
vc_player15 = VCTools(vc_client15)
vc_player16 = VCTools(vc_client16)
vc_player17 = VCTools(vc_client17)
vc_player18 = VCTools(vc_client18)
vc_player19 = VCTools(vc_client19)
vc_player20 = VCTools(vc_client20)
vc_player21 = VCTools(vc_client21)
vc_player22 = VCTools(vc_client22)
vc_player23 = VCTools(vc_client23)
vc_player24 = VCTools(vc_client24)
vc_player25 = VCTools(vc_client25)
vc_player26 = VCTools(vc_client26)
vc_player27 = VCTools(vc_client27)
vc_player28 = VCTools(vc_client28)
vc_player29 = VCTools(vc_client29)
vc_player30 = VCTools(vc_client30)
vc_player31 = VCTools(vc_client31)
vc_player32 = VCTools(vc_client32)
vc_player33 = VCTools(vc_client33)
vc_player34 = VCTools(vc_client34)
vc_player35 = VCTools(vc_client35)
vc_player36 = VCTools(vc_client36)
vc_player37 = VCTools(vc_client37)
vc_player38 = VCTools(vc_client38)
vc_player39 = VCTools(vc_client39)
vc_player40 = VCTools(vc_client40)
vc_player41 = VCTools(vc_client41)
vc_player42 = VCTools(vc_client42)
vc_player43 = VCTools(vc_client43)
vc_player44 = VCTools(vc_client44)
vc_player45 = VCTools(vc_client45)
vc_player46 = VCTools(vc_client46)
vc_player47 = VCTools(vc_client47)
vc_player48 = VCTools(vc_client48)
vc_player49 = VCTools(vc_client49)
vc_player50 = VCTools(vc_client50)

@vc_player.app.on_closed_voice_chat
@vc_player2.app2.on_closed_voice_chat()
@vc_player3.app3.on_closed_voice_chat()
@vc_player4.app4.on_closed_voice_chat()
@vc_player5.app5.on_closed_voice_chat()
@vc_player6.app6.on_closed_voice_chat()
@vc_player7.app7.on_closed_voice_chat()
@vc_player8.app8.on_closed_voice_chat()
@vc_player9.app9.on_closed_voice_chat()
@vc_player10.app10.on_closed_voice_chat()
@vc_player11.app11.on_closed_voice_chat()
@vc_player12.app12.on_closed_voice_chat()
@vc_player13.app13.on_closed_voice_chat()
@vc_player14.app14.on_closed_voice_chat()
@vc_player15.app15.on_closed_voice_chat()
@vc_player16.app16.on_closed_voice_chat()
@vc_player17.app17.on_closed_voice_chat()
@vc_player18.app18.on_closed_voice_chat()
@vc_player19.app19.on_closed_voice_chat()
@vc_player21.app21.on_closed_voice_chat()
@vc_player22.app22.on_closed_voice_chat()
@vc_player23.app23.on_closed_voice_chat()
@vc_player24.app24.on_closed_voice_chat()
@vc_player25.app25.on_closed_voice_chat()
@vc_player26.app26.on_closed_voice_chat()
@vc_player27.app27.on_closed_voice_chat()
@vc_player28.app28.on_closed_voice_chat()
@vc_player29.app29.on_closed_voice_chat()
@vc_player30.app30.on_closed_voice_chat()
@vc_player31.app31.on_closed_voice_chat()
@vc_player32.app32.on_closed_voice_chat()
@vc_player33.app33.on_closed_voice_chat()
@vc_player34.app34.on_closed_voice_chat()
@vc_player35.app35.on_closed_voice_chat()
@vc_player36.app36.on_closed_voice_chat()
@vc_player37.app37.on_closed_voice_chat()
@vc_player38.app38.on_closed_voice_chat()
@vc_player39.app39.on_closed_voice_chat()
@vc_player40.app40.on_closed_voice_chat()

@vc_player41.app41.on_closed_voice_chat()
@vc_player42.app42.on_closed_voice_chat()
@vc_player43.app43.on_closed_voice_chat()
@vc_player44.app44.on_closed_voice_chat()
@vc_player45.app45.on_closed_voice_chat()
@vc_player46.app46.on_closed_voice_chat()
@vc_player47.app47.on_closed_voice_chat()
@vc_player48.app48.on_closed_voice_chat()
@vc_player49.app49.on_closed_voice_chat()
@vc_player50.app50.on_closed_voice_chat()
async def on_closed_vc(_, update):
    await _pandautils.runcmd("rm -rf temp")
    vc_player.clear_vars()
    if not vc_player.CLEANMODE:
        return
    for event in vc_player.EVENTS:
        with contextlib.suppress(Exception):
            await event.delete()


@vc_player.app.on_stream_end()
@vc_player2.app2.on_stream_end()
@vc_player3.app3.on_stream_end()
@vc_player4.app4.on_stream_end()
@vc_player5.app5.on_stream_end()
@vc_player6.app6.on_stream_end()
@vc_player7.app7.on_stream_end()
@vc_player8.app8.on_stream_end()
@vc_player9.app9.on_stream_end()
@vc_player10.app10.on_stream_end()
@vc_player11.app11.on_stream_end()
@vc_player12.app12.on_stream_end()
@vc_player13.app13.on_stream_end()
@vc_player14.app14.on_stream_end()
@vc_player15.app15.on_stream_end()
@vc_player16.app16.on_stream_end()
@vc_player17.app17.on_stream_end()
@vc_player18.app18.on_stream_end()
@vc_player18.app18.on_stream_end()
@vc_player19.app19.on_stream_end()
@vc_player20.app20.on_stream_end()
@vc_player21.app21.on_stream_end()
@vc_player22.app22.on_stream_end()
@vc_player23.app23.on_stream_end()
@vc_player24.app24.on_stream_end()
@vc_player25.app25.on_stream_end()
@vc_player26.app26.on_stream_end()
@vc_player27.app27.on_stream_end()
@vc_player28.app28.on_stream_end()
@vc_player29.app29.on_stream_end()
@vc_player30.app30.on_stream_end()
@vc_player31.app31.on_stream_end()
@vc_player32.app32.on_stream_end()
@vc_player33.app33.on_stream_end()
@vc_player34.app34.on_stream_end()
@vc_player35.app35.on_stream_end()
@vc_player36.app36.on_stream_end()
@vc_player37.app37.on_stream_end()
@vc_player38.app38.on_stream_end()
@vc_player39.app39.on_stream_end()
@vc_player40.app40.on_stream_end()
@vc_player41.app41.on_stream_end()
@vc_player42.app42.on_stream_end()
@vc_player43.app43.on_stream_end()
@vc_player44.app44.on_stream_end()
@vc_player45.app45.on_stream_end()
@vc_player46.app46.on_stream_end()
@vc_player47.app47.on_stream_end()
@vc_player48.app48.on_stream_end()
@vc_player49.app49.on_stream_end()
@vc_player50.app50.on_stream_end()
async def handler(_, update):
    event = False
    if vc_player.REPEAT:
        return await vc_player.repeat()
    if not vc_player.PLAYLIST:
        if vc_player.CHAT_ID and not vc_player.SILENT:
            return await vc_player.leave_vc()
        else:
            return
    resp = await vc_player.handle_next(update)
    print("In the end it doesnt even matter")
    buttons = [
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
    ]
    if vc_player.BOTMODE:
        if resp and type(resp) is list:
            caption = resp[1].split(f"\n\n")[1] if f"\n\n" in resp[1] else resp[1]
            event = await tgbot.send_file(
                vc_player.CHAT_ID, file=resp[0], caption=caption, buttons=buttons
            )
        elif resp and type(resp) is str:
            resp = resp.split(f"\n\n")[1] if f"\n\n" in resp else resp
            event = await tgbot.send_message(
                vc_player.CHAT_ID, resp, buttons=buttons
            )
    else:
        try:
            results = await event.client.inline_query(Config.TG_BOT_USERNAME, "vcplayer")
            event = await results[0].click(vc_player.CHAT_ID, hide_via=True)
        except Exception:
            if resp and type(resp) is list:
                caption = resp[1].split(f"\n\n")[1] if f"\n\n" in resp[1] else resp[1]
                event = await event.client.send_file(
                    vc_player.CHAT_ID, file=resp[0], caption=caption, buttons=buttons
                )
            elif resp and type(resp) is str:
                resp = resp.split(f"\n\n")[1] if f"\n\n" in resp else resp
                event = await event.client.send_message(
                    vc_player.CHAT_ID, resp, buttons=buttons
                )
    if vc_player.CLEANMODE and event:
        vc_player.EVENTS.append(event)


async def check_vcassis(event):
    chat = await event.client.get_entity(event.chat_id)
    participants = await event.client.get_participants(chat)
    assis = await vc_player.client.get_me()
    cat_ub = await event.client.get_me()
    get_id = assis.id
    ids = [int(users.id) for users in participants]
    if get_id not in ids:
        await event.edit("VC assistant will be joining shortly...")
        if isinstance(chat, types.Chat):
            chat.username = None
        if username := chat.username:
            try:
                await vc_player.client(JoinChannelRequest(username))
                await event.edit(f"VC assistant Joined {chat.title} successfully.")
            except Exception:
                await event.edit("Failed to join this chat.")
                return False
        else:
            try:
                await event.client(InviteToChannelRequest(chat.id, [get_id]))
            except Exception:
                try:
                    await vc_player.client(
                        AddContactRequest(
                            id=cat_ub.id,
                            first_name="VC",
                            last_name="Assistant",
                            phone="zarox",
                        )
                    )
                    await vc_player.client(
                        AddContactRequest(
                            id=assis.id,
                            first_name="PandaUserbot",
                            last_name="",
                            phone="zarox",
                        )
                    )
                    await event.client(InviteToChannelRequest(chat.id, [get_id]))
                except TypeError:
                    await event.client(AddChatUserRequest(chat.id, get_id, fwd_limit=1))
                except Exception:
                    await event.edit(
                        "Failed to add VC assistant. Please provide add members right or invite manually."
                    )
                    return False
    return True


async def vc_reply(event, text, file=False, firstmsg=False, dlt=False, **kwargs):
    me = await event.client.get_me()
    if vc_player.BOTMODE:
        try:
            if file:
                catevent = await tgbot.send_file(
                    event.chat_id, file=file, caption=text, **kwargs
                )
            else:
                catevent = (
                    await tgbot.send_message(event.chat_id, text, **kwargs)
                    if firstmsg
                    else await event.edit(text, **kwargs)
                )
        except Exception:
            return await event.reply(
                f"Please disable Bot Mode or Invite {Config.TG_BOT_USERNAME} to the chat"
            )
    elif file:
        try:
            results = await event.client.inline_query(
                Config.TG_BOT_USERNAME, "vcplayer"
            )
            catevent = await results[0].click(event.chat_id, hide_via=True)
        except Exception:
            catevent = await event.client.send_file(
                event.chat_id, file=file, caption=text, **kwargs
            )
    elif vc_player.PUBLICMODE:
        catevent = (
            await event.client.send_message(event.chat_id, text, **kwargs)
            if firstmsg and event.sender_id != me.id
            else await event.edit(text, **kwargs)
        )
    else:
        catevent = await edit_or_reply(event, text)
    if dlt:
        await asyncio.sleep(dlt)
        return await catevent.delete()
    if vc_player.CLEANMODE and not firstmsg:
        vc_player.EVENTS.append(catevent)
    else:
        return catevent


async def sendmsg(event, res):
    buttons = buttons = [
        [
            Button.inline("⏮ Prev", data="previousvc"),
            Button.inline("⏸ Pause", data="pausevc"),
            Button.inline("⏭ Next", data="skipvc"),
        ],
        [
            Button.inline("🔁 repeat", data="repeatvc"),
            Button.inline("≡ Mainmenu", data="menuvc"),
        ],
        [
            Button.inline("🗑 close", data="vc_close0"),
        ],
    ]
    if res:
        if isinstance(res, list):
            await event.delete()
            event = await vc_reply(event, res[1], file=res[0], buttons=buttons)
        elif isinstance(res, tuple):
            event = await vc_reply(event, res[0], dlt=15)
        elif isinstance(res, str):
            event = await vc_reply(event, res, buttons=buttons)

if Var.VC_STRING_SESSION:
    asyncio.create_task(vc_player.start())
if Var.VC_STRING_SESSION2:
    asyncio.create_task(vc_player2.start())
if Var.VC_STRING_SESSION3:
    asyncio.create_task(vc_player3.start())
if Var.VC_STRING_SESSION4:
    asyncio.create_task(vc_player4.start())
if Var.VC_STRING_SESSION5:
    asyncio.create_task(vc_player5.start())
if Var.VC_STRING_SESSION6:
    asyncio.create_task(vc_player6.start())
if Var.VC_STRING_SESSION7:
    asyncio.create_task(vc_player7.start())
if Var.VC_STRING_SESSION8:
    asyncio.create_task(vc_player8.start())
if Var.VC_STRING_SESSION9:
    asyncio.create_task(vc_player9.start())
if Var.VC_STRING_SESSION10:
    asyncio.create_task(vc_player11.start())
if Var.VC_STRING_SESSION12:
    asyncio.create_task(vc_player12.start())
if Var.VC_STRING_SESSION13:
    asyncio.create_task(vc_player13.start())
if Var.VC_STRING_SESSION14:
    asyncio.create_task(vc_player14.start())
if Var.VC_STRING_SESSION15:
    asyncio.create_task(vc_player15.start())
if Var.VC_STRING_SESSION16:
    asyncio.create_task(vc_player16.start())
if Var.VC_STRING_SESSION17:
    asyncio.create_task(vc_player17.start())

if Var.VC_STRING_SESSION18:
    asyncio.create_task(vc_player18.start())
if Var.VC_STRING_SESSION19:
    asyncio.create_task(vc_player19.start())
if Var.VC_STRING_SESSION20:
    asyncio.create_task(vc_player20.start())
if Var.VC_STRING_SESSION21:
    asyncio.create_task(vc_player21.start())
if Var.VC_STRING_SESSION22:
    asyncio.create_task(vc_player22.start())
if Var.VC_STRING_SESSION23:
    asyncio.create_task(vc_player23.start())
if Var.VC_STRING_SESSION24:
    asyncio.create_task(vc_player24.start())
if Var.VC_STRING_SESSION25:
    asyncio.create_task(vc_player25.start())
if Var.VC_STRING_SESSION26:
    asyncio.create_task(vc_player26.start())
    
if Var.VC_STRING_SESSION27:
    asyncio.create_task(vc_player27.start())
if Var.VC_STRING_SESSION28:
    asyncio.create_task(vc_player28.start())
if Var.VC_STRING_SESSION29:
    asyncio.create_task(vc_player29.start())
if Var.VC_STRING_SESSION30:
    asyncio.create_task(vc_player30.start())
if Var.VC_STRING_SESSION31:
    asyncio.create_task(vc_player31.start())
if Var.VC_STRING_SESSION32:
    asyncio.create_task(vc_player32.start())
if Var.VC_STRING_SESSION33:
    asyncio.create_task(vc_player33.start())
if Var.VC_STRING_SESSION34:
    asyncio.create_task(vc_player34.start())
if Var.VC_STRING_SESSION35:
    asyncio.create_task(vc_player35.start())
if Var.VC_STRING_SESSION36:
    asyncio.create_task(vc_player36.start())

if Var.VC_STRING_SESSION37:
    asyncio.create_task(vc_player37.start())
if Var.VC_STRING_SESSION38:
    asyncio.create_task(vc_player38.start())
if Var.VC_STRING_SESSION39:
    asyncio.create_task(vc_player39.start())
if Var.VC_STRING_SESSION40:
    asyncio.create_task(vc_player40.start())
if Var.VC_STRING_SESSION41:
    asyncio.create_task(vc_player41.start())
if Var.VC_STRING_SESSION42:
    asyncio.create_task(vc_player42.start())
if Var.VC_STRING_SESSION43:
    asyncio.create_task(vc_player43.start())
if Var.VC_STRING_SESSION44:
    asyncio.create_task(vc_player44.start())
if Var.VC_STRING_SESSION45:
    asyncio.create_task(vc_player45.start())
if Var.VC_STRING_SESSION46:
    asyncio.create_task(vc_player46.start())

if Var.VC_STRING_SESSION47:
    asyncio.create_task(vc_player47.start())
if Var.VC_STRING_SESSION48:
    asyncio.create_task(vc_player48.start())

if Var.VC_STRING_SESSION49:
    asyncio.create_task(vc_player49.start())
if Var.VC_STRING_SESSION50:
    asyncio.create_task(vc_player50.start())
