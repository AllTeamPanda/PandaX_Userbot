FROM pandauserbotfile/pandauserbot:python202

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "bash", "start.sh" ]

