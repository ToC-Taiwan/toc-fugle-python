from configparser import ConfigParser

import fugle_trade.constant as fc
import fugle_trade.order as fo
from fugle_trade.sdk import SDK

import fugle_entity as fe
from logger import logger


class Fugle:
    def __init__(self):
        config = ConfigParser()
        config.read("data/config.ini")
        self._sdk = SDK(config)

    def login(self):
        self._sdk.login()

    def show_cert(self):
        cert = fe.Cert(self._sdk.certinfo())
        logger.info(cert.cn)
        logger.info(cert.is_valid)
        logger.info(cert.not_after)
        logger.info(cert.serial)

    def get_inventories(self):
        inventories = self._sdk.get_inventories()
        return inventories

    def get_order_results(self):
        tmp: list[fe.OrderResult] = []
        results = self._sdk.get_order_results()
        for result in results:
            tmp.append(fe.OrderResult.from_dict(result))
        return tmp

    def buy_stock(self, stock_num: str, price: float, quantity: int):
        order = fo.OrderObject(
            buy_sell=fc.Action.Buy,
            price=price,
            stock_no=stock_num,
            quantity=quantity,
            ap_code=fc.APCode.Common,
        )
        result = self._sdk.place_order(order)
        print(type(result))
