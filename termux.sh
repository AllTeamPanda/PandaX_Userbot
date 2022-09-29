PANDA="\n°Panda Userbot Install•"
PANDA+="\n "
PANDA+="\nMenjalankan Panda Userbot di Termux"
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
pkg update -y && pkg upgrade
clear
echo -e $PANDA
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
pkg install python3
pip3 install --upgrade pip
apt install postgresql
apt install neofetch
apt install ffmpeg
apt install curl
apt install megatools
apt install unzip
apt install wget
apt install liblapack-dev
apt install aria2
apt install zip
apt install sudo
apt install postgresql-client
cle
echo -e $PANDA
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
pkg install git -y
rm -rf PandaX_Userbot
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
pip3 install -U -r requirements.txt
python installer/termux.py
