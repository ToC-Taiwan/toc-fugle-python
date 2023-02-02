import os
import threading
import time
from concurrent import futures
from datetime import datetime
from queue import Queue

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
        self.beat_time = float()
        self.debug = False
        self.beat_queue: Queue = Queue()

    def Heartbeat(self, request_iterator, _):
        logger.info("new fugle gRPC client connected")
        threading.Thread(target=self.beat_timer, daemon=True).start()
        for beat in request_iterator:
            self.beat_time = datetime.now().timestamp()
            self.beat_queue.put(beat.message)
            if beat.message == "debug":
                self.debug = True
            else:
                self.debug = False
            yield basic_pb2.BeatMessage(message=beat.message)

    def beat_timer(self):
        self.beat_time = datetime.now().timestamp()
        while True:
            if datetime.now().timestamp() > self.beat_time + 10:
                logger.info("fugle grpc client disconnected")
                if self.debug is True:
                    return
                os._exit(0)
            if self.beat_queue.empty():
                time.sleep(1)
                continue
            self.beat_queue.get()

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


def serve(port: str, rabbit: RabbitMQS, fugle: Fugle):
    # gRPC servicer
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

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    logger.info("gRPC Server started at port %s", port)
    server.wait_for_termination()
