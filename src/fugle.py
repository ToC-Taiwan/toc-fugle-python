import os
import threading
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
        self.__order_map: dict[str, fe.OrderResult] = {}  # order_id: OrderResult
        self.__order_map_lock = threading.Lock()

        try:
            self.login()
        except Exception as e:  # pylint: disable=broad-except
            logger.error("Login failed: %s", e)
            os._exit(1)

        self.update_local_order()

        logger.info("fugle init done")
        logger.info("is trading day: %s", self.get_market_status().is_trading_day)

    def login(self) -> None:
        """
        login 登入
        """
        self._sdk.login()

    def connect_websocket(self):
        """
        connect_websocket Connect to websocket
        """
        threading.Thread(target=self._sdk.connect_websocket).start()

    def reset_password(self) -> None:
        """
        reset_password Reset password, never use this function
        """
        self._sdk.reset_password()
        raise Exception("Never use this function")

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

    def get_order_results(self) -> list[fe.OrderResult]:
        """
        取得委託列表

        Returns:
            list[fe.OrderResult]: 委託列表
        """
        arr: list[fe.OrderResult] = []
        for data in self._sdk.get_order_results():
            arr.append(fe.OrderResult.from_dict(data))
        return arr

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

    def buy_stock(self, stock_num: str, price: float, quantity: int) -> fe.PlaceOrderResponse:
        """
        buy_stock 買進股票

        Args:
            stock_num (str): 股票代碼
            price (float): 價格
            quantity (int): 數量

        Returns:
            fe.PlaceOrderResponse: 委託回應
        """
        if quantity > 1:
            return fe.PlaceOrderResponse.qty_too_large()

        order = fo.OrderObject(
            price=price,
            stock_no=stock_num,
            quantity=quantity,
            ap_code=fc.APCode.Common,
            buy_sell=fc.Action.Buy,
            price_flag=fc.PriceFlag.Limit,
            bs_flag=fc.BSFlag.ROD,
            trade=fc.Trade.Cash,
        )
        try:
            return fe.PlaceOrderResponse.from_dict(self._sdk.place_order(order))
        except Exception as e:  # pylint: disable=broad-except
            logger.error(e)
            return fe.PlaceOrderResponse.fail_res(e)

    def sell_stock(self, stock_num: str, price: float, quantity: int) -> fe.PlaceOrderResponse:
        """
        sell_stock 賣出股票

        Args:
            stock_num (str): 股票代碼
            price (float): 價格
            quantity (int): 數量

        Returns:
            fe.PlaceOrderResponse: 委託回應
        """
        if quantity > 1:
            return fe.PlaceOrderResponse.qty_too_large()

        order = fo.OrderObject(
            price=price,
            stock_no=stock_num,
            quantity=quantity,
            ap_code=fc.APCode.Common,
            buy_sell=fc.Action.Sell,
            price_flag=fc.PriceFlag.Limit,
            bs_flag=fc.BSFlag.ROD,
            trade=fc.Trade.Cash,
        )
        try:
            return fe.PlaceOrderResponse.from_dict(self._sdk.place_order(order))
        except Exception as e:  # pylint: disable=broad-except
            logger.error(e)
            return fe.PlaceOrderResponse.fail_res(e)

    def sell_first_stock(self, stock_num: str, price: float, quantity: int) -> fe.PlaceOrderResponse:
        """
        sell_first_stock 賣出股票(當沖)

        Args:
            stock_num (str): 股票代碼
            price (float): 價格
            quantity (int): 數量

        Returns:
            fe.PlaceOrderResponse: 委託回應
        """
        if quantity > 1:
            return fe.PlaceOrderResponse.qty_too_large()

        order = fo.OrderObject(
            price=price,
            stock_no=stock_num,
            quantity=quantity,
            ap_code=fc.APCode.Common,
            buy_sell=fc.Action.Sell,
            price_flag=fc.PriceFlag.Limit,
            bs_flag=fc.BSFlag.ROD,
            trade=fc.Trade.DayTradingSell,
        )
        try:
            return fe.PlaceOrderResponse.from_dict(self._sdk.place_order(order))
        except Exception as e:  # pylint: disable=broad-except
            logger.error(e)
            return fe.PlaceOrderResponse.fail_res(e)

    def cancel_stock(self, order_no: str) -> fe.CancelOrderResponse:
        """
        cancel_stock 取消委託

        Args:
            order_no (str): 委託單號

        Returns:
            fe.CancelOrderResponse: 取消委託回應
        """
        order = self.get_local_order_by_ord_no(order_no)
        if order is None:
            return fe.CancelOrderResponse(
                ret_code="-101",
                ret_msg="order not found",
                ord_date="",
                ord_time="",
            )
        try:
            return fe.CancelOrderResponse.from_dict(self._sdk.cancel_order(order.to_dict()))
        except Exception as e:  # pylint: disable=broad-except
            logger.error(e)
            return fe.CancelOrderResponse.fail_res(e)

    def get_local_order(self) -> list[fe.OrderResult]:
        with self.__order_map_lock:
            return list(self.__order_map.values())

    def get_local_order_by_ord_no(self, ord_no: str):
        with self.__order_map_lock:
            return self.__order_map.get(ord_no, None)

    def update_local_order(self):
        with self.__order_map_lock:
            cache = self.__order_map.copy()
            self.__order_map = {}
            try:
                for order in self.get_order_results():
                    if order.ord_no != "":
                        self.__order_map[order.ord_no] = order

            except Exception as e:  # pylint: disable=broad-except
                logger.error(e)
                self.__order_map = cache
