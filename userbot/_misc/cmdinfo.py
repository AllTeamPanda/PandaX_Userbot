# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


from typing import Dict, List, Union

from ..config import Config




def _format_about(
    about: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
) -> str:  # sourcery no-metrics
    if not isinstance(about, dict):
        return about
    tmp_chelp = ""
    if "header" in about and isinstance(about["header"], str):
        tmp_chelp += f"{about['header'].title()}"
        del about["header"]
    if "description" in about and isinstance(about["description"], str):
        tmp_chelp += "\n\n»  **Description** :\n" f"{about['description'].capitalize()}"
        del about["description"]
    if "fungsi" in about and isinstance(about["fungsi"], str):
        tmp_chelp += "\n\n»  **Function** :\n" f"{about['fungsi'].capitalize()}"
        del about["fungsi"]
    if "flags" in about:
        tmp_chelp += "\n\n»  **Available Flags** :"
        if isinstance(about["flags"], dict):
            for f_n, f_d in about["flags"].items():
                tmp_chelp += f"\n    ▫ `{f_n}` : {f_d.lower()}"
        else:
            tmp_chelp += f"\n    {about['flags']}"
        del about["flags"]
    if "options" in about:
        tmp_chelp += "\n\n»  **Available Options** :"
        if isinstance(about["options"], dict):
            for o_n, o_d in about["options"].items():
                tmp_chelp += f"\n    ▫ `{o_n}` : {o_d.lower()}"
        else:
            tmp_chelp += f"\n    {about['options']}"
        del about["options"]
    if "types" in about:
        tmp_chelp += "\n\n»  **Supported Types** :"
        if isinstance(about["types"], list):
            for _opt in about["types"]:
                tmp_chelp += f"\n    `{_opt}` ,"
        else:
            tmp_chelp += f"\n    {about['types']}"
        del about["types"]
    if "usage" in about:
        tmp_chelp += "\n\n»  **Syntax** :"
        if isinstance(about["usage"], list):
            for ex_ in about["usage"]:
                tmp_chelp += f"\n    `{ex_}`"
        else:
            tmp_chelp += f"\n    `{about['usage']}`"
        del about["usage"]
    if "examples" in about:
        tmp_chelp += "\n\n»  **Examples** :"
        if isinstance(about["examples"], list):
            for ex_ in about["examples"]:
                tmp_chelp += f"\n    `{ex_}`"
        else:
            tmp_chelp += f"\n    `{about['examples']}`"
        del about["examples"]
    if "others" in about:
        tmp_chelp += f"\n\n»  **Others** :\n{about['others']}"
        del about["others"]
    if about:
        for t_n, t_d in about.items():
            tmp_chelp += f"\n\n»  **{t_n.title()}** :\n"
            if isinstance(t_d, dict):
                for o_n, o_d in t_d.items():
                    tmp_chelp += f"    ▫ `{o_n}` : {o_d.lower()}\n"
            elif isinstance(t_d, list):
                for _opt in t_d:
                    tmp_chelp += f"    `{_opt}` ,"
                tmp_chelp += "\n"
            else:
                tmp_chelp += t_d
                tmp_chelp += "\n"
    return tmp_chelp.replace("{tr}", Config.COMMAND_HAND_LER)
