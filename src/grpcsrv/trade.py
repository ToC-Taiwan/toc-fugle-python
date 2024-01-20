import threading
from datetime import datetime

import google.protobuf.empty_pb2

from fugle import Fugle
from pb.forwarder import trade_pb2, trade_pb2_grpc
from rabbitmq import RabbitMQS
from simulator import Simulator
from status import OrderStatus


class RPCTrade(trade_pb2_grpc.TradeInterfaceServicer):
    def __init__(self, rabbit: RabbitMQS, fugle: Fugle):
        self.rabbit = rabbit
        self.fugle = fugle
        self.send_order_lock = threading.Lock()
        self.simulator = Simulator()

    def BuyStock(self, request, _):
        result = None
        if request.simulate is not True:
            result = self.fugle.buy_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )
        else:
            result = self.simulator.buy_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )

        if result.ret_msg != "":
            status = OrderStatus.FAILED
        else:
            status = OrderStatus.SUBMITTED

        return trade_pb2.TradeResult(
            order_id=result.ord_no,
            status=status.value,
            error=result.ret_msg,
        )

    def SellStock(self, request, _):
        result = None
        if request.simulate is not True:
            result = self.fugle.sell_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )
        else:
            result = self.simulator.sell_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )

        if result.ret_msg != "":
            status = OrderStatus.FAILED
        else:
            status = OrderStatus.SUBMITTED

        return trade_pb2.TradeResult(
            order_id=result.ord_no,
            status=status.value,
            error=result.ret_msg,
        )

    def SellFirstStock(self, request, _):
        result = None
        if request.simulate is not True:
            result = self.fugle.sell_first_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )
        else:
            result = self.simulator.sell_first_stock(
                request.stock_num,
                request.price,
                request.quantity,
            )

        if result.ret_msg != "":
            status = OrderStatus.FAILED
        else:
            status = OrderStatus.SUBMITTED

        return trade_pb2.TradeResult(
            order_id=result.ord_no,
            status=status.value,
            error=result.ret_msg,
        )

    def CancelStock(self, request, _):
        result = None
        if request.simulate is not True:
            result = self.fugle.cancel_stock(request.order_id)
        else:
            result = self.simulator.cancel_stock(request.order_id)

        if result.ret_msg != "":
            status = OrderStatus.FAILED
        else:
            status = OrderStatus.CANCELLED

        return trade_pb2.TradeResult(
            order_id=request.order_id,
            status=status.value,
            error=result.ret_msg,
        )

    def GetOrderStatusByID(self, request, _):
        result = None
        if request.simulate is not True:
            result = self.fugle.get_local_order_by_ord_no(request.order_id)
        else:
            result = self.simulator.get_local_order_by_ord_no(request.order_id)

        if result is None:
            return trade_pb2.TradeResult(
                order_id=request.order_id,
                status=OrderStatus.UNKNOW.value,
                error="order not found",
            )

        return trade_pb2.TradeResult(
            order_id=result.order_id,
            status=result.covert_to_order_status().value,
            error=result.error,
        )

    def GetLocalOrderStatusArr(self, request, _):
        with self.send_order_lock:
            self.rabbit.send_order_arr(self.fugle.get_local_order())
            return google.protobuf.empty_pb2.Empty()

    def GetSimulateOrderStatusArr(self, request, _):
        with self.send_order_lock:
            self.rabbit.send_order_arr(self.simulator.get_local_order())
            return google.protobuf.empty_pb2.Empty()

    def GetAccountBalance(self, request, _):
        balance = self.fugle.get_balance()
        if balance is None:
            return trade_pb2.AccountBalance(
                date="",
                balance=0,
            )
        return trade_pb2.AccountBalance(
            date=datetime.strftime(datetime.fromtimestamp(balance.updated_at), "%Y-%m-%d %H:%M:%S"),
            balance=float(balance.available_balance),
        )

    def GetSettlement(self, request, _):
        result = trade_pb2.SettlementList()
        settlements = self.fugle.get_settlements()
        for settle in settlements:
            result.settlement.append(
                trade_pb2.Settlement(
                    date=datetime.strftime(datetime.strptime(settle.c_date, "%Y%m%d"), "%Y-%m-%d %H:%M:%S"),
                    amount=float(settle.price),
                )
            )
        return result

    def GetMargin(self, request, _):
        return trade_pb2.Margin()

    def GetFuturePosition(self, request, _):
        return trade_pb2.FuturePositionArr()

    def GetStockPosition(self, request, _):
        response = trade_pb2.StockPositionArr()
        result = self.fugle.get_inventories()
        for pos in result:
            response.position_arr.append(
                trade_pb2.StockPosition(
                    code=pos.stk_no,
                    quantity=int(int(pos.cost_qty) / 1000),
                    price=float(pos.price_avg),
                )
            )
        return response
