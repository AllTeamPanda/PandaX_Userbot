from covid import Covid
from . import ilhammansiz
from Panda import PandaBot
from telethon import *
Stark = PandaBot.tgbot

@ilhammansiz(pattern="/covid ?(.*)")
async def corona(event):
    await event.reply("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`😟New Deaths  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔New Cases   : {country_data['new_cases']}`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await event.reply(f"`Corona Virus Info in {country}:`\n\n{output_text}")


Covid = """
- /covid Daftar covid 19
"""



@Stark.on(events.callbackquery.CallbackQuery(data="covid"))
async def _(event):
    await event.edit(Covid, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

@Stark.on(events.callbackquery.CallbackQuery(data="covids"))
async def _(event):
    await event.edit(Covid, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])



Telegraph = """
- /tm untuk mengubah gambar menjadi link telegraph
- /txt mengubah text menjadi telegraph
"""
@Stark.on(events.callbackquery.CallbackQuery(data="telegram"))
async def _(event):
    await event.edit(Telegraph, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

@Stark.on(events.callbackquery.CallbackQuery(data="telegrams"))
async def _(event):
    await event.edit(Telegraph, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])


TINY = """
- /tiny balas ke sticker untuk memperkecil
"""



@Stark.on(events.callbackquery.CallbackQuery(data="tiny"))
async def _(event):
    await event.edit(TINY, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

@Stark.on(events.callbackquery.CallbackQuery(data="tinys"))
async def _(event):
    await event.edit(TINY, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])


