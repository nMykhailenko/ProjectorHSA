FROM ubuntu:latest

RUN apt-get update && \
      apt-get -y install sudo 
RUN sudo apt update -y
RUN sudo apt install siege -y

ENTRYPOINT ["siege"]
