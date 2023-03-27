#!/bin/sh

cd /toc-fugle-python
PBPATH=/toc-fugle-python/src/pb
PYTHONPATH=$(PBPATH) python -BOO ./src/config.py
PYTHON_KEYRING_BACKEND=keyrings.cryptfile.cryptfile.CryptFileKeyring PYTHONPATH=$(PBPATH) python -BOO ./src/main.py
