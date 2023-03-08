# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from . import pdB


class PMPERMIT(object):
    # add message id of a user
    def set_msgid(self, user_id, msg_id):
        user = pdB.get_key("set_msgid") or {}
        if not user:
            user.update({user_id: msg_id})
            user = pdB.set_key("set_msgid", user)
        else:
            user.msg_id = msg_id
            

    # get warn message id
    def get_msgid(self, user_id):
        user = pdB.get_key("set_msgid")
        msg_id = None
        if user:
            msg_id = user.msg_id
            return msg_id
        

    # add user id to whitelist
    def set_whitelist(self, user_id, boolvalue):
        user = pdB.get_key("whitelist") or {}
        if not user:
            user.update({user_id: boolvalue})
            user = pdB.set_key("whitelist", user)
        else:
            user.boolvalue = str(boolvalue)
           
        return user_id

    # remove user id from whitelist
    def del_whitelist(self, user_id):
        user = pdB.get_key("whitelist")
        if user:
            pdB.del_key("whitelist")
                
        return False

    # get whitelist (approved)
    def get_whitelist(self, user_id):
        user = pdB.get_key("whitelist")
        rep = ""
        if user:
            rep = str(user.boolvalue)
        return rep

    # warn table func
    def set_warn(self, user_id, warn_count):
        user = pdB.get_key("warns") or {}
        if not user:
            user.update({user_id: warn_count})
            user = pdB.set_key("warns", user)
        else:
            user.warn_count = warn_count
                

    # get warn func
    def get_warn(self, user_id):
        user = pdB.get_key("warns")
        rep = ""
        if user:
            rep = str(user.warn_count)
        return rep

    # del warn func
    def del_warn(self, user_id):
        user = pdB.get_key("warns")
        if user:
            pdB.del_key("warns")
                    
        return False



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
