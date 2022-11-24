FROM ubuntu:latest

RUN mkdir -p '/app'
RUN apt-get update && \
      apt-get -y install sudo 
RUN sudo apt update -y
RUN sudo apt install siege -y

COPY redis-aof.txt ./app
COPY redis-rdb.txt ./app
COPY beanstalkd-urls.txt ./app

ENTRYPOINT ["siege"]
