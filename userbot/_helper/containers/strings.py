# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.

class Strings(object):
    def stat_string(self):
        return f"""
		        **Name:** {self.UserName()}
			**Version:** {self.assistant_version}
			**Python version:** {self.python_version}
			**Pyrogram version:** {self.pyrogram_version}
			**Database:** {self.db_status()}
			**Uptime:** {self.uptime()}
			**User Bio:** {self.UserBio()}
			"""

    def closed_menu_string(self):
        return """  • Menu is closed
                    """
