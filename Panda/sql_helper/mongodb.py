# Copyright (C) 2021-2022 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

# Recode by @robotrakitangakbagus, @diemmmmmmmmmm
# Import PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport

import os
from redis import Redis
from Panda.Var import Var
from Panda.core.logger import logging

LOGS = logging.getLogger("PandaUserbot")

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None
    if Var.MONGO_URI:
        LOGS.warning(
            "'pymongo' not found!\nInstall pymongo[srv] to use Mongo database.."
        )


def get_data(self_, key):
    data = self_.get(str(key))
    if data:
        try:
            data = eval(data)
        except BaseException:
            pass
    return data


# --------------------------------------------------------------------------------------------- #



def __init__(self, key):
    self.dB = MongoClient(key, serverSelectionTimeoutMS=5000)
    self.db = self.dB.Var.MONGO_URI
    self.re_cache()

def __repr__(self):
    return f"<Mongo\n -total_keys: {len(self.keys())}\n>"

@property
def name(self):
    return "Mongo"

@property
def usage(self):
    return self.db.command("dbstats")["dataSize"]

def re_cache(self):
    self._cache = {}
    for key in self.keys():
        self._cache.update({key: self.get_key(key)})

def ping():
    try:
        self.dB.server_info()
    except BaseException:
        return False
    return True

def keys(self):
    return self.db.list_collection_names()

def setdb(self, key, value):
    if key in self.keys():
        self.db[key].replace_one({"_id": key}, {"value": str(value)})
    else:
        self.db[key].insert_one({"_id": key, "value": str(value)})
    self._cache.update({key: value})
    return True

def deldb(self, key):
    if key in self.keys():
        try:
            del self._cache[key]
        except KeyError:
            pass
        self.db.drop_collection(key)
        return True

def getdb(self, key):
    if key in self._cache:
        return self._cache[key]
    if key in self.keys():
        value = get_data(self, key)
        self._cache.update({key: value})
        return value
    return None

def get(self, key):
    if x := self.db[key].find_one({"_id": key}):
        return x["value"]

def flushall(self):
    self.dB.drop_database("Var.MONGO_URI")
    self._cache = {}
    return True






class RedisConnection(Redis):
    def __init__(
        self,
        host,
        port,
        password,
        platform=None,
        logger=LOGS,
        *args,
        **kwargs,
    ):
        if host and ":" in host:
            spli_ = host.split(":")
            host = spli_[0]
            port = int(spli_[-1])
            if host.startswith("http"):
                raise RedisError("Your REDIS_URI should not start with http !")
        elif host and port:
            pass
        else:
            raise RedisError("Port Number not found")

        kwargs["host"] = host
        kwargs["password"] = password
        kwargs["port"] = port

        if platform.lower() == "qovery" and not host:
            var, hash, host, password = "", "", "", ""
            for vars in os.environ:
                if vars.startswith("QOVERY_REDIS_") and vars.endswith("_HOST"):
                    var = vars
            if var:
                hash = var.split("_", maxsplit=2)[1].split("_")[0]
            if hash:
                kwargs["host"] = os.environ(f"QOVERY_REDIS_{hash}_HOST")
                kwargs["port"] = os.environ(f"QOVERY_REDIS_{hash}_PORT")
                kwargs["password"] = os.environ(f"QOVERY_REDIS_{hash}_PASSWORD")
        if logger:
            logger.info("Connecting to redis database")
        super().__init__(**kwargs)

    def set_redis(self, key, value):
        return self.set(str(key), str(value))

    def get_redis(self, key):
        data = None
        if self.get(str(key)):
            try:
                data = eval(self.get(str(key)))
            except BaseException:
                data = self.get(str(key))
        return data

    def del_redis(self, key):
        return bool(self.delete(str(key)))
