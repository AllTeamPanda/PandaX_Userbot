
from .._database import DatabaseCute
SqL = DatabaseCute()



gvarstatus = SqL.getdb 
addgvar = SqL.setdb 
delgvar = SqL.deldb 
 

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


