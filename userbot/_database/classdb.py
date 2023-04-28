# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from . import pdB


class PMPERMIT(object):
    def is_user_approved(self, chat_id):
        ok = pdB.get_key("PMPERMIT") or {}
        wl = ok.get(chat_id)
        if wl:
            return wl
        return

    def approve_user(self, chat_id):
        ok = pdB.get_key("PMPERMIT")
        ok.update({chat_id})
        return pdB.set_key("PMPERMIT", ok)


    def disapprove_user(self, chat_id):
        ok = pdB.get_key("PMPERMIT")
        if ok:
            return pdB.del_key("PMPERMIT")
        return
    


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

    def set_welcome(self, chat, file_id, text=None):
        ok = pdB.get_key("WELCOME")
        ok.update({chat: {"file_id": file_id, "caption": text}})
        return pdB.set_key("WELCOME", ok)

    def get_welcome(self, chat):
        ok = pdB.get_key("WELCOME")
        wl = ok.get(chat)
        if wl:
            return wl
        return


    def del_welcome(self, chat):
        ok = pdB.get_key("WELCOME")
        wl = ok.get(chat)
        if wl:
            ok.pop(chat)
            return pdB.set_key("WELCOME", ok)
        return

    
   


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
