import random
import string
import threading
import time
from datetime import datetime

import fugle_trade.constant as fc

import fugle_entity as fe
from logger import logger


class Simulator:
    def __init__(self):
        self.__simulation_count_map: dict[str, int] = {}  # key: stock_num or code, value: count
        self.__simulation_lock = threading.Lock()

        self.__order_map: dict[str, fe.OrderResult] = {}  # order_id: OrderResult
        self.__order_map_lock = threading.Lock()

    def finish_simulation_order(self, order: fe.OrderResult, wait: int):
        self.insert_or_update_local_order(order)
        time.sleep(wait)
        if random.randint(1, 100) > 10:
            order.mat_qty = order.org_qty
            order.celable = "2"
            self.insert_or_update_local_order(order)

    def buy_stock(self, stock_num: str, price: float, quantity: int):
        with self.__simulation_lock:
            current = self.__simulation_count_map.get(stock_num, 0)
            if current < 0:
                if quantity + current > 0:
                    return fe.PlaceOrderResponse.fail_res(Exception("buy later quantity is too big"))
            self.__simulation_count_map[stock_num] = current + quantity

        now = datetime.now()
        sim_order = fe.OrderResult(
            ord_no=self.random_ord_no(),
            ord_date=now.strftime("%Y%m%d"),
            ord_time=now.strftime("%H%M%S%f")[:-3],
            work_date=now.strftime("%Y%m%d"),
            buy_sell=fc.Action.Buy.value,
            stock_no=stock_num,
            od_price=price,
            org_qty=quantity,
            celable="1",
            cel_qty=0,
            mat_qty=0,
            ord_status="2",
            pre_ord_no="",
            ap_code=fc.APCode.Common.value,
            price_flag=fc.PriceFlag.Limit.value,
            trade=fc.Trade.Cash.value,
            err_code="",
            err_msg="",
            avg_price=price,
            bs_flag=fc.BSFlag.ROD.value,
            org_qty_share=0,
            mat_qty_share=0,
            cel_qty_share=0,
        )
        threading.Thread(
            target=self.finish_simulation_order,
            args=(sim_order, random.randint(2, 10)),
        ).start()

        return fe.PlaceOrderResponse(
            ord_no=sim_order.ord_no,
            ord_date=sim_order.ord_date,
            ord_time=sim_order.ord_time,
            work_date=sim_order.work_date,
            ord_type="",
            ret_code="",
            ret_msg="",
        )

    def sell_stock(self, stock_num: str, price: float, quantity: int):
        with self.__simulation_lock:
            current = self.__simulation_count_map.get(stock_num, 0)
            if quantity > current:
                return fe.PlaceOrderResponse.fail_res(Exception("quantity is too big"))
            self.__simulation_count_map[stock_num] = current - quantity

        now = datetime.now()
        sim_order = fe.OrderResult(
            ord_no=self.random_ord_no(),
            ord_date=now.strftime("%Y%m%d"),
            ord_time=now.strftime("%H%M%S%f")[:-3],
            work_date=now.strftime("%Y%m%d"),
            buy_sell=fc.Action.Sell.value,
            stock_no=stock_num,
            od_price=price,
            org_qty=quantity,
            celable="1",
            cel_qty=0,
            mat_qty=0,
            ord_status="2",
            pre_ord_no="",
            ap_code=fc.APCode.Common.value,
            price_flag=fc.PriceFlag.Limit.value,
            trade=fc.Trade.Cash.value,
            err_code="",
            err_msg="",
            avg_price=price,
            bs_flag=fc.BSFlag.ROD.value,
            org_qty_share=0,
            mat_qty_share=0,
            cel_qty_share=0,
        )
        threading.Thread(
            target=self.finish_simulation_order,
            args=(sim_order, random.randint(2, 10)),
        ).start()

        return fe.PlaceOrderResponse(
            ord_no=sim_order.ord_no,
            ord_date=sim_order.ord_date,
            ord_time=sim_order.ord_time,
            work_date=sim_order.work_date,
            ord_type="",
            ret_code="",
            ret_msg="",
        )

    def sell_first_stock(self, stock_num: str, price: float, quantity: int):
        with self.__simulation_lock:
            current = self.__simulation_count_map.get(stock_num, 0)
            if current > 0:
                return fe.PlaceOrderResponse.fail_res(Exception("can not sell first"))
            self.__simulation_count_map[stock_num] = current - quantity

        now = datetime.now()
        sim_order = fe.OrderResult(
            ord_no=self.random_ord_no(),
            ord_date=now.strftime("%Y%m%d"),
            ord_time=now.strftime("%H%M%S%f")[:-3],
            work_date=now.strftime("%Y%m%d"),
            buy_sell=fc.Action.Sell.value,
            stock_no=stock_num,
            od_price=price,
            org_qty=quantity,
            celable="1",
            cel_qty=0,
            mat_qty=0,
            ord_status="2",
            pre_ord_no="",
            ap_code=fc.APCode.Common.value,
            price_flag=fc.PriceFlag.Limit.value,
            trade=fc.Trade.DayTradingSell.value,
            err_code="",
            err_msg="",
            avg_price=price,
            bs_flag=fc.BSFlag.ROD.value,
            org_qty_share=0,
            mat_qty_share=0,
            cel_qty_share=0,
        )
        threading.Thread(
            target=self.finish_simulation_order,
            args=(sim_order, random.randint(2, 10)),
        ).start()

        return fe.PlaceOrderResponse(
            ord_no=sim_order.ord_no,
            ord_date=sim_order.ord_date,
            ord_time=sim_order.ord_time,
            work_date=sim_order.work_date,
            ord_type="",
            ret_code="",
            ret_msg="",
        )

    def cancel_stock(self, ord_no: str):
        order = self.get_local_order_by_ord_no(ord_no)
        if order is None:
            return fe.CancelOrderResponse.fail_res(Exception("order not found"))

        with self.__simulation_lock:
            current = self.__simulation_count_map.get(order.stock_no, 0)
            if order.buy_sell == fc.Action.Buy.value:
                self.__simulation_count_map[order.stock_no] = current - order.org_qty
            else:
                self.__simulation_count_map[order.stock_no] = current + order.org_qty

        order.celable = "2"
        order.cel_qty = order.org_qty
        self.insert_or_update_local_order(order)
        return fe.CancelOrderResponse(
            ord_date=order.ord_date,
            ord_time=order.ord_time,
            ret_code="",
            ret_msg="",
        )

    def random_ord_no(self) -> str:
        """
        random ord_no for simulation

        Returns:
            str: ord_no
        """
        return "fugle-simulate-".join(random.choice(string.digits) for _ in range(5))

    def get_local_order(self) -> list[fe.OrderResult]:
        return list(self.__order_map.values())

    def get_local_order_by_ord_no(self, ord_no: str):
        with self.__order_map_lock:
            return self.__order_map.get(ord_no, None)

    def insert_or_update_local_order(self, order: fe.OrderResult):
        with self.__order_map_lock:
            self.__order_map[order.ord_no] = order

    def reset_simulator(self):
        """
        reset_simulator will clear all simulation order
        """
        clear_count = int()
        with self.__simulation_lock:
            for stock_num, count in self.__simulation_count_map.items():
                if count > 0:
                    logger.info("clear %d simulation for %s", count, stock_num)
                    clear_count += count
            self.__simulation_count_map = {}

        with self.__order_map_lock:
            self.__order_map = {}
