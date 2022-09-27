import re
import urllib
import urllib.parse

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply, get_text
from . import HELP


HELP(
    "search",
)

@ilhammansiz_on_cmd(
    ["duckduckgo", "ddg"],
    cmd_help={"help": "duckduckgo searcher!", "example": "{ch}ddg (query to search)"},
)
async def duckduckgo(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    query = get_text(message)
    if not query:
        await pablo.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    sample_url = "https://duckduckgo.com/?q={}".format(query.replace(" ", "+"))
    link = sample_url.rstrip()
    await pablo.edit(
        "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(query, link)
    )


@ilhammansiz_on_cmd(
    ["gs", "grs", "google"],
    cmd_help={"help": "Google Searcher!", "example": "{ch}gs (query to search)"},
)
async def grs(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    query = get_text(message)
    if not query:
        await pablo.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    query = urllib.parse.quote_plus(query)
    number_result = 8
    ua = UserAgent()
    google_url = (
        "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    )
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        try:
            link = r.find("a", href=True)
            title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
            description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
            if link != "" and title != "" and description != "":
                links.append(link["href"])
                titles.append(title)
                descriptions.append(description)

        except:
            continue
    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search("\/url\?q\=(.*)\&sa", l)
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))
    for x in to_remove:
        del titles[x]
        del descriptions[x]
    msg = ""

    for tt, liek, d in zip(titles, clean_links, descriptions):
        msg += f"[{tt}]({liek})\n`{d}`\n\n"
    await pablo.edit("**Search Query:**\n`" + query + "`\n\n**Results:**\n" + msg)

