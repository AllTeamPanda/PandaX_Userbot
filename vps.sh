
## Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••



PANDA="\n°Panda Userbot Install•"
PANDA+="\n "
PANDA+="\nMenjalankan Panda Userbot di Vps"
PANDA+="\n⚡ Sebelumnya Joinn Grup/Channel ⚡"
PANDA+="\n "
PANDA+="\n📣 Channel: @PandaUserbot"
PANDA+="\n📢 GrupSupport: @TeamSquadUserbotSupport"
PANDA+="\n "
LUQ="\n "
echo -e $PANDA
echo -e $LUQ
echo "Waiting..."
echo -e $LUQ
sudo apt update && upgrade -y
sudo apt install git -y
clear
echo -e $PANDA
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
sudo apt install python3
sudo apt install python3-pip
sudo apt install postgresql
sudo apt install neofetch
sudo apt install ffmpeg
sudo apt install curl
sudo apt install megatools
sudo apt install unzip
sudo apt install wget
sudo apt install liblapack-dev
sudo apt install aria2
sudo apt install zip
sudo apt install sudo
sudo apt install python3-wand
sudo apt install python3-lxml
sudo apt install postgresql-client
pip3 install av -q --no-binary av
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
cle
echo -e $PANDA
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
clear
echo -e $PANDA
echo -e $LUQ
echo "Cloning Panda Userbot"
echo -e $LUQ
git clone https://github.com/ilhammansiz/PandaX_Userbot
clear
echo -e $PANDA
echo -e $LUQ
echo "Menginstall Pakages"
echo -e $LUQ
cd PandaX_Userbot
pip3 install --no-cache-dir -r requirements.txt
python3 installer/termux.py
