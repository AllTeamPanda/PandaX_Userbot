# /usr/bin/python3
# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# Please read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Recode Panda Userbot


from os import path
from time import sleep


PANDA = "Panda Userbot"

def with_header(text):
    return PANDA + "\n\n" + text

def telethon():
    yes_no = input("").strip().lower()
    if yes_no in ["telethon", "t"]:
        return True
    elif yes_no in ["notelethon", "not"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return telethon()

def pyrogram():
    yes_no = input("").strip().lower()
    if yes_no in ["pyrogram", "p"]:
        return True
    elif yes_no in ["nopyrogram", "nop"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return pyrogram

def ask_process_info_text():
    strm = input("").lower().strip()
    if strm == "e":
        print("Exiting...")
        exit(0)
    elif strm != "a":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        ask_process_info_text()


def envtelethon():
    start = input("").strip().lower()
    if start in ["telethon", "t"]:
        print(f"Ketik y untuk Creating .env file..")
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "SESSION", "DATABASE_URL", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        print("* Created '.env' file successfully! 😃")

    else:
        print("OK!")

def envpyrogram():
    start = input("").strip().lower()
    if start in ["pyrogram", "p"]:
        print(f"Ketik y untuk Creating .env file..")
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "PyroSESSION", "DATABASE_URL", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        print("* Created '.env' file successfully! 😃")

    else:
        print("OK!")



if not path.exists(".env"):
    print(with_header("# Do you want to move toward creating .env file ? [y/N] "))
    envtelethon()
    envpyrogram()
    

print(f"Ketik 'bash start.sh' to try running Panda Userbot")
sleep(0.5)
print("\nMade with 🐼 by @PandaUserbot...")
