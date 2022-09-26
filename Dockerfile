FROM ubuntu:20.04

RUN apt-get update

RUN apt-get upgrade -y

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip install numpy

RUN pip install pyTelegramBotAPI

COPY code/* /home/

COPY entrypoint.sh /home/entrypoint.sh

CMD [ "bash" ]

ENTRYPOINT [ "/home/entrypoint.sh" ]
