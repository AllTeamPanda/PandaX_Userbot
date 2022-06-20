import asyncio
import glob
import importlib
import logging
from ..Osdb import Osdb as Config
import ntpath
import shlex
from typing import Tuple
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = "PandaUserbot"

"""
def load_plugins(plugin_name):
  
    if plugin_name not in Config.XTRA_NO_LOAD:
        plugin_path = "Plugins." + plugin_name
        loader_type = "[USER][XTRA-PetercordUserbot]"
        importlib.import_module(plugin_path)
        logging.info(f"{loader_type} - Loaded : " + str(plugin_name))
"""

def load_modulesPyro(plugin_name, assistant=False):
    """Load PLugins - Assitant & User Using ImportLib"""
    if plugin_name.endswith("__"):
        pass
    else:
        if plugin_name not in Config.MAIN_NO_LOAD:
            if assistant:
                plugin_path = "assistant." + plugin_name
            else:
                plugin_path = "ModulesPyro." + plugin_name
            loader_type = "[Assistant]" if assistant else "[User]"
            importlib.import_module(plugin_path)
            logging.info(f"{loader_type} - Loaded : " + str(plugin_name))


def plugin_collecter(path):
    """Collects All Files In A Path And Give Its Name"""
    if path.startswith("/"):
        path = path[1:]
    if path.endswith("/"):
        pathe = path + "*.py"
    else:
        pathe = path + "/*.py"
    Poppy = glob.glob(pathe)
    final = []
    Pop = Poppy
    for x in Pop:
        k = ntpath.basename(x)
        if k.endswith(".py"):
            lily = k.replace(".py", "")
            final.append(lily)
    return final  


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def update_it():
    """Update Userbot On StartUps."""
    try:
        repo = Repo()
    except GitCommandError:
        logging.debug("Invalid Git Command. Not Updating....")
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(Config.U_BRANCH, origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    if repo.active_branch.name != Config.U_BRANCH:
        logging.debug("You Active Branch Doesn't Match With The Default Branch. Please Make Sure You Are on Default Branch.")
        return
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(Config.U_BRANCH)
    try:
        ups_rem.pull(Config.U_BRANCH)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
    return
