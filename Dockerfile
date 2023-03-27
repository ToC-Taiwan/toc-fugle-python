FROM python:3.11.2-slim

USER root

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /toc-fugle-python

COPY data /toc-fugle-python/data
COPY logs /toc-fugle-python/logs
COPY scripts /toc-fugle-python/scripts
COPY src /toc-fugle-python/src

ENTRYPOINT ["/toc-fugle-python/scripts/docker-entrypoint.sh"]
