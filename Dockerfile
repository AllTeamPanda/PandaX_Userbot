# Panda - UserBot

FROM pandauserbotfile/pandauserbot:python202

RUN git clone -b main https://github.com/ilhammansiz/PandaX_Userbot /home/pandauserbot/ \
    && chmod 777 /home/pandauserbot \
    && mkdir /home/pandauserbot/bin/

WORKDIR /home/pandauserbot/

# command to run on container start
CMD [ "bash", "termux_install.sh" ]
