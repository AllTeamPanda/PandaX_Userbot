## Docker with Panda Userbot
## © PandaX_Userbot

FROM pandauserbotfile/pandauserbot:docker-python202

RUN git clone -b PandaUserbot https://github.com/ilhammansiz/PandaX_Userbot /home/pandauserbot/ \
    && chmod 777 /home/pandauserbot \
    && mkdir /home/pandauserbot/bin/

WORKDIR /home/pandauserbot/

CMD [ "bash", "termux_install.sh" ]
