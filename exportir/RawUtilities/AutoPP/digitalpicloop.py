
from .autopicloop import *

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

