import asyncio
import glob
import importlib
import logging
from ..Var import Config
import ntpath
import shlex
from typing import Tuple
import importlib
from pathlib import Path
import os

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = "main"



def load_modulesPyro(plugin_name, assistant=False):
    """Load PLugins - Assitant & User Using ImportLib"""
    if plugin_name.endswith("__"):
        pass
    else:
        if plugin_name not in Config.MAIN_NO_LOAD:
            if assistant:
                plugin_path = "userbot.modules.pyrogram.assistant." + plugin_name
            else:
                plugin_path = "userbot.modules.pyrogram." + plugin_name
            loader_type = "[🤖 Assistant]" if assistant else "[👤 User]"
            importlib.import_module(plugin_path)
            logging.info(f"{loader_type} - Connection : " + str(plugin_name))


def load_modulesTelethon(plugin_name, assistant=False):
    """Load PLugins - Assitant & User Using ImportLib"""
    if plugin_name.endswith("__"):
        pass
    else:
        if plugin_name not in Config.MAIN_NO_LOAD:
            if assistant:
                plugin_path = "userbot.modules.telethon.assistant." + plugin_name
            else:
                plugin_path = "userbot.modules.telethon." + plugin_name
            loader_type = "[🤖 Assistant]" if assistant else "[👤 User]"
            importlib.import_module(plugin_path)
            logging.info(f"{loader_type} - Connection : " + str(plugin_name))




def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        Path(f"userbot/modules/pyrogram/{shortname}.py")
        "userbot.modules.pyrogram.{}".format(shortname)
        logging.info("Successfully imported " + shortname)
    else:
        if plugin_path is None:
            Path(f"userbot/modules/pyrogram/{shortname}.py")
            f"userbot.modules.pyrogram.{shortname}"
        else:
            Path((f"{plugin_path}/{shortname}.py"))
            f"{plugin_path}/{shortname}".replace("/", ".")
        logging.info("Successfully imported " + shortname)



def buka(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/pyrogram/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/modules/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/modules/{folder}/{shortname}.py"))
                logging.info(f"Gagal membuka file {shortname} dikarenakan error {e}")



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

