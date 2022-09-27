
from ...._database import DatabaseCute
DB = DatabaseCute()


try:
    eval(DB.getdb("WELCOME"))
except BaseException:
    DB.setdb("WELCOME", "{}")




def add_welcome(chat_id, message_id):
    ok = eval(DB.getdb("WELCOME"))
    ok.update({chat_id: {"msg_id": message_id}})
    return DB.setdb("WELCOME", str(ok))


def welcome_info(chat_id):
    ok = eval(DB.getdb("WELCOME"))
    wl = ok.get(chat_id)
    if wl:
        return wl
    return


def del_welcome(chat_id):
    ok = eval(DB.getdb("WELCOME"))
    wl = ok.get(chat_id)
    if wl:
        ok.pop(chat_id)
        return DB.setdb("WELCOME", str(ok))
    return

