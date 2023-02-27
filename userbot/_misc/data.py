# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••




from .._database import pdB
DEV = [5057493677, 1593802955]



def _sudousers_list():
    try:
        sudousers = pdB.get_key("sudousers_list") 
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]

def _dev_list():
    try:
        _users = pdB.get_key("devs_list")
    except AttributeError:
        pass
    ulist = _users.keys()
    return [int(chat) for chat in ulist]


def _users_list():
    try:
        sudousers = pdB.get_key("sudousers_list")
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    ulist = [int(chat) for chat in ulist]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    try:
        blacklistchats = pdB.get_key("blacklist_chats_list") 
    except AttributeError:
        blacklistchats = {}
    blacklist = blacklistchats.keys()
    return [int(chat) for chat in blacklist]


def sudo_enabled_cmds():
    listcmds = pdB.get_key("sudo_enabled_cmds")
    return listcmds





