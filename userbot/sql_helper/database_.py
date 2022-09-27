
# Credits: @robotrakitangakbagus, @diemmmmmmmmmm
# FROM PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport



try:
    from . import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText

from ..Var import Var
import logging

LOGS = logging.getLogger("PandaUserbot")

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None
    if Var.MONGO_URI:
        LOGS.warning(
            "'pymongo' not found!\nInstall pymongo[srv] to use Mongo database.."
        )

class Sqldb(BASE):
    __tablename__ = "sqldb"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value



Sqldb.__table__.create(checkfirst=True)


def getdb(variable):
    try:
        return (
            SESSION.query(Sqldb)
            .filter(Sqldb.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def setdb(variable, value):
    if SESSION.query(Sqldb).filter(Sqldb.variable == str(variable)).one_or_none():
        deldb(variable)
    adder = Sqldb(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()


def deldb(variable):
    rem = (
        SESSION.query(Sqldb)
        .filter(Sqldb.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()


class MongoDB:
    def __init__(self, key):
        self.dB = MongoClient(key, serverSelectionTimeoutMS=5000)
        self.db = self.dB.BaseDB
        self.re_cache()

    def __repr__(self):
        return f"<Base.MonGoDB\n -total_keys: {len(self.keys())}\n>"

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

    def ping(self):
        if self.dB.server_info():
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
        self.dB.drop_database("BaseDB")
        self._cache = {}
        return True



def BaseDB():
    if Var.DB_URI:
        return getdb, setdb, deldb

    if MongoClient and Var.MONGO_URI:
        return MongoDB(Var.MONGO_URI)


