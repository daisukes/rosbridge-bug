FROM ubuntu:jammy

WORKDIR /root

RUN apt update && apt install -y \
	python3-pip

RUN pip3 install roslibpy

COPY ./test_ng.py /root/test_ng.py
COPY ./test_ok.py /root/test_ok.py
