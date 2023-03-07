from . import pdB

class WELCOME():
    try:
        eval(pdB.get_key("WELCOME"))
    except BaseException:
        pdB.set_key("WELCOME", "{}")

    def set_welcome(self, chat_id, file_id, text=None):
        ok = eval(pdB.get_key("WELCOME"))
        ok.update({chat_id: {"file_id": file_id, "caption": text}})
        return pdB.set_key("WELCOME", str(ok))

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
            return pdB.set_key("WELCOME", str(ok))
        return

    def get_welcome_ids(self):
        chat_ids = []
        all_welcome = eval(pdB.get_key("WELCOME"))
        for x in all_welcome:
            if not (int(x.chat_id) in chat_ids):
                chat_ids.append(int(x.chat_id))
        return chat_ids


class DV():
    setdv = pdB.set_key
    getdv = pdB.get_key
    getalldv = pdB.get_key
    deldv = pdB.del_key



class Database(DV, WELCOME):
    pass
