## PandaX_Userbot

__ziplink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $PANDA_USERBOT_REPO == "BUKAN_USERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL0FmdGFoQmFnYXMvTmV3X1VzZXJib3QvYXJjaGl2ZS9QYW5kYVVzZXJib3Quemlw" | base64 -d
    elif [[ $PANDA_USERBOT_REPO == "PANDA_USERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL2lsaGFtbWFuc2l6L1BhbmRhWF9Vc2VyYm90L2FyY2hpdmUvUGFuZGFVc2VyYm90LnppcA==" | base64 -d
    elif [[ $PANDA_USERBOT_REPO =~ $regex ]]
    then
        if [[ $PANDA_USERBOT_REPO_BRANCH ]]
        then
            echo "${PANDA_USERBOT_REPO}/archive/${PANDA_USERBOT_REPO_BRANCH}.zip"
        else
            echo "${PANDA_USERBOT_REPO}/archive/PandaUserbot.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL0FmdGFoQmFnYXMvTmV3X1VzZXJib3QvYXJjaGl2ZS9QYW5kYVVzZXJib3Quemlw" | base64 -d
    fi
}

__repolink () {
    local regex
    local rlink
    regex='(https?)://github.com/.+/.+'
    if [[ $UPSTREAM_REPO == "BUKAN_USERBOT" ]]
    then
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL0FmdGFoQmFnYXMvTmV3X1VzZXJib3Q=" | base64 -d`
    elif [[ $UPSTREAM_REPO == "PANDA_USERBOT" ]]
    then
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL2lsaGFtbWFuc2l6L1BhbmRhWF9Vc2VyYm90" | base64 -d`
    elif [[ $UPSTREAM_REPO =~ $regex ]]
    then
        rlink=`echo "${UPSTREAM_REPO}"`
    else
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL0FmdGFoQmFnYXMvTmV3X1VzZXJib3Q=" | base64 -d`
    fi
    echo "$rlink"
}




_install_python_version() {
    python3${pVer%.*} -c "$1"
}

_install_deploy_git() {
    $(_install_python_version 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO = "https://github.com/PandaUserbot/Dev"
ACTIVE_BRANCH_NAME = "main"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}

_start_install_git() {
    local repolink=$(__repolink)
    $(_install_python_version 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO="'$repolink'"
ACTIVE_BRANCH_NAME = "'$UPSTREAM_REPO_BRANCH'" or "PandaUserbot"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}


_install_pandauserbot () {
    local zippath
    zippath="pandauserbot.zip"
    echo "  Downloading source code ..."
    wget -q $(__ziplink) -O "$zippath"
    echo "  Unpacking Data ..."
    PANDA_USERBOTPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    _install_deploy_git
    cd $PANDA_USERBOTPATH
    _start_install_git
    echo "    Starting PandaUserBot    "
    echo "
           ꧁༺ Panda Userbot ༻꧂
            Menginstal........
    "
    python3 -m Panda
}

_install_pandauserbot
