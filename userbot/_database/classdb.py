from . import pdB


class DV():
    setdv = pdB.set_key
    getdv = pdB.get_key
    getalldv = pdB.get_key
    deldv = pdB.del_key



class Database(DV):
    pass
