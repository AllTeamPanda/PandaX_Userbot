
# Copyright (C) 2021-2022 TeamUltroid
# Recode by Ilham mansiez

from Panda import SqL


def get_approved():
    return SqL.getdb("PMPERMIT") or []


def approve_user(id):
    ok = get_approved()
    if id in ok:
        return True
    ok.append(id)
    return SqL.setdb("PMPERMIT", ok)


def disapprove_user(id):
    ok = get_approved()
    if id in ok:
        ok.remove(id)
        return SqL.setdb("PMPERMIT", ok)


def is_approved(id):
    return id in get_approved()
