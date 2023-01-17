import os
import threading
import time
from concurrent import futures
from datetime import datetime
from queue import Queue

import google.protobuf.empty_pb2
import grpc

from env import RequiredEnv
from logger import logger
from pb import health_pb2, health_pb2_grpc, trade_pb2_grpc
from rabbitmq import RabbitMQS


class gRPCHealthCheck(health_pb2_grpc.HealthCheckInterfaceServicer):
    def __init__(self):
        self.beat_time = float()
        self.debug = False

    def Heartbeat(self, request_iterator, _):
        logger.info("new gRPC client connected")
        self.beat_queue: Queue = Queue()
        threading.Thread(target=self.beat_timer).start()
        for beat in request_iterator:
            self.beat_time = datetime.now().timestamp()
            self.beat_queue.put(beat.message)
            if beat.message == "debug":
                self.debug = True
            else:
                self.debug = False
            yield health_pb2.BeatMessage(message=beat.message)

    def beat_timer(self):
        self.beat_time = datetime.now().timestamp()
        while True:
            if datetime.now().timestamp() > self.beat_time + 10:
                logger.info("grpc client disconnected")
                if self.debug is True:
                    return
                os._exit(1)
            if self.beat_queue.empty():
                time.sleep(1)
                continue
            self.beat_queue.get()

    def Terminate(self, request, _):
        threading.Thread(target=self.wait_and_terminate).start()
        return google.protobuf.empty_pb2.Empty()  # pylint: disable=no-member

    def wait_and_terminate(self):
        time.sleep(3)
        os._exit(1)


class gRPCTrade(trade_pb2_grpc.TradeInterfaceServicer):
    def __init__(self, rq: RabbitMQS):
        self.rq = rq
        self.send_order_lock = threading.Lock()

    def BuyStock(self, request, _):
        logger.info("BuyStock")

    def SellStock(self, request, _):
        logger.info("SellStock")

    def SellFirstStock(self, request, _):
        logger.info("SellFirstStock")

    def CancelStock(self, request, _):
        logger.info("CancelStock")

    def GetOrderStatusByID(self, request, _):
        logger.info("GetOrderStatusByID")

    def GetLocalOrderStatusArr(self, request, _):
        logger.info("GetLocalOrderStatusArr")


def serve(port: str, cfg: RequiredEnv):
    # set call back
    rq = RabbitMQS(
        str(cfg.rabbitmq_url),
        str(cfg.rabbitmq_exchange),
        128,
    )

    # gRPC servicer
    health_servicer = gRPCHealthCheck()
    trade_servicer = gRPCTrade(rq=rq)
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
    health_pb2_grpc.add_HealthCheckInterfaceServicer_to_server(health_servicer, server)
    trade_pb2_grpc.add_TradeInterfaceServicer_to_server(trade_servicer, server)

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    logger.info("gRPC Server started at port %s", port)
    server.wait_for_termination()
