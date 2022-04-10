import re

import requests


def paste_text(text):
    asciich = ["**", "`", "__"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    try:
        nekokey = (
            requests.post("https://nekobin.com/api/documents", json={"content": text})
            .json()
            .get("result")
            .get("key")
        )
        link = f"https://nekobin.com/{nekokey}"
    except Exception:
        url = "https://del.dog/documents"
        r = requests.post(url, data=text).json()
        link = f"https://del.dog/{r['key']}"
        if r["isUrl"]:
            link = f"https://del.dog/v/{r['key']}"
    return link

