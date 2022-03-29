## Docker with Panda Userbot
## © PandaX_Userbot

FROM ilhammansiz17/pandauserbot:docker-userbot

RUN git clone -b PandaUserbot https://github.com/ilhammansiz/PandaX_Userbot
    
WORKDIR /app/


CMD [ "bash", "start.sh" ]
