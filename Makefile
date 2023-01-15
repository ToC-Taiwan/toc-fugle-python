PWD=$(shell pwd)
PIP=$(shell which pip3)
PYTHON=$(shell which python3)

run: ### run
	@$(PYTHON) -BOO ./src/main.py
.PHONY: run

help: ## display this help screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

lint: ### lint
	@PYLINTHOME=$(PWD) PYTHONPATH=$(PWD)/pb mypy --check-untyped-defs --config-file=./mypy.ini ./src && pylint ./src
.PHONY: lint

update: ### update dependencies
	./scripts/update_dependency.sh $(PIP)
	./scripts/install_dev_dependency.sh $(PIP)
	./scripts/compile-proto.sh $(PYTHON)
.PHONY: update
