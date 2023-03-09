# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from . import pdB


class PMPERMIT(object):
    def get_approved():
        return pdB.get_key("PMPERMIT") or []

    def approve_user(chat_id):
        ok = get_approved()
        if chat_id in ok:
            return True
        ok.append(chat_id)
        return pdB.set_key("PMPERMIT", ok)


    def disapprove_user(chat_id):
        ok = get_approved()
        if chat_id in ok:
            ok.remove(chat_id)
            return pdB.set_key("PMPERMIT", ok)


    def is_user_approved(chat_id):
        return chat_id in get_approved()



MY_AFK = {}

class AFK(object):
    """AMC -> Afk Modification Class"""

    def set_afk(self, afk, reason, afktime):
        global MY_AFK
        afk_db = pdB.get_key("AFK_DB") or {}
        if afk_db:
            pdB.del_key("AFK_DB")
        afk_db.update({0: {"afk": afk, "reason": reason, "afktime": afktime}})
        pdB.set_key("AFK_DB", afk_db)
        MY_AFK[0] = {"afk": afk, "reason": reason, "afktime": afktime}

    def get_afk(self):
        return MY_AFK.get(0)


    
            



class WELCOME():
    try:
        pdB.get_key("WELCOME") or {}
    except BaseException:
        pdB.set_key("WELCOME", "{}")

    def set_welcome(self, chat_id, file_id, text=None):
        ok = pdB.get_key("WELCOME")
        ok.update({chat_id: {"file_id": file_id, "caption": text}})
        return pdB.set_key("WELCOME", ok)

    def get_welcome(self, chat_id):
        ok = pdB.get_key("WELCOME")
        wl = ok.get(chat_id)
        if wl:
            return wl
        return


    def del_welcome(self, chat_id):
        ok = pdB.get_key("WELCOME")
        wl = ok.get(chat_id)
        if wl:
            ok.pop(chat_id)
            return pdB.set_key("WELCOME", ok)
        return

    def get_welcome_ids(self):
        chat_ids = []
        all_welcome = pdB.get_key("WELCOME") or {}
        for x in all_welcome:
            if not (int(x.chat_id) in chat_ids):
                chat_ids.append(int(x.chat_id))
        return chat_ids


class DV():
    setdv = pdB.set_key
    getdv = pdB.get_key
    deldv = pdB.del_key

    def getalldv(self):
        kv_data = {}
        mydata = pdB.get_key
        for x in mydata:
            kv_data.update({x.keys: x.values})

        return kv_data



class Database(DV, WELCOME, AFK, PMPERMIT):
    pass
