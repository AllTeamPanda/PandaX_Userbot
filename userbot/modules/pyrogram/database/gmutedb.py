"""
from . import db_x as SqL


def list_gmuted():
    return SqL.getdb("GMUTE") or []

def gmute(user):
    ok = list_gmuted()
    ok.append(int(user))
    return SqL.setdb("GMUTE", ok)


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(int(user))
        return SqL.setdb("GMUTE", ok)

def is_gmuted(user):
    return int(user) in list_gmuted()

"""


from .gmute_sql import *

gmute = gmute
ungmute = ungmute
is_gmuted = is_gmuted
