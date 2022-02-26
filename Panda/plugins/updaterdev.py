"""
This module updates the userbot based on upstream revision
"""
# Credits: @robotrakitangakbagus, @diemmmmmmmmmm
# FROM PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport
# Mengupdate pengguna dengan Dev mengendalikannya khusus Pandabot

import os, shutil
import heroku3
from Panda.Config import Config
from Panda import DEVLIST, PandaBot
from ..core.managers import edit_or_reply
from Panda.events import register
import asyncio
import os
from . import BOTLOG_CHATID

plugin_category = "modules"
## ===================================

REPO_URL = "https://github.com/PandaUserbot/Dev"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME 
HEROKU_API_KEY = Config.HEROKU_API_KEY
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
## ======================================

def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err

@register(incoming=True, from_users=DEVLIST, pattern=r"^update$")
async def panda(cool):
    restart = await cool.reply("Sedang Mengupdate Secara Devoloper Panda Userbot ")
    ilhammansiz = Heroku.apps()[HEROKU_APP_NAME]
    await asyncio.sleep(3)
    await restart.delete()
    ilhammansiz.restart()
    r = await cool.reply("Berhasil Mengupdate Bisa digunakan kembali")
    await r.delete()



## Ngapain lu anjeng 
## Ngentot
