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
from pb import basic_pb2_grpc, health_pb2, health_pb2_grpc, history_pb2_grpc, stream_pb2_grpc, trade_pb2_grpc
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


class gRPCBasic(basic_pb2_grpc.BasicDataInterfaceServicer):
    def GetAllStockDetail(self, request, _):
        logger.info("GetAllStockDetail")

    def GetAllFutureDetail(self, request, _):
        logger.info("GetAllFutureDetail")


class gRPCHistory(history_pb2_grpc.HistoryDataInterfaceServicer):
    def GetStockHistoryTick(self, request, _):
        logger.info("GetStockHistoryTick")

    def GetStockHistoryKbar(self, request, _):
        logger.info("GetStockHistoryKbar")

    def GetStockHistoryClose(self, request, _):
        logger.info("GetStockHistoryClose")

    def GetStockHistoryCloseByDateArr(self, request, _):
        logger.info("GetStockHistoryCloseByDateArr")

    def GetStockTSEHistoryTick(self, request, _):
        logger.info("GetStockTSEHistoryTick")

    def GetStockTSEHistoryKbar(self, request, _):
        logger.info("GetStockTSEHistoryKbar")

    def GetStockTSEHistoryClose(self, request, _):
        logger.info("GetStockTSEHistoryClose")

    def GetOTCHistoryKbar(self, request, _):
        logger.info("GetOTCHistoryKbar")

    def GetFutureHistoryTick(self, request, _):
        logger.info("GetFutureHistoryTick")

    def GetFutureHistoryKbar(self, request, _):
        logger.info("GetFutureHistoryKbar")

    def GetFutureHistoryClose(self, request, _):
        logger.info("GetFutureHistoryClose")


class gRPCTrade(trade_pb2_grpc.TradeInterfaceServicer):
    def __init__(self, rq: RabbitMQS):
        self.rq = rq
        self.send_order_lock = threading.Lock()

    def GetFuturePosition(self, request, _):
        logger.info("GetFuturePosition")

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

    def GetSimulateOrderStatusArr(self, request, _):
        logger.info("GetSimulateOrderStatusArr")

    def GetNonBlockOrderStatusArr(self, request, _):
        logger.info("GetNonBlockOrderStatusArr")

    def BuyFuture(self, request, _):
        logger.info("BuyFuture")

    def SellFuture(self, request, _):
        logger.info("SellFuture")

    def SellFirstFuture(self, request, _):
        logger.info("SellFirstFuture")

    def CancelFuture(self, request, _):
        logger.info("CancelFuture")


class gRPCStream(stream_pb2_grpc.StreamDataInterfaceServicer):
    def GetStockSnapshotByNumArr(self, request, _):
        logger.info("GetStockSnapshotByNumArr")

    def GetAllStockSnapshot(self, request, _):
        logger.info("GetAllStockSnapshot")

    def GetStockSnapshotTSE(self, request, _):
        logger.info("GetStockSnapshotTSE")

    def GetStockSnapshotOTC(self, request, _):
        logger.info("GetStockSnapshotOTC")

    def GetStockVolumeRank(self, request, _):
        logger.info("GetStockVolumeRank")

    def SubscribeStockTick(self, request, _):
        logger.info("SubscribeStockTick")

    def UnSubscribeStockTick(self, request, _):
        logger.info("UnSubscribeStockTick")

    def SubscribeStockBidAsk(self, request, _):
        logger.info("SubscribeStockBidAsk")

    def UnSubscribeStockBidAsk(self, request, _):
        logger.info("UnSubscribeStockBidAsk")

    def SubscribeFutureTick(self, request, _):
        logger.info("SubscribeFutureTick")

    def UnSubscribeFutureTick(self, request, _):
        logger.info("UnSubscribeFutureTick")

    def SubscribeFutureBidAsk(self, request, _):
        logger.info("SubscribeFutureBidAsk")

    def UnSubscribeFutureBidAsk(self, request, _):
        logger.info("UnSubscribeFutureBidAsk")

    def UnSubscribeStockAllTick(self, request, _):
        logger.info("UnSubscribeStockAllTick")

    def UnSubscribeStockAllBidAsk(self, request, _):
        logger.info("UnSubscribeStockAllBidAsk")

    def GetFutureSnapshotByCodeArr(self, request, _):
        logger.info("GetFutureSnapshotByCodeArr")


def serve(port: str, cfg: RequiredEnv):
    # set call back
    rq = RabbitMQS(
        str(cfg.rabbitmq_url),
        str(cfg.rabbitmq_exchange),
        128,
    )

    # gRPC servicer
    health_servicer = gRPCHealthCheck()
    basic_servicer = gRPCBasic()
    history_servicer = gRPCHistory()
    trade_servicer = gRPCTrade(rq=rq)
    stream_servicer = gRPCStream()
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
    basic_pb2_grpc.add_BasicDataInterfaceServicer_to_server(basic_servicer, server)
    history_pb2_grpc.add_HistoryDataInterfaceServicer_to_server(history_servicer, server)
    trade_pb2_grpc.add_TradeInterfaceServicer_to_server(trade_servicer, server)
    stream_pb2_grpc.add_StreamDataInterfaceServicer_to_server(stream_servicer, server)

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    logger.info("gRPC Server started at port %s", port)
    server.wait_for_termination()
