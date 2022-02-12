
# Copyright (C) 2021-2022 TeamUltroid
# Recode Ilham Mansiez

from Panda import SqL


def get_logger():
    return SqL.getdb("LOGUSERS") or []


def is_logger(id_):
    return id_ in get_logger()


def log_user(id_):
    pmperm = get_logger()
    pmperm.append(id_)
    return SqL.setdb("LOGUSERS", pmperm)


def nolog_user(id_):
    pmperm = get_logger()
    pmperm.remove(id_)
    return SqL.setdb("LOGUSERS", pmperm)
