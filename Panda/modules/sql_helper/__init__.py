from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from ...file import Database

if Database.DB_URI.startswith("postgres://"):
    uri = Database.DB_URI.replace("postgres://", "postgresql://", 1)
else:
    uri = Database.DB_URI


def start() -> scoped_session:
    engine = create_engine(uri)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI tidak dikonfigurasi. Fitur yang membutuhkan database mengalami masalah."
    )
    print(str(e))
