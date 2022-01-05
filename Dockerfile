# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# As Panda Userbot

FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash INSTALL.sh
ENTRYPOINT ["python3", "-m", "Pandabot"]
