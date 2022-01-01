import os
import sys

from decouple import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True


    APP_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("APP_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    STRING_SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=None)
    MONGO_URI = config("MONGO_URI", default=None)
