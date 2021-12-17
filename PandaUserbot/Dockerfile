FROM biansepang/weebproject:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/ilhammansiz/PandaX_Userbot /home/pandax_userbot/ \
    && chmod 777 /home/pandax_userbot \
    && mkdir /home/pandax_userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/pandax_userbot/

# Setup Working Directory
WORKDIR /home/pandax_userbot/

# Finalization
CMD ["python3","-m","PandaToxic"]
