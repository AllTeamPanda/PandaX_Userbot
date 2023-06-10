import asyncio
import contextlib
from pathlib import Path

import requests
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    NodeJSNotInstalled,
    NotInGroupCallError,
    TooOldNodeJSVersion,
)
from pytgcalls.types import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from telethon import functions
from telethon.errors import ChatAdminRequiredError
from userbot.Session import *
from userbot._misc.logger import logging
from userbot.helpers import _pandautils, fileinfo
from userbot.helpers.functions import get_ytthumb, yt_search
from yt_dlp import YoutubeDL

from .stream_helper import Stream, check_url, video_dl, yt_regex

LOGS = logging.getLogger(__name__)


class VCTools:
    def __init__(self, client) -> None:
        self.app = PyTgCalls(client, overload_quiet_mode=True)
        self.app2 = PyTgCalls(client, overload_quiet_mode=True)
        self.app3 = PyTgCalls(client, overload_quiet_mode=True)
        self.app4 = PyTgCalls(client, overload_quiet_mode=True)
        self.app5 = PyTgCalls(client, overload_quiet_mode=True)
        self.app6 = PyTgCalls(client, overload_quiet_mode=True)
        self.app7 = PyTgCalls(client, overload_quiet_mode=True)
        self.app8 = PyTgCalls(client, overload_quiet_mode=True)
        self.app9 = PyTgCalls(client, overload_quiet_mode=True)
        self.app10 = PyTgCalls(client, overload_quiet_mode=True)
        self.app11 = PyTgCalls(client, overload_quiet_mode=True)
        self.app12 = PyTgCalls(client, overload_quiet_mode=True)
        self.app13 = PyTgCalls(client, overload_quiet_mode=True)
        self.app14 = PyTgCalls(client, overload_quiet_mode=True)
        self.app15 = PyTgCalls(client, overload_quiet_mode=True)
        self.app16 = PyTgCalls(client, overload_quiet_mode=True)
        self.app17 = PyTgCalls(client, overload_quiet_mode=True)
        self.app18 = PyTgCalls(client, overload_quiet_mode=True)
        self.app19 = PyTgCalls(client, overload_quiet_mode=True)
        self.app20 = PyTgCalls(client, overload_quiet_mode=True)
        self.app21 = PyTgCalls(client, overload_quiet_mode=True)
        self.app22 = PyTgCalls(client, overload_quiet_mode=True)
        self.app23 = PyTgCalls(client, overload_quiet_mode=True)
        self.app24 = PyTgCalls(client, overload_quiet_mode=True)

        self.app25 = PyTgCalls(client, overload_quiet_mode=True)
        self.app26 = PyTgCalls(client, overload_quiet_mode=True)
        self.app27 = PyTgCalls(client, overload_quiet_mode=True)
        self.app28 = PyTgCalls(client, overload_quiet_mode=True)
        self.app29 = PyTgCalls(client, overload_quiet_mode=True)
        self.app30 = PyTgCalls(client, overload_quiet_mode=True)
        self.app31 = PyTgCalls(client, overload_quiet_mode=True)
        self.app32 = PyTgCalls(client, overload_quiet_mode=True)
        self.app33 = PyTgCalls(client, overload_quiet_mode=True)
        self.app34 = PyTgCalls(client, overload_quiet_mode=True)

        self.app35 = PyTgCalls(client, overload_quiet_mode=True)
        self.app36 = PyTgCalls(client, overload_quiet_mode=True)
        self.app37 = PyTgCalls(client, overload_quiet_mode=True)
        self.app38 = PyTgCalls(client, overload_quiet_mode=True)
        self.app39 = PyTgCalls(client, overload_quiet_mode=True)
        self.app40 = PyTgCalls(client, overload_quiet_mode=True)
        self.app41 = PyTgCalls(client, overload_quiet_mode=True)
        self.app42 = PyTgCalls(client, overload_quiet_mode=True)
        self.app43 = PyTgCalls(client, overload_quiet_mode=True)
        self.app44 = PyTgCalls(client, overload_quiet_mode=True)
        self.app45 = PyTgCalls(client, overload_quiet_mode=True)
        self.app46 = PyTgCalls(client, overload_quiet_mode=True)
        self.app47 = PyTgCalls(client, overload_quiet_mode=True)
        self.app48 = PyTgCalls(client, overload_quiet_mode=True)
        self.app49 = PyTgCalls(client, overload_quiet_mode=True)
        self.app50 = PyTgCalls(client, overload_quiet_mode=True)
        self.client = client
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []
        self.PREVIOUS = []
        self.EVENTS = []
        self.SILENT = False
        self.PUBLICMODE = False
        self.BOTMODE = False
        self.CLEANMODE = True
        self.REPEAT = False

    def clear_vars(self):
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []
        self.PREVIOUS = []
        self.EVENTS = []
        self.REPEAT = False

    async def start(self):
        if vclient:
            await self.app.start()
        if vclient2:
            await self.app2.start()
        if vclient3:
            await self.app3.start()
        if vclient4:
            await self.app4.start()
        if vclient5:
            await self.app.start()
        if vclient6:
            await self.app6.start()
        if vclient7:
            await self.app7.start()
        if vclient8:
            await self.app8.start()
        if vclient9:
            await self.app9.start()
        if vclient10:
            await self.app10.start()
        if vclient11:
            await self.app11.start()
        if vclient12:
            await self.app12.start()
        if vclient13:
            await self.app13.start()
        if vclient14:
            await self.app14.start()
        if vclient15:
            await self.app15.start()
        if vclient16:
            await self.app16.start()
        if vclient17:
            await self.app17.start()
        if vclient18:
            await self.app18.start()
        if vclient19:
            await self.app19.start()
        if vclient20:
            await self.app20.start()
        if vclient21:
            await self.app21.start()
        if vclient22:
            await self.app22.start()
        if vclient23:
            await self.app23.start()
        if vclient24:
            await self.app24.start()
        if vclient25:
            await self.app25.start()
        if vclient26:
            await self.app26.start()
        if vclient27:
            await self.app27.start()
        if vclient28:
            await self.app28.start()
        if vclient29:
            await self.app29.start()
        if vclient30:
            await self.app30.start()
        if vclient31:
            await self.app31.start()
        if vclient32:
            await self.app32.start()
        if vclient33:
            await self.app33.start()
        if vclient34:
            await self.app34.start()
        if vclient35:
            await self.app35.start()
        if vclient36:
            await self.app36.start()
        if vclient37:
            await self.app37.start()
        if vclient38:
            await self.app38.start()
        if vclient39:
            await self.app39.start()
        if vclient40:
            await self.app41.start()
        if vclient42:
            await self.app42.start()
        if vclient43:
            await self.app43.start()
        if vclient44:
            await self.app44.start()
        if vclient45:
            await self.app45.start()
        if vclient46:
            await self.app46.start()
        if vclient47:
            await self.app47.start()
        if vclient48:
            await self.app48.start()
        if vclient49:
            await self.app49.start()
        if vclient50:
            await self.app50.start()
        
          
    async def join_vc(self, chat, join_as=None):
        self.SILENT = True
        if self.CHAT_ID:
            return f"Already in a group call on {self.CHAT_NAME}"
        if join_as:
            try:
                join_as_chat = await self.client.get_entity(int(join_as))
                join_as_title = f" as **{join_as_chat.title}**"
            except ValueError:
                return "Give Chat Id for joining as"
        else:
            join_as_chat = await self.client.get_me()
            join_as_title = ""
        try:
            if vclient:
                await self.app.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient2:
                await self.app2.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient3:
                await self.app3.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient4:
                await self.app4.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient5:
                await self.app5.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient6:
                await self.app6.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient7:
                await self.app7.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient8:
                await self.app8.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient9:
                await self.app9.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient10:
                await self.app10.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient11:
                await self.app11.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient12:
                await self.app12.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient13:
                await self.app13.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient14:
                await self.app14.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient15:
                await self.app15.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient16:
                await self.app16.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient17:
                await self.app17.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient18:
                await self.app18.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient19:
                await self.app19.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient20:
                await self.app20.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient21:
                await self.app21.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient22:
                await self.app22.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient23:
                await self.app23.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient24:
                await self.app24.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient25:
                await self.app25.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient26:
                await self.app26.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient27:
                await self.app27.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient28:
                await self.app28.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient29:
                await self.app29.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient30:
                await self.app30.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient31:
                await self.app31.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient32:
                await self.app32.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient33:
                await self.app33.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient34:
                await self.app34.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient35:
                await self.app35.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient36:
                await self.app36.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            
            if vclient37:
                await self.app37.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient38:
                await self.app38.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient39:
                await self.app39.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient40:
                await self.app40.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient41:
                await self.app41.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient42:
                await self.app42.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient43:
                await self.app43.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient44:
                await self.app44.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient45:
                await self.app45.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient46:
                await self.app46.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient47:
                await self.app47.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient48:
                await self.app48.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient49:
                await self.app49.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )
            if vclient50:
                await self.app50.join_group_call(
                    chat_id=chat.id,
                    stream=AudioPiped("userbot/resources/literasi.mp3"),
                    join_as=join_as_chat,
                    stream_type=StreamType().pulse_stream,
                )

        except NoActiveGroupCall:
            try:
                vcchat = await self.client.get_entity(-chat.id)
                await self.client(
                    functions.phone.CreateGroupCallRequest(
                        peer=vcchat,
                        title="Panda VC 🎶",
                    )
                )
                await self.join_vc(chat=chat, join_as=join_as)
            except ChatAdminRequiredError:
                try:
                    if PandaBot:
                        await PandaBot(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot2:
                        await PandaBot2(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot3:
                        await PandaBot3(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot4:
                        await PandaBot4(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot5:
                        await PandaBot5(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot6:
                        await PandaBot6(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot7:
                        await PandaBot7(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot8:
                        await PandaBot8(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot9:
                        await PandaBot9(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot10:
                        await PandaBot10(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot11:
                        await PandaBot11(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot12:
                        await PandaBot12(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot13:
                        await PandaBot13(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot14:
                        await PandaBot14(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot15:
                        await PandaBot15(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot16:
                        await PandaBot16(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot17:
                        await PandaBot17(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot18:
                        await PandaBot18(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot19:
                        await PandaBot19(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot20:
                        await PandaBot20(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot21:
                        await PandaBot21(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot22:
                        await PandaBot22(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot23:
                        await PandaBot23(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot24:
                        await PandaBot24(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot25:
                        await PandaBot25(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot26:
                        await PandaBot26(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot27:
                        await PandaBot27(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot28:
                        await PandaBot28(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot29:
                        await PandaBot29(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot30:
                        await PandaBot30(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot31:
                        await PandaBot31(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot32:
                        await PandaBot32(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot33:
                        await PandaBot33(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot34:
                        await PandaBot34(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot35:
                        await PandaBot35(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot36:
                        await PandaBot36(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot37:
                        await PandaBot37(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                      
                    if PandaBot38:
                        await PandaBot38(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot39:
                        await PandaBot39(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot40:
                        await PandaBot40(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot41:
                        await PandaBot41(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot42:
                        await PandaBot42(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot43:
                        await PandaBot43(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                        
                    if PandaBot44:
                        await PandaBot44(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot45:
                        await PandaBot45(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot46:
                        await PandaBot46(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot47:
                        await PandaBot47(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot48:
                        await PandaBot48(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot49:
                        await PandaBot49(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    if PandaBot50:
                        await PandaBot50(
                            functions.phone.CreateGroupCallRequest(
                                peer=chat,
                                title="Panda VC 🎶",
                            )
                        )
                    
                    await self.join_vc(chat=chat, join_as=join_as)
                except ChatAdminRequiredError:
                    return "You need to become an admin to start VC, or ask admins to start"
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return "Latest version of NodeJs is not installed"
        except AlreadyJoinedError:
            if vclient:
                await self.app.leave_group_call(chat.id)
            if vclient2:
                await self.app2.leave_group_call(chat.id)
            if vclient3:
                await self.app3.leave_group_call(chat.id)
            if vclient4:
                await self.app4.leave_group_call(chat.id)
            if vclient5:
                await self.app5.leave_group_call(chat.id)
            if vclient6:
                await self.app6.leave_group_call(chat.id)
            if vclient7:
                await self.app7.leave_group_call(chat.id)
            if vclient8:
                await self.app8.leave_group_call(chat.id)
            if vclient9:
                await self.app9.leave_group_call(chat.id)
            if vclient10:
                await self.app10.leave_group_call(chat.id)
            if vclient11:
                await self.app11.leave_group_call(chat.id)
            if vclient12:
                await self.app12.leave_group_call(chat.id)
            if vclient13:
                await self.app13.leave_group_call(chat.id)
            if vclient14:
                await self.app14.leave_group_call(chat.id)
            if vclient15:
                await self.app15.leave_group_call(chat.id)
            if vclient16:
                await self.app16.leave_group_call(chat.id)
            if vclient17:
                await self.app17.leave_group_call(chat.id)
            if vclient18:
                await self.app18.leave_group_call(chat.id)
            if vclient19:
                await self.app19.leave_group_call(chat.id)
            if vclient20:
                await self.app20.leave_group_call(chat.id)
            if vclient21:
                await self.app21.leave_group_call(chat.id)
            if vclient22:
                await self.app22.leave_group_call(chat.id)
            if vclient23:
                await self.app23.leave_group_call(chat.id)
            if vclient24:
                await self.app24.leave_group_call(chat.id)
            if vclient25:
                await self.app25.leave_group_call(chat.id)
            if vclient26:
                await self.app26.leave_group_call(chat.id)
            if vclient27:
                await self.app27.leave_group_call(chat.id)
            if vclient28:
                await self.app28.leave_group_call(chat.id)
            if vclient29:
                await self.app29.leave_group_call(chat.id)
            if vclient30:
                await self.app30.leave_group_call(chat.id)
            if vclient31:
                await self.app21.leave_group_call(chat.id)
            if vclient32:
                await self.app32.leave_group_call(chat.id)
            if vclient33:
                await self.app33.leave_group_call(chat.id)
            if vclient34:
                await self.app34.leave_group_call(chat.id)
            if vclient35:
                await self.app35.leave_group_call(chat.id)
            if vclient36:
                await self.app36.leave_group_call(chat.id)
            if vclient37:
                await self.app37.leave_group_call(chat.id)
            if vclient38:
                await self.app38.leave_group_call(chat.id)
            if vclient40:
                await self.app40.leave_group_call(chat.id)
            if vclient41:
                await self.app41.leave_group_call(chat.id)
            if vclient42:
                await self.app42.leave_group_call(chat.id)
            if vclient43:
                await self.app43.leave_group_call(chat.id)
            if vclient44:
                await self.app44.leave_group_call(chat.id)
            if vclient45:
                await self.app45.leave_group_call(chat.id)
            if vclient46:
                await self.app46.leave_group_call(chat.id)
            if vclient47:
                await self.app47.leave_group_call(chat.id)
            if vclient48:
                await self.app48.leave_group_call(chat.id)
            if vclient49:
                await self.app49.leave_group_call(chat.id)
            if vclient50:
                await self.app50.leave_group_call(chat.id)
            
            await asyncio.sleep(3)
            await self.join_vc(chat=chat, join_as=join_as)
        self.CHAT_ID = chat.id
        self.CHAT_NAME = chat.title
        return f"Joined VC of **{chat.title}**{join_as_title}"

    async def leave_vc(self):
        with contextlib.suppress(NotInGroupCallError, NoActiveGroupCall):
            if vclient:
                await self.app.leave_group_call(self.CHAT_ID)
            if vclient2:
                await self.app2.leave_group_call(self.CHAT_ID)
            if vclient3:
                await self.app3.leave_group_call(self.CHAT_ID)
            if vclient4:
                await self.app4.leave_group_call(self.CHAT_ID)
            if vclient5:
                await self.app5.leave_group_call(self.CHAT_ID)
            if vclient6:
                await self.app6.leave_group_call(self.CHAT_ID)
            
            if vclient7:
                await self.app7.leave_group_call(self.CHAT_ID)
            if vclient8:
                await self.app8.leave_group_call(self.CHAT_ID)
            if vclient9:
                await self.app9.leave_group_call(self.CHAT_ID)
            if vclient10:
                await self.app10.leave_group_call(self.CHAT_ID)
            if vclient11:
                await self.app11.leave_group_call(self.CHAT_ID)
            if vclient12:
                await self.app12leave_group_call(self.CHAT_ID)
            if vclient13:
                await self.app13.leave_group_call(self.CHAT_ID)
            if vclient14:
                await self.app14.leave_group_call(self.CHAT_ID)
            if vclient15:
                await self.app15.leave_group_call(self.CHAT_ID)
            if vclient16:
                await self.app16.leave_group_call(self.CHAT_ID)
            if vclient17:
                await self.app17.leave_group_call(self.CHAT_ID)
            if vclient18:
                await self.app18.leave_group_call(self.CHAT_ID)
            if vclient19:
                await self.app19.leave_group_call(self.CHAT_ID)
            if vclient20:
                await self.app20.leave_group_call(self.CHAT_ID)
            if vclient21:
                await self.app21.leave_group_call(self.CHAT_ID)
            if vclient22:
                await self.app22.leave_group_call(self.CHAT_ID)
            if vclient23:
                await self.app23.leave_group_call(self.CHAT_ID)
            if vclient24:
                await self.app24.leave_group_call(self.CHAT_ID)
            if vclient25:
                await self.app25.leave_group_call(self.CHAT_ID)
            if vclient26:
                await self.app26.leave_group_call(self.CHAT_ID)
            if vclient27:
                await self.app27.leave_group_call(self.CHAT_ID)
            if vclient28:
                await self.app28.leave_group_call(self.CHAT_ID)
            if vclient29:
                await self.app29.leave_group_call(self.CHAT_ID)
            if vclient30:
                await self.app30.leave_group_call(self.CHAT_ID)
            if vclient31:
                await self.app31.leave_group_call(self.CHAT_ID)
            if vclient32:
                await self.app32.leave_group_call(self.CHAT_ID)
            if vclient33:               
                await self.app33.leave_group_call(self.CHAT_ID)
            if vclient34:
                await self.app34.leave_group_call(self.CHAT_ID)
            if vclient35:
                await self.app35.leave_group_call(self.CHAT_ID)
            if vclient36:
                await self.app36.leave_group_call(self.CHAT_ID)
            if vclient37:
                await self.app37.leave_group_call(self.CHAT_ID)
            if vclient38:
                await self.app38.leave_group_call(self.CHAT_ID)
            if vclient39:
                await self.app39.leave_group_call(self.CHAT_ID)
            if vclient40:
                await self.app40.leave_group_call(self.CHAT_ID)
            if vclient41:
                await self.app41.leave_group_call(self.CHAT_ID)
            if vclient42:
                await self.app42.leave_group_call(self.CHAT_ID)
            if vclient43:
                await self.app43.leave_group_call(self.CHAT_ID)
            if vclient44:
                await self.app44.leave_group_call(self.CHAT_ID)
            if vclient45:
                await self.app45.leave_group_call(self.CHAT_ID)
            if vclient46:
                await self.app46.leave_group_call(self.CHAT_ID)
            if vclient47:
                await self.app47.leave_group_call(self.CHAT_ID)
            if vclient47:
                await self.app47.leave_group_call(self.CHAT_ID)
            if vclient48:
                await self.app48.leave_group_call(self.CHAT_ID)
            if vclient49:
                await self.app49.leave_group_call(self.CHAT_ID)
            if vclient50:
                await self.app50.leave_group_call(self.CHAT_ID)
        
        await _pandautils.runcmd("rm -rf temp")
        self.clear_vars()
        if not self.CLEANMODE:
            return
        for event in self.EVENTS:
            with contextlib.suppress(Exception):
                await event.delete()

    async def duration(self, name):
        int_ = int(name)
        ute, ond_ = divmod(int_, 60)
        ond = f"0{ond_}" if int(ond_) in list(range(10)) else ond_
        return f"{ute}:{ond}"

    async def play_song(
        self,
        event,
        input,
        stream=Stream.audio,
        force=False,
        reply=False,
        prev=False,
        **kwargs,
    ):
        yt_url = False
        img = False
        if not input:
            return
        if reply:
            path = Path(input[0])
            if not path.exists():
                return "`File Path is invalid`"
            if not path.name.endswith(
                (".mkv", ".mp4", ".webm", ".m4v", ".mp3", ".flac", ".wav", ".m4a")
            ):
                return "`File is invalid for Streaming`"
            playable = str(path.absolute())
            title = path.name
            duration = await self.duration(reply.file.duration)
            img = input[1]
            url = f"https://t.me/c/{str(abs(reply.chat_id))[3:] if str(abs(reply.chat_id)).startswith('100') else abs(reply.chat_id)}/{reply.id}"
        elif yt_regex.match(input):
            yt_url = input
        elif check_url(input):
            try:
                res = requests.get(input, allow_redirects=True, stream=True)
                ctype = res.headers.get("Content-Type")
                if not any(opt in ctype for opt in ["video", "audio"]):
                    return "**INVALID URL**"
                if name := res.headers.get("Content-Disposition", None):
                    title = name.split('="')[0].split('"') or ""
                else:
                    title = input
                playable = input
                url = input
                img = (
                    "https://telegra.ph/file/c910a0ee1b10cfe0ef9db.jpg"
                )
                seconds = (await fileinfo(input))["duration"]
                duration = await self.duration(seconds)
            except Exception as e:
                return f"**INVALID URL**\n\n{e}"
        else:
            path = Path(input)
            if path.exists():
                if not path.name.endswith(
                    (".mkv", ".mp4", ".webm", ".m4v", ".mp3", ".flac", ".wav", ".m4a")
                ):
                    return "`File is invalid for Streaming`"
                playable = str(path.absolute())
                title = path.name
                if kwargs:
                    duration = kwargs["duration"]
                    url = kwargs["url"]
                    img = kwargs["img"]
                else:
                    img = "https://telegra.ph/file/c910a0ee1b10cfe0ef9db.jpg"
                    seconds = (await fileinfo(path))["duration"]
                    duration = await self.duration(seconds)
                    url = ""
            else:
                yt_url = await yt_search(input)

        if yt_url:
            with YoutubeDL({}) as ytdl:
                ytdl_data = ytdl.extract_info(yt_url, download=False)

                title = ytdl_data.get("title", None)
            if not title:
                return "Error Fetching URL"

            await event.edit("`Downloading...`")
            playable = await video_dl(yt_url, title)
            img = await get_ytthumb(ytdl_data["id"])
            duration = await self.duration(ytdl_data["duration"])
            url = yt_url

        msg = f"**🎧 Playing:** [{title}]({url})\n"
        msg += f"**⏳ Duration:** `{duration}`\n"
        msg += f"**💭 Chat:** `{self.CHAT_NAME}`"
        LOGS.info(playable)
        if self.PLAYING and not force:
            self.PLAYLIST.append(
                {
                    "title": title,
                    "path": playable,
                    "stream": stream,
                    "img": img,
                    "duration": duration,
                    "url": url,
                }
            )
            return (
                f"**🎧 Added to playlist:** [{title}]({url})\n\n👾 Position: {len(self.PLAYLIST)+1}",
                0,
            )
        if not self.PLAYING:
            self.PLAYLIST.append(
                {
                    "title": title,
                    "path": playable,
                    "stream": stream,
                    "img": img,
                    "duration": duration,
                    "url": url,
                }
            )
            await self.skip()
            return [img, msg] if img else msg
        if force:
            self.PLAYLIST.insert(
                0,
                {
                    "title": title,
                    "path": playable,
                    "stream": stream,
                    "img": img,
                    "duration": duration,
                    "url": url,
                },
            )
            await self.skip(prev=prev)
            return [img, msg] if img else msg

    async def handle_next(self, update):
        if isinstance(update, StreamAudioEnded):
            return await self.skip()

    async def skip(self, clear=False, prev=False):
        self.SILENT = False
        if clear:
            self.PLAYLIST = []
        if prev:
            self.PREVIOUS.pop(-1)
            self.PLAYLIST.insert(1, self.PLAYING)
        elif self.PLAYING:
            self.PREVIOUS.append(self.PLAYING)
        # log chat name
        if not self.PLAYLIST:
            if self.PLAYING:
                                        
                if vclient:
                    await self.app.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient2:
                    await self.app2.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient3:
                    await self.app3.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient4:
                    await self.app4.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient5:
                    await self.app5.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    ) 
                if vclient6:
                    await self.app6.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient7:
                    await self.app7.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient8:
                    await self.app8.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient9:
                    await self.app9.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient10:
                    await self.app10.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient11:
                    await self.app11.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient12:
                    await self.app12.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient13:
                    await self.app13.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient14:
                    await self.app114.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient15:
                    await self.app15.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient16:
                    await self.app16.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient17:
                    await self.app17.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient18:
                    await self.app18.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient19:
                    await self.app19.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient20:
                    await self.app20.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                                        
                    
                if vclient21:
                    await self.app21.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient22:
                    await self.app22.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient23:
                    await self.app23.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient24:
                    await self.app24.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient25:
                    await self.app25.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                                        
                    
                if vclient26:
                    await self.app26.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient27:
                    await self.app27.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient28:
                    await self.app28.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient29:
                    await self.app29.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient30:
                    await self.app30.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                                                            
                if vclient31:
                    await self.app31.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient32:
                    await self.app32.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient33:
                    await self.app33.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient34:
                    await self.app34.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient35:
                    await self.app35.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient36:
                    await self.app36.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient37:
                    await self.app37.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient38:
                    await self.app38.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient39:
                    await self.app39.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient40:
                    await self.app40.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                
                if vclient41:
                    await self.app41.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient42:
                    await self.app42.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient43:
                    await self.app43.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient44:
                    await self.app44.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient45:
                    await self.app45.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient46:
                    await self.app46.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient47:
                    await self.app47.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient48:
                    await self.app48.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient49:
                    await self.app49.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                if vclient50:
                    await self.app50.change_stream(
                        self.CHAT_ID,
                        AudioPiped("userbot/resources/literasi.mp3"),
                    )
                
            self.PLAYING = False
            return "**Skipped Stream\nEmpty Playlist**"

        next_song = self.PLAYLIST.pop(0)
        if next_song["stream"] == Stream.audio:
            streamable = AudioPiped(next_song["path"])
        else:
            streamable = AudioVideoPiped(next_song["path"])
        try:
            if vclient:
                await self.app.change_stream(self.CHAT_ID, streamable)
            if vclient2:
                await self.app2.change_stream(self.CHAT_ID, streamable)
            if vclient3:
                await self.app3.change_stream(self.CHAT_ID, streamable)
            if vclient4:
                await self.app4.change_stream(self.CHAT_ID, streamable)
            if vclient5:
                await self.app5.change_stream(self.CHAT_ID, streamable)
            if vclient6:
                await self.app6.change_stream(self.CHAT_ID, streamable)
            if vclient7:
                await self.app7.change_stream(self.CHAT_ID, streamable)
            if vclient8:
                await self.app8.change_stream(self.CHAT_ID, streamable)
            if vclient9:
                await self.app9.change_stream(self.CHAT_ID, streamable)
            if vclient10:
                await self.app10.change_stream(self.CHAT_ID, streamable)
            if vclient11:
                await self.app11.change_stream(self.CHAT_ID, streamable)
            if vclient12:
                await self.app12.change_stream(self.CHAT_ID, streamable)
            if vclient13:
                await self.app13.change_stream(self.CHAT_ID, streamable)
            if vclient14:
                await self.app14.change_stream(self.CHAT_ID, streamable)
            if vclient15:
                await self.app15.change_stream(self.CHAT_ID, streamable)
            if vclient16:
                await self.app16.change_stream(self.CHAT_ID, streamable)
            if vclient17:
                await self.app17.change_stream(self.CHAT_ID, streamable)
            if vclient18:
                await self.app18.change_stream(self.CHAT_ID, streamable)
            if vclient19:
                await self.app19.change_stream(self.CHAT_ID, streamable)
            if vclient20:
                await self.app20.change_stream(self.CHAT_ID, streamable)
            if vclient21:
                await self.app21.change_stream(self.CHAT_ID, streamable)
            if vclient22:
                await self.app22.change_stream(self.CHAT_ID, streamable)
            if vclient23:
                await self.app23.change_stream(self.CHAT_ID, streamable)
            if vclient24:
                await self.app24.change_stream(self.CHAT_ID, streamable)
            if vclient25:
                await self.app25.change_stream(self.CHAT_ID, streamable)
            if vclient26:
                await self.app26.change_stream(self.CHAT_ID, streamable)
            if vclient27:
                await self.app27.change_stream(self.CHAT_ID, streamable)
            if vclient28:
                await self.app28.change_stream(self.CHAT_ID, streamable)
                
            if vclient29:
                await self.app29.change_stream(self.CHAT_ID, streamable)
            if vclient30:
                await self.app30.change_stream(self.CHAT_ID, streamable)
            if vclient31:
                await self.app31.change_stream(self.CHAT_ID, streamable)
            if vclient32:
                await self.app32.change_stream(self.CHAT_ID, streamable)
            if vclient33:
                await self.app33.change_stream(self.CHAT_ID, streamable)
            if vclient34:
                await self.app34.change_stream(self.CHAT_ID, streamable)
            if vclient35:
                await self.app35.change_stream(self.CHAT_ID, streamable)
            if vclient36:
                await self.app36.change_stream(self.CHAT_ID, streamable)
            if vclient37:
                await self.app37.change_stream(self.CHAT_ID, streamable)
            if vclient38:
                await self.app38.change_stream(self.CHAT_ID, streamable)
            if vclient39:
                await self.app39.change_stream(self.CHAT_ID, streamable)
            if vclient40:
                await self.app40.change_stream(self.CHAT_ID, streamable)
            if vclient41:
                await self.app41.change_stream(self.CHAT_ID, streamable)
            if vclient42:
                await self.app42.change_stream(self.CHAT_ID, streamable)
            if vclient43:
                await self.app43.change_stream(self.CHAT_ID, streamable)
            if vclient44:
                await self.app44.change_stream(self.CHAT_ID, streamable)
            if vclient45:
                await self.app45.change_stream(self.CHAT_ID, streamable)
            if vclient46:
                await self.app46.change_stream(self.CHAT_ID, streamable)
            if vclient47:
                await self.app47.change_stream(self.CHAT_ID, streamable)
            if vclient48:
                await self.app48.change_stream(self.CHAT_ID, streamable)
            if vclient49:
                await self.app49.change_stream(self.CHAT_ID, streamable)
            if vclient50:
                await self.app50.change_stream(self.CHAT_ID, streamable)
       
        except Exception:
            await self.skip()
        self.PLAYING = next_song
        msg = f"**🌬 Skipped Stream**\n\n"
        msg += f"**🎧 Playing:** [{next_song['title']}]({next_song['url']})\n"
        msg += f"**⏳ Duration:** `{next_song['duration']}`\n"
        msg += f"**💭 Chat:** `{self.CHAT_NAME}`"
        return [next_song["img"], msg] if next_song["img"] else msg

    async def repeat(self):
        if next_song := self.PLAYING:
            if next_song["stream"] == Stream.audio:
                streamable = AudioPiped(next_song["path"])
            else:
                streamable = AudioVideoPiped(next_song["path"])
            try:
                if vclient:
                    await self.app.change_stream(self.CHAT_ID, streamable)
                if vclient2:
                    await self.app2.change_stream(self.CHAT_ID, streamable)
                if vclient3:
                    await self.app3.change_stream(self.CHAT_ID, streamable)
                if vclient4:
                    await self.app4.change_stream(self.CHAT_ID, streamable)
                if vclient5:
                    await self.app5.change_stream(self.CHAT_ID, streamable)
                if vclient6:
                    await self.app6.change_stream(self.CHAT_ID, streamable)
                if vclient7:
                    await self.app7.change_stream(self.CHAT_ID, streamable)
                if vclient8:
                    await self.app8.change_stream(self.CHAT_ID, streamable)
                if vclient9:
                    await self.app9.change_stream(self.CHAT_ID, streamable)
                if vclient10:
                    await self.app10.change_stream(self.CHAT_ID, streamable)
                if vclient11:
                    await self.app11.change_stream(self.CHAT_ID, streamable)
                if vclient12:
                    await self.app12.change_stream(self.CHAT_ID, streamable)
                if vclient13:
                    await self.app13.change_stream(self.CHAT_ID, streamable)
                if vclient14:
                    await self.app14.change_stream(self.CHAT_ID, streamable)
                if vclient15:
                    await self.app15.change_stream(self.CHAT_ID, streamable)
                if vclient16:
                    await self.app16.change_stream(self.CHAT_ID, streamable)
                if vclient17:
                    await self.app17.change_stream(self.CHAT_ID, streamable)
                if vclient18:
                    await self.app18.change_stream(self.CHAT_ID, streamable)
                if vclient19:
                    await self.app19.change_stream(self.CHAT_ID, streamable)
                if vclient20:
                    await self.app20.change_stream(self.CHAT_ID, streamable)
                if vclient21:
                    await self.app2.change_stream(self.CHAT_ID, streamable)
                if vclient22:
                    await self.app22.change_stream(self.CHAT_ID, streamable)
                if vclient23:
                    await self.app23.change_stream(self.CHAT_ID, streamable)
                if vclient24:
                    await self.app24.change_stream(self.CHAT_ID, streamable)
                if vclient25:
                    await self.app25.change_stream(self.CHAT_ID, streamable)
                if vclient26:
                    await self.app26.change_stream(self.CHAT_ID, streamable)
                if vclient27:
                    await self.app27.change_stream(self.CHAT_ID, streamable)
                if vclient28:
                    await self.app28.change_stream(self.CHAT_ID, streamable)
                if vclient29:
                    await self.app29.change_stream(self.CHAT_ID, streamable)
                if vclient30:
                    await self.app30.change_stream(self.CHAT_ID, streamable)
                if vclient31:
                    await self.app31.change_stream(self.CHAT_ID, streamable)
                if vclient32:
                    await self.app32.change_stream(self.CHAT_ID, streamable)
                if vclient33:
                    await self.app33.change_stream(self.CHAT_ID, streamable)
                if vclient34:
                    await self.app34.change_stream(self.CHAT_ID, streamable)
                if vclient35:
                    await self.app35.change_stream(self.CHAT_ID, streamable)
                if vclient36:
                    await self.app36.change_stream(self.CHAT_ID, streamable)
                if vclient37:
                    await self.app37.change_stream(self.CHAT_ID, streamable)
                if vclient38:
                    await self.app38.change_stream(self.CHAT_ID, streamable)
                if vclient39:
                    await self.app39.change_stream(self.CHAT_ID, streamable)
                if vclient40:
                    await self.app40.change_stream(self.CHAT_ID, streamable)
                if vclient41:
                    await self.app41.change_stream(self.CHAT_ID, streamable)
                if vclient42:
                    await self.app42.change_stream(self.CHAT_ID, streamable)
                if vclient43:
                    await self.app43.change_stream(self.CHAT_ID, streamable)
                if vclient44:
                    await self.app44.change_stream(self.CHAT_ID, streamable)
                if vclient45:
                    await self.app45.change_stream(self.CHAT_ID, streamable)
                if vclient46:
                    await self.app46.change_stream(self.CHAT_ID, streamable)
                if vclient47:
                    await self.app47.change_stream(self.CHAT_ID, streamable)
                if vclient48:
                    await self.app48.change_stream(self.CHAT_ID, streamable)
                if vclient49:
                    await self.app49.change_stream(self.CHAT_ID, streamable)
                if vclient50:
                    await self.app50.change_stream(self.CHAT_ID, streamable)
       
            except Exception:
                await self.skip()

    async def pause(self):
        if not self.PLAYING:
            return "Nothing is playing to Pause"
        if not self.PAUSED:
            if vclient:
                await self.app.pause_stream(self.CHAT_ID)
            if vclient2:
                await self.app2.pause_stream(self.CHAT_ID)
            if vclient3:
                await self.app3.pause_stream(self.CHAT_ID)
            if vclient4:
                await self.app4.pause_stream(self.CHAT_ID)
            if vclient5:
                await self.app5.pause_stream(self.CHAT_ID)
            if vclient6:
                await self.app6.pause_stream(self.CHAT_ID)
            if vclient7:
                await self.app7.pause_stream(self.CHAT_ID)
            if vclient8:
                await self.app8.pause_stream(self.CHAT_ID)
            if vclient9:
                await self.app9.pause_stream(self.CHAT_ID)
            if vclient10:
                await self.app10.pause_stream(self.CHAT_ID)
            if vclient11:
                await self.app11.pause_stream(self.CHAT_ID)
            if vclient12:
                await self.app12.pause_stream(self.CHAT_ID)
            if vclient13:
                await self.app13.pause_stream(self.CHAT_ID)
            if vclient14:
                await self.app14.pause_stream(self.CHAT_ID)
            if vclient15:
                await self.app15.pause_stream(self.CHAT_ID)
            if vclient16:
                await self.app16.pause_stream(self.CHAT_ID)
            if vclient17:
                await self.app17.pause_stream(self.CHAT_ID)
            if vclient18:
                await self.app18.pause_stream(self.CHAT_ID)
            if vclient19:
                await self.app19.pause_stream(self.CHAT_ID)
            if vclient20:
                await self.app20.pause_stream(self.CHAT_ID)
            if vclient21:
                await self.app21.pause_stream(self.CHAT_ID)
            if vclient22:
                await self.app22.pause_stream(self.CHAT_ID)
            if vclient23:
                await self.app23.pause_stream(self.CHAT_ID)
            if vclient24:
                await self.app24.pause_stream(self.CHAT_ID)
            if vclient25:
                await self.app25.pause_stream(self.CHAT_ID)
            if vclient26:
                await self.app26.pause_stream(self.CHAT_ID)
            if vclient27:
                await self.app27.pause_stream(self.CHAT_ID)
            if vclient28:
                await self.app28.pause_stream(self.CHAT_ID)
            if vclient29:
                await self.app29.pause_stream(self.CHAT_ID)
            if vclient30:
                await self.app30.pause_stream(self.CHAT_ID)
            if vclient31:
                await self.app31.pause_stream(self.CHAT_ID)
            if vclient32:
                await self.app32.pause_stream(self.CHAT_ID)
            if vclient33:
                await self.app33.pause_stream(self.CHAT_ID)
            if vclient34:
                await self.app34.pause_stream(self.CHAT_ID)
            if vclient35:
                await self.app35.pause_stream(self.CHAT_ID)
            if vclient36:
                await self.app36.pause_stream(self.CHAT_ID)
            if vclient37:
                await self.app37.pause_stream(self.CHAT_ID)
            if vclient38:
                await self.app38.pause_stream(self.CHAT_ID)
            if vclient39:
                await self.app39.pause_stream(self.CHAT_ID)
            if vclient40:
                await self.app40.pause_stream(self.CHAT_ID)
            if vclient41:
                await self.app41.pause_stream(self.CHAT_ID)
            if vclient42:
                await self.app42.pause_stream(self.CHAT_ID)
            if vclient43:
                await self.app43.pause_stream(self.CHAT_ID)
            if vclient44:
                await self.app44.pause_stream(self.CHAT_ID)
            if vclient45:
                await self.app45.pause_stream(self.CHAT_ID)
            if vclient46:
                await self.app46.pause_stream(self.CHAT_ID)
            if vclient47:
                await self.app47.pause_stream(self.CHAT_ID)
            if vclient48:
                await self.app48.pause_stream(self.CHAT_ID)
            if vclient49:
                await self.app49.pause_stream(self.CHAT_ID)
            if vclient50:
                await self.app50.pause_stream(self.CHAT_ID)
         
            self.PAUSED = True
        return f"Paused Stream on {self.CHAT_NAME}"

    async def resume(self):
        if not self.PLAYING:
            return "Nothing is playing to Resume"
        if self.PAUSED:
            if vclient:
                await app.resume_stream(self.CHAT_ID)
            if vclient2:
                await app2.resume_stream(self.CHAT_ID)
            if vclient3:
                await app3.resume_stream(self.CHAT_ID)
            if vclient4:
                await app4.resume_stream(self.CHAT_ID)
            if vclient5:
                await app5.resume_stream(self.CHAT_ID)
            if vclient6:
                await app6.resume_stream(self.CHAT_ID)
            if vclient7:
                await app7.resume_stream(self.CHAT_ID)
            if vclient8:
                await app8.resume_stream(self.CHAT_ID)
            if vclient9:
                await app9.resume_stream(self.CHAT_ID)
    
            if vclient10:
                await app10.resume_stream(self.CHAT_ID)
            if vclient11:
                await app11.resume_stream(self.CHAT_ID)
            if vclient12:
                await app12.resume_stream(self.CHAT_ID)
            if vclient13:
                await app13.resume_stream(self.CHAT_ID)
            if vclient14:
                await app14.resume_stream(self.CHAT_ID)
            if vclient15:
                await app15.resume_stream(self.CHAT_ID)
            if vclient16:
                await app16.resume_stream(self.CHAT_ID)
            if vclient17:
                await app17.resume_stream(self.CHAT_ID)
            if vclient18:
                await app18.resume_stream(self.CHAT_ID)
            if vclient19:
                await app19.resume_stream(self.CHAT_ID)
    
            if vclient20:
                await app20.resume_stream(self.CHAT_ID)
            if vclient21:
                await app21.resume_stream(self.CHAT_ID)
            if vclient22:
                await app22.resume_stream(self.CHAT_ID)
            if vclient23:
                await app24.resume_stream(self.CHAT_ID)
            if vclient25:
                await app25.resume_stream(self.CHAT_ID)
            if vclient26:
                await app26.resume_stream(self.CHAT_ID)
            if vclient27:
                await app27.resume_stream(self.CHAT_ID)
            if vclient28:
                await app28.resume_stream(self.CHAT_ID)
            if vclient29:
                await app29.resume_stream(self.CHAT_ID)
            if vclient30:
                await app30.resume_stream(self.CHAT_ID)
    
            if vclient31:
                await app31.resume_stream(self.CHAT_ID)
            if vclient32:
                await app32.resume_stream(self.CHAT_ID)
            if vclient33:
                await app33.resume_stream(self.CHAT_ID)
            if vclient34:
                await app34.resume_stream(self.CHAT_ID)
            if vclient35:
                await app35.resume_stream(self.CHAT_ID)
            if vclient36:
                await app36.resume_stream(self.CHAT_ID)
            if vclient37:
                await app37.resume_stream(self.CHAT_ID)
            if vclient38:
                await app38.resume_stream(self.CHAT_ID)
            if vclient39:
                await app39.resume_stream(self.CHAT_ID)
            if vclient40:
                await app40.resume_stream(self.CHAT_ID)
    
            if vclient41:
                await app41.resume_stream(self.CHAT_ID)
            if vclient42:
                await app42.resume_stream(self.CHAT_ID)
            if vclient43:
                await app43.resume_stream(self.CHAT_ID)
            if vclient44:
                await app45.resume_stream(self.CHAT_ID)
            if vclient46:
                await app46.resume_stream(self.CHAT_ID)
            if vclient47:
                await app47.resume_stream(self.CHAT_ID)
            if vclient48:
                await app48.resume_stream(self.CHAT_ID)
            if vclient49:
                await app49.resume_stream(self.CHAT_ID)
            if vclient50:
                await app50.resume_stream(self.CHAT_ID)
            
            self.PAUSED = False
        return f"Resumed Stream on {self.CHAT_NAME}"
