from . import pdB





class WELCOME():
    try:
        eval(pdB.get_key("WELCOME"))
    except BaseException:
        pdB.set_key("WELCOME", "{}")

    def set_welcome(self, chat_id, file_id, text=None):
        ok = eval(pdB.get_key("WELCOME"))
        ok.update({chat_id: {"file_id": file_id, "caption": text}})
        return pdB.set_key("WELCOME", ok)

    def get_welcome(self, chat_id):
        ok = eval(pdB.get_key("WELCOME"))
        wl = ok.get(chat_id)
        if wl:
            return wl
        return


    def del_welcome(self, chat_id):
        ok = eval(pdB.get_key("WELCOME"))
        wl = ok.get(chat_id)
        if wl:
            ok.pop(chat_id)
            return pdB.set_key("WELCOME", ok)
        return



class DV():
    setdv = pdB.set_key
    getdv = pdB.get_key
    getalldv = pdB.get_key
    deldv = pdB.del_key



class Database(DV, WELCOME):
    pass
