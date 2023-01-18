import json
from configparser import ConfigParser

import fugle_trade.constant as fc
import fugle_trade.order as fo
from fugle_trade.sdk import SDK

import fugle_entity as fe
from logger import logger

# from pprint import pprint


class Fugle:
    def __init__(self):
        config = ConfigParser()
        config.read("data/config.ini")
        self._sdk = SDK(config)
        self.login()

    def login(self):
        self._sdk.login()

    def certinfo(self):
        return fe.Cert.from_dict(self._sdk.certinfo())

    def get_balance(self):
        return fe.Balance.from_dict(self._sdk.get_balance())

    def get_market_status(self):
        return fe.MarketStatus.from_dict(self._sdk.get_market_status())

    def get_trade_status(self):
        return fe.TradeStatus.from_dict(self._sdk.get_trade_status())

    def get_transactions(self, query_range: str):
        arr: list[fe.FillOrder] = []
        for data in self._sdk.get_transactions(query_range):
            arr.append(fe.FillOrder.from_dict(data))
        return arr

    def get_inventories(self):
        arr: list[fe.Inventory] = []
        for data in self._sdk.get_inventories():
            arr.append(fe.Inventory.from_dict(data))
        return arr

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

    def print_original(self, data):
        logger.info(json.dumps(data, indent=4, ensure_ascii=False))
