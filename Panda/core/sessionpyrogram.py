from pyrogram import Client

from ..Config import Config

if Config.PYROGRAM_SESSION:
    # pylint: disable=invalid-name
    PandaBotPy = Client(Config.PYROGRAM_SESSION, Config.APP_ID, Config.API_HASH)
else:
    # pylint: disable=invalid-name
    PandaBotPy = Client("Panda", Config.APP_ID, Config.API_HASH)

PandaBotPy = Client(
    ":memory:",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
)
