# Panda - UserBot
# # Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
# recode by ilham mansiz
# This file is a part of < https://github.com/ilhammansiz/PandaX_Userbot/ >

nowtime=$(date)
echo "
PandaUserBot
(C) Panda
Powered By @diemmmmmmmmmm
Time : $nowtime
"
installrun () {
    apt -qq update -y
    apt -qq install -y --no-install-recommends \
        git \
        ffmpeg \
        mediainfo \
        unzip \
        wget \
        gifsicle 
  }
  
# Thanks To Userge For The Chrome Version Hecks  
install_chrome () {
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt -fqqy install ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
    wget https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
    wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && unzip opencv.zip && mv -f opencv-master /usr/bin/ && rm opencv.zip
    wget https://people.eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel -P ./bot_utils_files/ai_helpers/
}

terakhir () {
    echo "
    
=+---------------------------------------------------------+=
꧁༺ Panda Userbot ༻꧂
Copyright (C) 2021 PandaX_Userbot
Powered By @diemmmmmmmmmm with Telegram
=+---------------------------------------------------------+=
    "
}

_start_all () {
    installrun
    install_chrome
    pip3 install –upgrade pip
    pip3 install --no-cache-dir -r requirements.txt
    terakhir
}

_start_all
