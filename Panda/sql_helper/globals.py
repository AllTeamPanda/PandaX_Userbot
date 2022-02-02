try:
    from . import BASE, Config, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None


class Globals(BASE):
    __tablename__ = "globals"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value


Globals.__table__.create(checkfirst=True)


def gvarstatus(variable):
    try:
        return (
            SESSION.query(Globals)
            .filter(Globals.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def addgvar(variable, value):
    if SESSION.query(Globals).filter(Globals.variable == str(variable)).one_or_none():
        delgvar(variable)
    adder = Globals(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()


def delgvar(variable):
    rem = (
        SESSION.query(Globals)
        .filter(Globals.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()



def get_chats():
    cha = gvarstatus("VC_AUTH_GROUPS")
    if not cha:
        cha = "{}"
    return eval(cha)


def add_vcauth(chat_id, admins=False):
    omk = get_chats()
    omk.update({chat_id: {"admins": admins}})
    addgvar("VC_AUTH_GROUPS", str(omk))
    return True


def check_vcauth(chat_id):
    omk = get_chats()
    if omk.get(chat_id):
        return omk[chat_id], omk[chat_id]["admins"]
    return None, None


def rem_vcauth(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        try:
            del omk[chat_id]
            addgvar("VC_AUTH_GROUPS", str(omk))
            return True
        except KeyError:
            return False
    return None








def get_stuff():
    return gvarstatus("FILTERS") or {}


def add_filter(chat, word, msg, media, button):
    ok = get_stuff()
    if ok.get(chat):
        ok[chat].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({chat: {word: {"msg": msg, "media": media, "button": button}}})
    addgvar("FILTERS", ok)


def rem_filter(chat, word):
    ok = get_stuff()
    if ok.get(chat) and ok[chat].get(word):
        ok[chat].pop(word)
        addgvar("FILTERS", ok)


def rem_all_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        ok.pop(chat)
        addgvar("FILTERS", ok)


def get_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        return ok[chat]


def list_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        return "".join(f"👉 `{z}`\n" for z in ok[chat])




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
    if MongoClient and Config.MONGO_URI:
        return MongoDB(Config.MONGO_URI)
