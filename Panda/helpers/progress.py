import hashlib
import math
import re
import time
from typing import Dict, Tuple

from telethon.errors.rpcerrorlist import MessageNotModifiedError

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)

_TASKS: Dict[str, Tuple[int, int]] = {}


async def md5(fname: str) -> str:
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def humanbytes(size: int) -> str:
    if size is None or isinstance(size, str):
        return ""

    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    seconds = round(seconds, 2)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
    )
    return tmp[:-2]


def readable_time(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (
        ((str(int(days)) + " day(s), ") if days else "")
        + ((str(int(hours)) + ":") if hours else "00:")
        + ((str(int(minutes)) + ":") if minutes else "00:")
        + (str(int(seconds)) if seconds else "00")
    )


def human_to_bytes(size: str) -> int:
    units = {
        "M": 2 ** 20,
        "MB": 2 ** 20,
        "G": 2 ** 30,
        "GB": 2 ** 30,
        "T": 2 ** 40,
        "TB": 2 ** 40,
    }

    size = size.upper()
    if not re.match(r" ", size):
        size = re.sub(r"([KMGT])", r" \1", size)
    number, unit = [string.strip() for string in size.split()]
    return int(float(number) * units[unit])


async def progress(
    current,
    total,
    gdrive,
    start,
    prog_type,
    file_name=None,
    is_cancelled=False,
    delay=5,
):  # sourcery no-metrics
    if is_cancelled is True:
        raise CancelProcess
    task_id = f"{gdrive.chat_id}.{gdrive.id}"
    if current == total:
        if task_id not in _TASKS:
            return
        del _TASKS[task_id]
        try:
            await gdrive.edit("`finalizing process ...`")
        except MessageNotModifiedError:
            pass
        except Exception as e:
            LOGS.error(str(e))
        return
    now = time.time()
    if task_id not in _TASKS:
        _TASKS[task_id] = (now, now)
    start, last = _TASKS[task_id]
    elapsed_time = now - start
    oldtmp = ""
    if (now - last) >= delay:
        _TASKS[task_id] = (start, now)
        percentage = current * 100 / total
        speed = current / elapsed_time
        eta = round((total - current) / speed)
        elapsed_time = round(elapsed_time)
        if "upload" in prog_type.lower():
            status = f"Uploading"
        elif "download" in prog_type.lower():
            status = f"Downloading"
        else:
            status = "Unknown"
        progress_str = "`{0}` | `[{1}{2}] {3}%`".format(
            status,
            "".join(
                Config.FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 5))
            ),
            "".join(
                Config.UNFINISHED_PROGRESS_STR
                for i in range(20 - math.floor(percentage / 5))
            ),
            round(percentage, 2),
        )
        tmp = (
            f"{progress_str}\n"
            f"`{humanbytes(current)} of {humanbytes(total)}"
            f" @ {humanbytes(speed)}`\n"
            f"**ETA :**` {time_formatter(eta)}`\n"
            f"**Duration :** `{time_formatter(elapsed_time)}`"
        )
        if tmp != oldtmp:
            if file_name:
                await gdrive.edit(
                    f"**{prog_type}**\n\n"
                    f"**File Name : **`{file_name}`**\nStatus**\n{tmp}"
                )
            else:
                await gdrive.edit(f"**{prog_type}**\n\n" f"**Status**\n{tmp}")
            oldtmp = tmp


class CancelProcess(Exception):
    """
    Cancel Process
    """
