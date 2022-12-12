FROM debian:latest
WORKDIR /root
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN pip install honeypots
RUN pip install --upgrade requests
RUN pip install pymongo