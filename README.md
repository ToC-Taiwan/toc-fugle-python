# TOC FUGLE PYTHON

[![BUILD](https://img.shields.io/github/actions/workflow/status/ToC-Taiwan/toc-fugle-python/main.yml?style=for-the-badge&logo=github)](https://github.com/ToC-Taiwan/toc-fugle-python/actions/workflows/main.yml)
[![Python](https://img.shields.io/badge/Python-3.11.6-yellow?logo=python&logoColor=yellow&style=for-the-badge)](https://python.org)
[![CONTAINER](https://img.shields.io/badge/Container-Docker-blue?style=for-the-badge&logo=docker&logoColor=blue)](https://www.docker.com/)

[![RELEASE](https://img.shields.io/github/release/ToC-Taiwan/toc-fugle-python?style=for-the-badge)](https://github.com/ToC-Taiwan/toc-fugle-python/releases/latest)
[![LICENSE](https://img.shields.io/github/license/ToC-Taiwan/toc-fugle-python?style=for-the-badge)](COPYING)

## Reference

- Schedule restart at 08:20, 14:40 every day

## Initialize

```sh
pip install --no-warn-script-location --no-cache-dir -U -r requirements.txt
```

## .env example

```sh
cp .env.example .env
```

### Make

- show help

```sh
make help
```

- run

```sh
make
```

- update dependencies

```sh
make update
```

## Local RabbitMQ

```sh
docker stop toc-rabbitmq
docker system prune --volumes -f
docker rmi -f $(docker images -a -q)

docker run -d \
  --restart always \
  --name toc-rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=password \
  rabbitmq:3.12.10-management
```

## Authors

- [**Tim Hsu**](https://github.com/Chindada)
