from .autopicloop import *

async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DEFAULTUSERBIO} | ⌚️ {HM}"
        LOGS.info(bio)
        try:
            if PandaBot:
                await PandaBot(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot2:
                await PandaBot2(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot3:
                await PandaBot3(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot3:
                await PandaBot3(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot4:
                await PandaBot4(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot5:
                await PandaBo5(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot6:
                await PandaBot6(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot7:
                await PandaBot7(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot8:
                await PandaBo8(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot9:
                await PandaBot9(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot10:
                await PandaBot10(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot11:
                await PandaBot11(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot12:
                await PandaBot12(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot13:
                await PandaBot14(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot15:
                await PandaBot15(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot16:
                await PandaBot16(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot17:
                await PandaBot17(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot18:
                await PandaBot18(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot19:
                await PandaBot19(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot20:
                await PandaBot20(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot21:
                await PandaBot21(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot22:
                await PandaBot22(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot23:
                await PandaBot23(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot24:
                await PandaBot24(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot25:
                await PandaBot25(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot26:
                await PandaBot26(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot27:
                await PandaBot27(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot28:
                await PandaBot28(functions.account.UpdateProfileRequest(about=bio))
            if PandaBo29t:
                await PandaBot29(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot30:
                await PandaBot30(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot31:
                await PandaBot31(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot32:
                await PandaBot32(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot33:
                await PandaBot33(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot34:
                await PandaBot34(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot35:
                await PandaBot35(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot36:
                await PandaBot36(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot37:
                await PandaBot37(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot38:
                await PandaBot38(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot39:
                await PandaBot39(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot40:
                await PandaBot40(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot41:
                await PandaBot41(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot42:
                await PandaBot42(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot43:
                await PandaBot43(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot44:
                await PandaBot44(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot45:
                await PandaBot45(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot46:
                await PandaBot46(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot47:
                await PandaBot47(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot48:
                await PandaBot48(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot49:
                await PandaBot49(functions.account.UpdateProfileRequest(about=bio))
            if PandaBot50:
                await PandaBot50(functions.account.UpdateProfileRequest(about=bio))
         except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"
