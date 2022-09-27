from sqlalchemy import Column, String

from . import BASE, SESSION


class Autopost(BASE):
    __tablename__ = "autopost"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, to_channel, target_channel):
        self.to_channel = to_channel
        self.target_channel = target_channel


Autopost.__table__.create(checkfirst=True)


def get_autopost(target_channel):
    try:
        return SESSION.query(Autopost).filter(Autopost.target_channel == int(target_channel)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def check_if_autopost_in_db(to_channel, target_channel):
    try:
        return SESSION.query(Autopst).get(int(target_channel))
    finally:
        SESSION.close()


def add_new_autopost(to_channel, target_channel):
    adder = Autopost(int(target_channel), int(to_channel))
    SESSION.add(adder)
    SESSION.commit()


def del_autopost(to_channel, target_channel):
    rem = SESSION.query(Autopost).get(int(target_channel), int(to_channel))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


