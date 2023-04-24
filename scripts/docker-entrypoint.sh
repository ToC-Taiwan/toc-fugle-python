#!/bin/sh

cd /toc-fugle-python
PBPATH=/toc-fugle-python/src/pb
PYTHONPATH=$PBPATH python -BO ./src/config.py
PYTHON_KEYRING_BACKEND=keyrings.cryptfile.cryptfile.CryptFileKeyring PYTHONPATH=$PBPATH python -BO ./src/main.py
