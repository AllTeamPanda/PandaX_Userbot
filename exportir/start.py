# /usr/bin/python3
# Panda - UserBot
# Copyright (C) 2022-2023 Panda Userbot
import os
from base64 import b64decode
from time import sleep
from os import system, path

UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO") or None
U_BRANCH = os.environ.get("U_BRANCH") or None

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
        
        
def Zip():
    global regex
    regex='(https?)://github.com/.+/.+'
    if UPSTREAM_REPO == "PANDA_USERBOT":
        Zip = "aHR0cHM6Ly9naXRodWIuY29tL0FsbFRlYW1QYW5kYS9QYW5kYVhfVXNlcmJvdC9hcmNoaXZlL21haW4uemlw"
        code = Zip.encode()
        msg = b64decode(code)
        Url = msg.decode()
        system(f"wget {Url}")
        system("bash start")

    elif UPSTREAM_REPO == regex:
          if U_BRANCH:
              Url = f"{UPSTREAM_REPO}/archive/{U_BRANCH}.zip"
              system(f"wget {Url}")
              system("bash start")      
          else:
              Url = f"{UPSTREAM_REPO}/archive/main.zip"
              system(f"wget {Url}")
              system("bash start")
    else:
        Zip = "aHR0cHM6Ly9naXRodWIuY29tL0FsbFRlYW1QYW5kYS9QYW5kYVhfVXNlcmJvdC9hcmNoaXZlL21haW4uemlw"
        code = Zip.encode()
        msg = b64decode(code)
        msg.decode()
        Url = msg.decode()
        system(f"wget {Url}")
        system("bash start")      
             

if not path.exists(".env"):
    print(Start("Typing y for start env"))
    envbot()
    Zip()
