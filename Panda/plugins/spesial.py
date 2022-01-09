import random
from . import PandaBot

plugin_category = "Plugins"

import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL

FONT_FILE_TO_USE = "./ulPanda/core/Voice In My Head_080621160753.otf"

Spesial = [
     "https://telegra.ph/file/3a128f03b625e0f1a96d1.mp4"
     "https://telegra.ph/file/fc0d6c09d8ddf89aa9772.mp4"
     "https://telegra.ph/file/f915c7aeab2c481747163.mp4"
     "https://telegra.ph/file/58db2cd17ea842954e605.mp4"
     "https://telegra.ph/file/c76f67ab5288941e7e96a.mp4"
]


@PandaBot.ilhammansiz_cmd(
    pattern="spesial(?: |$)(.*)",
    command=("spesial", plugin_category),
    info={
        "header": "Gambar tetek 😂.",
        "description": "Menemukan tetek wkwk😂",
        "usage": "{tr}spesial ",
    },
)
async def spesial(event):
    while True:
        piclink = random.randint(0, len(Spesial) - 1)
        SPESIAL = Spesial[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(SPESIAL, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        await event.client.upload_file(photo)  # pylint:disable=E0602
