
# Copyright (C) 2021-2022 TeamUltroid
# Recode Ilham mansiz

from Panda import SqL


def get_stuff(key=None):
    return SqL.getdb(key) or {}


def add_welcome(chat, msg, media, button):
    ok = get_stuff("WELCOME")
    ok.update({chat: {"welcome": msg, "media": media, "button": button}})
    return SqL.setdb("WELCOME", ok)


def get_welcome(chat):
    ok = get_stuff("WELCOME")
    return ok.get(chat)


def delete_welcome(chat):
    ok = get_stuff("WELCOME")
    if ok.get(chat):
        ok.pop(chat)
        return SqL.setdb("WELCOME", ok)


def add_goodbye(chat, msg, media, button):
    ok = get_stuff("GOODBYE")
    ok.update({chat: {"goodbye": msg, "media": media, "button": button}})
    return SqL.setdb("GOODBYE", ok)


def get_goodbye(chat):
    ok = get_stuff("GOODBYE")
    return ok.get(chat)


def delete_goodbye(chat):
    ok = get_stuff("GOODBYE")
    if ok.get(chat):
        ok.pop(chat)
        return SqL.setdb("GOODBYE", ok)


def add_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    x.update({chat: True})
    return SqL.setdb("THANK_MEMBERS", x)


def remove_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    if x.get(chat):
        x.pop(chat)
        return SqL.setdb("THANK_MEMBERS", x)


def must_thank(chat):
    x = get_stuff("THANK_MEMBERS")
    return x.get(chat)
