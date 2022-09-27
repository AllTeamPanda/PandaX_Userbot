from sqlalchemy import Column, String

from . import BASE, SESSION

default_thumb = "https://icon-icons.com/downloadimage.php?id=106660&root=1527/PNG/512/&file=shield_106660.png"
default_text = "PandaUserbot"

class pmdb(BASE):
    __tablename__ = "pmdb"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, text=default_text, thumb=default_thumb, psl=3):
        self.text = text
        self.thumb = thumb
        self.psl = psl


pmdb.__table__.create(checkfirst=True)



def add_pm_text(thumb=default_thumb, text=default_text):
    adder = pmdb(thumb, text)
    SESSION.add(adder)
    SESSION.commit()

def add_pm_thumb(thumb=default_thumb, text=default_text):
    adder = pmdb(text, thumb)
    SESSION.add(adder)
    SESSION.commit()

def get_thumb(text):
    try:
        return SESSION.query(pmdb).filter(pmdb.text == thumb).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

def get_pm_text(thumb):
    try:
        return SESSION.query(pmdb).filter(pmdb.text == thumb).one()
    except BaseException:
        return None
    finally:
        SESSION.close()




def set_pm_spam_limit(psl=3):
    adder = pmdb(int(psl), int(psl))
    SESSION.add(adder)
    SESSION.commit()

def get_pm_spam_limit(pls=3):
    try:
        return SESSION.query(pmdb).filter(pmdb.psl == int(psl)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()
