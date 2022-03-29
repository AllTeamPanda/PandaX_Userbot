#!/bin/bash


_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $USERBOT_REPO == "PANDA_USERBOT" ]]
    then
        echo "https://github.com/ilhammansiz/PandaX_Userbot/archive/PandaUserbot.zip"
    elif [[ $USERBOT_REPO =~ $regex ]]
    then
        if [[ $USERBOT_REPO_BRANCH ]]
        then
            echo "${USERBOT_REPO}/archive/${USERBOT_REPO_BRANCH}.zip"
        else
            echo "${USERBOT_REPO}/archive/PandaUserbot.zip"
        fi
    else
        echo "https://github.com/ilhammansiz/PandaX_Userbot/archive/PandaUserbot.zip"
    fi
}


_install_bot () {
    local zippath
    zippath="pandax_userbot.zip"
    echo "  Downloading source code ..."
    wget -q $(_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    USERBOTPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    sleep 5
    cd $USERBOTPATH
    echo " 𝐒𝐭𝐚𝐫𝐭•𝐔𝐬𝐞𝐫𝐛𝐨𝐭-  "
    python3 -m Panda
}

_install_bot
