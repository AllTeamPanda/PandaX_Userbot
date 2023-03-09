# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.


import os

OTHERDV = [
    "NO_LOAD",
    "SUDO_USERS",
    "SUDO_CMDS",
    "PMPERMIT",
    "PM_LIMIT",
    "PMPERMIT_PIC",
    "PMPERMIT_TEXT",
    "PREFIX",
    "HELP_EMOJI",
]


class OtherConfig(object):
    def NoLoad(self):
        """Get your No load module list"""
        noloadvar = self.getdv("NO_LOAD") or os.getenv("NO_LOAD")
        data_list = noloadvar if noloadvar else False
        return data_list or self.NO_LOAD or []

    def SudoUsers(self):
        """Get sudo users"""
        sudovar = self.getdv("SUDO_USERS") or os.getenv("SUDO_USERS")
        data_list = [int(x) for x in sudovar] if sudovar else False
        return data_list or self.SUDO_USERS or []

    def Pmpermit(self):
        """Check whether pmpermit is on | off"""
        return self.getdv("PMPERMIT") or self.PMPERMIT or None

    def PmpermitLimit(self):
        """Check the number of warns, defaults to 4"""
        return self.getdv("PM_LIMIT") or self.PM_LIMIT or 4

    def PmpermitPic(self):
        """Check whether you have added a pic in your pmpermit or not"""
        return self.getdv("PMPERMIT_PIC") or self.PMPERMIT_PIC or None

    def PmpermitText(self):
        """Get the pmpermit text"""
        return self.getdv("PMPERMIT_TEXT") or self.PMPERMIT_TEXT or None

    def MyPrefix(self):
        """Get list of prefixes (command handlers)"""
        return self.getdv("PREFIX") or "."

    def HelpEmoji(self):
        """This will return the emoji which will be used in helpdex"""
        return self.getdv("HELP_EMOJI") or self.HELP_EMOJI or ""

    def SudoCmds(self):
        """returns a list of command names"""
        return self.getdv("SUDO_CMDS") or os.getenv("SUDO_CMDS")
