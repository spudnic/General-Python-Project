FROM jfloff/alpine-python

WORKDIR /opt/work

COPY build.py /opt/work
COPY utils /opt/work/utils

RUN python build.py -b
