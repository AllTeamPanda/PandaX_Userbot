import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# the secret configuration specific things
from ..Var import Var
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


def start() -> scoped_session:
    engine = create_engine(Var.DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    LOGS.error(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    LOGS.error(str(e))


def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    if os.getenv("RAILWAY_STATIC_URL"):
        return "railway"
    if os.getenv("KUBERNETES_PORT"):
        return "qovery"
    if os.getenv("WINDOW") and os.getenv("WINDOW") != "0":
        return "windows"
    if os.getenv("RUNNER_USER") or os.getenv("HOSTNAME"):
        return "github actions"
    if os.getenv("ANDROID_ROOT"):
        return "termux"
    return "local"


HOSTED_ON = where_hosted()

