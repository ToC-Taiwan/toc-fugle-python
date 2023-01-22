PIP=$(shell which pip3)
PYTHON=$(shell which python3)
PBPATH=$(PWD)/src/pb

run: config ### run
	@PYTHON_KEYRING_BACKEND=keyrings.cryptfile.cryptfile.CryptFileKeyring PYTHONPATH=$(PBPATH) $(PYTHON) -BOO ./src/main.py
.PHONY: run

lint: ### lint
	@mypy --check-untyped-defs --config-file=./mypy.ini ./src
	@PYTHONPATH=$(PBPATH) PYLINTHOME=$(PWD) pylint ./src
.PHONY: lint

install: ### install dependencies
	@$(PIP) install --no-warn-script-location --no-cache-dir -r requirements.txt
	@./scripts/install_dev_dependency.sh $(PIP)
.PHONY: install

update: ### update dependencies
	@./scripts/update_dependency.sh $(PIP)
	@./scripts/install_dev_dependency.sh $(PIP)
	@./scripts/compile-proto.sh $(PYTHON)
.PHONY: update

proto: ### compile proto
	@./scripts/compile-proto.sh $(PYTHON)
.PHONY: proto

config: ### config
	@PYTHONPATH=$(PBPATH) $(PYTHON) -BOO ./src/config.py
.PHONY: config

help: ## display this help screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help
