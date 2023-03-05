import os
from glob import glob
from typing import Any, Dict, List, Union

from userbot import *
from userbot._misc.tools import translate
from yaml import safe_load

Plang = udB.get_key("language") or os.getenv("LANGUAGE", "en")

languages = {}
PATH = "pyPanda/strings/{}.yml"


def load(file):
    if not file.endswith(".yml"):
        return
    elif not os.path.exists(file):
        file = PATH.format("en")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        languages[code] = safe_load(
            open(file, encoding="UTF-8"),
        )
    except Exception as er:
        LOGS.info(f"Error in {file[:-4]} language file")
        LOGS.exception(er)


load(PATH.format(Plang))


def get_string(key: str, _res: bool = True) -> Any:
    lang = Plang or "en"
    try:
        return languages[lang][key]
    except KeyError:
        try:
            en_ = languages["en"][key]
            tr = translate(en_, lang_tgt=lang).replace("\ N", "\n")
            if en_.count("{}") != tr.count("{}"):
                tr = en_
            if languages.get(lang):
                languages[lang][key] = tr
            else:
                languages.update({lang: {key: tr}})
            return tr
        except KeyError:
            if not _res:
                return
            return f"Warning: could not load any string with the key `{key}`"
        except TypeError:
            pass
        except Exception as er:
            LOGS.exception(er)
        if not _res:
            return None
        return languages["en"].get(key) or f"Failed to load language string '{key}'"


def get_help(key):
    get_string(f"help_{key}")
    

def get_languages() -> Dict[str, Union[str, List[str]]]:
    for file in glob("pyPanda/strings/*yml"):
        load(file)
    return {
        code: {
            "name": languages[code]["name"],
            "natively": languages[code]["natively"],
            "authors": languages[code]["authors"],
        }
        for code in languages
    }
