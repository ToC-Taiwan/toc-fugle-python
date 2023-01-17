import json
from configparser import ConfigParser

from fugle_trade.sdk import SDK

from fugle_entity import Cert
from logger import logger

config = ConfigParser()
config.read("data/config.ini")

sdk = SDK(config)
cert = Cert(sdk.certinfo())

logger.info(cert.cn)
logger.info(cert.is_valid)
logger.info(cert.not_after)
logger.info(cert.serial)

# login
sdk.login()

inventories = sdk.get_inventories()
for inventory in inventories:
    print(json.dumps(inventory, indent=4))


results = sdk.get_order_results()
for result in results:
    print(json.dumps(result, indent=4))
