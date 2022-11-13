
# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



from pyrogram import Client


from .._database._var import Database

class Pyrobot(Client):
    def __init__(self):
        super().__init__(
            "BotToken",
            api_id=Database.APP_ID,
            api_hash=Database.API_HASH,
            bot_token=Database.BOT_TOKEN,
        )
