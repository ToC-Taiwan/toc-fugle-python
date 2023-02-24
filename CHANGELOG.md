# CHANGELOG

## v1.0.0

> 2023-02-24

### Bug Fixes (10)

* **cron:** fix redundant argument in shcedule terminate
* **dependency:** fix wrong jinja2 install script
* **docker:** fix wrong makefile name
* **docker:** add docker entrypoint back
* **exception:** pass exception of fugle mid-night which is not able to be handled
* **fugle:** fix try fetch data before login
* **hook:** fix lint hook fail
* **log:** fix missing true after market time
* **script:** fix proto script, modify venv script
* **thread:** fix system exit only exit child thread

### Features (14)

* **callback:** add fugle callback to rq, add basic fugle method
* **cb:** add websocket on close cb
* **config:** add config template, api key, secret, fugle login
* **fugle:** add cancel all stock order
* **fugle:** add get inventories from fugle
* **fugle:** finish all basic method in fugle
* **grpc:** complete grpc trade stock, get order from local
* **log:** ignore error message when not in open time
* **login:** add load password from keyring
* **order:** implement all condition on order status, limit order qty to 1, skip pre order in local
* **proto:** use new protobuf layout, modify makefile
* **proto:** change to re-design rpc layout
* **rabbitmq:** if exchange exist skip create
* **simulator:** add simulator for fugle trade
