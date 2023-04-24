
t base64
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

from userbot.config import Config
from userbot.helpers.utils import _format
from userbot import *
from userbot.modules.telethon import (
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
            counter += counter
            await asyncio.sleep(Config.CHANGE_TIME)
        except BaseException:
            return
        AUTOPICSTART = gvarstatus("autopic") == "true"

