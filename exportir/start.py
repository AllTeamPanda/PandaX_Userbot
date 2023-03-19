# /usr/bin/python3
# Panda - UserBot
# Copyright (C) 2022-2023 Panda Userbot

from base64 import b64decode
from time import sleep
from os import system, path
from userbot import Config

PANDA = "★ PANDA USERBOT DEPLOY★"


def clear():
    system("clear")


def Start(text):
    return PANDA + "\n\n" + text

def telethon():
    thon = input("").strip().lower()
    if thon in ["yas", "y"]:
        return True
    elif yes_no in ["notelethon", "not"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return telethon()



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


def envbot():
    starthon = input("").strip().lower()
    if starthon in ["yas", "y"]:
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "SESSION", "MONGO_URI", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN"]:   
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        sleep(0.1)
        system("screen -S Panda")
        
def Zip():
    global regex
    regex='(https?)://github.com/.+/.+'
    if Config.UPSTREAM_REPO == "PANDA_USERBOT":
        Zip = "aHR0cHM6Ly9naXRodWIuY29tL1RlYW1YUGFuZGEvUGFuZGEvYXJjaGl2ZS9tYWluLnppcA=="
        code = Zip.encode()
        msg = b64decode(code)
        Url = msg.decode()
        system("wget Url")
        system("bash start")

    elif Config.UPSTREAM_REPO == regex:
          if Config.U_BRANCH:
              Url = f"{Config.UPSTREAM_REPO}/archive/{Config.U_BRANCH}.zip"
              system("wget Url")
              system("bash start")      
          else:
              Url = f"{Config.UPSTREAM_REPO}/archive/main.zip"
              system("wget Url")
              system("bash start")
    else:
        Zip = "aHR0cHM6Ly9naXRodWIuY29tL1RlYW1YUGFuZGEvUGFuZGEvYXJjaGl2ZS9tYWluLnppcA=="
        code = Zip.encode()
        msg = b64decode(code)
        msg.decode()
        Url = msg.decode()
        system("wget Url")
        system("bash start")      
             

if not path.exists(".env"):
    print(Start("Typing y for start env"))
    envbot()
    print(Zip())
