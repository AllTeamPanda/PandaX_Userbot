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
        sleep(0.1)
        
   

if not path.exists(".env"):
    print(Start("Typing y for start env"))
    envbot()
    print(system("bash start"))
