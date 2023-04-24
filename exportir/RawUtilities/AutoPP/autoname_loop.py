
from .autopicloop import *

async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚️ {HM}||›  {DEFAULTUSER} ‹||📅 {DM}"
        LOGS.info(name)
        try:
            if PandaBot:
                await PandaBot(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot2:
                await PandaBot2(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot3:
                await PandaBot3(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot3:
                await PandaBot3(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot4:
                await PandaBot4(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot5:
                await PandaBo5(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot6:
                await PandaBot6(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot7:
                await PandaBot7(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot8:
                await PandaBo8(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot9:
                await PandaBot9(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot10:
                await PandaBot10(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot11:
                await PandaBot11(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot12:
                await PandaBot12(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot13:
                await PandaBot14(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot15:
                await PandaBot15(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot16:
                await PandaBot16(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot17:
                await PandaBot17(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot18:
                await PandaBot18(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot19:
                await PandaBot19(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot20:
                await PandaBot20(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot21:
                await PandaBot21(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot22:
                await PandaBot22(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot23:
                await PandaBot23(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot24:
                await PandaBot24(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot25:
                await PandaBot25(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot26:
                await PandaBot26(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot27:
                await PandaBot27(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot28:
                await PandaBot28(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBo29t:
                await PandaBot29(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot30:
                await PandaBot30(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot31:
                await PandaBot31(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot32:
                await PandaBot32(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot33:
                await PandaBot33(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot34:
                await PandaBot34(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot35:
                await PandaBot35(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot36:
                await PandaBot36(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot37:
                await PandaBot37(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot38:
                await PandaBot38(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot39:
                await PandaBot39(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot40:
                await PandaBot40(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot41:
                await PandaBot41(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot42:
                await PandaBot42(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot43:
                await PandaBot43(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot44:
                await PandaBot44(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot45:
                await PandaBot45(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot46:
                await PandaBot46(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot47:
                await PandaBot47(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot48:
                await PandaBot48(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot49:
                await PandaBot49(functions.account.UpdateProfileRequest(first_name=name))
            if PandaBot50:
                await PandaBot50(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"
