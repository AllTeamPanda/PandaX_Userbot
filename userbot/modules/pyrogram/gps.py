# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
 


import logging

from geopy.geocoders import Nominatim

from userbot._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from userbot._func._helpers import edit_or_reply, get_text

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"
from . import HELP


HELP(
    "gps",
)

@ilhammansiz_on_cmd(
    ["gps"],
    cmd_help={
        "help": "Find and send the given location",
        "example": "{ch}gps <text>",
    },
)
async def gps(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    args = get_text(message)
    if not args:
        await pablo.edit("Please Provide location for sending GPS")
        return
    try:
        geolocator = Nominatim(user_agent="FridayUB")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
    except Exception as e:
        logging.info(e)
        await pablo.edit("`I Can't Find That Location!`")
        return
    gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
    await client.send_location(message.chat.id, float(latitude), float(longitude))
    await pablo.reply(
        "Open with: [Google Maps]({})".format(gm),
        disable_web_page_preview=False,
    )
    await pablo.delete()
