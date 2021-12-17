try:
    from . import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText


class Globals(BASE):
    __tablename__ = "globals"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value


Globals.__table__.create(checkfirst=True)


def gvarstatus(variable):
    try:
        return (
            SESSION.query(Globals)
            .filter(Globals.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def addgvar(variable, value):
    if SESSION.query(Globals).filter(Globals.variable == str(variable)).one_or_none():
        delgvar(variable)
    adder = Globals(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()


def delgvar(variable):
    rem = (
        SESSION.query(Globals)
        .filter(Globals.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()



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
