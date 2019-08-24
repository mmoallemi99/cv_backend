FROM ubuntu

RUN apt -y update
RUN apt -y upgrade

RUN apt -y install python3
RUN apt -y install python3-pip

COPY . /opt/source-code

ARG LANG=en_US.UTF-8
ARG LC_ALL=en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8


RUN pip3 install -r /opt/source-code/requirements.txt


ENTRYPOINT DJANGO_APP=/opt/source-code/manage.py runserver



