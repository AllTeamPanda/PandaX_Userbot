## Docker with Panda Userbot
## © PandaX_Userbot

FROM ilhammansiz17/pandauserbot:docker-python

COPY . .

RUN bash Text.sh


CMD [ "bash", "start.sh" ]
