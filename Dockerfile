FROM ilhammansiz17/masteruserbot:MasterUserbot


RUN git clone https://github.com/ilhammansiz/PandaX_Userbot /root/PandaX_Userbot
WORKDIR /root/PandaX_Userbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "bot.py"]  
