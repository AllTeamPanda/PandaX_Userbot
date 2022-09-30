import requests
import bs4

from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import edit_or_reply, get_text
from . import HELP


HELP(
    "xvideo",
)

@ilhammansiz_on_cmd(
    ["xvideo"],
    cmd_help={
        "help": "Get direct Downloadable",
        "example": "{ch}xvideo xvideo_link",
    },
)
async def xvid(client, message):
    editer= await edit_or_reply(message, "`Please Wait.....`")
    msg = get_text(message)
    if not msg:
            await editer.edit("`Please Enter Valid Input`")
            return
    try:
        req = requests.get(msg)
        soup = bs4.BeautifulSoup(req.content, 'html.parser')

        soups = soup.find("div",{"id":"video-player-bg"})
        link =""
        for a in soups.find_all('a', href=True):
            link = a["href"]
        await editer.edit(f"HERE IS YOUR LINK:\n`{link}`")
    except:
        await editer.edit("Something went wrong")





@ilhammansiz_on_cmd(
    ["xsearch"],
    cmd_help={
        "help": "Xvideo Searcher",
        "example": "{ch}xsearch query",
    },
)

async def xvidsearch(client, message):
    editer= await edit_or_reply(message, "`Please Wait.....`")
    msg = get_text(message)
    if not msg:
            await editer.edit("`Please Enter Valid Input`")
            return
    try:
        qu = msg.replace(" ","+")
        page= requests.get(f"http://178.128.114.78/search/{qu}").content
        soup = bs4.BeautifulSoup(page, 'html.parser')
        col= soup.findAll("div",{"class":"thumb"})

        links= ""

        for i in col:
            a = i.find("a")
            link = a.get('href')

            semd = link.split("/")[2]

            links += f"<a href='http://178.128.114.78/search/{link}'>• {semd.upper()}</a>\n"
        await editer.edit(links,parse_mode="HTML")


    except:
         await editer.edit("Something Went Wrong")

