FROM ubuntu:latest
MAINTAINER linuxtho

RUN apt-get update \
    && apt-get -y install python python-pip python-setuptools libyaml-dev

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt \
    && python setup.py install \
    && cp etc/benji.yml /etc/benji.yml

ENTRYPOINT ["/usr/local/bin/benji"]
