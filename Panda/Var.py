# Copyright (C) 2021-2022 TeamUltroid
# import Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import os
"""
os.system("pip3 install --no-cache-dir -U -q -r PandaVersion/Panda/Mansiez.txt")
"""  
import sys


from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True


    
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    STRING_SESSION = os.environ.get(
        "SESSION", None)
    STRING_SESSION = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("SESSION", None)
    MONGO_URI = os.environ.get("MONGO_URI", default=None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    REDIS_URI = os.environ.get("REDIS_URI", "redis-18892.c292.ap-southeast-1-1.ec2.cloud.redislabs.com:18892")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "9A6h30jSdRsO8DiFasSN4G8qXnUNA9H2")
    REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
    REDISHOST = os.environ.get("REDISHOST", None)
    REDISPORT = os.environ.get("REDISPORT", None)
    REDISUSER = os.environ.get("REDISUSER", None)
    
