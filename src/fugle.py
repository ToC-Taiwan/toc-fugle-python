import inspect
import logging
import os
import threading
from configparser import ConfigParser
from datetime import datetime

import fugle_trade.constant as fc
import fugle_trade.order as fo
from fugle_trade.sdk import SDK

import fugle_entity as fe
from logger import logger

logging.getLogger("websocket").propagate = False


MAX_LOGIN_RETRY = 3


class Fugle:
    def __init__(self):
        try:
            self._config = ConfigParser()
            self._config.read("data/config.ini")
        except Exception as error:
            logger.error("fugle initial failed: %s", error)
            os._exit(1)

        self._sdk = None
        self.__order_map: dict[str, fe.OrderResult] = {}  # order_id: OrderResult
        self.__order_map_lock = threading.Lock()
        self.__get_inventory_time = 0.0
        self.__login_times = 0
        logger.info("fugle init done")

    def login(self) -> None:
        """
        login 登入
        """
        self._sdk = SDK(self._config)
        try:
            if self.__login_times - 1 > MAX_LOGIN_RETRY:
                logger.error("re-login over %d times, exit", MAX_LOGIN_RETRY)
                os._exit(1)
            self.__login_times += 1
            if self.__login_times > 1:
                logger.warning("try re-login %d of %d", self.__login_times - 1, MAX_LOGIN_RETRY)
            self._sdk.login()
            self.set_callback()
            self.connect_websocket()
            logger.info("login to fugle")

        except Exception as error:
            logger.error("login failed: %s", error)
            os._exit(1)

    def current_method_name(self):
        """
        current_method_name Get current method name
        """
        return inspect.currentframe().f_back.f_code.co_name

    def process_error(self, error: str, method_name: str):
        """
        process_error Process error
        """
        code = error.split(":")[0].strip()
        if code == "000997":
            return
        # if code == "A00001":
        #     self.login()
        # else:
        logger.error("%s error: %s", method_name, error)

    def connect_websocket(self):
        """
        connect_websocket Connect to websocket
        """
        logger.info("connect to fugle websocket")
        threading.Thread(target=self._sdk.connect_websocket, daemon=True).start()

    def reset_password(self) -> None:
        """
        reset_password Reset password, never use this function
        """
        self._sdk.reset_password()
        raise RuntimeError("Never use this function")

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

    def get_balance(self) -> fe.Balance | None:
        """
        取得銀行餘額相關資訊。 (每 180 秒可查詢一次)

        Returns:
            fe.Balance: 銀行餘額相關資訊
        """
        try:
            return fe.Balance.from_dict(self._sdk.get_balance())
        except Exception:
            return None

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
        if datetime.now().timestamp() - self.__get_inventory_time < 10:
            return []

        try:
            arr: list[fe.Inventory] = []
            for data in self._sdk.get_inventories():
                arr.append(fe.Inventory.from_dict(data))
            self.__get_inventory_time = datetime.now().timestamp()
            return arr
        except Exception as error:
            self.process_error(str(error), self.current_method_name())
            return []

    def get_settlements(self) -> list[fe.Settlement] | list:
        """
        取得交割款資訊

        Returns:
            list[fe.Settlement]: 交割款資訊
        """
        try:
            arr: list[fe.Settlement] = []
            for data in self._sdk.get_settlements():
                arr.append(fe.Settlement.from_dict(data))
            return arr
        except Exception:
            return []

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
        except Exception as error:
            self.process_error(str(error), self.current_method_name())
            return fe.PlaceOrderResponse.fail_res(error)

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
        except Exception as error:
            self.process_error(str(error), self.current_method_name())
            return fe.PlaceOrderResponse.fail_res(error)

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
        except Exception as error:
            self.process_error(str(error), self.current_method_name())
            return fe.PlaceOrderResponse.fail_res(error)

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
        except Exception as error:
            self.process_error(str(error), self.current_method_name())
            return fe.CancelOrderResponse.fail_res(error)

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

            except Exception as error:
                self.__order_map = cache
                if self.is_market_open() is True:
                    self.process_error(str(error), self.current_method_name())

    def cancel_all_stock(self):
        for order in self.get_local_order():
            if order.celable == "1":
                self.cancel_stock(order.ord_no)

    def is_market_open(self) -> bool:
        """
        is_market_open 是否開市

        Returns:
            bool: 是否開市
        """
        now = datetime.now()
        if now.hour < 8 or now.hour > 15:
            return False
        return True

    def set_callback(self):
        @self._sdk.on("error")
        def on_error(self, err):
            logger.error("on_error: %s", err)
            if str(err) == "Connection to remote host was lost.":
                self.login()

        @self._sdk.on("close")
        def on_close(self, _, close_status_code, close_msg):
            """
            ws type: <class 'websocket._app.WebSocketApp'>
            close_status_code type: <class 'NoneType'>
            close_msg type: <class 'NoneType'>

            example:
            ws on_close 1000 Closed by the WebSocketManager
            """
            logger.error("ws on_close %s:%s", str(close_status_code), str(close_msg))
            self.login()

        @self._sdk.on("order")
        def on_order(self, _):
            self.update_local_order()

        @self._sdk.on("dealt")
        def on_dealt(self, _):
            self.update_local_order()
