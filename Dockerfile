FROM python:3.10.8-slim

USER root

RUN apt update && apt install -y make

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /toc-fugle-python

COPY data /toc-fugle-python/data
COPY logs /toc-fugle-python/logs
COPY scripts /toc-fugle-python/scripts
COPY src /toc-fugle-python/src
COPY Makefile /toc-fugle-python/Makefile

ENTRYPOINT ["/toc-fugle-python/scripts/docker-entrypoint.sh"]
