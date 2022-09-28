from ...._database import DatabaseCute
DB = DatabaseCute()




def get_stuff():
    return DB.getdb("AFK_DB") or []

def go_afk(time, reason=""):
    DB.setdb("AFK_DB", [time, reason])
    return

def check_afk():
    afk = get_stuff()
    if afk:
        return afk[0], afk[1]
    return False


def no_afk():
    return DB.deldb("AFK_DB")

