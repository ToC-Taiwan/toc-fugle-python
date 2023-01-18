import json
import threading
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
        self._sdk.login()

    def reset_password(self) -> None:
        """
        重設密碼
        """
        self._sdk.reset_password()

    def get_sdk(self) -> SDK:
        """
        get_sdk Get the SDK object

        Returns:
            SDK: SDK object
        """
        return self._sdk

    def certinfo(self) -> fe.Cert:
        """
        取得憑證相關資訊

        Returns:
            fe.Cert: 憑證相關資訊
        """
        return fe.Cert.from_dict(self._sdk.certinfo())

    def get_balance(self) -> fe.Balance:
        """
        取得銀行餘額相關資訊。 (每 180 秒可查詢一次)

        Returns:
            fe.Balance: 銀行餘額相關資訊
        """
        return fe.Balance.from_dict(self._sdk.get_balance())

    def get_market_status(self) -> fe.MarketStatus:
        """
        取得開盤狀態

        Returns:
            fe.MarketStatus: 開盤狀態
        """
        return fe.MarketStatus.from_dict(self._sdk.get_market_status())

    def get_order_results(self):
        """
        取得委託列表
        """
        # TODO: wait 2023 market open

    def get_trade_status(self) -> fe.TradeStatus:
        """
        取得用戶交易額度, 交易權限相關資訊

        Returns:
            fe.TradeStatus: 交易額度, 交易權限相關資訊
        """
        return fe.TradeStatus.from_dict(self._sdk.get_trade_status())

    def get_transactions(self, query_range: str) -> list[fe.FillOrder]:
        """
        取得指定時間範圍內的成交明細

        Args:
            query_range (str): 時間區間，目前有效數值為 "0d"(當日)、"3d"、"1m"、"3m"

        Returns:
            list[fe.FillOrder]: 成交明細
        """
        arr: list[fe.FillOrder] = []
        for data in self._sdk.get_transactions(query_range):
            arr.append(fe.FillOrder.from_dict(data))
        return arr

    def get_inventories(self) -> list[fe.Inventory]:
        """
        取得當下的庫存明細

        Returns:
            list[fe.Inventory]: 庫存明細
        """
        arr: list[fe.Inventory] = []
        for data in self._sdk.get_inventories():
            arr.append(fe.Inventory.from_dict(data))
        return arr

    def get_settlements(self) -> list[fe.Settlement]:
        """
        取得交割款資訊

        Returns:
            list[fe.Settlement]: 交割款資訊
        """
        arr: list[fe.Settlement] = []
        for data in self._sdk.get_settlements():
            arr.append(fe.Settlement.from_dict(data))
        return arr

    def get_key_info(self) -> fe.KeyInfo:
        """
        取得金鑰資訊

        Returns:
            fe.KeyInfo: 金鑰資訊
        """
        return fe.KeyInfo.from_dict(self._sdk.get_key_info())

    def get_machine_time(self) -> fe.FugleTime:
        """
        取得主機端的時間

        Returns:
            fe.FugleTime: 主機端的時間
        """
        return fe.FugleTime.from_dict(self._sdk.get_machine_time())

    def buy_stock(self, stock_num: str, price: float, quantity: int):
        order = fo.OrderObject(
            buy_sell=fc.Action.Buy,
            price=price,
            stock_no=stock_num,
            quantity=quantity,
            ap_code=fc.APCode.Common,
        )
        self._sdk.place_order(order)

    def cancel_order(self):
        pass

    def modify_price(self):
        pass

    def connect_websocket(self):
        threading.Thread(target=self._sdk.connect_websocket).start()

    def print_original(self, data):
        logger.info(json.dumps(data, indent=4, ensure_ascii=False))
