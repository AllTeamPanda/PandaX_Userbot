# /usr/bin/python3
# Panda - UserBot
# Copyright (C) 2022-2023 Panda Userbot


from time import sleep
from os import system, path

PANDA = "★ PANDA USERBOT DEPLOY★"


def clear():
    system("clear")


def Start(text):
    return PANDA + "\n\n" + text

def telethon():
    thon = input("").strip().lower()
    if thon in ["telethon", "t"]:
        return True
    elif yes_no in ["notelethon", "not"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return telethon()

def pyrogram():
    pyro = input("").strip().lower()
    if pyro in ["pyrogram", "p"]:
        return True
    elif pyro in ["nopyrogram", "nop"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return pyrogram()

def info_text():
    strm = input("").lower().strip()
    if strm == "e":
        print("Exiting...")
        exit(0)
    elif strm != "a":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        info_text()
    elif strm != "ap":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        info_text()


def envtelethon():
    starthon = input("").strip().lower()
    if starthon in ["telethon", "t"]:
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "SESSION", "MONGO_URI", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        sleep(0.1)
        system("screen -S PandaX_Userbot")
        sleep(0.1)
        system("bash start")
   
def envpyrogram():
    startpyro = input("").strip().lower()
    if startpyro in ["pyrogram", "p"]:
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "PyroSESSION", "MONGO_URI", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        sleep(0.1)
        system("screen -S PandaX_Userbot")
        sleep(0.1)
        system("bash start")



if not path.exists(".env"):
    print(Start("Typing t for telethon and Tpyping p for pyrogram"))
    envtelethon()
    envpyrogram()
    
