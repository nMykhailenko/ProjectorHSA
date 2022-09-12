FROM ubuntu:latest

RUN mkdir -p '/app'
RUN apt-get update && \
      apt-get -y install sudo 
RUN sudo apt update -y
RUN sudo apt install siege -y

COPY urls.txt ./app

ENTRYPOINT ["siege"]
