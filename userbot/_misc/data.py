# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot



from .._database import pdB
DEV = [5057493677, 1593802955]



def _sudousers_list():
    try:
        sudousers = pdB.get_key("sudousers_list") or []
    except AttributeError:
        pass
    ulist = sudousers
    return ulist

def _dev_list():
    try:
        _users = pdB.get_key("devs_list") or []
    except AttributeError:
        pass
    ulist = _users
    return ulist


def _users_list():
    try:
        sudousers = pdB.get_key("sudousers_list") or []
    except AttributeError:
        pass
    ulist = sudousers
    ulist = [int(chat) for chat in ulist]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    try:
        blacklistchats = pdB.get_key("blacklist_chats_list") 
    except AttributeError:
        pass
    blacklist = blacklistchats
    return blacklist


def sudo_enabled_cmds():
    listcmds = pdB.get_key("sudo_enabled_cmds") or []
    return list(listcmds)





