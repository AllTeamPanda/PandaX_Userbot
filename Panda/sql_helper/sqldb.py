try:
    from . import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText



class Sqldb(BASE):
    __tablename__ = "sqldb"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value


Sqldb.__table__.create(checkfirst=True)


def get(variable):
    try:
        return (
            SESSION.query(Sqldb)
            .filter(Sqldb.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def set(variable, value):
    if SESSION.query(Sqldb).filter(Sqldb.variable == str(variable)).one_or_none():
        del(variable)
    adder = Sqldb(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()


def del(variable):
    rem = (
        SESSION.query(Sqldb)
        .filter(Sqldb.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()
