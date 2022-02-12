
# Copyright (C) 2021-2022 TeamUltroid
# Recode Ilham mansiz


from Panda import SqL


def get_dnd_chats():
    return SqL.getdb("DND_CHATS") or []


def add_dnd(chat_id):
    x = get_dnd_chats()
    x.append(int(chat_id))
    return SqL.setdb("DND_CHATS", x)


def del_dnd(chat_id):
    x = get_dnd_chats()
    x.remove(int(chat_id))
    return SqL.setdb("DND_CHATS", x)


def chat_in_dnd(chat_id):
    return int(chat_id) in get_dnd_chats()
