# Copyright (C) 2021-2022 TeamUltroid
# editor by panda


import os
import sys
from Panda.Var import Var
from .core.logger import logging

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None

LOGS = logging.getLogger("PandaUserbot")


def get_data(self_, key):
    data = self_.get(str(key))
    if data:
        try:
            data = eval(data)
        except BaseException:
            pass
    return data


class MongoDB:
    def __init__(self, key):
        self.dB = MongoClient(key, serverSelectionTimeoutMS=5000)
        self.db = self.dB.PandaBASE
        self.re_cache()

    def __repr__(self):
        return f"<Panda.MonGoDB\n -total_keys: {len(self.keys())}\n>"

    @property
    def name(self):
        return "Mongo"

    @property
    def usage(self):
        return 0

    def re_cache(self):
        self._cache = {}
        for key in self.keys():
            self._cache.update({key: self.get_key(key)})

    def ping(self):
        if self.dB.server_info():
            return True

    def keys(self):
        return self.db.list_collection_names()

    def set_key(self, key, value):
        if key in self.keys():
            self.db[key].replace_one({"_id": key}, {"value": str(value)})
        else:
            self.db[key].insert_one({"_id": key, "value": str(value)})
        self._cache.update({key: value})
        return True

    def del_key(self, key):
        if key in self.keys():
            try:
                del self._cache[key]
            except KeyError:
                pass
            self.db.drop_collection(key)
            return True

    def get_key(self, key):
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
        self.dB.drop_database("PandaBASE")
        self._cache = {}
        return True




def PandaBASE():
    if MongoClient and Var.MONGO_URI:
        return MongoDB(Var.MONGO_URI)
