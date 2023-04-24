# batmanpfp and thorpfp by cat userbot

import asyncio
import base64
import os
import random
import re
import shutil
import time
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from ...config import Config
from ...helpers.utils import _format
from ... import *
from . import (
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    _pandautils,
    edit_delete,
    logging,
)

plugin_category = "plugins"
DEFAULTUSERBIO = DEFAULT_BIO or " ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ  "
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

autopic_path = os.path.join(os.getcwd(), "userbot", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "userbot", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "userbot", "photo_pfp.png")

digitalpfp = Config.DIGITAL_PIC or "https://telegra.ph/file/aeaebe33b1f3988a0b690.jpg"

COLLECTION_STRINGS = {
    "batmanpfp_strings": [
        "awesome-batman-wallpapers",
        "batman-arkham-knight-4k-wallpaper",
        "batman-hd-wallpapers-1080p",
        "the-joker-hd-wallpaper",
        "dark-knight-joker-wallpaper",
    ],
    "thorpfp_strings": [
        "thor-wallpapers",
        "thor-wallpaper",
        "thor-iphone-wallpaper",
        "thor-wallpaper-hd",
    ],
}


async def autopicloop():
    AUTOPICSTART = gvarstatus("autopic") == "true"
    if AUTOPICSTART and Config.DEFAULT_PIC is None:
        if BOTLOG:
            if PandaBot:
                await PandaBot.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot2:
                await PandaBot2.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot3:
                await PandaBot3.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot4:
                await PandaBot4.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot5:
                await PandaBot5.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot6:
                await PandaBot6.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot7:
                await PandaBot7.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot8:
                await PandaBot8.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot9:
                await PandaBot9.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot10:
                await PandaBot10.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot11:
                await PandaBot11.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot12:
                await PandaBot12.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot13:
                await PandaBot13.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot14:
                await PandaBot14.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot15:
                await PandaBot15.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot16:
                await PandaBot16.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot17:
                await PandaBot17.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot18:
                await PandaBot18.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot19:
                await PandaBot19.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot20:
                await PandaBot20.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot21:
                await PandaBot21.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot22:
                await PandaBot22.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot23:
                await PandaBot23.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot24:
                await PandaBot24.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")  
            if PandaBot25:
                await PandaBot25.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot26:
                await PandaBot26.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot27:
                await PandaBot27.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot28:
                await PandaBot28.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot29:
                await PandaBot29.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot30:
                await PandaBot30.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot31:
                await PandaBot31.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot32:
                await PandaBot32.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot33:
                await PandaBot33.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot34:
                await PandaBot34.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot35:
                await PandaBot35.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot36:
                await PandaBot36.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot37:
                await PandaBot37.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot38:
                await PandaBot38.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot39:
                await PandaBot39.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot40:
                await PandaBot40.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot41:
                await PandaBot41.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot42:
                await PandaBot42.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot43:
                await PandaBot43.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot44:
                await PandaBot44.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot45:
                await PandaBot45.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot46:
                await PandaBot46.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot47:
                await PandaBot47.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot48:
                await PandaBot48.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot48:
                await PandaBot48.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            if PandaBot50:
                await PandaBot50.send_message(BOTLOG_CHATID, "**Error**\n`For functing of autopic you need to set DEFAULT_PIC var in Heroku vars`")
            return
    if gvarstatus("autopic") is not None:
        try:
            counter = int(gvarstatus("autopic_counter"))
        except Exception as e:
            LOGS.warn(str(e))
    while AUTOPICSTART:
        if not os.path.exists(autopic_path):
            downloader = SmartDL(Config.DEFAULT_PIC, autopic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(autopic_path, autophoto_path)
        im = Image.open(autophoto_path)
        file_test = im.rotate(counter, expand=False).save(autophoto_path, "PNG")
        current_time = datetime.now().strftime("  Time: %H:%M \n  Date: %d.%m.%y ")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((150, 250), current_time, font=fnt, fill=(124, 252, 0))
        img.save(autophoto_path)
        file = await pandaub.upload_file(autophoto_path)
        try:
            await pandaub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            counter += counter
            await asyncio.sleep(Config.CHANGE_TIME)
        except BaseException:
            return
        AUTOPICSTART = gvarstatus("autopic") == "true"


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("digitalpic") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%H:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        panda = str(base64.b64decode("UGFuZGEvaGVscGVycy9zdHlsZXMvZGlnaXRhbC50dGY="))[
            2:36
        ]
        fnt = ImageFont.truetype(panda, 200)
        drawn_text.text((350, 100), current_time, font=fnt, fill=(124, 252, 0))
        img.save(autophoto_path)
        file = await PandaBot.upload_file(autophoto_path)
        file2 = await PandaBot2.upload_file(autophoto_path)
        file3 = await PandaBot3.upload_file(autophoto_path)
        file4 = await PandaBot4.upload_file(autophoto_path)
        file5 = await PandaBot5.upload_file(autophoto_path)
        file6 = await PandaBot6.upload_file(autophoto_path)
        file7 = await PandaBot7.upload_file(autophoto_path)
        file8 = await PandaBot8.upload_file(autophoto_path)
        file9 = await PandaBot9.upload_file(autophoto_path)
        file10 = await PandaBot10.upload_file(autophoto_path)
        file11 = await PandaBot11.upload_file(autophoto_path)
        file12 = await PandaBot12.upload_file(autophoto_path)
        file13 = await PandaBot13.upload_file(autophoto_path)
        file14 = await PandaBot14.upload_file(autophoto_path)
        file15 = await PandaBot15.upload_file(autophoto_path)
        file16 = await PandaBot16.upload_file(autophoto_path)
        file17 = await PandaBot17.upload_file(autophoto_path)
        file18 = await PandaBot18.upload_file(autophoto_path)
        file19 = await PandaBot19.upload_file(autophoto_path)
        file20 = await PandaBot20.upload_file(autophoto_path)
        file21 = await PandaBot21.upload_file(autophoto_path)
        file22 = await PandaBot22.upload_file(autophoto_path)
        file23 = await PandaBot23.upload_file(autophoto_path)
        file24 = await PandaBot24.upload_file(autophoto_path)

        file25 = await PandaBot25.upload_file(autophoto_path)
        file26 = await PandaBot26.upload_file(autophoto_path)
        file27 = await PandaBot27.upload_file(autophoto_path)
        file28 = await PandaBot28.upload_file(autophoto_path)
        file29 = await PandaBot29.upload_file(autophoto_path)
        file30 = await PandaBot30.upload_file(autophoto_path)
        file31 = await PandaBot31.upload_file(autophoto_path)
        file32 = await PandaBot32.upload_file(autophoto_path)
        
        file33 = await PandaBot33.upload_file(autophoto_path)
        file34 = await PandaBot34.upload_file(autophoto_path)
        file35 = await PandaBot35.upload_file(autophoto_path)
        file36 = await PandaBot36.upload_file(autophoto_path)
        file37 = await PandaBot37.upload_file(autophoto_path)
        file38 = await PandaBot38.upload_file(autophoto_path)
        file39 = await PandaBot39.upload_file(autophoto_path)
        file40 = await PandaBot40.upload_file(autophoto_path)
        file41 = await PandaBot41.upload_file(autophoto_path)
        file42 = await PandaBot42.upload_file(autophoto_path)
        file43 = await PandaBot43.upload_file(autophoto_path)
        file44 = await PandaBot44.upload_file(autophoto_path)
        file45 = await PandaBot45.upload_file(autophoto_path)
        file46 = await PandaBot46.upload_file(autophoto_path)
        file47 = await PandaBot47.upload_file(autophoto_path)
        file48 = await PandaBot48.upload_file(autophoto_path)
        file49 = await PandaBot49.upload_file(autophoto_path)
        file50 = await PandaBot50.upload_file(autophoto_path)
        try:
            if i > 0:
                if PandaBot:
                    await PandaBot(functions.photos.DeletePhotosRequest(await PandaBot.get_profile_photos("me", limit=1)))
                if PandaBot2:
                    await PandaBot2(functions.photos.DeletePhotosRequest(await PandaBot2.get_profile_photos("me", limit=1)))
                if PandaBot3:
                    await PandaBot3(functions.photos.DeletePhotosRequest(await PandaBot3.get_profile_photos("me", limit=1)))
                if PandaBot4:
                    await PandaBot4(functions.photos.DeletePhotosRequest(await PandaBot4.get_profile_photos("me", limit=1)))
                if PandaBot5:
                    await PandaBot5(functions.photos.DeletePhotosRequest(await PandaBot5.get_profile_photos("me", limit=1)))
                if PandaBot6:
                    await PandaBot6(functions.photos.DeletePhotosRequest(await PandaBot6.get_profile_photos("me", limit=1)))
                if PandaBot7:
                    await PandaBot7(functions.photos.DeletePhotosRequest(await PandaBot7.get_profile_photos("me", limit=1)))
                if PandaBot8:
                    await PandaBot8(functions.photos.DeletePhotosRequest(await PandaBot8.get_profile_photos("me", limit=1)))
                if PandaBot9:
                    await PandaBot9(functions.photos.DeletePhotosRequest(await PandaBot9.get_profile_photos("me", limit=1)))
                if PandaBot10:
                    await PandaBot10(functions.photos.DeletePhotosRequest(await PandaBot10.get_profile_photos("me", limit=1)))
                if PandaBot11:
                    await PandaBot11(functions.photos.DeletePhotosRequest(await PandaBot11.get_profile_photos("me", limit=1)))
                if PandaBot12:
                    await PandaBot12(functions.photos.DeletePhotosRequest(await PandaBot12.get_profile_photos("me", limit=1)))
                if PandaBot13:
                    await PandaBot13(functions.photos.DeletePhotosRequest(await PandaBot13.get_profile_photos("me", limit=1)))
                if PandaBot14:
                    await PandaBot14(functions.photos.DeletePhotosRequest(await PandaBot14.get_profile_photos("me", limit=1)))
                if PandaBot15:
                    await PandaBot15(functions.photos.DeletePhotosRequest(await PandaBot15.get_profile_photos("me", limit=1)))
                if PandaBot16:
                    await PandaBot16(functions.photos.DeletePhotosRequest(await PandaBot16.get_profile_photos("me", limit=1)))
                if PandaBot17:
                    await PandaBot17(functions.photos.DeletePhotosRequest(await PandaBot17.get_profile_photos("me", limit=1)))
                if PandaBot18:
                    await PandaBot18(functions.photos.DeletePhotosRequest(await PandaBot18.get_profile_photos("me", limit=1)))
                if PandaBot19:
                    await PandaBot19(functions.photos.DeletePhotosRequest(await PandaBot19.get_profile_photos("me", limit=1)))
                if PandaBot20:
                    await PandaBot20(functions.photos.DeletePhotosRequest(await PandaBot20.get_profile_photos("me", limit=1)))
                if PandaBot21:
                    await PandaBot21(functions.photos.DeletePhotosRequest(await PandaBot21.get_profile_photos("me", limit=1)))
                if PandaBot22:
                    await PandaBot22(functions.photos.DeletePhotosRequest(await PandaBot22.get_profile_photos("me", limit=1)))
                if PandaBot23:
                    await PandaBot23(functions.photos.DeletePhotosRequest(await PandaBot23.get_profile_photos("me", limit=1)))
                if PandaBot24:
                    await PandaBot24(functions.photos.DeletePhotosRequest(await PandaBot24.get_profile_photos("me", limit=1)))
                if PandaBot25:
                    await PandaBot25(functions.photos.DeletePhotosRequest(await PandaBot25.get_profile_photos("me", limit=1)))
                if PandaBot26:
                    await PandaBot26(functions.photos.DeletePhotosRequest(await PandaBot26.get_profile_photos("me", limit=1)))
                if PandaBot27:
                    await PandaBot27(functions.photos.DeletePhotosRequest(await PandaBot27.get_profile_photos("me", limit=1)))
                if PandaBot28:
                    await PandaBot28(functions.photos.DeletePhotosRequest(await PandaBot28.get_profile_photos("me", limit=1)))
                if PandaBot29:
                    await PandaBot29(functions.photos.DeletePhotosRequest(await PandaBot29.get_profile_photos("me", limit=1)))
                if PandaBot30:
                    await PandaBot(functions.photos.DeletePhotosRequest(await PandaBot.get_profile_photos("me", limit=1)))
                if PandaBot:
                    await PandaBot30(functions.photos.DeletePhotosRequest(await PandaBot30.get_profile_photos("me", limit=1)))
                if PandaBot31:
                    await PandaBot31(functions.photos.DeletePhotosRequest(await PandaBot31.get_profile_photos("me", limit=1)))
                if PandaBot32:
                    await PandaBot32(functions.photos.DeletePhotosRequest(await PandaBot32.get_profile_photos("me", limit=1)))
                if PandaBot33:
                    await PandaBot33(functions.photos.DeletePhotosRequest(await PandaBot33.get_profile_photos("me", limit=1)))
                if PandaBot34:
                    await PandaBot34(functions.photos.DeletePhotosRequest(await PandaBot34.get_profile_photos("me", limit=1)))
                if PandaBot35:
                    await PandaBot35(functions.photos.DeletePhotosRequest(await PandaBot35.get_profile_photos("me", limit=1)))
                if PandaBot36:
                    await PandaBot36(functions.photos.DeletePhotosRequest(await PandaBot36.get_profile_photos("me", limit=1)))
                if PandaBot37:
                    await PandaBot37(functions.photos.DeletePhotosRequest(await PandaBot37.get_profile_photos("me", limit=1)))
                if PandaBot38:
                    await PandaBot38(functions.photos.DeletePhotosRequest(await PandaBot38.get_profile_photos("me", limit=1)))
                if PandaBot39:
                    await PandaBot39(functions.photos.DeletePhotosRequest(await PandaBot39.get_profile_photos("me", limit=1)))
            
                if PandaBot40:
                    await PandaBot40(functions.photos.DeletePhotosRequest(await PandaBot40.get_profile_photos("me", limit=1)))
                if PandaBot41:
                    await PandaBot41(functions.photos.DeletePhotosRequest(await PandaBot41.get_profile_photos("me", limit=1)))
                if PandaBot42:
                    await PandaBot42(functions.photos.DeletePhotosRequest(await PandaBot42.get_profile_photos("me", limit=1)))
                if PandaBot43:
                    await PandaBot43(functions.photos.DeletePhotosRequest(await PandaBot43.get_profile_photos("me", limit=1)))
                if PandaBot44:
                    await PandaBot44(functions.photos.DeletePhotosRequest(await PandaBot44.get_profile_photos("me", limit=1)))
                if PandaBot45:
                    await PandaBot45(functions.photos.DeletePhotosRequest(await PandaBot45.get_profile_photos("me", limit=1)))
                if PandaBot46:
                    await PandaBot46(functions.photos.DeletePhotosRequest(await PandaBot46.get_profile_photos("me", limit=1)))
                if PandaBot47:
                    await PandaBot47(functions.photos.DeletePhotosRequest(await PandaBot47.get_profile_photos("me", limit=1)))
                if PandaBot48:
                    await PandaBot48(functions.photos.DeletePhotosRequest(await PandaBot48.get_profile_photos("me", limit=1)))
                if PandaBot49:
                    await PandaBot49(functions.photos.DeletePhotosRequest(await PandaBot49.get_profile_photos("me", limit=1)))
                if PandaBot50:
                    await PandaBot50(functions.photos.DeletePhotosRequest(await PandaBot50.get_profile_photos("me", limit=1))    
                           
            i += 1
            if PandaBot:
                await PandaBot(functions.photos.UploadProfilePhotoRequest(file))
            if PandaBot2:
                await PandaBot2(functions.photos.UploadProfilePhotoRequest(file2))
            if PandaBot3:
                await PandaBot3(functions.photos.UploadProfilePhotoRequest(file3))
            if PandaBot4:
                await PandaBot4(functions.photos.UploadProfilePhotoRequest(file4))
            if PandaBot5:
                await PandaBot5(functions.photos.UploadProfilePhotoRequest(file5))
            if PandaBot6:
                await PandaBot6(functions.photos.UploadProfilePhotoRequest(file6))
            if PandaBot7:
                await PandaBot7(functions.photos.UploadProfilePhotoRequest(file7))
            if PandaBot8:
                await PandaBot8(functions.photos.UploadProfilePhotoRequest(file8))
            if PandaBot9:
                await PandaBot9(functions.photos.UploadProfilePhotoRequest(file9))
            if PandaBot10:
                await PandaBot10(functions.photos.UploadProfilePhotoRequest(file10))
            if PandaBot11:
                await PandaBot11(functions.photos.UploadProfilePhotoRequest(file11))
            if PandaBot12:
                await PandaBot12(functions.photos.UploadProfilePhotoRequest(file12))
            if PandaBot13:
                await PandaBot13(functions.photos.UploadProfilePhotoRequest(file13))
            if PandaBot14:
                await PandaBot14(functions.photos.UploadProfilePhotoRequest(file14))
            if PandaBot15:
                await PandaBot15(functions.photos.UploadProfilePhotoRequest(file15))
            if PandaBot16:
                await PandaBot16(functions.photos.UploadProfilePhotoRequest(file16))
            if PandaBot17:
                await PandaBot17(functions.photos.UploadProfilePhotoRequest(file17))
            if PandaBot18:
                await PandaBot18(functions.photos.UploadProfilePhotoRequest(file18))

            if PandaBot19:
                await PandaBot19(functions.photos.UploadProfilePhotoRequest(file19))
            if PandaBot20:
                await PandaBot20(functions.photos.UploadProfilePhotoRequest(file20))
            if PandaBot21:
                await PandaBot21(functions.photos.UploadProfilePhotoRequest(file21))
            if PandaBot22:
                await PandaBot22(functions.photos.UploadProfilePhotoRequest(file22))
            if PandaBot23:
                await PandaBot23(functions.photos.UploadProfilePhotoRequest(file23))
            if PandaBot24:
                await PandaBot24(functions.photos.UploadProfilePhotoRequest(file24))
            if PandaBot25:
                await PandaBot25(functions.photos.UploadProfilePhotoRequest(file25))
            if PandaBot26:
                await PandaBot26(functions.photos.UploadProfilePhotoRequest(file26))
            if PandaBot27:
                await PandaBot27(functions.photos.UploadProfilePhotoRequest(file27))
            if PandaBot28:
                await PandaBot28(functions.photos.UploadProfilePhotoRequest(file28))

            if PandaBot29:
                await PandaBot29(functions.photos.UploadProfilePhotoRequest(file29))
            if PandaBot30:
                await PandaBot30(functions.photos.UploadProfilePhotoRequest(file30))
            if PandaBot31:
                await PandaBot31(functions.photos.UploadProfilePhotoRequest(file31))
            if PandaBot32:
                await PandaBot32(functions.photos.UploadProfilePhotoRequest(file32))
            if PandaBot33:
                await PandaBot33(functions.photos.UploadProfilePhotoRequest(file33))
            if PandaBot:
                await PandaBot34(functions.photos.UploadProfilePhotoRequest(file34))
            if PandaBot35:
                await PandaBot35(functions.photos.UploadProfilePhotoRequest(file35))
            if PandaBot36:
                await PandaBot36(functions.photos.UploadProfilePhotoRequest(file36))
            if PandaBot37:
                await PandaBot37(functions.photos.UploadProfilePhotoRequest(file37))
            if PandaBot38:
                await PandaBot38(functions.photos.UploadProfilePhotoRequest(file38))

            if PandaBot39:
                await PandaBot39(functions.photos.UploadProfilePhotoRequest(file39))
            if PandaBot40:
                await PandaBot40(functions.photos.UploadProfilePhotoRequest(file40))
            if PandaBot41:
                await PandaBot41(functions.photos.UploadProfilePhotoRequest(file41))
            if PandaBot42:
                await PandaBot42(functions.photos.UploadProfilePhotoRequest(file42))
            if PandaBot43:
                await PandaBot43(functions.photos.UploadProfilePhotoRequest(file43))
            if PandaBot44:
                await PandaBot44(functions.photos.UploadProfilePhotoRequest(file44))
            if PandaBot45:
                await PandaBot45(functions.photos.UploadProfilePhotoRequest(file45))
            if PandaBot46:
                await PandaBot46(functions.photos.UploadProfilePhotoRequest(file46))
            if PandaBot47:
                await PandaBot47(functions.photos.UploadProfilePhotoRequest(file47))
            if PandaBot48:
                await PandaBot48(functions.photos.UploadProfilePhotoRequest(file48))

            if PandaBot49:
                await PandaBot49(functions.photos.UploadProfilePhotoRequest(file49))

            if PandaBot50:
                await PandaBot50(functions.photos.UploadProfilePhotoRequest(file50))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"


async def bloom_pfploop():
    BLOOMSTART = gvarstatus("bloom") == "true"
    if BLOOMSTART and Config.DEFAULT_PIC is None:
        if BOTLOG:
            return await pandaub.send_message(
                BOTLOG_CHATID,
                "**Error**\n`For functing of bloom you need to set DEFAULT_PIC var in Heroku vars`",
            )
        return
    while BLOOMSTART:
        if not os.path.exists(autopic_path):
            downloader = SmartDL(Config.DEFAULT_PIC, autopic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        # RIP Danger zone Here no editing here plox
        R = random.randint(0, 256)
        B = random.randint(0, 256)
        G = random.randint(0, 256)
        FR = 256 - R
        FB = 256 - B
        FG = 256 - G
        shutil.copy(autopic_path, autophoto_path)
        image = Image.open(autophoto_path)
        image.paste((R, G, B), [0, 0, image.size[0], image.size[1]])
        image.save(autophoto_path)
        current_time = datetime.now().strftime("\n Time: %H:%M:%S \n \n Date: %d/%m/%y")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(FR, FG, FB))
        drawn_text.text((95, 250), "      😈", font=ofnt, fill=(FR, FG, FB))
        img.save(autophoto_path)
        file = await pandaub.upload_file(autophoto_path)
        try:
            await pandaub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(Config.CHANGE_TIME)
        except BaseException:
            return
        BLOOMSTART = gvarstatus("bloom") == "true"


async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚️ {HM}||›  {DEFAULTUSER} ‹||📅 {DM}"
        LOGS.info(name)
        try:
            await pandaub(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DEFAULTUSERBIO} | ⌚️ {HM}"
        LOGS.info(bio)
        try:
            await pandaub(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


async def animeprofilepic(collection_images):
    rnd = random.randint(0, len(collection_images) - 1)
    pack = collection_images[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    img = requests.get(fy)
    with open("donottouch.jpg", "wb") as outfile:
        outfile.write(img.content)
    return "donottouch.jpg"


async def autopfp_start():
    if gvarstatus("autopfp_strings") is not None:
        AUTOPFP_START = True
        string_list = COLLECTION_STRINGS[gvarstatus("autopfp_strings")]
    else:
        AUTOPFP_START = False
    i = 0
    while AUTOPFP_START:
        await animeprofilepic(string_list)
        file = await pandaub.upload_file("donottouch.jpg")
        if i > 0:
            await pandaub(
                functions.photos.DeletePhotosRequest(
                    await pandaub.get_profile_photos("me", limit=1)
                )
            )
        i += 1
        await pandaub(functions.photos.UploadProfilePhotoRequest(file))
        await _pandautils.runcmd("rm -rf donottouch.jpg")
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOPFP_START = gvarstatus("autopfp_strings") is not None


@pandaub.ilhammansiz_cmd(
    pattern="batmanpfp$",
    command=("batmanpfp", plugin_category),
    info={
        "header": "Changes profile pic with random batman pics every 1 minute",
        "description": "Changes your profile pic every 1 minute with random batman pics.\
        If you like to change the time then set CHANGE_TIME var in Heroku with time (in seconds) between each change of profilepic.",
        "note": "To stop this do '.end batmanpfp'",
        "usage": "{tr}batmanpfp",
    },
)
async def _(event):
    "To set random batman profile pics"
    if gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        return await edit_delete(event, f"`{pfp_string} is already running.`")
    addgvar("autopfp_strings", "batmanpfp_strings")
    await event.edit("`Starting batman Profile Pic.`")
    await autopfp_start()


@pandaub.ilhammansiz_cmd(
    pattern="thorpfp$",
    command=("thorpfp", plugin_category),
    info={
        "header": "Changes profile pic with random thor pics every 1 minute",
        "description": "Changes your profile pic every 1 minute with random thor pics.\
        If you like to change the time then set CHANGE_TIME var in Heroku with time(in seconds) between each change of profilepic.",
        "note": "To stop this do '.end thorpfp'",
        "usage": "{tr}thorpfp",
    },
)
async def _(event):
    "To set random thor profile pics"
    if gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        return await edit_delete(event, f"`{pfp_string} is already running.`")
    addgvar("autopfp_strings", "thorpfp_strings")
    await event.edit("`Starting thor Profile Pic.`")
    await autopfp_start()


@pandaub.ilhammansiz_cmd(
    pattern="autopic ?(.*)",
    command=("autopic", plugin_category),
    info={
        "header": "Changes profile pic every 1 minute with the custom pic with time",
        "description": "If you like to change the time interval for every new pic change \
            then set CHANGE_TIME var in Heroku with time(in seconds) between each change of profilepic.",
        "options": "you can give integer input with cmd like 40,55,75 ..etc.\
             So that your profile pic will rotate with that specific angle",
        "note": "For functioning of this cmd you need to set DEFAULT_PIC var in heroku. \
            To stop this do '.end autopic'",
        "usage": [
            "{tr}autopic",
            "{tr}autopic <any integer>",
        ],
    },
)
async def _(event):
    "To set time on your profile pic"
    if Config.DEFAULT_PIC is None:
        return await edit_delete(
            event,
            "**Error**\nFor functing of autopic you need to set DEFAULT_PIC var in Heroku vars",
            parse_mode=_format.parse_pre,
        )
    downloader = SmartDL(Config.DEFAULT_PIC, autopic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    input_str = event.pattern_match.group(1)
    if input_str:
        try:
            input_str = int(input_str)
        except ValueError:
            input_str = 60
    else:
        if gvarstatus("autopic_counter") is None:
            addgvar("autopic_counter", 30)
    if gvarstatus("autopic") is not None and gvarstatus("autopic") == "true":
        return await edit_delete(event, f"`Autopic is already enabled`")
    addgvar("autopic", True)
    if input_str:
        addgvar("autopic_counter", input_str)
    await edit_delete(event, f"`Autopic has been started by my Master`")
    await autopicloop()


@pandaub.ilhammansiz_cmd(
    pattern="digitalpfp$",
    command=("digitalpfp", plugin_category),
    info={
        "header": "Updates your profile pic every 1 minute with time on it",
        "description": "Deletes old profile pic and Update profile pic with new image with time on it.\
             You can change this image by setting DIGITAL_PIC var in heroku with telegraph image link",
        "note": "To stop this do '.end digitalpfp'",
        "usage": "{tr}digitalpfp",
    },
)
async def _(event):
    "To set random colour pic with time to profile pic"
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, f"`Digitalpic is already enabled`")
    addgvar("digitalpic", True)
    await edit_delete(event, f"`digitalpfp has been started by my Master`")
    await digitalpicloop()


@pandaub.ilhammansiz_cmd(
    pattern="bloom$",
    command=("bloom", plugin_category),
    info={
        "header": "Changes profile pic every 1 minute with the random colour pic with time on it",
        "description": "If you like to change the time interval for every new pic chnage \
            then set CHANGE_TIME var in Heroku with time(in seconds) between each change of profilepic.",
        "note": "For functioning of this cmd you need to set DEFAULT_PIC var in heroku. \
            To stop this do '.end bloom'",
        "usage": "{tr}bloom",
    },
)
async def _(event):
    "To set random colour pic with time to profile pic"
    if Config.DEFAULT_PIC is None:
        return await edit_delete(
            event,
            "**Error**\nFor functing of bloom you need to set DEFAULT_PIC var in Heroku vars",
            parse_mode=_format.parse_pre,
        )
    downloader = SmartDL(Config.DEFAULT_PIC, autopic_path, progress_bar=True)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("bloom") is not None and gvarstatus("bloom") == "true":
        return await edit_delete(event, f"`Bloom is already enabled`")
    addgvar("bloom", True)
    await edit_delete(event, f"`Bloom has been started by my Master`")
    await bloom_pfploop()


@pandaub.ilhammansiz_cmd(
    pattern="autoname$",
    command=("autoname", plugin_category),
    info={
        "header": "Changes your name with time",
        "description": "Updates your profile name along with time. Set AUTONAME var in heroku with your profile name,",
        "note": "To stop this do '.end autoname'",
        "usage": "{tr}autoname",
    },
)
async def _(event):
    "To set your display name along with time"
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`Autoname is already enabled`")
    addgvar("autoname", True)
    await edit_delete(event, "`AutoName has been started by my Master `")
    await autoname_loop()


@pandaub.ilhammansiz_cmd(
    pattern="autobio$",
    command=("autobio", plugin_category),
    info={
        "header": "Changes your bio with time",
        "description": "Updates your profile bio along with time. Set DEFAULT_BIO var in heroku with your fav bio,",
        "note": "To stop this do '.end autobio'",
        "usage": "{tr}autobio",
    },
)
async def _(event):
    "To update your bio along with time"
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"`Autobio is already enabled`")
    addgvar("autobio", True)
    await edit_delete(event, "`Autobio has been started by my Master `")
    await autobio_loop()


@pandaub.ilhammansiz_cmd(
    pattern="end (.*)",
    command=("end", plugin_category),
    info={
        "header": "To stop the functions of autoprofile",
        "description": "If you want to stop autoprofile functions then use this cmd.",
        "options": {
            "autopic": "To stop autopic",
            "digitalpfp": "To stop difitalpfp",
            "bloom": "To stop bloom",
            "autoname": "To stop autoname",
            "autobio": "To stop autobio",
            "thorpfp": "To stop thorpfp",
            "batmanpfp": "To stop batmanpfp",
        },
        "usage": "{tr}end <option>",
        "examples": ["{tr}end autopic"],
    },
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "thorpfp" and gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        if pfp_string != "thorpfp":
            return await edit_delete(event, f"`thorpfp is not started`")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        delgvar("autopfp_strings")
        return await edit_delete(event, "`thorpfp has been stopped now`")
    if input_str == "batmanpfp" and gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        if pfp_string != "batmanpfp":
            return await edit_delete(event, f"`batmanpfp is not started`")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        delgvar("autopfp_strings")
        return await edit_delete(event, "`batmanpfp has been stopped now`")
    if input_str == "autopic":
        if gvarstatus("autopic") is not None and gvarstatus("autopic") == "true":
            delgvar("autopic")
            if os.path.exists(autopic_path):
                file = await event.client.upload_file(autopic_path)
                try:
                    await event.client(functions.photos.UploadProfilePhotoRequest(file))
                    os.remove(autopic_path)
                except BaseException:
                    return
            return await edit_delete(event, "`Autopic has been stopped now`")
        return await edit_delete(event, "`Autopic haven't enabled`")
    if input_str == "digitalpfp":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "`Digitalpfp has been stopped now`")
        return await edit_delete(event, "`Digitalpfp haven't enabled`")
    if input_str == "bloom":
        if gvarstatus("bloom") is not None and gvarstatus("bloom") == "true":
            delgvar("bloom")
            if os.path.exists(autopic_path):
                file = await event.client.upload_file(autopic_path)
                try:
                    await event.client(functions.photos.UploadProfilePhotoRequest(file))
                    os.remove(autopic_path)
                except BaseException:
                    return
            return await edit_delete(event, "`Bloom has been stopped now`")
        return await edit_delete(event, "`Bloom haven't enabled`")
    if input_str == "autoname":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "`Autoname has been stopped now`")
        return await edit_delete(event, "`Autoname haven't enabled`")
    if input_str == "autobio":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "`Autobio has been stopped now`")
        return await edit_delete(event, "`Autobio haven't enabled`")
    END_CMDS = [
        "autopic",
        "digitalpfp",
        "bloom",
        "autoname",
        "autobio",
        "thorpfp",
        "batmanpfp",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"{input_str} is invalid end command.Mention clearly what should i end.",
            parse_mode=_format.parse_pre,
        )


pandaub.loop.create_task(autopfp_start())
pandaub.loop.create_task(autopicloop())
pandaub.loop.create_task(digitalpicloop())
pandaub.loop.create_task(bloom_pfploop())
pandaub.loop.create_task(autoname_loop())
pandaub.loop.create_task(autobio_loop())
