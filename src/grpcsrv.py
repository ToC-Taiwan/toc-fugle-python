import os
import threading
import time
from concurrent import futures
from datetime import datetime

import google.protobuf.empty_pb2
import grpc

from fugle import Fugle
from logger import logger
from pb import basic_pb2, basic_pb2_grpc, trade_pb2, trade_pb2_grpc
from rabbitmq import RabbitMQS
from simulator import Simulator
from status import OrderStatus


class RPCBasic(basic_pb2_grpc.BasicDataInterfaceServicer):
    def __init__(self):
        self.heart_beat_client_arr: list[str] = []
        self.heart_beat_client_arr_lock = threading.Lock()

    def Heartbeat(self, request_iterator, context: grpc.ServicerContext):
        for beat in request_iterator:
            with self.heart_beat_client_arr_lock:
                if len(self.heart_beat_client_arr) > 0:
                    yield basic_pb2.BeatMessage(error="fugle only one client allowed")
                else:
                    self.heart_beat_client_arr.append(beat.message)
                    threading.Thread(target=self.check_context, args=(context,), daemon=True).start()
                    logger.info("new fugle gRPC client connected: %s", beat.message)
            yield basic_pb2.BeatMessage(message=beat.message)

    def check_context(self, context: grpc.ServicerContext):
        while context.is_active():
            time.sleep(1)

        logger.info("fugle gRPC client disconnected")
        with self.heart_beat_client_arr_lock:
            if len(self.heart_beat_client_arr) > 0 and self.heart_beat_client_arr[0] == "debug":
                self.heart_beat_client_arr.clear()
                return
            os._exit(0)

    def Terminate(self, request, _):
        threading.Thread(target=self.wait_and_terminate, daemon=True).start()
        return google.protobuf.empty_pb2.Empty()

    def wait_and_terminate(self):
        time.sleep(3)
        os._exit(0)


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


class GRPCServer:
    def __init__(self, rabbit: RabbitMQS, fugle: Fugle):
        basic_servicer = RPCBasic()
        trade_servicer = RPCTrade(rabbit=rabbit, fugle=fugle)
        server = grpc.server(
            futures.ThreadPoolExecutor(),
            options=[
                (
                    "grpc.max_send_message_length",
                    1024 * 1024 * 1024,
                ),
                (
                    "grpc.max_receive_message_length",
                    1024 * 1024 * 1024,
                ),
            ],
        )

        basic_pb2_grpc.add_BasicDataInterfaceServicer_to_server(basic_servicer, server)
        trade_pb2_grpc.add_TradeInterfaceServicer_to_server(trade_servicer, server)

        self.server = server

    def serve(self, port: str):
        self.server.add_insecure_port(f"[::]:{port}")
        self.server.start()
        logger.info("gRPC Server started at port %s", port)
        self.server.wait_for_termination()
