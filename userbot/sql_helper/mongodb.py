# Copyright (C) 2021-2022 PandaUserbot

# Recode by @robotrakitangakbagus, @diemmmmmmmmmm
# Import PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport

import motor.motor_asyncio
from ..Var import Database


def mongodb():
    if Database.MONGO_DB:
        return motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
    else:
        return None
